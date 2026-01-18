# [Paper Title]

**Status:** [draft | complete]
**Extracted:** YYYY-MM-DD
**Extractor:** Claude Code (Iteration C)

---

## Citation & Local Paths

**Citation Key:** `[slug_from_shortlist]`
**Full Citation:** [Author(s) (Year). Title. Venue.]

**Local Paths Consulted:**
- TOC: `knowledge_library/docling/[slug]/toc.md`
- Chunks opened:
  - `knowledge_library/docling/[slug]/chunks/[section].md`
  - (list all chunks read during extraction)

---

## Paper Classification

**Paper Type:** `[llm_llm_interaction | llm_simulates_humans | prompting_intervention | methods_tooling | adjacent_extension]`
**Core Score:** `X/6` from shortlist
**Relevance to TrustBench:** [1-2 sentence justification]

---

## Research Question / Contribution

1. **Primary RQ:** [State the paper's main research question]
2. **Key Contribution:** [What does this paper uniquely provide?]
3. **Relevance to Trust:** [How does this inform our trust measurement question?]

---

## Experiment Setup (CODABLE)

### Game Mechanics
- **Game(s) Tested:** [Trust Game | Dictator Game | Prisoner's Dilemma | Public Goods | etc.]
- **Endowments:** [Initial allocations for each role]
- **Multipliers:** [Transformation ratios - e.g., 3x in Trust Game]
- **Rounds/Episodes:** [One-shot | N rounds | Episodes per condition]
- **Roles:** [Investor/Trustee | Player1/Player2 | etc.]

### Protocol Details
- **Communication Allowed?** [Y/N - describe if applicable]
- **Repeated Play?** [Y/N - describe memory/history handling]
- **Treatments/Conditions:** [List experimental manipulations]
  - Condition 1: [description]
  - Condition 2: [description]
- **LLM-LLM Interaction?** [Y/N - or LLM-simulates-human?]
- **Persona Injection?** [Y/N - demographic/role prompts used?]

---

## Prompting & Agent Design (CODABLE)

### Prompt Structure
**System Message:**
```
[Exact or paraphrased system prompt if disclosed]
```

**User/Role Message (Investor):**
```
[Exact or paraphrased investor/player1 prompt]
```

**User/Role Message (Trustee):**
```
[Exact or paraphrased trustee/player2 prompt]
```

### Persona Format (if used)
- **Persona Type:** [Demographic attributes | BDI beliefs | Narrative background | None]
- **Example Persona:**
```
[Sample persona text from paper]
```

### Structured Outputs
- **Output Format:** [Free text | JSON schema | Constrained choice | Numeric only]
- **JSON Schema (if applicable):**
```json
{
  "action": "...",
  "reasoning": "..."
}
```
- **Parsing Strategy:** [Regex | JSON parse | LLM repair | Manual review]

### Sampling Settings
- **Temperature:** [value(s) tested]
- **Top-p:** [value(s) tested]
- **N samples per condition:** [How many independent draws?]
- **Self-consistency used?** [Y/N - majority voting?]
- **Seed handling:** [Fixed | Random | Not disclosed]

---

## Metrics & Aggregation (CODABLE)

### Trust Metrics
- **Trust Definition:** [e.g., "Amount sent by investor / Endowment" OR other measure]
- **Calculation:** [Formula or procedure]
- **Range:** [0-1 | 0-100 | 0-10 tokens | etc.]

### Reciprocity Metrics
- **Reciprocity Definition:** [e.g., "Amount returned / Amount received" OR other measure]
- **Calculation:** [Formula or procedure]
- **Range:** [0-1 | 0-100 | etc.]

### Efficiency Metrics (if applicable)
- **Efficiency Definition:** [Joint surplus | Total welfare | etc.]
- **Calculation:** [Formula]

### Sample Sizes
- **N per condition:** [Number of episodes/games per treatment]
- **Total episodes:** [Total simulations run]
- **Replication strategy:** [Independent runs | Bootstrapped | Self-consistency samples]

### Aggregation & Statistical Tests
- **Aggregation Method:** [Mean | Median | Mode | Distribution comparison]
- **Statistical Tests:** [t-test | ANOVA | Wilcoxon | Chi-square | etc.]
- **Significance Level:** [p < 0.05 | other threshold]
- **Effect Size Reported?** [Y/N - Cohen's d, r, etc.]

---

## Results (High-Level Summary)

### Main Findings
1. [Key finding 1 with effect size if available]
2. [Key finding 2]
3. [Key finding 3]

### Human Baseline Comparisons
- **Human Baseline Source:** [Paper citation | Classic study | Own data collection]
- **Human Trust Level:** [Numeric value or range]
- **Human Reciprocity Level:** [Numeric value or range]
- **LLM vs Human Comparison:** [Higher | Lower | Similar | Context-dependent]
- **Statistical Comparison:** [How was this tested?]

### Surprising/Unexpected Results
- [Any anomalies, failures, or contradictions noted]

---

## Minimal Replication Target

**What MUST be replicated for TrustBench MVP:**
1. [Core game mechanic - e.g., "One-shot Trust Game with 10-token endowment, 3x multiplier"]
2. [Minimal prompt structure - e.g., "Role-based prompts without personas"]
3. [Baseline metrics - e.g., "Mean trust ratio, mean reciprocity ratio"]
4. [Sample size - e.g., "50+ episodes per model"]

**Can be deferred to extensions:**
- [Treatment variations]
- [Persona manipulations]
- [Advanced prompting techniques]

---

## Extensions & TrustBench Alignment

**Potential Extensions (aligned to TrustBench story):**
1. [Extension idea 1 - e.g., "Add persona treatments from this paper"]
2. [Extension idea 2 - e.g., "Compare self-consistency vs single-sample"]
3. [Extension idea 3 - e.g., "Test repeated Trust Game with memory"]

**Why These Extensions Matter:**
- [1-2 sentences on how extensions contribute to central RQ]

---

## Implementation Notes

### Parsing Rules
- **Input Validation:** [What checks are needed for prompt construction?]
- **Output Parsing:** [How to extract numeric actions from LLM text?]
- **Fallback Strategy:** [What to do if parse fails?]

### Failure Modes
- **Common Errors Observed:** [e.g., "LLM refuses to play", "Outputs text instead of number"]
- **Mitigation:** [e.g., "Retry with repair prompt", "Log and skip episode"]

### Logging Requirements
**Per-Episode Logs (minimum):**
- `episode_id`, `model`, `temperature`, `top_p`, `seed`
- `role` (investor/trustee)
- `prompt_text`, `raw_output_text`
- `parsed_action` (numeric or structured)
- `parse_errors` (if any)
- `timestamp`, `request_id`

**Aggregated Logs:**
- `condition`, `n_episodes`, `mean_trust`, `sd_trust`, `mean_reciprocity`, `sd_reciprocity`
- `model_comparison_table` (if multi-model)

---

## Open Questions / Follow-Ups

1. [Question about implementation detail not fully specified in paper]
2. [Clarification needed on metric calculation]
3. [Potential extension or variation to explore]
4. [Cross-paper comparison opportunity]

---

## Extraction Quality Checklist

- [ ] All key game parameters extracted and codable
- [ ] Prompt templates documented (exact or paraphrased)
- [ ] Metrics fully defined with formulas
- [ ] Human baseline data identified (if present)
- [ ] Sample sizes and statistical tests noted
- [ ] Replication target clearly scoped
- [ ] Local paths to all consulted chunks listed
- [ ] Implementation notes include failure modes and logging

---

**End of Template**
*Use this template for every paper extraction in Iteration C1+*
