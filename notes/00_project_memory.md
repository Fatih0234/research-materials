# Project Memory: LLM Trust Bench

**Last Updated:** 2026-01-18 (Iteration B complete - Literature Narrowing)

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

**Completed:** Iteration A - Project initialization and structure
**Next File Created:** `plans/01_paper_shortlist.csv`

---

## Iteration B Outcomes: Literature Narrowing

### Final Paper Shortlist (Created: 2026-01-18)

**Location:** `plans/01_paper_shortlist.csv`

#### CORE Papers (7 selected from 20 candidates):

1. **Xie/Huang et al. (2024) NeurIPS** - Can Large Language Model Agents Simulate Human Trust Behaviors?
   - PRIMARY REPLICATION TARGET
   - Path: `knowledge_library/docling/arxiv_2402.04559/toc.md`
   - Type: llm_llm_interaction | Games: Trust Game, Dictator Game
   - Core Score: 6/6 (2+2+2) - Perfect fit on all axes

2. **Akata et al. (2025) Nature Human Behaviour** - Playing repeated games with large language models
   - Path: `knowledge_library/docling/www_nature_com_s41562_025_02172_y/toc.md`
   - Type: llm_simulates_humans | Games: Prisoner's Dilemma, Battle of the Sexes
   - Core Score: 5/6 - Social Chain-of-Thought prompting technique

3. **Horton (2023)** - Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?
   - Path: `knowledge_library/docling/arxiv_2301.07543/toc.md`
   - Type: methods_tooling | Foundational framework
   - Core Score: 5/6 - Theoretical grounding + methodology

4. **Sreedhar et al. (2025)** - Simulating Cooperative Prosocial Behavior with Multi-Agent LLMs
   - Path: `knowledge_library/docling/arxiv_2502.12504/toc.md`
   - Type: llm_llm_interaction | Game: Public Goods
   - Core Score: 5/6 - Multi-agent coordination and emergent behaviors

5. **Wang et al. (2023)** - Self-Consistency Improves Chain of Thought Reasoning
   - Path: `knowledge_library/docling/arxiv_2203.11171/toc.md`
   - Type: prompting_intervention
   - Core Score: 4/6 - Critical sampling/aggregation technique

6. **Aher et al. (2023) ICML** - Using Large Language Models to Simulate Multiple Humans
   - Path: `knowledge_library/docling/proceedings_mlr_press_aher23a/toc.md`
   - Type: llm_simulates_humans | Games: Milgram, Wisdom of Crowds
   - Core Score: 4/6 - Persona variance and artifact detection

7. **Agarwal et al. (2025)** - Will Systems of LLM Agents Cooperate
   - Path: `knowledge_library/docling/arxiv_2501.16173v1/toc.md`
   - Type: llm_llm_interaction | Game: Iterated Prisoner's Dilemma
   - Core Score: 4/6 - Attitudinal conditioning effects

#### OPTIONAL Papers (7 selected):

1. **Choi et al. (2025)** - Pay What LLM Wants (522 personas) - Real persona grounding
2. **Park et al. (2024)** - Belief-Behavior Consistency in Trust - Trust-specific validation
3. **Akata et al. (2025) IJCAI** - Game Theory + LLMs Survey - Taxonomy reference
4. **Concordia Framework** - GABM architecture patterns
5. **Alekseenko et al. (2025)** - Beauty Contest - Iterative reasoning
6. **Murashige & Ito (2025)** - Ultimatum/Dictator - Fairness controls
7. **BIS Working Paper** - Bank Run simulation (future extension)

### Narrative Arc (Why These Papers)

The selected shortlist tells a coherent story in 6 acts:

1. **Theoretical Foundation (Horton 2023)**: Establishes the concept of *Homo Silicus* and justifies LLMs as implicit models of human economic behavior trained on vast text corpora

2. **Primary Empirical Target (Xie et al. 2024)**: The NeurIPS Trust Game paper is our replication anchor - it tests LLM-LLM trust with BDI reasoning, demographic variations, and human baseline comparisons

3. **Prompting Architecture (Wang, Akata Nature)**: Self-consistency sampling (Wang) provides robust behavioral distributions; Social Chain-of-Thought (Akata) demonstrates how prompting interventions unlock Theory-of-Mind and coordination

