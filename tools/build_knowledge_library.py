import argparse
import asyncio
import csv
import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
from crawl4ai.cache_context import CacheMode
from docx import Document


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILES = [
    ROOT / "LLM Trust Bench_ Research & Implementation.md",
    ROOT
    / "Literature Review_ Behavioral Economics Experiments and Large Language Models.docx",
]

OUTPUT_DIR = ROOT / "knowledge_library"
PAPERS_DIR = OUTPUT_DIR / "papers"
DOCLING_DIR = OUTPUT_DIR / "docling"
WEB_DIR = OUTPUT_DIR / "web"
INDEX_JSON = OUTPUT_DIR / "index.json"
INDEX_CSV = OUTPUT_DIR / "index.csv"

URL_PATTERN = re.compile(r"https?://[^\s)\]>\"]+")

DISCOVERY_BLOCKLIST = {
    "wikipedia.org",
    "github.com",
    "skatebench.t3.gg",
    "create.t3.gg",
    "ainews.com",
    "searchengineland.com",
    "news.stanford.edu",
    "emergentmind.com",
}


def extract_urls_from_text(text):
    urls = []
    for match in URL_PATTERN.findall(text):
        url = match.strip().strip(").,];")
        if "](" in url:
            url = url.split("](")[0]
        url = re.sub(r"\\([_~])", r"\1", url)
        urls.append(url)
    return urls


def extract_urls():
    url_map = {}
    for path in SOURCE_FILES:
        if path.suffix.lower() == ".docx":
            doc = Document(path)
            text = "\n".join(p.text for p in doc.paragraphs if p.text)
        else:
            text = path.read_text(encoding="utf-8")

        for url in extract_urls_from_text(text):
            url_map.setdefault(url, set()).add(path.name)

    return url_map


def arxiv_pdf_url(url):
    match = re.search(r"arxiv\.org/(abs|html|pdf)/([0-9.]+v?\d*)", url)
    if not match:
        return None
    arxiv_id = match.group(2).rstrip(".")
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"


def is_pdf_url(url):
    parsed = urlparse(url)
    if parsed.path.lower().endswith(".pdf"):
        return True
    if parsed.netloc.endswith("openreview.net") and parsed.path == "/pdf":
        return True
    return False


def slug_from_url(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if "arxiv.org" in parsed.netloc:
        match = re.search(r"(abs|html|pdf)/([0-9.]+v?\d*)", path)
        if match:
            return f"arxiv_{match.group(2).rstrip('.')}"
    if parsed.netloc.endswith("openreview.net") and parsed.path == "/pdf":
        query = parsed.query
        if query.startswith("id="):
            return f"openreview_{query.replace('id=', '')}"
    if path:
        base = path.split("/")[-1]
    else:
        base = parsed.netloc
    base = re.sub(r"\.pdf$", "", base, flags=re.IGNORECASE)
    base = re.sub(r"[^a-zA-Z0-9]+", "_", base).strip("_")
    return f"{parsed.netloc.replace('.', '_')}_{base}" if base else parsed.netloc


def discover_pdf_links(url, timeout=20):
    parsed = urlparse(url)
    if any(
        parsed.netloc == blocked or parsed.netloc.endswith(f".{blocked}")
        for blocked in DISCOVERY_BLOCKLIST
    ):
        return []
    try:
        resp = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "knowledge-library-bot/1.0"},
        )
        resp.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    pdf_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if ".pdf" in href.lower():
            pdf_links.append(urljoin(url, href))
    return list(dict.fromkeys(pdf_links))


def download_pdf(url, dest_path, timeout=30):
    resp = requests.get(
        url, stream=True, timeout=timeout, headers={"User-Agent": "knowledge-library"}
    )
    resp.raise_for_status()
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as fh:
        for chunk in resp.iter_content(chunk_size=1024 * 1024):
            if chunk:
                fh.write(chunk)
    return dest_path


def run_docling(pdf_path, output_dir):
    from docling.document_converter import DocumentConverter
    from docling_core.types.doc import ImageRefMode

    converter = DocumentConverter()
    result = converter.convert(str(pdf_path))
    if result.status.name != "SUCCESS":
        raise RuntimeError(f"docling conversion failed: {result.status}")

    output_dir.mkdir(parents=True, exist_ok=True)
    md_path = output_dir / f"{pdf_path.stem}.md"
    json_path = output_dir / f"{pdf_path.stem}.json"

    result.document.save_as_markdown(md_path, image_mode=ImageRefMode.REFERENCED)
    result.document.save_as_json(json_path, image_mode=ImageRefMode.REFERENCED)
    return md_path, json_path


