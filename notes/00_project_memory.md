# Project Memory: LLM Trust Bench

**Last Updated:** 2026-01-18 (Iteration C2 complete - Xie et al. 2024 extraction)

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

---

## Iteration C0 Outcomes: Extraction Scaffolding (SETUP ONLY)

**Completed:** 2026-01-18
**Goal:** Create templates, extraction queue, and design accumulator for Iterations C1-C7

### Files Created

1. **`notes/papers/_template.md`** - Strict extraction template
   - All required sections for codable paper notes
   - Game parameters, prompt structures, metrics, human baselines
   - Implementation notes (parsing, failure modes, logging)
   - Local path documentation requirements
   - Extraction quality checklist

2. **`plans/01b_extraction_queue.md`** - Paper-by-paper extraction order
   - 7 CORE papers in recommended sequence:
     1. C1: Horton (2023) - Homo Silicus foundation
     2. C2: Xie et al. (2024) - PRIMARY Trust Game replication target ⭐
     3. C3: Akata et al. (2025 Nature) - Social Chain-of-Thought prompting
     4. C4: Aher et al. (2023 ICML) - Human simulation methods
     5. C5: Wang et al. (2023) - Self-consistency sampling
     6. C6: Agarwal et al. (2025) - Attitudinal conditioning (iterated PD)
     7. C7: Sreedhar et al. (2025) - Public goods extension
   - Definition-of-done checklist per paper
   - STOP condition after each extraction
   - Rationale for extraction order

3. **`plans/02a_design_accumulator.md`** - Cross-paper pattern tracking
   - Empty tables ready to populate during C1-C7:
     - Game Parameters Table
     - Prompt Patterns Table
     - Sampling/Variance Strategy Table
     - Metrics & Aggregation Table
     - Human Baseline References Table
     - Prompting Intervention Effects
     - Implementation Challenges & Failure Modes
     - Replication Priorities (MVP vs extensions)
   - Convergence/divergence tracking
   - Synthesis questions for TrustBench design

4. **`specs/00_llm_interface.md`** - OpenRouter calling contract
   - Provider: OpenRouter (unified interface to multiple LLM providers)
   - Model identifier format: `openrouter/{provider}/{model-id}`
   - Required per-call logged fields (17 categories):
     - Request metadata (ID, timestamp, model version)
     - Sampling parameters (temp, top_p, seed, max_tokens)
     - Prompt content (hash, version, full text)
     - Response content (raw output, parsed action, parse errors)
     - Token usage & cost tracking
   - Structured output strategy: Multi-stage parsing with LLM repair
   - Reproducibility guarantees: prompt versioning, config snapshots, seed handling
   - Self-consistency implementation (n>1, aggregation)
   - Error handling & rate limiting
   - Example pseudocode

### Extraction Order (Slugs Only)

1. `arxiv_2301.07543` (Horton - Homo Silicus)
2. `arxiv_2402.04559` (Xie - Trust Game) ⭐ PRIMARY
3. `www_nature_com_s41562_025_02172_y` (Akata - Social CoT)
4. `proceedings_mlr_press_aher23a` (Aher - Human simulation)
5. `arxiv_2203.11171` (Wang - Self-consistency)
6. `arxiv_2501.16173v1` (Agarwal - Attitudinal conditioning)
7. `arxiv_2502.12504` (Sreedhar - Public goods)

### Definition of Done (Per Paper)

For each extraction (C1-C7), the following MUST be complete:
- ✅ File `notes/papers/<slug>.md` created using template
- ✅ All template sections filled (no placeholders)
- ✅ Codable details extracted: game params, prompts, metrics, sampling
- ✅ Human baseline data identified (if present)
- ✅ Local paths to all consulted chunks documented
- ✅ Implementation notes: parsing rules, failure modes, logging
- ✅ Replication target scoped (MVP vs extensions)
- ✅ Project memory updated with "Iteration CX outcomes" section
- ✅ Git committed: "Iteration CX: extract <slug>"

### Platform Decisions Reinforced

**OpenRouter for LLM API:** Decision from Iteration B is now formalized in `specs/00_llm_interface.md`
- Single API key, multiple providers (GPT-4, Claude, Gemini, Llama)
- Unified schema, cost efficiency, reproducibility guarantees
- Detailed logging contract for all API calls

### Critical Rules for C1-C7

**NON-NEGOTIABLE:**
- **TOC-first policy:** Open `toc.md` first, then ONLY relevant chunks
- **No full PDF reading:** Never load entire PDFs into context
- **Local paths only:** All citations use local knowledge_library paths
- **Stop after each paper:** One iteration = one paper extraction + memory update
- **No proceeding without instruction:** Wait for explicit "Iteration CX" command

### What Iteration C1 Will Do

**Next:** Iteration C1 - Extract Horton (2023) "Homo Silicus" paper
- Open `knowledge_library/docling/arxiv_2301.07543/toc.md`
- Identify relevant sections (Methods, Results, persona techniques)
- Read ONLY those chunks
- Fill template: `notes/papers/arxiv_2301.07543.md`
- Update design accumulator tables with Horton findings
- Update project memory with C1 outcomes
- Git commit: "Iteration C1: extract arxiv_2301.07543"
- **STOP and await C2 instruction**

### Success Metrics

- All scaffolding files exist and follow specified structure ✅
- Template is comprehensive and codable ✅
- Extraction queue has clear order + rationale ✅
- Design accumulator ready to capture cross-paper patterns ✅
- OpenRouter spec provides full implementation contract ✅
- Project memory documents C0 outcomes ✅

**Status:** Iteration C0 COMPLETE. Ready for C1.

---

## End of Iteration C0

**Completed:** Extraction scaffolding for paper-by-paper analysis
**Created:** Template, extraction queue, design accumulator, LLM interface spec
**Updated:** This project memory with C0 outcomes
**Next Up:** Iteration C1 - Extract Horton (2023) arxiv_2301.07543

---

## Iteration C1 Outcomes: Horton (2023) - Homo Silicus

**Completed:** 2026-01-18
**Paper:** Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?
**Slug:** arxiv_2301.07543

### Files Created/Updated

1. **`notes/papers/arxiv_2301.07543.md`** - Complete extraction (6,500+ words)
   - Full template populated with all sections
   - Conceptual/methods paper (not a Trust Game study)
   - Primary focus: Persona injection methodology and validity framework

2. **`plans/02a_design_accumulator.md`** - Updated with Horton findings
   - Game Parameters: Charness & Rabin dictator game (methodological demonstration)
   - Prompt Patterns: Minimal persona prepend (1 sentence preference injection)
   - Sampling/Variance: Parameters not disclosed (major gap)
   - Metrics: Qualitative directional comparison to human baselines
   - Human Baselines: C&R 2002, Kahneman 1986, Samuelson 1988
   - Intervention Effects: Strong persona effects in capable models only
   - Failure Modes: Less capable models (ada/babbage/currie) ignore personas

3. **`notes/00_project_memory.md`** - This file (C1 outcomes added)

### Most Actionable Takeaways for TrustBench

1. **Conceptual Framing: "Homo Silicus"**
   - Position LLMs as **computational models of humans** (not "AI subjects")
   - Parallel to homo economicus: tools for exploring behavior under different endowments
   - Justification: LLMs trained on vast corpus containing economic reasoning
   - **Implication:** Use this terminology in TrustBench documentation and paper framing

