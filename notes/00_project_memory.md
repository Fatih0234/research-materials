# Project Memory: LLM Trust Bench

**Last Updated:** 2026-01-18 (Iteration A complete)

---

## Project Goal

Design and implement **TrustBench**: A replicable experimental framework to answer the central research question:

> **"Do large language model agents trust each other, and how does that compare to humans?"**

This project will produce:
1. **A** - Replicable experiment runner generating JSON/CSV results
2. **B** - GunBench-style static website displaying precomputed results
3. **C** - Academic paper outline with section notes mapped to outputs

---

## Repository Conventions (Learned from README.md)

### Knowledge Library Design
- **Source of truth:** `knowledge_library/index.json` (41 total sources: 28 PDFs converted, 13 web crawled)
- **For PDFs:** Use Docling outputs; start with per-paper TOC (`docling/<slug>/toc.md`), then read only relevant chunks from `docling/<slug>/chunks/`
- **For web sources:** Use chunked markdown from `web/chunks/<slug>/`
- **NEVER** load entire PDFs into context; always use TOC → selective chunk pattern
- **Citation format:** Use LOCAL PATHS (not external URLs)

### Index Schema Key Fields
Each entry contains:
- `source_url`: original citation
- `source_files`: which review cited it
- `local_pdf`, `docling_dir`: for PDF sources
- `local_markdown`, `local_markdown_chunks`: for web sources
- `docling_toc_md`, `docling_toc_json`: per-paper table of contents
- `docling_chunks_dir`: section-level chunks
- `status`: conversion status flag

### Pipeline
- Built with `uv` + Python (docling, crawl4ai, python-docx)
- Idempotent: reuses existing outputs

---

## Initial Scope (Starting Point)

### Focus Game: Trust Game (MVP)
Starting with the classic **Trust Game** (Berg et al., 1995):
- **Player 1 (Investor):** Sends portion of endowment to Player 2
- **Player 2 (Trustee):** Receives tripled amount, decides how much to return
- Measures: trust (amount sent), reciprocity (amount returned)

### Why Trust Game First?
1. **Simple, well-studied** - extensive human baseline data available
2. **Core behavioral construct** - trust/reciprocity fundamental to cooperation
3. **Clear LLM comparisons** - several papers in library test this
4. **Extendable** - can add treatments (framing, roles, repeated play)

### Planned Extensions (Post-MVP)
After Trust Game baseline is stable:
- **LLM-LLM dyads** (pairwise trust matrices)
- **Persona interventions** (role prompts, demographic cues)
- **Repeated games** (study reciprocity evolution)
- **Other games** (Dictator, Ultimatum, Public Goods - if scope allows)

---

## Literature Narrowing Criteria

### What STAYS (Core Papers):
1. **Trust Game implementations** with LLMs (preferably LLM-LLM interactions)
2. **Human vs LLM comparisons** with clear baseline data
3. **Prompting interventions** that affect trust/cooperation (personas, framing, Chain-of-Thought)
4. **Methodological contributions** (sampling strategies, reproducibility practices)
5. **Papers with replicable details** (prompts, parameters, data schemas)

### What GOES (Excluded):
1. Papers on unrelated games (unless they contribute critical methods)
2. Pure theory papers without experiments
3. Studies lacking implementation details
4. Papers focused only on LLM capabilities (not behavioral alignment)
5. Tangential topics (fairness-only, pure mechanism design, etc.) unless directly supporting trust measurement

### Target Shortlist Size:
- **Longlist:** 10–20 papers (initial scan)
- **Core shortlist:** 5–8 papers (detailed extraction)
- **Optional/reference:** 2–4 papers (methods or extensions)

---

## Available Resources

### Primary Inputs
1. **Literature Review (DOCX):** `Literature Review_ Behavioral Economics Experiments and Large Language Models.docx`
2. **Research Plan (MD):** `LLM Trust Bench_ Research & Implementation.md`
3. **Knowledge Library:** 41 sources indexed (28 PDFs, 13 web)

### Key Papers Visible in Index (Sample)
From quick inspection:
- `http://agent-trust.camel-ai.org/` (converted - likely Agent Trust benchmark)
- Multiple arXiv papers (2203.11171, 2301.07543, 2502.03158, 2502.12504, etc.)

---

## Current Status

### Completed (Iteration A):
✅ Read and understood README.md conventions
✅ Inspected knowledge_library/index.json (41 sources, statuses confirmed)
✅ Created directory structure: `notes/`, `notes/papers/`, `plans/`, `specs/`, `results/`, `app/`
✅ Initialized this project memory file

### Next Actions (Iteration B - Literature Narrowing):

**Primary Tasks:**
1. Read the two review files to understand existing literature synthesis:
   - `Literature Review_ Behavioral Economics Experiments and Large Language Models.docx`
   - `LLM Trust Bench_ Research & Implementation.md`

2. Query `index.json` for Trust Game papers:
   - Search for keywords: trust game, investor-trustee, reciprocity, cooperation
   - Identify papers with LLM-LLM interactions
   - Flag papers with human baselines

3. Build `plans/01_paper_shortlist.csv` with columns:
   - `slug` (paper identifier from index)
   - `citation_key_or_title`
   - `game(s)` (Trust, Dictator, Public Goods, etc.)
   - `main_claim`
   - `why_relevant` (to central RQ)
   - `what_to_replicate` (minimal viable replication)
   - `data_available` (Y/N)
   - `methods_extract_path` (local TOC/chunk paths)

4. Apply elimination rules:
   - Prioritize Trust Game studies
   - Keep LLM-LLM interaction papers
   - Retain prompting intervention studies
   - Drop tangential/theory-only papers

5. Mark 5–8 core papers and 2–4 optional papers

**Output:** `plans/01_paper_shortlist.csv` with justified selections

**Stop Condition:** After shortlist is built and documented

---

## Open Questions

*None at this stage - proceeding with defined criteria*

---

## Technical Decisions (Tentative)

### Architecture (Defaults)
- **Offline pipeline:** Runner generates `results/` JSON; website reads static files
- **Reproducibility:** Fixed seeds, record model/version/temp, store full prompts+outputs
- **Start simple:** One-shot Trust Game for MVP
- **Data format:** JSON schema for episodes + aggregated results

### Technology Stack (TBD)
- Runner: Python (likely)
- Website: Static site generator (Hugo/Eleventy style, like GunBench)
- Visualization: D3.js or similar for trust matrices

*These defaults can change if literature reveals better practices*

---

## Work Pattern (Confirmed)

Following strict incremental approach:
1. **One paper at a time** - read TOC first, then selective chunks
2. **Write summaries to disk** after each paper
3. **Update this memory file** after every iteration
4. **Never load full PDFs** unless absolutely required
5. **Cite local paths** in all artifacts

---

## End of Iteration A

**Next Up:** Iteration B - Literature Narrowing
**Next File to Create:** `plans/01_paper_shortlist.csv`