def _safe_heading_filename(text, max_len=120):
    text = text.strip()
    if not text:
        return "section"
    text = re.sub(r"[\\\\/:*?\"<>|]", "-", text)
    text = re.sub(r"\\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    import hashlib

    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:6]
    return f"{text[:max_len].rstrip()}-{digest}"


def split_markdown_by_heading(markdown_text):
    lines = markdown_text.splitlines()
    chunks = []
    current_heading = "preamble"
    current_lines = []

    def flush():
        if current_lines:
            chunks.append((current_heading, "\n".join(current_lines).strip() + "\n"))

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#"):
            flush()
            current_heading = stripped.lstrip("#").strip() or "section"
            current_lines = [line]
        else:
            current_lines.append(line)

    flush()
    if not chunks:
        chunks.append(("full", markdown_text.strip() + "\n"))
    return chunks


def split_markdown_by_heading_with_levels(markdown_text):
    lines = markdown_text.splitlines()
    chunks = []
    current_heading = "preamble"
    current_level = 1
    current_lines = []

    def flush():
        if current_lines:
            chunks.append(
                {
                    "title": current_heading,
                    "level": current_level,
                    "content": "\n".join(current_lines).strip() + "\n",
                }
            )

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#"):
            flush()
            hashes = len(stripped) - len(stripped.lstrip("#"))
            current_level = hashes
            current_heading = stripped.lstrip("#").strip() or "section"
            current_lines = [line]
        else:
            current_lines.append(line)

    flush()
    if not chunks:
        chunks.append(
            {
                "title": "full",
                "level": 1,
                "content": markdown_text.strip() + "\n",
            }
        )
    return chunks


def write_docling_chunks(docling_dir, md_path):
    chunk_dir = docling_dir / "chunks"
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for old_file in chunk_dir.glob("*.md"):
        old_file.unlink()

    markdown_text = md_path.read_text(encoding="utf-8")
    chunks = split_markdown_by_heading_with_levels(markdown_text)
    toc_entries = []

    for idx, chunk in enumerate(chunks, start=1):
        heading_slug = _safe_heading_filename(chunk["title"])
        chunk_name = f"{idx:02d}-{heading_slug}.md"
        chunk_path = chunk_dir / chunk_name
        chunk_path.write_text(chunk["content"], encoding="utf-8")
        toc_entries.append(
            {
                "title": chunk["title"],
                "level": chunk["level"],
                "chunk_path": str(chunk_path.relative_to(ROOT)),
            }
        )

    toc_md_path = docling_dir / "toc.md"
    toc_json_path = docling_dir / "toc.json"

    lines = ["# Table of Contents", ""]
    for entry in toc_entries:
        indent = "  " * max(entry["level"] - 1, 0)
        title = entry["title"]
        rel_path = entry["chunk_path"]
        lines.append(f"{indent}- [{title}]({rel_path})")
    toc_md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    toc_json_path.write_text(json.dumps(toc_entries, indent=2), encoding="utf-8")
    return toc_md_path, toc_json_path, chunk_dir