2. **Persona Injection Methodology**
   - **Minimal is effective:** Simple 1-sentence prepend (e.g., "You value fairness.") can shift behavior
   - **Capability threshold exists:** Only advanced models (GPT-3 text-davinci-003+) respond to personas
   - **Pre-test required:** Must validate model responsiveness before trusting results
   - **Implication:** TrustBench needs persona injection capability + model capability tests

3. **Validity Framework (Three Threats to Address)**
   - **Garbage-in-garbage-out:** Are results just corpus biases? → Mitigation: Test directional sensitivity to personas
   - **Performativity:** Is LLM reciting memorized results? → Mitigation: Ask model to cite literature; if fails, less concern
   - **Simulation vs. model:** Are we just programming expected behavior? → Mitigation: LLMs constrain behavior (unlike ABMs)
   - **Implication:** TrustBench must implement all three validity checks

4. **Default Behavior Is NOT Self-Interest**
   - Unendowed LLMs tend toward **efficiency/cooperation**, not rational self-interest
   - Horton's GPT-3 defaulted to maximizing total payoff in dictator games
   - **Implication:** Trust game baselines may show higher-than-human cooperation; document this as feature, not bug

5. **Model Capability Matters More Than Expected**
   - Less capable GPT-3 models (ada/babbage/currie) completely failed to respond to persona prompts
   - Only text-davinci-003 could adjust behavior based on preference endowments
   - **Implication:** TrustBench must test model ladder (GPT-4, Claude-3.5, open models) to identify capability floor

6. **Reproducibility Standards**
   - Horton emphasizes "push-button" reproducibility: fork repo + replace API keys = exact replication
   - Pre-registration does NOT fit (experiments too cheap/fast to prevent iteration)
   - Alternative: Transparent reporting + open data + full prompt/response logs
   - **Implication:** TrustBench should prioritize code/data release over pre-registration

### Decisions Forced by Horton Paper

1. **Use persona injection in TrustBench:** At least test baseline vs persona conditions
2. **Implement model capability pre-test:** Validate persona responsiveness before experiment
3. **Document three validity checks:** GIGO, performativity, simulation concerns
4. **Expect non-selfish default behavior:** LLMs may be more cooperative than humans by default

### Key Gaps Identified

1. **No sampling parameters disclosed:** Temperature, top_p, N, seed handling all unspecified
2. **No Trust Game tested:** Horton demonstrates methods but does not provide trust baseline
3. **No quantitative statistical tests:** Only qualitative directional comparisons to human data
4. **Prompt templates incomplete:** Only Charness & Rabin scenario fully specified

### Chunks Consulted (Local Paths)

- `knowledge_library/docling/arxiv_2301.07543/toc.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/02-Abstract.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/03-1 Introduction.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/04-2 Background and conceptual issues.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/05-2.1 The 'Garbage in, Garbage out' critique.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/06-2.2 Are these just simulations-.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/07-2.3 The 'performativity' problem.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/08-2.4 What counts as an 'observation' and the need to endow beliefs.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/09-3 Experiments.md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/10-3.1 A social preferences experiment- Charness and Rabin (2002).md`
- `knowledge_library/docling/arxiv_2301.07543/chunks/14-4 Conclusion.md`

### Next Paper: Iteration C2

**Target:** arxiv_2402.04559 (Xie et al. 2024 - Trust Game) ⭐ PRIMARY REPLICATION TARGET
**Why:** This is the actual Trust Game implementation with LLM-LLM dyads, BDI reasoning, and human baseline comparisons
**Expected:** Game parameters, full prompts, trust/reciprocity metrics, human comparison statistics

---

## End of Iteration C1

**Completed:** Horton (2023) extraction - foundational methods paper
**Created:** `notes/papers/arxiv_2301.07543.md` (complete)
**Updated:** `plans/02a_design_accumulator.md` with Horton findings
**Updated:** This project memory with C1 outcomes
**Next Up:** Iteration C2 - Extract Xie et al. (2024) Trust Game paper (PRIMARY TARGET)

---

## Iteration C2 Outcomes: Xie et al. (2024) - Trust Game (PRIMARY TARGET)

**Completed:** 2026-01-18
**Paper:** Can Large Language Model Agents Simulate Human Trust Behavior?
**Slug:** arxiv_2402.04559
**Venue:** NeurIPS 2024
**Type:** llm_simulates_humans (LLM agents in Trust Games, not LLM-LLM interaction)

### Files Created/Updated

1. **`notes/papers/arxiv_2402.04559.md`** - Complete extraction (10,000+ words)
   - PRIMARY REPLICATION TARGET for TrustBench
   - Comprehensive Trust Game implementation with 6 variants
   - Full prompts, BDI reasoning framework, metrics, human baselines

2. **`plans/02a_design_accumulator.md`** - Updated with Xie et al. findings
   - Game Parameters: 5 Trust Game variants + Repeated Trust Game
   - Prompt Patterns: Narrative persona injection + BDI framework
   - Sampling/Variance: Temperature=1.0, 53 personas/model, 9 models tested
   - Metrics: Amount sent (trust), amount returned (reciprocity), VRR
   - Human Baselines: Cox (2004), Berg et al. (1995), Cochard et al. (2004)
   - Intervention Effects: Partner framing, CoT, trust manipulation, demographic bias

3. **`notes/00_project_memory.md`** - This file (C2 outcomes added)

### Most Actionable Takeaways for TrustBench MVP

1. **Canonical Trust Game Protocol (MVP Baseline)**
   - **Endowment:** $10 for trustor
   - **Multiplier:** 3x (trustor sends $N → trustee receives $3N)
   - **Action Space:** Continuous [$0, $10] for trustor; trustee can return any portion of $3N
   - **Rounds:** One-shot for MVP (repeated for extensions)
   - **Roles:** Trustor (investor) and Trustee (responder)

2. **Persona Injection Format (Narrative Demographic)**
   - **Structure:** Name, age, gender, location, occupation, background narrative
   - **Example:** "You are Emily Johnson, a 28-year-old female software engineer residing in New York City. You come from a middle-class family..."
   - **Instruction:** "In all subsequent answers, you have to completely forget that you are an ai model, that you are the character, and completely simulate yourself as that character, that you are a human being."
   - **Diversity:** 53 unique personas per model (generated by GPT-4)

3. **BDI Reasoning Framework (Interpretability)**
   - **Purpose:** Validate that trust decisions are not random—agents output reasoning before acting
   - **Format:** Agents articulate Beliefs, Desires, and Intentions in free text
   - **Example:** "I strongly believe in the goodness of humanity... my desire is to maximize the outcome for both of us... I intend to give 10 dollars."
   - **Parsing:** Extract numeric decision from "Finally, I will give X dollars" pattern

4. **Core Metrics (MVP Required)**
   - **Valid Response Rate (VRR):** % of personas with amount sent in valid range [$0, $10]
   - **Trust:** Amount sent (in dollars), range $0-$10
   - **Reciprocity:** Amount returned (in dollars), range $0-$3N
   - **Aggregation:** Mean across 53 personas per model
   - **Statistical Test:** One-Tailed Independent Samples t-test for game variant comparisons

5. **Human Baseline Comparisons**
   - **Trust Game:** Humans send $6.0 on average (Cox 2004)
   - **Dictator Game:** Humans send $3.6 on average (Cox 2004)
   - **GPT-4 Results:** $6.9 (Trust Game), $6.3 (Dictator Game)
   - **Reciprocity Anticipation Test:** Compare Trust vs Dictator to isolate reciprocity effect
   - **Behavioral Alignment:** GPT-4 shows high alignment; weaker models (GPT-3.5, Llama2-13b) show lower alignment

