# Persona Datasets for TrustBench

## Overview

This directory contains persona prompt datasets extracted from published research on LLM trust behavior experiments.

## Available Datasets

### xie_examples.jsonl (6 personas)

**Source:** Xie et al. (2024) - "Can Large Language Model Agents Simulate Human Trust Behavior?"
**arXiv:** 2402.04559
**Local Path:** `knowledge_library/docling/arxiv_2402.04559/`

#### Extraction Methodology

1. **TOC-First Approach:** Started with `toc.md` to identify persona-related chunks
2. **Targeted Chunk Reading:** Extracted from:
   - `chunks/41-Examples of Persona Prompt.md` (primary source: 5 personas)
   - `chunks/54-Trust Game + CoT Prompt.md` (example prompt: 1 persona)
   - `chunks/55-Trust Game + Trust Manipulation Prompt.md` (example prompt: 1 persona)
   - `chunks/57-Trust Game + Human Player Prompt.md` (example prompt: 1 persona)
3. **Deduplication:** Emily Wilson appears in multiple chunks; deduplicated by exact text match

#### Critical Limitation: The Xie-53 Gap

**Paper Claims:** Xie et al. (2024) states in Section 2.2:
> "We ask GPT-4 to generate 53 types of personas based on a given template. Each persona needs to have information including name, age, gender, address, job and background. Examples of the personas are shown in Appendix H.1."

**Actual Availability in Published Materials:**
- The published PDF (arXiv 2402.04559) contains **only 6 example personas** in Appendix H.1
- The paper does **not** include the full 53-persona dataset
- The full dataset appears to be available only in the authors' GitHub repository (github.com/camel-ai/agent-trust)

**Extraction Policy Applied:**
- **NON-NEGOTIABLE RULE:** "Do NOT invent personas beyond what is present in the Xie paper materials in this repo"
- **LOCAL-ONLY CONSTRAINT:** "Use ONLY local paths and docling chunks already present"
- **NO EXTERNAL URLS:** Per iteration instructions

**Result:** This dataset contains only the 6 personas extractable from local paper chunks, NOT the full 53.

#### Schema

Each persona record contains:

**Required Fields:**
- `persona_id`: Identifier (format: `xie_ex_001` through `xie_ex_006`)
- `source_slug`: Paper identifier (`arxiv_2402.04559`)
- `source_paths`: Array of local chunk paths where persona text appears
- `persona_text`: The complete persona prompt as written in the paper

**Extracted Fields (when present in persona_text):**
- `name`: Character name
- `age`: Age in years
- `gender`: Gender identity
- `occupation`: Job/profession
- `location`: City/region of residence

#### Persona Provenance Table

| persona_id | name | source_paths |
|------------|------|--------------|
| xie_ex_001 | Emily Johnson | chunks/41-Examples of Persona Prompt.md |
| xie_ex_002 | Javier Rodriguez | chunks/41-Examples of Persona Prompt.md |
| xie_ex_003 | Aisha Patel | chunks/41-Examples of Persona Prompt.md |
| xie_ex_004 | Jamal Thompson | chunks/41-Examples of Persona Prompt.md |
| xie_ex_005 | Mei Chen | chunks/41-Examples of Persona Prompt.md |
| xie_ex_006 | Emily Wilson | chunks/54,55,57 (multiple prompt examples) |

#### Usage Notes

1. **For Replication Studies:** This 6-persona subset is sufficient for micro-validation runs (e.g., 1 model × 2 framings × 6 personas = 12 runs)
2. **For Full Xie Replication:** Would require obtaining the full 53-persona dataset from the authors' repository (outside scope of local-only extraction)
3. **Persona Text Format:** Each `persona_text` is ready to use as a system prompt (begins with "You are...")

#### Validation Checks Performed

```bash
# Line count
wc -l data/personas/xie_examples.jsonl
# Expected: 6

# Unique persona_ids
jq -r '.persona_id' data/personas/xie_examples.jsonl | sort -u | wc -l
# Expected: 6

# Exact persona_text deduplication
jq -r '.persona_text' data/personas/xie_examples.jsonl | sort -u | wc -l
# Expected: 6 (no duplicate persona texts)
```

## Future Work

To obtain the full Xie-53 dataset:
1. Option A: Extract from authors' GitHub repository (requires relaxing local-only constraint)
2. Option B: Contact authors for supplemental materials
3. Option C: Use 6-persona subset for pilot/validation studies

## References

Xie, Q., Chen, W., & Li, G. (2024). Can Large Language Model Agents Simulate Human Trust Behavior? *Advances in Neural Information Processing Systems (NeurIPS 2024)*. arXiv:2402.04559.
