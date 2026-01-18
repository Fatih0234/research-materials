# Design Accumulator: Cross-Paper Patterns

**Created:** 2026-01-18 (Iteration C0)
**Purpose:** Accumulate design patterns across all 7 core papers to inform unified TrustBench design

**Instructions:** After extracting each paper in Iterations C1-C7, update the relevant tables below with findings.

---

## 1. Game Parameters Table

| Paper Slug | Game | Endowment | Multiplier | Rounds | Communication | Treatments | Notes |
|------------|------|-----------|------------|--------|--------------|------------|-------|
| _Example_ | Trust Game | 10 tokens | 3x | 1 (one-shot) | No | Baseline, Persona | - |
| arxiv_2301.07543 | Dictator (C&R 2002) | Varies by scenario | N/A | 1 (one-shot) | No | Persona (4 types) | Not a Trust Game; demonstrates methodology |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

**Patterns to Watch:**
- Do all Trust Game papers use 3x multiplier? Or is there variation?
- What's the most common endowment size?
- How many rounds for repeated games?

---

## 2. Prompt Patterns Table

| Paper Slug | Role | Persona (Y/N) | CoT (Y/N) | SCoT (Y/N) | Output Format | Notable Prompt Features |
|------------|------|---------------|-----------|------------|---------------|------------------------|
| _Example_ | Investor | Y (demographic) | N | N | JSON schema | BDI reasoning framework |
| | Trustee | Y | N | N | JSON schema | Belief-desire-intention |
| arxiv_2301.07543 | Person B (dictator) | Y (preference) | N | N | Constrained choice ("left"/"right") | Minimal persona prepend (1 sentence) |
| | | | | | | Preference types: inequity-averse, efficient, self-interested, none |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Patterns to Watch:**
- Is BDI reasoning common or unique to one paper?
- When is Chain-of-Thought used vs not used?
- What output formats dominate (free text vs JSON vs numeric)?

---

## 3. Sampling / Variance Strategy Table

| Paper Slug | Temp | Top-p | N Samples/Condition | Self-Consistency (Y/N) | Seed Handling | Notes |
|------------|------|-------|---------------------|------------------------|---------------|-------|
| _Example_ | 0.7 | 0.9 | 50 | Y (majority vote) | Random per episode | - |
| arxiv_2301.07543 | Not disclosed | Not disclosed | Not disclosed (likely small) | N | Not disclosed | ~$50 total cost, "minutes" runtime |
| | | | | | | Emphasizes low cost enables "arbitrarily large" N |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Patterns to Watch:**
- What temperature range is most common for behavioral experiments?
- Is self-consistency widely adopted or niche?
- How many samples are needed for stable distributions?

---

## 4. Metrics & Aggregation Table

| Paper Slug | Trust Metric | Reciprocity Metric | Efficiency Metric | Aggregation Method | Statistical Tests | Effect Sizes Reported? |
|------------|--------------|-------------------|-------------------|-------------------|-------------------|----------------------|
| _Example_ | Amount sent / Endowment | Amount returned / Received | Joint surplus | Mean ± SD | t-test, ANOVA | Cohen's d = 0.5 |
| arxiv_2301.07543 | N/A (not trust game) | N/A | Total payoff (sum of allocations) | Fraction choosing each option | None (qualitative comparison) | No |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Patterns to Watch:**
- Is there a canonical trust metric definition? Or do papers differ?
- What statistical tests are standard for this domain?
- Are effect sizes routinely reported?

---

## 5. Human Baseline References Table

| Paper Slug | Baseline Source | Baseline Trust Measure | Baseline Reciprocity Measure | How LLM-Human Comparison Done | LLM vs Human Result |
|------------|-----------------|------------------------|------------------------------|-------------------------------|---------------------|
| _Example_ | Berg et al. 1995 | ~50% of endowment sent | ~30% returned | Mean comparison, t-test | LLM higher trust |
| arxiv_2301.07543 | Charness & Rabin 2002 | N/A (dictator game) | N/A | Qualitative directional comparison | Qualitative agreement |
| | Kahneman et al. 1986 | N/A (fairness survey) | N/A | Qualitative comparison | Directional match |
| | Samuelson & Zeckhauser 1988 | N/A (status quo bias) | N/A | Qualitative comparison | Status quo bias replicated |
| | | | | | |
| | | | | | |
| | | | | | |