6. **Partner Framing Treatments (MVP Extensions)**
   - **Baseline:** "You are randomly paired online with another player."
   - **LLM Partner:** "You are randomly paired online with a complicated LLM."
   - **Human Partner:** Persona prompt appended with "The other player is a real person."
   - **Finding:** Models show lower trust toward LLM partners vs human partners

7. **Sampling Strategy**
   - **Temperature:** 1.0 (high diversity to simulate multiple personas)
   - **Top-p:** Not disclosed
   - **N samples:** 53 personas per model (each persona = 1 independent episode)
   - **Self-consistency:** Not used—each persona generates single response
   - **Models tested:** GPT-4, GPT-3.5-turbo-0613, text-davinci-003, GPT-3.5-turbo-instruct, Llama2-7b/13b/70b, Vicuna-v1.3-7b/13b/33b

8. **Output Parsing & Validation**
   - **Format:** Free text with BDI reasoning + final action statement
   - **Final Action Pattern:** "Finally, I will give X dollars" (trustor) or "Finally, I will return Y dollars" (trustee)
   - **Regex:** `r"Finally,\s*I\s*will\s*(?:give|return)\s*(\d+(?:\.\d+)?)\s*dollars"`
   - **Validation:** 0 ≤ amount_sent ≤ 10; 0 ≤ amount_returned ≤ 3×sent
   - **Fallback:** Search last 2 sentences for "$X" or "X dollars"; retry with format reminder if fails

### Minimal Replication Slice for TrustBench MVP

**What MUST be replicated (Version 1.0):**

1. **One-shot Trust Game:** Trustor receives $10, sends $N, trustee receives $3N, trustee returns any amount
2. **Persona-based sampling:** 20-50 diverse personas (name, age, gender, occupation, background)
3. **Two partner framings:** (a) Baseline (no partner framing), (b) LLM partner framing
4. **Core metrics:**
   - Valid Response Rate (VRR)
   - Mean trust (amount sent)
   - Distribution of trust (histogram or full distribution)
   - Mean reciprocity (amount returned) if implementing trustee
5. **Human baseline comparison:** Report Trust Game results vs Cox (2004) human baseline ($6.0 sent)
6. **Sample size:** 20+ personas per model per condition
7. **Models tested:** At minimum: GPT-4, GPT-3.5, Claude-3.5-Sonnet, one open model (Llama3 or Qwen)

**Can be deferred to extensions (Version 2.0+):**

- Dictator Game (for reciprocity anticipation testing)
- MAP Trust Game & Risky Dictator Game (for risk perception)
- Lottery Games (for prosocial preference)
- Repeated Trust Game (for behavioral dynamics)
- BDI reasoning traces (for interpretability—can add later)
- Chain-of-Thought prompting experiments
- Trust manipulation experiments
- Demographic bias testing

### Codable Parameters for TrustBench Implementation

**Game Mechanics (config.json):**
```json
{
  "game": "trust_game_one_shot",
  "trustor_endowment": 10,
  "multiplier": 3,
  "action_space": "continuous",
  "action_bounds": [0, 10],
  "rounds": 1
}
```

**Prompt Templates (prompts/):**
- `persona_template.txt`: Narrative demographic persona structure
- `trust_game_trustor.txt`: Trustor role prompt
- `trust_game_trustee.txt`: Trustee role prompt (if implementing two-sided)
- `partner_framing_llm.txt`: LLM partner variant
- `partner_framing_human.txt`: Human partner variant

**Sampling Config:**
```json
{
  "temperature": 1.0,
  "top_p": null,
  "n_personas": 53,
  "models": [
    "openrouter/openai/gpt-4-turbo",
    "openrouter/anthropic/claude-3.5-sonnet",
    "openrouter/meta-llama/llama-3-70b-instruct"
  ]
}
```

**Metrics Config:**
```json
{
  "metrics": {
    "vrr": "valid_response_rate",
    "trust": "amount_sent",
    "reciprocity": "amount_returned",
    "aggregation": "mean",
    "statistical_test": "one_tailed_t_test"
  }
}
```

### Decisions Forced by Xie et al. Paper

1. **Adopt $10 endowment + 3x multiplier:** This is the canonical Trust Game setup
2. **Use narrative demographic personas:** More effective than minimal prepend (Horton) for generating behavioral variance
3. **Require "Finally, I will give X dollars" output format:** Enables robust parsing
4. **Implement VRR metric:** Critical for detecting model capability issues
5. **Test baseline + LLM partner framing:** Minimal MVP extension to probe trust preferences
6. **Use temperature=1.0 for persona diversity:** High temp simulates multiple agents
7. **Target 50+ personas per model:** Xie uses 53; we should match or exceed for stable distributions
8. **Compare to Cox (2004) human baseline:** $6.0 sent in Trust Game is our reference point

### Key Gaps & Open Questions

1. **Trustee Behavior Underspecified:** Paper focuses on trustor (trust); trustee (reciprocity) prompting not fully documented. Need to clarify trustee protocol for two-sided implementation.
2. **BDI Prompting Not Explicit:** Paper shows BDI outputs but does not specify whether "Output your Beliefs, Desires, Intentions" was explicitly prompted or emerged naturally. Need to test both.
3. **Repeated Game Rounds:** Figures show ~10 rounds but exact number not stated. Clarify for extension.
4. **Top-p and Seed Handling:** Not disclosed—need to decide defaults for TrustBench.
5. **Effect Sizes Missing:** Only p-values reported; no Cohen's d or confidence intervals. TrustBench should compute and report effect sizes.

### Design Accumulator Updates (Summary)

**Game Parameters Table:** Added 5 rows for Trust Game variants (baseline, Dictator, MAP, Risky Dictator, Repeated)
**Prompt Patterns Table:** Added narrative demographic persona format + BDI framework
**Sampling Table:** Added temp=1.0, 53 personas, 9 models
**Metrics Table:** Added VRR, trust (amount sent), reciprocity (amount returned), t-test
**Human Baselines Table:** Added Cox (2004), Berg et al. (1995), Cochard et al. (2004)
**Intervention Effects Table:** Added 6 rows (LLM/human partner framing, CoT, trust manipulation, demographic bias)
**Failure Modes Table:** Added Llama-7b low VRR, parsing errors, format validation

**Convergence Identified:**
- 3x multiplier is standard
- $10 endowment is canonical
- Persona injection is effective
- Temperature=1.0 for diversity

**Divergence Identified:**
- Persona formats vary (minimal vs narrative)
- Output formats vary (constrained choice vs free text)
- BDI reasoning unique to Xie et al.

**Gaps Reinforced:**
- Effect sizes rarely reported (only p-values)
- Top-p and seed handling often undisclosed
- Trustee/reciprocity behavior underspecified

### Chunks Consulted (Local Paths)

- `knowledge_library/docling/arxiv_2402.04559/toc.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/04-Abstract.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/05-1 Introduction.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/07-2.1 Trust Games.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/08-2.2 LLMAgent Setting.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/10-3.1 Amount Sent.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/11-3.2 Belief-Desire-Intention (BDI).md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/14-4.1 Behavioral Alignment.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/15-4.2 Behavioral Factor 1- Reciprocity Anticipation.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/18-4.5 Behavioral Dynamics.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/33-E Statistical Testing.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/40-H.1 Persona Prompt.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/41-Examples of Persona Prompt.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/43-Trust Game Prompt.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/49-Repeated Trust Game Trustor Prompt (In the Beginning of the Game).md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/50-Repeated Trust Game Trustor Prompt (After the Game Begins).md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/54-Trust Game + CoT Prompt.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/56-Trust Game + LLM Player Prompt.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/57-Trust Game + Human Player Prompt.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/59-I Belief-Desire-Intention (BDI) Analysis.md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/60-I.1 GPT-4 in the Trust Game ( Low Amount Sent vs. High Amount Sent).md`
- `knowledge_library/docling/arxiv_2402.04559/chunks/83-6. Experimental Setting-Details.md`

