# Iteration C Extraction Queue

**Created:** 2026-01-18 (Iteration C0)
**Purpose:** Paper-by-paper extraction checklist for Iteration C1-C7

---

## Extraction Order & Rationale

The 7 CORE papers are extracted in the following order to build knowledge progressively:

1. **Theoretical Foundation First** → Establishes "Homo Silicus" framework
2. **Primary Replication Target** → Our main empirical anchor (Trust Game)
3. **Prompting Techniques** → Methods to unlock better LLM behavior
4. **Human Simulation Methods** → Persona variance and distribution matching
5. **Sampling & Aggregation** → Self-consistency for robust measurements
6. **Economic Framing** → Theoretical justification for LLM agents
7. **Extension to N-Player** → Public goods as future direction

---

## Extraction Checklist

### 1️⃣ Iteration C1: Horton (2023) - Homo Silicus Foundation
**Slug:** `arxiv_2301.07543`
**Paper Type:** `methods_tooling`
**Core Score:** 5/6 (1+2+2)

**Methods Extract Path:**
- TOC: `knowledge_library/docling/arxiv_2301.07543/toc.md`
- Target sections: Introduction, Methods (persona endowment), Results (validation), Discussion

**Planned Output:**
- `notes/papers/arxiv_2301.07543.md` (using template)

**Why First:**
- Provides theoretical grounding for using LLMs as economic agents
- Establishes persona injection techniques we'll reuse
- Validates that LLMs encode latent social information from training

**STOP Condition:** ✋ After writing `arxiv_2301.07543.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

### 2️⃣ Iteration C2: Xie et al. (2024) - Primary Trust Game Replication
**Slug:** `arxiv_2402.04559`
**Paper Type:** `llm_llm_interaction`
**Core Score:** 6/6 (2+2+2) ⭐ **PRIMARY TARGET**

**Methods Extract Path:**
- TOC: `knowledge_library/docling/arxiv_2402.04559/toc.md`
- Target sections: Methods, Experimental Design, Prompts (Appendix), Results, Human Baseline

**Planned Output:**
- `notes/papers/arxiv_2402.04559.md` (using template)

**Why Second:**
- **This is our main replication target** - must extract thoroughly
- One-shot AND repeated Trust Game with LLM-LLM dyads
- Includes BDI reasoning framework prompts
- Provides human baseline comparison data
- Demographic variation experiments (for future extensions)

**STOP Condition:** ✋ After writing `arxiv_2402.04559.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

### 3️⃣ Iteration C3: Akata et al. (2025 Nature) - Social Chain-of-Thought
**Slug:** `www_nature_com_s41562_025_02172_y`
**Paper Type:** `prompting_intervention`
**Core Score:** 5/6 (2+2+1)

**Methods Extract Path:**
- TOC: `knowledge_library/docling/www_nature_com_s41562_025_02172_y/toc.md`
- Target sections: Methods (SCoT prompting), Results (PD/coordination games), Supplementary Materials (prompts)

**Planned Output:**
- `notes/papers/www_nature_com_s41562_025_02172_y.md` (using template)

**Why Third:**
- **Social Chain-of-Thought** is a critical prompting intervention for cooperation
- Shows how to unlock Theory-of-Mind reasoning in LLMs
- Demonstrates dramatic improvement in coordination games
- Provides prompt templates we can adapt for Trust Game

**STOP Condition:** ✋ After writing `www_nature_com_s41562_025_02172_y.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

### 4️⃣ Iteration C4: Aher et al. (2023 ICML) - Human Simulation Methods
**Slug:** `proceedings_mlr_press_aher23a`
**Paper Type:** `llm_simulates_humans`
**Core Score:** 4/6 (1+1+2)

**Methods Extract Path:**
- TOC: `knowledge_library/docling/proceedings_mlr_press_aher23a/toc.md`
- Target sections: Methods (multi-persona sampling), Results (human replication accuracy), Limitations (artifacts)

**Planned Output:**
- `notes/papers/proceedings_mlr_press_aher23a.md` (using template)

**Why Fourth:**
- Establishes methodology for generating **human-like distributions** (not just point estimates)
- Identifies key artifacts: **hyper-accuracy, hyper-obedience**
- Multi-persona sampling technique for variance
- Validation protocols against human experimental benchmarks

**STOP Condition:** ✋ After writing `proceedings_mlr_press_aher23a.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

### 5️⃣ Iteration C5: Wang et al. (2023) - Self-Consistency Sampling
**Slug:** `arxiv_2203.11171`
**Paper Type:** `prompting_intervention`
**Core Score:** 4/6 (0+2+2)

