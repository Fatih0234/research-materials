# LLM Trust / Behavioral Econ Knowledge Library

This folder contains a local, structured knowledge library built from two literature reviews about whether LLMs can replicate trust, reciprocity, fairness, and strategic thinking like humans. The goal is to make cited sources easy for AI agents to find, parse, and reuse.

## What's here

- `Literature Review_ Behavioral Economics Experiments and Large Language Models.docx`
- `LLM Trust Bench_ Research & Implementation.md`
- `knowledge_library/`
  - `papers/`   downloaded PDFs
  - `docling/`  Docling outputs for PDFs (`.md`, `.json`, and `_artifacts`)
    - `docling/<slug>/chunks/` heading-based chunks for each PDF
    - `docling/<slug>/toc.md` and `docling/<slug>/toc.json` per-paper table of contents
  - `web/`      crawl4ai markdown for non-PDF sources
    - `web/chunks/` heading-based chunks of crawled pages
  - `index.json` and `index.csv` map citations to local paths
- `tools/build_knowledge_library.py` end-to-end pipeline (download, Docling, crawl, chunk)

## How to use (for AI agents)

1) Start with `knowledge_library/index.json`.
   - Each entry maps a source URL to local files.
   - Use `local_pdf` + `docling_dir` for PDFs.
   - Use `local_markdown` + `local_markdown_chunks` for web sources.

2) Prefer Docling outputs for PDFs.
   - `docling/<slug>/<slug>.md` for text.
   - `docling/<slug>/<slug>.json` for structured content (tables, coordinates, images).
   - `docling/<slug>/<slug>_artifacts/` for extracted images.
   - `docling/<slug>/toc.md` + `docling/<slug>/toc.json` for the paper’s table of contents.
   - `docling/<slug>/chunks/NN-<Exact Subtitle>.md` for section-level content.

3) For web sources, use the chunked markdown files.
   - `web/chunks/<slug>/NN-<Exact Subtitle>.md` follows page headings.
   - This is best for retrieval or agent ingestion.

## Index schema (summary)

Each `index.json` entry includes:
- `source_url`: original citation URL
- `source_files`: which review file cited it
- `download_url`: resolved PDF link (if any)
- `local_pdf`: local PDF path (if downloaded)
- `docling_dir`: Docling output folder (if converted)
- `local_markdown`: crawled markdown for non-PDF sources
- `local_markdown_chunks`: chunked markdown files
- `docling_toc_md`: table of contents for the PDF (markdown)
- `docling_toc_json`: table of contents for the PDF (json)
- `docling_chunks_dir`: folder holding PDF section chunks
- `status`: status flag (`converted_existing`, `crawled_existing`, etc.)
- `notes`: error details, if any

## Pipeline (rebuild)

This project uses `uv` to manage the Python environment.

```bash
uv venv .venv
. .venv/bin/activate
uv pip install docling crawl4ai python-docx
python tools/build_knowledge_library.py
```

Notes:
- `crawl4ai` requires Playwright browsers. If crawling fails, run:
  ```bash
  python -m playwright install
  ```
- The pipeline is idempotent: existing outputs are reused where possible.

## Agent-friendly usage pattern

- Use `index.json` as the single source of truth.
- Choose the best local asset based on task:
  - extraction/summarization from PDFs: Docling `.md` or `.json`
  - browsing site content: web chunks
  - navigating long papers: start at the per-paper TOC, then pull specific chunks only
- Cite local paths (not external URLs) when referencing content.

## Design note for agents

Each paper is treated like a small “book.” The first step should be reading its table of contents (`docling/<slug>/toc.md` or `docling/<slug>/toc.json`) and then selecting only the relevant chunk files from `docling/<slug>/chunks/`. This avoids pulling entire PDFs (including long appendices) into context and keeps retrieval focused.

## Maintenance

- To update citations, edit the two review files and re-run the pipeline.
- If a source is paywalled or blocked, it will appear with a failure status in the index.