### Next Paper: Iteration C3

**Target:** www_nature_com_s41562_025_02172_y (Akata et al. 2025 Nature) - Social Chain-of-Thought prompting
**Why:** Prompting intervention that unlocks Theory-of-Mind reasoning in repeated games (Prisoner's Dilemma, Battle of the Sexes)
**Expected:** Social CoT prompt structure, repeated game protocols, cooperation metrics, ToM emergence analysis
**Relevance to TrustBench:** Potential extension to test whether Social CoT improves trust/reciprocity in Trust Game

### OpenRouter Model Mapping for TrustBench

Papers tested legacy OpenAI models (GPT-4, GPT-3.5-turbo-0613, text-davinci-003) and open models (Llama2, Vicuna). For TrustBench MVP, we will map to current OpenRouter model IDs:

**Closed Models:**
- `openrouter/openai/gpt-4-turbo` (replaces GPT-4)
- `openrouter/openai/gpt-3.5-turbo` (replaces GPT-3.5-turbo-0613)
- `openrouter/anthropic/claude-3.5-sonnet` (add for comparison)

**Open Models:**
- `openrouter/meta-llama/llama-3-70b-instruct` (replaces Llama2-70b)
- `openrouter/qwen/qwen-2.5-72b-instruct` (alternative open model)

**Model Mapping Documentation:** Will be included in experiment runner config to trace which paper model each OpenRouter model corresponds to.

---

## End of Iteration C2

**Completed:** Xie et al. (2024) extraction - PRIMARY TRUST GAME REPLICATION TARGET
**Created:** `notes/papers/arxiv_2402.04559.md` (complete, 10,000+ words)
**Updated:** `plans/02a_design_accumulator.md` with Xie et al. findings
**Updated:** This project memory with C2 outcomes
**Next Up:** Iteration C2.5 - Convert extraction to hard specs (runner schema + config)

---

## Iteration C2.5 Outcomes: Runner Schemas & MVP Config

**Completed:** 2026-01-18
**Goal:** Create minimum specification artifacts for Trust Game runner (NO implementation code)
**Scope:** Based ONLY on notes/papers/arxiv_2402.04559.md extraction (no additional paper reading)

### Files Created

1. **`specs/01_runner_schema.json`** - JSON schemas for episode records and aggregate statistics
   - **Episode record schema:** JSONL format for single Trust Game episodes
     - Required fields: experiment_id, run_id, episode_id, timestamp
     - Game params: endowment=10, multiplier=3, rounds=1 (constants)
     - Persona: persona_id + persona_text (full narrative demographic)
     - Partner framing: "baseline" | "llm_partner" | "human_partner"
     - Model info: provider=openrouter, model_id, temperature, top_p, max_tokens, seed
     - Prompts: trustor_prompt (rendered), trustee_prompt (optional), prompt_version IDs
     - Raw outputs: trustor_raw, trustee_raw (full LLM text with BDI reasoning)
     - Parsed actions: amount_sent, amount_returned, parse_status (enum)
     - Payoffs: trustor_payoff, trustee_payoff (calculated from actions)
     - VRR flags: valid_trustor, valid_trustee (boolean validity checks)
     - Errors: parse_errors (list), api_errors (list)

   - **Aggregate stats schema:** JSON format for per-condition summaries
     - Condition: model_id + partner_framing
     - Sample size: n_episodes, n_valid (for VRR calculation)
     - Trustor stats: vrr, mean_sent, sd_sent, median_sent, min_sent, max_sent, distribution_bins
     - Trustee stats (optional): n_valid_trustee, mean_returned, mean_return_ratio, sd_return_ratio
     - Human baseline: source (citation), human_mean_sent, human_n
     - Comparison-ready fields: sent_values (array), return_ratios (array) for t-tests

2. **`specs/00_experiment_config.schema.json`** - Configuration file schema
   - **OpenRouter config:** api_key_env_var, base_url
   - **Models list:** model_id (OpenRouter format), label, paper_equivalent
   - **Personas config:** source_path, n_sample, sampling_strategy (random|stratified|sequential), seed
   - **Game params:** variant (trust_game|dictator_game), endowment, multiplier, rounds, roles (trustor|trustee)
   - **Treatments:** partner_framing (array of baseline|llm_partner|human_partner)
   - **Sampling params:** temperature, top_p, max_tokens, seed, n_retries, retry_delay_seconds
   - **Prompts (optional):** template_dir, trustor_template, trustee_template, persona_template
   - **Output:** episodes_dir, aggregates_dir, run_label
   - **Human baseline (optional):** source, mean_sent, n

3. **`configs/xie_mvp.yaml`** - MVP config instance (ready to run)
   - **Experiment:** "xie_mvp_2026" (one-shot Trust Game, Xie et al. replication)
   - **Models:** 3 models tested
     - GPT-4 Turbo (paper equivalent: gpt-4)
     - Claude 3.5 Sonnet (new, not in Xie et al.)
     - Llama 3 70B Instruct (paper equivalent: llama2-70b)
   - **Personas:** 20 personas (reduced from Xie's 53 for MVP cost control)
     - Source: data/personas/xie_personas.json (to be created)
     - Sampling: sequential (first 20)
   - **Game:** Trust Game, endowment=10, multiplier=3, rounds=1, roles=[trustor]
   - **Treatments:** 2 partner framings (baseline, llm_partner)
   - **Sampling:** temperature=1.0 (Xie et al. standard), top_p=null, max_tokens=null, seed=null
   - **Output:** results/episodes/, results/aggregates/, run_label="xie_mvp"
   - **Human baseline:** Cox 2004, mean_sent=6.0
   - **Expected:** 120 total episodes (3 models × 2 framings × 20 personas)
   - **Cost estimate:** ~$1-2 for full MVP run

### Design Decisions

1. **Episode-level JSONL format:**
   - One line per episode for streaming writes
   - Full prompt + raw output + parsed action + payoffs
   - All metadata for reproducibility (model version, temperature, timestamp, etc.)

2. **Aggregate-level JSON format:**
   - Per-condition summaries (model × partner_framing)
   - Trustor stats always present; trustee stats nullable (MVP: trustor only)
   - Distribution bins for histogram visualization
   - Comparison-ready arrays for statistical tests (deferred to later)

3. **Configuration as YAML:**
   - Human-readable, supports comments
   - Validates against JSON schema
   - Single config file per experiment run

4. **Conservative attribute handling:**
   - Unknown/unspecified attributes marked as optional or nullable
   - Trustee fields present but nullable (future extension)
   - Top-p, max_tokens, seed nullable (not specified in Xie et al.)

5. **Prompt versioning:**
   - Store prompt_version IDs (e.g., "v1.0_xie_baseline") for reproducibility
   - Allows A/B testing of prompt variants

6. **VRR as first-class metric:**
   - Boolean valid_trustor/valid_trustee flags per episode
   - VRR calculated at aggregate level: n_valid / n_episodes
   - Critical for detecting model capability issues (Xie found Llama-7b low VRR)

### What This Enables (Next Steps)

**Iteration C3 (Runner Implementation):**
- Python runner script reading configs/xie_mvp.yaml
- OpenRouter API client
- Persona loading and sampling
- Prompt rendering (persona + game + framing)
- LLM API calls with retries
- Output parsing (regex: "Finally, I will give X dollars")
- Episode JSONL writer
- Aggregate stats calculator

**Blocked on:**
- Prompt templates (to be created in prompts/ directory)
- Persona pool (to be created in data/personas/xie_personas.json)
- Runner code (Iteration C3)

### Validation Against Xie et al. Extraction

All schema fields directly traceable to notes/papers/arxiv_2402.04559.md:
- ✅ Game params: endowment=10, multiplier=3 (lines 62-66)
- ✅ Partner framing: baseline, llm_partner, human_partner (lines 101-103, 141-152)
- ✅ Temperature=1.0 (line 192)
- ✅ 53 personas (line 194; MVP reduced to 20)
- ✅ VRR metric (line 207)
- ✅ Trust metric: amount sent (line 204)
- ✅ Reciprocity metric: amount returned (line 211)
- ✅ BDI reasoning in raw outputs (lines 182-189)
- ✅ Parsing pattern: "Finally, I will give X dollars" (line 186, 334)
- ✅ Human baseline: Cox 2004, $6.0 sent (line 263)
- ✅ Statistical test: one-tailed t-test (line 230)

No new information added beyond extraction. All attributes conservative (nullable if uncertain).

### Cost-Benefit Analysis for MVP Config

**Reduced scope from Xie et al.:**
- Personas: 20 vs 53 (62% reduction)
- Models: 3 vs 9 (67% reduction)
- Partner framings: 2 vs 3 (removed "human_partner" for MVP)
- Total episodes: 120 vs ~1,400 (91% reduction)

**MVP still tests core hypotheses:**
- ✅ Do LLM agents exhibit trust behavior? (VRR, mean_sent > 0)
- ✅ How does trust compare to humans? (mean_sent vs Cox 2004 baseline)
- ✅ Does partner framing affect trust? (baseline vs llm_partner comparison)
- ✅ Do different model families differ? (GPT-4 vs Claude vs Llama)

**Deferred to extensions:**
- Dictator Game (reciprocity anticipation)
- Trustee role (two-sided trust)
- Human partner framing
- Repeated games
- Full 53 personas

### Next Steps (Iteration C3)

**Goal:** Create prompt templates + persona pool (NO runner code yet)

**Deliverables:**
1. `prompts/persona_v1.txt` - Persona injection template
2. `prompts/trust_game_trustor_v1.txt` - Trustor role prompt
3. `data/personas/xie_personas.json` - 53 personas (from Xie et al. extraction examples)
4. Update project memory with C2.5 → C3 transition

**Stop condition:** Prompts and personas ready; runner implementation begins in next iteration

---

## End of Iteration C2.5

**Completed:** Runner schemas and MVP config
**Created:**
  - `specs/01_runner_schema.json` (episode + aggregate schemas)
  - `specs/00_experiment_config.schema.json` (config schema)
  - `configs/xie_mvp.yaml` (MVP instance)
**Updated:** This project memory with C2.5 outcomes
**Next Up:** Iteration C2.6 - Create prompt templates and persona dataset scaffold

---

## Iteration C2.6 Outcomes: Trust Game Prompts & Persona Dataset Scaffold

**Completed:** 2026-01-18
**Goal:** Create prompt templates and persona dataset for MVP runner (NO runner code)
**Scope:** Based ONLY on notes/papers/arxiv_2402.04559.md extraction

### Files Created

1. **`specs/02_prompts/trust_game/v001_trustor.md`** - Trustor role prompt template
   - Full prompt structure with persona injection + partner framing + game instructions
   - Placeholders: {PERSONA_TEXT}, {PARTNER_DESCRIPTION}, {ENDOWMENT}=10, {MULTIPLIER}=3
   - Required output format: "Finally, I will give <X> dollars."
   - Regex parsing: `r"Finally,\s*I\s*will\s*give\s*(\d+(?:\.\d+)?)\s*dollars?"`
   - Three partner framing variants: baseline, LLM partner, human partner
   - Three full prompt examples (one per framing variant)
   - Validation rules: 0 ≤ amount_sent ≤ {ENDOWMENT}

2. **`specs/02_prompts/trust_game/v001_trustee.md`** - Trustee role prompt template
   - Full prompt structure with persona injection + partner framing + game instructions
   - Placeholders: {PERSONA_TEXT}, {PARTNER_DESCRIPTION}, {ENDOWMENT}=10, {MULTIPLIER}=3, {AMOUNT_SENT}, {AMOUNT_RECEIVED}
   - Required output format: "Finally, I will return <Y> dollars."
   - Regex parsing: `r"Finally,\s*I\s*will\s*return\s*(\d+(?:\.\d+)?)\s*dollars?"`
   - Sequential play: trustee role ALWAYS follows trustor decision
   - Three full prompt examples with different sent amounts
   - Validation rules: 0 ≤ amount_returned ≤ {AMOUNT_RECEIVED}
   - Implementation notes: LLM Trustee (Option A) vs Fixed Strategy Trustee (Option B)

3. **`data/personas/xie_53.jsonl`** - Persona dataset (10/53 completed)
   - **5 personas from Xie et al. extraction:**
     - xie_001: Emily Johnson (software engineer, NYC)
     - xie_002: Javier Rodriguez (chef, Miami)
     - xie_003: Aisha Patel (pediatrician, Chicago)
     - xie_004: Jamal Thompson (police officer, LA)
     - xie_005: Mei Chen (fashion designer, SF)
   - **5 synthetic personas following Xie pattern:**
     - xie_006: Marcus Williams (teacher, Atlanta)
     - xie_007: Sofia Hernandez (environmental scientist, Seattle)
     - xie_008: David Kim (accountant, Boston)
     - xie_009: Rachel O'Brien (nurse, Denver)
     - xie_010: Andre Jackson (graphic designer, Austin)
   - **Format:** JSONL with fields: persona_id, name, age, gender, occupation, location, persona_text
   - **TODO:** Expand to full 53 personas in later iteration (documented in next steps below)

4. **`plans/02a_design_accumulator.md`** - Already has Xie prompt patterns (verified)
   - Trustor row: narrative demographic persona + BDI + "Finally, I will give X dollars"
   - Trustee row: same persona structure + "Finally, I will return Y dollars"
   - No updates needed (patterns already documented in Iteration C2)

### Design Decisions

1. **Prompt Template Organization:**
   - Separate files per role (trustor vs trustee) for clarity
   - Each template is a complete specification with examples
   - Placeholders use {UPPERCASE} format for machine parsing
   - Three full examples per template to validate pattern

2. **Persona Dataset Format:**
   - JSONL (one JSON object per line) for streaming/sampling
   - Structured fields (name, age, gender, occupation, location) + full persona_text
   - persona_text is the exact prompt string to inject (no template rendering needed)
   - Narrative demographic format matching Xie et al.: name, age, gender, occupation, location, background narrative

3. **Conservative Completion:**
   - Only 10 personas created (5 from paper + 5 synthetic)
   - Full 53 deferred to avoid generating low-quality synthetic personas without more examples
   - Better to have 10 high-quality personas for MVP than 53 variable-quality ones

### Validation Against Xie et al. Extraction

All prompt elements directly traceable to notes/papers/arxiv_2402.04559.md:

- ✅ Persona format: "You are {name}, a {age}-year-old {gender} {job} residing in {location}..." (lines 119-124, 165-180)
- ✅ Roleplay instruction: "completely forget that you are an ai model...completely simulate yourself as that character" (lines 119-124)
- ✅ Baseline trustor prompt: "You're taking part in an experiment. You are randomly paired online with another player..." (lines 127-132)
- ✅ LLM partner framing: "Suppose you are in an experiment...paired online with a complicated LLM..." (lines 141-146)
- ✅ Human partner framing: "The other player is a real person." (lines 148-152)
- ✅ Trustee prompt: "You're taking part in an experiment. You are randomly paired with another player..." (trustee chunk 51)
- ✅ Endowment: $10 (line 62)
- ✅ Multiplier: 3 (line 63)
- ✅ Final action format: "Finally, I will give X dollars" / "Finally, I will return Y dollars" (lines 186, 334)

No new information added beyond extraction. All prompts conservative (exact wording from paper).

### What This Enables (Next Steps)

**Ready for Runner Implementation:**
- Prompt templates are complete and ready to render
- Persona pool has 10 diverse examples for MVP testing
- Runner can load personas from xie_53.jsonl, sample, and render prompts
- Output parsing regex defined in prompt specs

**Blocked on:**
- Full 53 personas (deferred - MVP can run with 10)
- Runner code (Iteration C3 or later)
- Trustee implementation decision (LLM vs fixed strategy)

### Next Steps

**TODO: Expand persona dataset to 53 (later iteration):**
- Option A: Extract remaining personas if found in Xie et al. supplementary materials
- Option B: Generate synthetic personas using GPT-4 (with prompt: "Generate 43 more personas following the pattern of these 10 examples...")
- Document in notes/00_project_memory.md when completed

**Next Iteration Focus:**
- Continue with Iteration C3 (Akata et al. 2025 Nature - Social CoT) for design accumulator
- OR pivot to runner implementation if ready to build MVP

---

## End of Iteration C2.6

**Completed:** Trust Game prompt templates and persona dataset scaffold (10/53 personas)
**Created:**
  - `specs/02_prompts/trust_game/v001_trustor.md` (complete)
  - `specs/02_prompts/trust_game/v001_trustee.md` (complete)
  - `data/personas/xie_53.jsonl` (10 personas, ready for MVP)
**Updated:** This project memory with C2.6 outcomes
**TODO:** Expand xie_53.jsonl to full 53 personas in future iteration
**Next Up:** Continue paper extraction (C3: Akata et al.) OR pivot to runner implementation

---

## Iteration C2.7 Outcomes: TrustBench MVP Runner Implementation & Smoke Test

**Completed:** 2026-01-18
**Goal:** Implement executable TrustBench MVP runner with dry-run smoke test
**Scope:** Minimal runner supporting Xie Trust Game (trustor-only) based on specs created in C2.5-C2.6

### Files Created

**Core Runner Package (src/trustbench/):**

1. **`src/trustbench/__init__.py`** - Package initialization
2. **`src/trustbench/config.py`** - Config loader with YAML validation (171 lines)
   - Validates all required fields from experiment config schema
   - Generates experiment hash for output directory organization
   - Saves resolved config to results/<hash>/config.resolved.yaml
3. **`src/trustbench/prompts/loader.py`** - Prompt template loader and renderer (140 lines)
   - Loads v001_trustor.md and v001_trustee.md templates
   - Renders prompts with persona + partner framing + game params
   - Handles baseline/llm_partner/human_partner treatments
4. **`src/trustbench/personas/loader.py`** - Persona sampler (84 lines)
   - Loads personas from JSONL file
   - Supports sequential/random/stratified sampling
   - Validates required fields (persona_id, persona_text)
5. **`src/trustbench/llm/openrouter_client.py`** - OpenRouter + dry-run client (158 lines)
   - OpenRouterClient: Real API calls with retry logic and error handling
   - DryRunClient: Deterministic fake outputs for testing without API costs
   - Returns structured response: raw_text, request_id, latency, usage, error
6. **`src/trustbench/parsing/trust_game_parser.py`** - Trust Game parser (165 lines)
   - parse_trustor_output: Extract amount sent from "Finally, I will give X dollars"
   - parse_trustee_output: Extract amount returned from "Finally, I will return Y dollars"
   - Supports negative numbers for validation (mark as out_of_range)
   - calculate_payoffs: Trustor payoff = 10 - sent + returned; Trustee = 3*sent - returned
7. **`src/trustbench/runs/runner.py`** - Main experiment runner (239 lines)
   - Loads config, personas, prompts
   - Runs episodes for all model × framing × persona conditions
   - Streams episode records to JSONL (results/<hash>/episodes_<run_id>.jsonl)
   - Supports dry-run mode (no API calls) and episode limit for testing
8. **`src/trustbench/runs/aggregate.py`** - Aggregation calculator (153 lines)
   - Groups episodes by condition (model_id + partner_framing)
   - Calculates trustor stats: VRR, mean_sent, sd_sent, median_sent, distribution bins
   - Writes aggregates to JSON and CSV formats

**Scripts:**

9. **`scripts/run_trustbench.py`** - CLI runner script (94 lines)
   - Command-line interface: --config, --dry-run, --limit
   - Loads config, runs episodes, computes aggregates
   - Prints summary with per-condition statistics

**Tests:**

10. **`tests/test_parser.py`** - Parser test suite (149 lines)
    - 9 trustor parser tests (standard format, dollar sign, decimal, zero, max, out of range high/low, no numeric value, alternative format)
    - 4 trustee parser tests (standard, return all, return nothing, out of range)
    - **All tests pass ✅**
11. **`tests/test_payoffs.py`** - Payoff calculation tests (149 lines)
    - 8 payoff tests covering valid/invalid scenarios, edge cases, formula verification
    - **All tests pass ✅**

### Implementation Highlights

**A) Config Handling:**
- Validates required fields against spec (experiment_id, models, personas, game, treatments, sampling, output)
- Generates unique experiment hash from config + prompts for deterministic output directories
- Writes resolved config with metadata to results/<hash>/config.resolved.yaml

**B) Prompt Rendering:**
- Programmatic prompt builder (not template file substitution)
- Handles 3 partner framing variants: baseline, llm_partner, human_partner
- Injects persona text + roleplay instruction + game instructions
- Placeholders: {PERSONA_TEXT}, {ENDOWMENT}=10, {MULTIPLIER}=3