async def crawl_to_markdown(url, dest_path):
    config = CrawlerRunConfig(
        word_count_threshold=1,
        cache_mode=CacheMode.BYPASS,
        user_agent="knowledge-library-bot/1.0",
        wait_until="domcontentloaded",
        page_timeout=60000,
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url, config=config)
    if not result.success:
        raise RuntimeError(result.error_message or "crawl failed")

    markdown = ""
    md_obj = getattr(result, "markdown", None)
    if md_obj is None:
        markdown = ""
    elif isinstance(md_obj, str):
        markdown = md_obj
    else:
        markdown = getattr(md_obj, "raw_markdown", None) or getattr(
            md_obj, "markdown_with_citations", ""
        )
    if not markdown.strip():
        raise RuntimeError("empty markdown result")

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(markdown, encoding="utf-8")
    return dest_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-download", action="store_true")
    parser.add_argument("--skip-docling", action="store_true")
    parser.add_argument("--skip-crawl", action="store_true")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    DOCLING_DIR.mkdir(parents=True, exist_ok=True)
    WEB_DIR.mkdir(parents=True, exist_ok=True)

    url_map = extract_urls()

    index_entries = []
    for url, sources in sorted(url_map.items()):
        entry = {
            "source_url": url,
            "source_files": sorted(sources),
            "download_url": None,
            "local_pdf": None,
            "docling_dir": None,
            "local_markdown": None,
            "local_markdown_chunks": [],
            "docling_toc_md": None,
            "docling_toc_json": None,
            "docling_chunks_dir": None,
            "status": "pending",
            "notes": None,
        }

        pdf_url = None
        if is_pdf_url(url):
            pdf_url = url
        else:
            pdf_url = arxiv_pdf_url(url)
            if not pdf_url:
                pdf_links = discover_pdf_links(url)
                if pdf_links:
                    pdf_url = pdf_links[0]

        entry["download_url"] = pdf_url

        if not pdf_url:
            entry["status"] = "skipped_non_pdf"
            entry["notes"] = "no pdf link discovered"
            index_entries.append(entry)
            continue

        slug = slug_from_url(pdf_url)
        pdf_path = PAPERS_DIR / f"{slug}.pdf"
        entry["local_pdf"] = str(pdf_path.relative_to(ROOT))

        if pdf_path.exists():
            entry["status"] = "downloaded_existing"
        elif not args.skip_download:
            try:
                download_pdf(pdf_url, pdf_path)
                entry["status"] = "downloaded"
            except Exception as exc:  # noqa: BLE001
                entry["status"] = "download_failed"
                entry["notes"] = str(exc)

        if entry["status"] in {"downloaded", "downloaded_existing"} and not args.skip_docling:
            try:
                docling_dir = DOCLING_DIR / slug
                md_path = docling_dir / f"{pdf_path.stem}.md"
                json_path = docling_dir / f"{pdf_path.stem}.json"
                if md_path.exists() and json_path.exists():
                    entry["docling_dir"] = str(docling_dir.relative_to(ROOT))
                    entry["status"] = "converted_existing"
                else:
                    run_docling(pdf_path, docling_dir)
                    entry["docling_dir"] = str(docling_dir.relative_to(ROOT))
                    entry["status"] = "converted"
                if md_path.exists():
                    toc_md, toc_json, chunk_dir = write_docling_chunks(
                        docling_dir, md_path
                    )
                    entry["docling_toc_md"] = str(toc_md.relative_to(ROOT))
                    entry["docling_toc_json"] = str(toc_json.relative_to(ROOT))
                    entry["docling_chunks_dir"] = str(chunk_dir.relative_to(ROOT))
            except Exception as exc:  # noqa: BLE001
                entry["status"] = "docling_failed"
                entry["notes"] = str(exc)

        index_entries.append(entry)

    if not args.skip_crawl:
        for entry in index_entries:
            if entry["status"] != "skipped_non_pdf":
                continue
            slug = slug_from_url(entry["source_url"])
            md_path = WEB_DIR / f"{slug}.md"
            entry["local_markdown"] = str(md_path.relative_to(ROOT))
            if md_path.exists():
                entry["status"] = "crawled_existing"
            else:
                try:
                    asyncio.run(crawl_to_markdown(entry["source_url"], md_path))
                    entry["status"] = "crawled"
                except Exception as exc:  # noqa: BLE001
                    entry["status"] = "crawl_failed"
                    entry["notes"] = str(exc)
                    continue

            chunk_dir = WEB_DIR / "chunks" / slug
            chunk_dir.mkdir(parents=True, exist_ok=True)
            for old_file in chunk_dir.glob("*.md"):
                old_file.unlink()
            markdown_text = md_path.read_text(encoding="utf-8")
            chunks = split_markdown_by_heading(markdown_text)
            chunk_paths = []
            for idx, (heading, content) in enumerate(chunks, start=1):
                heading_slug = _safe_heading_filename(heading)
                chunk_name = f"{idx:02d}-{heading_slug}.md"
                chunk_path = chunk_dir / chunk_name
                chunk_path.write_text(content, encoding="utf-8")
                chunk_paths.append(str(chunk_path.relative_to(ROOT)))
            entry["local_markdown_chunks"] = chunk_paths

    with open(INDEX_JSON, "w", encoding="utf-8") as fh:
        json.dump(index_entries, fh, indent=2)

    with open(INDEX_CSV, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "source_url",
                "source_files",
                "download_url",
                "local_pdf",
                "docling_dir",
                "local_markdown",
                "local_markdown_chunks",
                "docling_toc_md",
                "docling_toc_json",
                "docling_chunks_dir",
                "status",
                "notes",
            ],
        )
        writer.writeheader()
        for row in index_entries:
            row = dict(row)
            row["source_files"] = ";".join(row["source_files"])
            row["local_markdown_chunks"] = ";".join(row["local_markdown_chunks"])
            writer.writerow(row)


if __name__ == "__main__":
    main()