**Patterns to Watch:**
- Do papers cite Berg et al. (1995) or other classic studies?
- Are LLMs generally more trusting, less trusting, or similar to humans?
- Is there a "gold standard" human baseline we should use?

---

## 6. Prompting Intervention Effects Summary

**Track papers that test prompt variations and their impact:**

| Paper Slug | Intervention Tested | Effect on Trust/Cooperation | Effect Size | Takeaway for TrustBench |
|------------|---------------------|----------------------------|-------------|------------------------|
| _Example_ | Social CoT prompting | +25% cooperation in PD | p < 0.001 | SCoT unlocks ToM reasoning |
| arxiv_2301.07543 | Persona endowments (preference types) | Strong directional effects | Not quantified | Only capable models (text-davinci-003) respond to personas |
| | Inequity-averse persona | → Chooses equitable allocations | Qualitative | Validates persona injection as tool |
| | Efficiency persona | → Maximizes total payoff | Qualitative | Default (unendowed) behavior = efficiency-seeking |
| | Self-interested persona | → Maximizes own payoff | Qualitative | Not the default (contra homo economicus) |

---

## 7. Implementation Challenges & Failure Modes

**Track common issues across papers:**

| Paper Slug | Common Parsing Errors | Refusal Behaviors | Model-Specific Quirks | Mitigation Strategies |
|------------|----------------------|-------------------|----------------------|----------------------|
| _Example_ | Text instead of number | "I can't play unfairly" | GPT-4 overly cautious | Roleplay framing, retry logic |
| arxiv_2301.07543 | Not disclosed | Not mentioned | Less capable models (ada/babbage/currie) ignore personas | Pre-test model capability before trusting results |
| | | | Less capable models default to same choice repeatedly | Use only capable models (text-davinci-003+) |
| | | | | Capability threshold exists for persona responsiveness |
| | | | | |

---

## 8. Replication Priorities (Ranked by Paper)

After all papers extracted, rank which features are:
- **MUST-HAVE (MVP):** Core to answering central RQ
- **SHOULD-HAVE (V2):** Important extensions
- **NICE-TO-HAVE (Future):** Interesting but not critical

| Feature | Source Paper(s) | Priority | Rationale |
|---------|----------------|----------|-----------|
| _Example: One-shot Trust Game_ | Xie et al. 2024 | MUST-HAVE | Primary replication target |
| | | | |
| | | | |
| | | | |

---

## 9. Convergence & Divergence Notes

**As patterns emerge, document:**

### Convergence (Where papers agree)
- [e.g., "All Trust Game papers use 3x multiplier"]
- [e.g., "Self-consistency improves distribution quality"]

### Divergence (Where papers differ)
- **Persona formats vary**: Horton uses minimal preference injection (1 sentence prepend); others may use demographic or BDI approaches
- [e.g., "Temperature ranges from 0.5 to 1.0"]

### Gaps (What's missing)
- **Horton does not disclose sampling parameters**: Temperature, top-p, N, seed handling all unspecified
- **Horton does not test trust games**: Paper is foundational for methods but does not provide trust game baseline
- **No quantitative human baseline comparison**: Only qualitative directional agreement
- [e.g., "No paper tests Trust Game with both CoT and SCoT"]
- [e.g., "Limited multi-model comparisons in same protocol"]

---

## 10. Synthesis for TrustBench Design

**After C1-C7 complete, use this accumulator to answer:**

1. **What is the canonical Trust Game protocol?**
   - Endowment: [consensus value]
   - Multiplier: [consensus value]
   - Rounds: [one-shot vs repeated - decide based on MVP scope]

2. **What prompt structure should TrustBench use?**
   - System message: [pattern from papers]
   - Role messages: [pattern from papers]
   - Persona format: [simplest effective approach]

3. **What sampling strategy is most rigorous?**
   - Temperature: [recommended value]
   - Top-p: [recommended value]
   - N samples: [minimum for stable results]
   - Self-consistency: [Y/N - justify]

4. **What metrics must TrustBench report?**
   - Trust: [formula]
   - Reciprocity: [formula]
   - Efficiency: [formula if applicable]
   - Aggregation: [mean ± SD vs full distribution]

5. **What human baseline should TrustBench use?**
   - Source: [most cited or most comparable]
   - Values: [trust %, reciprocity %]
   - Comparison method: [statistical test]

---

**Accumulator Status:** 🚧 Empty - populate during Iterations C1-C7

**Next Action:** Proceed to Iteration C1 (Horton 2023) and begin filling tables.