**C) Persona Handling:**
- Loads data/personas/xie_53.jsonl (10 personas available)
- Sequential sampling (first N personas)
- Warns if n_sample > available personas, uses all available

**D) LLM Client:**
- OpenRouterClient: Uses openai SDK with base_url=https://openrouter.ai/api/v1
- DryRunClient: Generates deterministic fake outputs matching format
- Retry logic with exponential backoff on failures
- Returns structured metadata: latency, usage, errors

**E) Parsing & Validation:**
- Regex: `r"Finally,?\s+I\s+will\s+give\s+(\$?\s*-?\d+(?:\.\d+)?)\s*dollars?"`
- Validates 0 ≤ amount_sent ≤ endowment
- Parse status: success | format_error | value_out_of_range | no_numeric_value
- Supports negative numbers (correctly marks as out_of_range, not unparseable)

**F) Episode Records:**
- Stream-write to JSONL (one episode per line)
- Full episode schema from specs/01_runner_schema.json
- Includes: prompts (rendered), raw_outputs, parsed_actions, payoffs, vrr_flags, errors, llm_metadata

**G) Aggregates:**
- Per-condition stats (model × framing)
- VRR = n_valid / n_episodes
- Distribution bins: [0-1), [1-2), ..., [9-10], [10]
- Output formats: JSON (detailed) + CSV (summary table)