**Methods Extract Path:**
- TOC: `knowledge_library/docling/arxiv_2203.11171/toc.md`
- Target sections: Methods (self-consistency algorithm), Results (temperature/sampling effects), Implementation

**Planned Output:**
- `notes/papers/arxiv_2203.11171.md` (using template)

**Why Fifth:**
- **Self-consistency** is the key technique for robust behavioral distributions
- Sample multiple reasoning paths, aggregate via majority vote (or mean for numeric)
- Critical for moving from single-shot to distribution-based trust measurement
- Temperature/top_p parameter guidance

**STOP Condition:** ✋ After writing `arxiv_2203.11171.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

### 6️⃣ Iteration C6: Agarwal et al. (2025) - Attitudinal Conditioning
**Slug:** `arxiv_2501.16173v1`
**Paper Type:** `llm_llm_interaction`
**Core Score:** 4/6 (2+1+1)

**Methods Extract Path:**
- TOC: `knowledge_library/docling/arxiv_2501.16173v1/toc.md`
- Target sections: Methods (prompt-based attitude manipulation), Results (equilibrium shifts), Iterated PD protocol

**Planned Output:**
- `notes/papers/arxiv_2501.16173v1.md` (using template)

**Why Sixth:**
- Demonstrates **plasticity of cooperative behavior** via prompting
- Attitudinal personas ("aggressive" vs "cooperative") shift equilibria
- Iterated game protocol with memory
- Relevant for testing prompt sensitivity in Trust Game

**STOP Condition:** ✋ After writing `arxiv_2501.16173v1.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

### 7️⃣ Iteration C7: Sreedhar et al. (2025) - Public Goods Extension
**Slug:** `arxiv_2502.12504`
**Paper Type:** `llm_llm_interaction`
**Core Score:** 5/6 (2+2+1)

**Methods Extract Path:**
- TOC: `knowledge_library/docling/arxiv_2502.12504/toc.md`
- Target sections: Methods (multi-agent coordination), Results (treatment effects), Public goods game protocol

**Planned Output:**
- `notes/papers/arxiv_2502.12504.md` (using template)

**Why Seventh (Last):**
- Extends from **dyadic trust to N-player cooperation**
- Multi-agent LLM system coordination
- Treatment effects (priming, transparency, heterogeneity) validated
- Emergent behaviors: coordination, cheating detection
- **Future extension for TrustBench** beyond Trust Game

**STOP Condition:** ✋ After writing `arxiv_2502.12504.md` + updating `00_project_memory.md`, STOP and await next iteration instruction.

---

## Definition of Done (Per Paper)

For each extraction to be considered **complete**, the following must be true:

✅ **File Created:** `notes/papers/<slug>.md` exists and follows template structure
✅ **All Template Sections Filled:** No `[TODO]` or `[FILL IN]` placeholders remaining
✅ **Codable Details Extracted:**
   - Game parameters (endowments, multipliers, rounds) with exact values
   - Prompt templates (exact or close paraphrase)
   - Metrics formulas (trust, reciprocity, efficiency)
   - Sampling settings (temp, top_p, n_samples)
   - Human baseline data (if present in paper)
✅ **Local Paths Listed:** All TOC and chunk paths consulted are documented in note
✅ **Implementation Notes:** Parsing rules, failure modes, logging requirements specified
✅ **Replication Target Scoped:** Minimal viable replication clearly distinguished from extensions
✅ **Project Memory Updated:** `notes/00_project_memory.md` has new "Iteration CX outcomes" section
✅ **Git Committed:** Changes committed with message "Iteration CX: extract <slug>"

**If any checklist item is incomplete, the extraction is NOT done.**

---

## Cross-Paper Accumulation

As each paper is extracted, update `plans/02a_design_accumulator.md` with:
- Game parameters in table
- Prompt patterns observed
- Sampling/variance strategies
- Metrics & aggregation methods
- Human baseline references

This accumulator will inform the unified TrustBench design in Iteration D.

---

## After All 7 Papers Extracted

**Next Step: Iteration D - Runner Design**
- Synthesize findings from all 7 papers
- Define canonical TrustBench protocol
- Design experiment runner schema
- Specify OpenRouter integration
- Plan static website structure

**But NOT YET. For now, focus on C1 → C7 one at a time.**

---

**End of Extraction Queue**
*Proceed to Iteration C1 (Horton 2023) when ready.*
