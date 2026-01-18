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