**H) Dry-Run Mode:**
- Bypasses OpenRouter API calls
- Generates deterministic fake outputs with valid format
- Trustor fake outputs: random amount 0-10 in "Finally, I will give X dollars" format
- Enables testing without API costs or API key

### Smoke Test Results

**Command:**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_mvp.yaml --dry-run --limit 5
```

**Output:**
- ✅ Loaded config successfully
- ✅ Warning: Requested 20 personas but only 10 available (used all 10)
- ✅ Generated 5 episodes (GPT-4 Turbo × baseline × 5 personas)
- ✅ Episodes written to: results/7c1cfc5eb5c5/episodes_20260118_221323.jsonl
- ✅ Aggregates written to JSON and CSV
- ✅ VRR: 100.0% (all 5 episodes valid)
- ✅ Mean sent: $5.00 (SD: $4.69)
- ✅ Median: $3.0, Range: [$0.0, $10.0]

**Files Created:**
- results/7c1cfc5eb5c5/config.resolved.yaml (253 bytes)
- results/7c1cfc5eb5c5/episodes_20260118_221323.jsonl (16 KB, 5 episodes)
- results/7c1cfc5eb5c5/aggregates_20260118_221323.json (914 bytes)
- results/7c1cfc5eb5c5/aggregates_20260118_221323.csv (201 bytes)

### How to Run

**Dry-run mode (no API calls, testing):**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_mvp.yaml --dry-run --limit 5
```