4. **Multi-Agent Dynamics (Sreedhar, Agarwal)**: Public goods game (Sreedhar) and iterated PD (Agarwal) extend from dyadic trust to N-player cooperation, showing emergent behaviors and preference plasticity

5. **Validation & Artifacts (Aher ICML, Park belief-behavior)**: Identifies key challenges - hyper-accuracy, hyper-obedience, belief-behavior gaps - that must be monitored when using LLMs as human proxies

6. **Implementation Toolkit (Choi personas, Concordia)**: Provides concrete techniques for persona grounding with real data and multi-agent system architecture

**Result**: A minimal but complete toolkit covering human baselines, LLM-LLM trust, prompting interventions, sampling methods, and validation protocols.

### Platform Decisions

#### OpenRouter for LLM API Calls (DECIDED)

**Choice:** Use OpenRouter as the unified LLM calling layer for the experiment runner.

**Rationale:**
- **Single API key, multiple providers**: Access GPT-4, Claude, Gemini, Llama via one interface
- **Model comparison requirement**: TrustBench must test same prompts across multiple model families
- **Cost efficiency**: Provider arbitrage and usage budgeting built-in
- **Unified schema**: Single request/response format reduces integration complexity
- **Reproducibility**: Consistent API logging for all providers

**Implementation:**
- Runner accepts model parameter format: `openrouter/openai/gpt-4-turbo`, `openrouter/anthropic/claude-3.5-sonnet`
- Store `{provider, model_id, api_version, timestamp}` in results JSON
- Document full prompt + completion for each game episode
- Track token usage and cost per experiment run

**Alternative Considered:** Direct provider APIs (OpenAI SDK, Anthropic SDK, etc.)
- **Rejected because:** Requires maintaining multiple API clients, separate billing, inconsistent schemas

### Gaps Discovered

1. **Limited Direct Human Baseline Data**:
   - Classic Berg et al. (1995) Trust Game human data not directly in corpus
   - Will extract from cited sources in Xie et al. and Horton papers
   - May need to supplement with published experimental economics datasets

2. **Few Pure LLM-LLM Trust Papers**:
   - Only Xie et al. (2024) directly tests LLM-LLM dyadic trust
   - Sreedhar (public goods) and Agarwal (PD) provide N-player cooperation data
   - This scarcity validates our contribution - TrustBench fills a gap

3. **Prompting Standardization**:
   - Papers use varying prompt structures (BDI vs plain text vs JSON schemas)
   - No consensus on persona injection format (narrative vs structured attributes)
   - TrustBench will need to define canonical prompt templates and test sensitivity

4. **Reproducibility Gaps**:
   - Some papers lack full prompt disclosure or exact model versions
   - Temperature/sampling parameters often underspecified
   - Our implementation will enforce strict reproducibility standards

5. **Safety-Economics Tradeoff**:
   - RLHF-aligned models may refuse "ruthless" strategies needed for valid economic simulation
   - Will need roleplay framing or explicit "this is research" context
   - ACL tutorial identified this but no standard solution exists

### Next Steps: Iteration C

**Goal:** Extract detailed paper-by-paper notes for each CORE paper (7 total)

**Deliverables:**
1. Create `notes/papers/<slug>.md` for each core paper
2. Extract and document:
   - Game rules and parameters (endowments, multipliers, rounds)
   - Full prompt templates (system + user messages)
   - BDI reasoning schemas or equivalent
   - Human baseline data and effect sizes
   - Evaluation metrics and aggregation methods
   - Model/version/temperature specifications
   - Data availability and replication notes

**Process:**
- Follow TOC-first pattern: Read `toc.md`, identify relevant sections
- Pull ONLY relevant chunks (Methods, Results, Prompts sections)
- Document extraction in structured markdown with local path citations
- Build reusable extraction template for consistency

**Stop Condition:**
- All 7 core papers have complete extraction notes
- Methods inventory compiled (prompts, schemas, metrics)
- Ready to begin experiment runner design (Iteration D)

---

## End of Iteration B

**Completed:** Literature narrowing with 7 core + 7 optional papers selected
**Created:** `plans/01_paper_shortlist.csv` (20 papers evaluated, scored, classified)
**Updated:** This project memory with shortlist rationale and OpenRouter decision
**Next Up:** Iteration C - Paper-by-paper detailed extraction
