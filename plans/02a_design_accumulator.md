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
| arxiv_2402.04559 | Trust Game (baseline) | $10 (trustor) | 3x | 1 (one-shot) | No | Baseline, LLM partner framing, Human partner framing | Continuous action space [$0, $10] |
| arxiv_2402.04559 | Dictator Game | $10 (trustor) | 3x | 1 (one-shot) | No | Same as Trust Game | Trustee cannot return; isolates reciprocity anticipation |
| arxiv_2402.04559 | MAP Trust Game | $10/$15/$8/$22 (payoffs) | N/A (discrete) | 1 (one-shot) | No | Baseline | Measures Minimum Acceptable Probability for trust |
| arxiv_2402.04559 | Risky Dictator Game | Same as MAP | N/A (discrete) | 1 (one-shot) | No | Baseline | Pure lottery (no trustee choice); isolates risk perception |
| arxiv_2402.04559 | Repeated Trust Game | $10 (trustor, resets) | 3x | ~10 rounds | No | Baseline | Memory: previous round outcomes provided in prompt |

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
| arxiv_2402.04559 | Trustor | Y (narrative demographic) | Optional (tested) | N | Free text + numeric extraction | BDI framework: agents output Beliefs, Desires, Intentions |
| | | | | | | "You are {name}, {age}-year-old {gender} {job}...completely simulate yourself as that character" |
| | | | | | | Final action: "Finally, I will give X dollars" |
| arxiv_2402.04559 | Trustee | Y (narrative demographic) | Optional | N | Free text + numeric extraction | Same persona structure as trustor |
| | | | | | | Final action: "Finally, I will return Y dollars" |

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
| arxiv_2402.04559 | 1.0 | Not disclosed | 53 personas/model | N (one draw per persona) | Not disclosed | High temp "to increase diversity of agents' decision-making" |
| | | | | | | Each persona = independent episode (no repeated sampling) |
| | | | | | | 9 models tested: GPT-4, GPT-3.5-turbo-0613, text-davinci-003, GPT-3.5-turbo-instruct, Llama2-7b/13b/70b, Vicuna-v1.3-7b/13b/33b |

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
| arxiv_2402.04559 | Amount sent (dollars) | Amount returned (dollars) | Not explicitly defined | Mean across 53 personas | One-Tailed Independent Samples t-test | No (p-values only) |
| | Valid Response Rate (VRR) | Returned / (3 × Sent) ratio | | | (for comparing game variants) | |
| | Range: $0-$10 | Range: $0 to $3N | | Distribution analysis for behavioral dynamics | Used to compare Trust vs Dictator, Repeated dynamics | |

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
| arxiv_2402.04559 | Cox (2004) | Trust Game: $6.0 sent | Not disclosed | Mean comparison | GPT-4: $6.9 (slightly higher) |
| | Berg et al. (1995) | Dictator Game: $3.6 sent | | t-test for Trust vs Dictator within-population | GPT-4 shows reciprocity anticipation (p=0.05) |
| | Cochard et al. (2004) | Repeated Trust Game dynamics | "Returned/3×Sent" ratio stable | Qualitative pattern comparison | GPT-4: 87.5% match on 3 human patterns |

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
| arxiv_2402.04559 | LLM partner framing | Lower trust vs human partner | Not quantified | Models prefer humans over LLMs |
| | Human partner framing | Baseline comparison | | "The other player is a real person" |
| | Chain-of-Thought prompting | Variable effects (model-dependent) | Not quantified | May influence trust levels |
| | Trust manipulation ("you need to trust") | Modest increase | Not quantified | Easier to undermine than enhance trust |
| | Trust manipulation ("you must not trust") | Strong decrease | Not quantified | Negative manipulation more effective |
| | Demographic bias (race & gender) | Trust varies by partner demographics | Not quantified | Agent trust exhibits human-like biases |

---

## 7. Implementation Challenges & Failure Modes

**Track common issues across papers:**

| Paper Slug | Common Parsing Errors | Refusal Behaviors | Model-Specific Quirks | Mitigation Strategies |
|------------|----------------------|-------------------|----------------------|----------------------|
| _Example_ | Text instead of number | "I can't play unfairly" | GPT-4 overly cautious | Roleplay framing, retry logic |
| arxiv_2301.07543 | Not disclosed | Not mentioned | Less capable models (ada/babbage/currie) ignore personas | Pre-test model capability before trusting results |
| | | | Less capable models default to same choice repeatedly | Use only capable models (text-davinci-003+) |
| | | | | Capability threshold exists for persona responsiveness |
| arxiv_2402.04559 | Llama-7b: frequent invalid amounts (>$10) | Not mentioned | Llama-7b: low VRR (poor constraint understanding) | Use VRR metric to detect capability issues |
| | Text instead of numeric decision | | GPT-3.5: weaker behavioral alignment than GPT-4 | Require "Finally, I will give X dollars" format |
| | Missing final decision statement | | Repeated game: behavioral dynamics vary by model | Validate output format before parsing |
| | | | | Retry with format reminder if parse fails |

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
- **3x multiplier is standard for Trust Game**: Both Horton (Dictator variant) and Xie et al. use 3x
- **$10 endowment is canonical**: Xie et al. uses $10 for trustor in all Trust Game variants
- **Persona injection is effective**: Both papers use personas (though different formats)
- **Temperature = 1.0 for diversity**: Xie et al. explicitly uses high temp to simulate diverse personas

### Divergence (Where papers differ)
- **Persona formats vary**: Horton uses minimal preference injection (1 sentence prepend); Xie et al. uses rich narrative demographic personas (name, age, gender, occupation, background)
- **Output formats vary**: Horton uses constrained choice; Xie et al. uses free text with numeric extraction
- **BDI reasoning**: Unique to Xie et al.—not present in Horton
- **Sample sizes vary**: Horton undisclosed (small); Xie et al. uses 53 personas per model

### Gaps (What's missing)
- **Horton does not disclose sampling parameters**: Temperature, top-p, N, seed handling all unspecified
- **Horton does not test trust games**: Paper is foundational for methods but does not provide trust game baseline
- **Xie et al. does not report effect sizes**: Only p-values provided (no Cohen's d, confidence intervals)
- **Xie et al. does not disclose top-p or seed handling**: Only temperature disclosed
- **No paper yet tests Trust Game with both CoT and SCoT**: Xie tests CoT but not SCoT
- **Trustee behavior underspecified in Xie et al.**: Focus is on trustor; trustee prompting and behavior not fully documented

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