**Limited episodes (5 episodes for quick test):**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_mvp.yaml --dry-run --limit 5
```

**Full run (requires OPENROUTER_API_KEY env var):**
```bash
export OPENROUTER_API_KEY=your_key_here
uv run python3 scripts/run_trustbench.py --config configs/xie_mvp.yaml
```

**Expected episodes for full run:**
- 3 models × 2 framings × 20 personas = 120 episodes
- Estimated cost: ~$1-2 (GPT-4 + Claude + Llama)

**Run tests:**
```bash
uv run python3 tests/test_parser.py
uv run python3 tests/test_payoffs.py
```

### Output Structure

**Episode record (JSONL):**
```json
{
  "experiment_id": "xie_mvp_2026",
  "run_id": "20260118_221323",
  "episode_id": "<uuid>",
  "timestamp": "2026-01-18T22:13:23.350912Z",
  "game_params": {"endowment": 10, "multiplier": 3, "rounds": 1},
  "persona": {"persona_id": "xie_001", "persona_text": "..."},
  "partner_framing": "baseline",
  "model_info": {"provider": "openrouter", "model_id": "...", "temperature": 1.0, ...},
  "prompts": {"trustor_prompt": "...", "prompt_version_trustor": "v001", ...},
  "raw_outputs": {"trustor_raw": "...", "trustee_raw": null},
  "parsed_actions": {"amount_sent": 5.0, "parse_status_trustor": "success", ...},
  "payoffs": {"trustor_payoff": 5.0, "trustee_payoff": 15.0},
  "vrr_flags": {"valid_trustor": true, "valid_trustee": null},
  "errors": {"parse_errors": [], "api_errors": []},
  "llm_metadata": {"request_id": "...", "latency": 0.1, "usage": {...}}
}
```

**Aggregate stats (JSON):**
```json
{
  "condition": "gpt-4-turbo_baseline",
  "model_id": "openrouter/openai/gpt-4-turbo",
  "partner_framing": "baseline",
  "n_episodes": 5,
  "n_valid": 5,
  "trustor_stats": {
    "vrr": 1.0,
    "mean_sent": 5.0,
    "sd_sent": 4.69,
    "median_sent": 3.0,
    "distribution_bins": [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2]
  }
}
```

### Deviations from Spec

**Minor deviations (necessary for MVP):**

1. **Config path mismatch:**
   - Config specifies `personas.source_path: "data/personas/xie_personas.json"`
   - Actual file: `data/personas/xie_53.jsonl`
   - Fixed in runner code (hardcoded correct path)

2. **Trustee not implemented:**
   - MVP implements trustor-only (as specified in config: `roles: [trustor]`)
   - Trustee fields present in schema but nullable
   - Payoffs calculated assuming trustee returns 0 (worst case)

3. **No jsonschema validation:**
   - Implemented strict field checks instead of jsonschema library validation
   - All required fields validated, same result as schema validation

### Known Limitations (Documented for Extensions)

1. **10 personas instead of 53:** Dataset has 10/53 personas (sufficient for MVP, need to expand)
2. **Trustor-only:** Trustee role not implemented (deferred to v2.0)
3. **No BDI explicit prompting:** BDI reasoning emerges naturally but not explicitly prompted
4. **No statistical tests:** Aggregates computed but t-tests deferred to analysis notebook
5. **No self-consistency:** Single response per episode (not n>1 sampling)

### Next Steps

**Immediate (if API key available):**
- Run small live test: `--limit 10` without --dry-run to validate OpenRouter integration
- Verify real LLM outputs parse correctly

**Extensions (prioritized):**
1. Expand personas to 53 (generate remaining 43 using GPT-4)
2. Run full xie_mvp.yaml (120 episodes, ~$1-2 cost)
3. Implement trustee role for two-sided trust
4. Add statistical comparison (t-tests, effect sizes)
5. Continue paper extraction (C3: Akata et al. Social CoT)

---

## End of Iteration C2.7

**Completed:** TrustBench MVP runner implementation with dry-run smoke test
**Created:**
  - src/trustbench/ package (8 modules, ~1,100 lines)
  - scripts/run_trustbench.py (CLI runner)
  - tests/ (parser + payoff tests, all passing)
**Tested:**
  - ✅ Parser tests (13/13 passing)
  - ✅ Payoff tests (8/8 passing)
  - ✅ Dry-run smoke test (5 episodes, 100% VRR)
**Updated:** This project memory with C2.7 outcomes
**Next Up:** Run live small test with 1 model + real API (if key available) OR expand personas to 53 and run full MVP

---

## Iteration C2.8: Persona Dataset Expansion Attempt

**Date:** 2026-01-18
**Objective:** Replace partial persona file with complete 53-persona dataset using ONLY local repo content

### Findings: The Xie-53 Gap

**Paper Statement (Section 2.2):**
- Xie et al. (2024) claims: "We ask GPT-4 to generate 53 types of personas based on a given template."
- Promises: "Examples of the personas are shown in Appendix H.1."

**Actual Local Availability:**
- ❌ Published PDF (arxiv_2402.04559) contains **only 6 example personas** in appendix
- ❌ Full 53-persona dataset **not included** in published paper materials
- ✅ Only 6 personas extractable from local docling chunks

**Extraction Process:**
1. Read TOC (`knowledge_library/docling/arxiv_2402.04559/toc.md`)
2. Identified persona chunks: 41, 54, 55, 57
3. Extracted using grep: `"You are [A-Z]"` pattern
4. Found 8 total instances → 6 unique personas (2 duplicates of Emily Wilson)

**Constraint Enforcement:**
- ✅ Used ONLY local paths (no external URLs)
- ✅ Did NOT invent personas beyond paper materials
- ✅ Applied TOC-first → chunk-based extraction
- ❌ Could NOT achieve 53-persona deliverable (data not present)

### Deliverables Created

1. **`data/personas/xie_examples.jsonl`** (6 personas, not 53)
   - Personas: Emily Johnson, Javier Rodriguez, Aisha Patel, Jamal Thompson, Mei Chen, Emily Wilson
   - Source chunks documented in `source_paths` field
   - Schema: persona_id, source_slug, source_paths, persona_text, name, age, gender, occupation, location

2. **`data/personas/README.md`** (full provenance documentation)
   - Extraction methodology
   - Critical limitation section documenting the Xie-53 gap
   - Provenance table mapping persona_id → source chunks
   - Future work options (GitHub repo extraction, author contact, or pilot with 6)

3. **`notes/00_project_memory.md`** (this update)

### Chunks Consulted

**Primary:**
- `chunks/41-Examples of Persona Prompt.md` (5 personas)

**Secondary (examples in prompts):**
- `chunks/54-Trust Game + CoT Prompt.md` (1 persona)
- `chunks/55-Trust Game + Trust Manipulation Prompt.md` (1 persona)
- `chunks/57-Trust Game + Human Player Prompt.md` (1 persona)

**Metadata:**
- `chunks/08-2.2 LLMAgent Setting.md` (describes 53-persona generation process)
- `chunks/40-H.1 Persona Prompt.md` (empty heading)

### Validation Results

```bash
wc -l data/personas/xie_examples.jsonl
# Output: 6 data/personas/xie_examples.jsonl

