# Iteration A Report: Repo Intake & Memory Bootstrap

**Date:** 2026-01-18
**Status:** ✅ Complete

---

## Objectives

1. ✅ Read README.md and understand repository conventions
2. ✅ Inspect knowledge_library/index.json to assess available sources
3. ✅ Create initial directory structure
4. ✅ Initialize project memory file
5. ✅ Document findings and plan next iteration

---

## Key Findings

### Repository Structure & Conventions

**Knowledge Library Design:**
- **41 total sources** indexed in `knowledge_library/index.json`
  - 28 PDFs (status: `converted_existing`) with Docling outputs
  - 13 web sources (status: `crawled_existing`) with markdown chunks
- **Critical workflow:** Always start with TOC → select specific chunks (NEVER load full PDFs)
- **Citation format:** Use local paths, not external URLs

**Index Schema:**
Each source entry provides:
- Original URL and citation context
- Local file paths (PDFs, Docling outputs, web markdown)
- Per-paper table of contents (`.toc.md` and `.toc.json`)
- Section-level chunks in `chunks/` directories
- Status flags and processing notes

**Pipeline:**
- Python-based (`uv` + docling + crawl4ai + python-docx)
- Idempotent design (reuses existing outputs)

### Sample Sources (First 5)
1. `http://agent-trust.camel-ai.org/` - Converted PDF (likely Agent Trust benchmark)
2. `https://arxiv.org/abs/2203.11171` - Converted PDF
3. `https://arxiv.org/abs/2301.07543` - Converted PDF
4. `https://arxiv.org/abs/2502.03158` - Converted PDF
5. `https://arxiv.org/abs/2502.12504` - Converted PDF

---

## Files Created

### Directory Structure
```
/Volumes/T7/llm-applied-economics/
├── notes/
│   ├── papers/          (for per-paper extractions)
│   └── 00_project_memory.md
├── plans/               (for shortlists and design docs)
├── specs/               (for schemas and specifications)
├── results/             (placeholder for experiment outputs)
└── app/                 (placeholder for website code)
```

### Key File: `notes/00_project_memory.md`

**Contents:**
- **Project goal:** TrustBench - measure LLM-LLM trust vs human baselines
- **Deliverables:** (A) Experiment runner, (B) Static results website, (C) Paper outline
- **Repository conventions learned:** TOC-first pattern, local citations, chunked reading
- **Initial scope:** Trust Game MVP, then extensions (LLM-LLM dyads, personas, repeated play)
- **Literature narrowing criteria:** What stays (Trust Game + LLM-LLM + prompting), what goes (tangential/theory-only)
- **Target shortlist:** 5–8 core papers, 2–4 optional
- **Technical defaults:** Offline pipeline, reproducibility focus, JSON schemas
- **Next actions:** Defined for Iteration B

---

## Decisions Made

### Scope Boundary
- **Start with:** Trust Game (classic 2-player, investor-trustee setup)
- **Why:** Simple, well-studied, extensive human data, clear LLM comparisons possible
- **Post-MVP extensions:** LLM-LLM pairwise matrices, persona interventions, repeated games

### Literature Narrowing Strategy
**Include:**
- Trust Game implementations with LLMs
- Human vs LLM comparison studies
- Prompting interventions affecting trust/cooperation
- Papers with replicable methods and data

**Exclude:**
- Unrelated games (unless critical methods)
- Theory-only papers
- Studies lacking implementation details
- Tangential topics not supporting trust measurement

### Work Pattern Commitment
- One paper at a time
- TOC first, then selective chunks
- Write summaries to disk after each extraction
- Update project memory after every iteration
- NEVER load full PDFs into context

---

## Next Iteration: B - Literature Narrowing

### Inputs to Read
1. `Literature Review_ Behavioral Economics Experiments and Large Language Models.docx`
2. `LLM Trust Bench_ Research & Implementation.md`
3. Query `knowledge_library/index.json` for Trust Game papers

### Tasks
1. Build longlist (10–20 candidate papers)
2. Apply elimination criteria
3. Produce shortlist (5–8 core + 2–4 optional)
4. Create `plans/01_paper_shortlist.csv`

### Output Deliverable
**File:** `plans/01_paper_shortlist.csv`
**Columns:**
- `slug` (paper ID from index)
- `citation_key_or_title`
- `game(s)` (e.g., Trust, Dictator, Public Goods)
- `main_claim`
- `why_relevant` (to central RQ)
- `what_to_replicate` (minimal scope)
- `data_available` (Y/N)
- `methods_extract_path` (local TOC/chunk references)

### Stop Condition
After shortlist CSV is created and documented in project memory.

---

## Open Questions

*None at this stage - criteria are clear*

---

## Summary

✅ **Iteration A successfully completed**
✅ Repository structure and conventions fully understood
✅ Project memory file initialized with clear scope and next steps
✅ Directory scaffolding in place
✅ Ready to proceed with literature narrowing (Iteration B)

**Files to commit:**
- `notes/00_project_memory.md`
- `notes/iteration_a_report.md` (this file)
- Empty directories: `notes/papers/`, `plans/`, `specs/`, `results/`, `app/`