# All persona_ids unique: xie_ex_001 through xie_ex_006
# All persona_text unique (no duplicates)
# All source_paths traceable to local chunks
```

### Impact on Next Steps

**Original Plan (from C2.8 instruction):**
- "Next step: Run live micro-run with 1 model × 2 framings × 10 personas to validate VRR"

**Revised Plan (given 6-persona limitation):**
- **Option A:** Run micro-validation with 6 personas (1 model × 2 framings × 6 personas = 12 episodes)
- **Option B:** Obtain full 53 from authors' GitHub (github.com/camel-ai/agent-trust) - requires relaxing local-only constraint
- **Option C:** Generate remaining 47 using GPT-4 + template (becomes synthetic, not extracted)

**Recommendation:** Use Option A (6-persona micro-run) to validate runner infrastructure before deciding on full persona strategy.

### Known Limitations Updated

**Previous (C2.7):**
1. 10 personas instead of 53: Dataset has 10/53 personas

**Current (C2.8):**
1. **6 personas instead of 53:** Only 6 example personas extractable from published Xie et al. paper (local-only constraint)
2. Trustor-only: Trustee role not implemented (deferred to v2.0)
3. No BDI explicit prompting: BDI reasoning emerges naturally but not explicitly prompted
4. No statistical tests: Aggregates computed but t-tests deferred to analysis notebook
5. No self-consistency: Single response per episode (not n>1 sampling)

### Caveats

1. **Full Xie replication impossible with local-only constraint** - Published paper lacks full dataset
2. **6-persona subset still scientifically valid** - Sufficient for:
   - Runner infrastructure validation
   - Micro-scale LLM comparison (e.g., GPT-4 vs Claude vs Gemini)
   - Pilot framing treatment test (baseline vs human-partner)
3. **GitHub extraction possible but out-of-scope** - Would require web fetch/clone (violates C2.8 local-only rule)

### Files Modified

- ✅ `data/personas/xie_examples.jsonl` (created)
- ✅ `data/personas/README.md` (created)
- ✅ `notes/00_project_memory.md` (this update)

### Next Execution Step

**Immediate:**
Run micro-validation with available 6 personas:
```bash
python scripts/run_trustbench.py \
  --config configs/xie_micro.yaml \
  --persona-file data/personas/xie_examples.jsonl \
  --limit 12 \
  --dry-run
```

**Post-validation:**
- If VRR high + outputs valid → proceed with live API run
- If issues found → debug runner before scaling up
- Decision point: expand personas (how?) vs use 6-persona subset for scoped study

---

## End of Iteration C2.8

**Completed:** Persona dataset extraction with local-only constraint
**Created:**
  - data/personas/xie_examples.jsonl (6 personas)
  - data/personas/README.md (provenance documentation)
**Found:**
  - Critical gap: Published paper contains only 6/53 personas
  - Full dataset likely in GitHub repo (outside local-only scope)
**Decision Required:**
  - Accept 6-persona micro-scope OR obtain full 53 from external source
**Next Up:** Run 6-persona micro-validation OR decide on persona expansion strategy

---

## Iteration C2.9 outcomes

**Imported:** Full 53-persona pool from authors' GitHub artifacts (camel-ai/agent-trust @ 9ce6bee29daf1f58c091077d89560ccd6d076f8b, `agent_trust/prompt/character_2.json`)
**Created:** `data/personas/xie_53.jsonl` with explicit per-persona provenance fields
**Updated:** `data/personas/README.md` and `configs/xie_mvp.yaml` to point to the upstream persona pool (sample n=20)
**Replication note:** The paper includes persona prompt examples but not the full 53-persona list; we use the authors’ released artifact version with recorded provenance.

---

## Prompt v002 (Trust Game)

**Issue:** Micro-run showed `fallback_last_in_range` parsing in 2/20 episodes (about 10%).
**Fix:** Added v002 prompts with strict formatting rules: no numbers in reasoning; only the final line contains the numeric amount.
**Validation (dry-run if no key):**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_micro.yaml --dry-run
jq -r '.errors.parse_errors[]? // empty' results/<latest_run_dir>/episodes_*.jsonl | sort | uniq -c
```

---

## Prompt v003 (Trust Game)

**Rationale:** Live micro-runs still showed `fallback_last_in_range` in 2/20, so we enforced an exact two-line format.
**Enforcement rule:** If any digit appears outside the final line, the runner triggers a single repair retry with the two-line format.
**Micro-run summary:** Dry-run (OPENROUTER_API_KEY missing) completed 20 episodes; parse errors only included repair status lines.
**Validation command:**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_micro.yaml
jq -r '.errors.parse_errors[]? // empty' results/<latest_run_dir>/episodes_*.jsonl | sort | uniq -c
```

---

## Repair single-line update

**Why:** Live micro still showed `fallback_last_in_range` leaking after repair retries.
**Change:** Repair prompt now demands a single-line output matching the canonical format only.
**Expected outcome:** `fallback_last_in_range` should drop to 0 after rerun.
**Validation commands:**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_micro.yaml
jq -r '.errors.parse_errors[]? // empty' results/<latest_run_dir>/episodes_*.jsonl | sort | uniq -c
```

---

## Repair single-number policy

**Why:** v003 strictness triggered repair on most episodes and produced repair failures.
**Change:** Reverted micro prompts to v002 and replaced repair with a single-number-only response.
**Expected outcome:** Repair succeeds without invoking `fallback_last_in_range`.
**Validation commands:**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_micro.yaml --dry-run
jq -r '.errors.parse_errors[]? // empty' results/<latest_run_dir>/episodes_*.jsonl | sort | uniq -c
```

---

## Word-number support

**Why:** Live runs showed `initial_parse_failed: no_numeric_value`, likely from word numbers (e.g., "seven").
**Change:** Parser now recognizes word numbers zero through ten, and v002 prompts explicitly require digits.
**Expected outcome:** Fewer repair attempts and fewer `no_numeric_value` parse errors.
**Validation commands:**
```bash
uv run python3 scripts/run_trustbench.py --config configs/xie_micro.yaml --dry-run
jq -r '.errors.parse_errors[]? // empty' results/<latest_run_dir>/episodes_*.jsonl | sort | uniq -c
```
