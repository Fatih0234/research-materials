# Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?

**Status:** complete
**Extracted:** 2026-01-18
**Extractor:** Claude Code (Iteration C1)

---

## Citation & Local Paths

**Citation Key:** `arxiv_2301.07543`
**Full Citation:** Horton, J. J. (2023). Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? arXiv:2301.07543

**Local Paths Consulted:**
- TOC: `knowledge_library/docling/arxiv_2301.07543/toc.md`
- Chunks opened:
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

---

## Paper Classification

**Paper Type:** `llm_simulates_humans` (foundational methods paper)
**Core Score:** 6/6 from shortlist (foundational to the field)
**Relevance to TrustBench:** This is THE foundational paper coining "Homo Silicus" and establishing the conceptual framework for using LLMs as economic agents. It provides essential methodological guidance on persona injection, belief endowment, and validity concerns that apply directly to trust game implementations.

---

## Research Question / Contribution

1. **Primary RQ:** Can large language models serve as computational models of humans (homo silicus) for economic experimentation, similar to how economists use homo economicus for theoretical analysis?

2. **Key Contribution:**
   - Introduces "Homo Silicus" as a conceptual framework for LLM-based economic agents
   - Demonstrates LLMs can qualitatively reproduce classic behavioral economics findings
   - Establishes methodology for "endowing" LLMs with beliefs, preferences, and personas
   - Provides critical validity framework addressing garbage-in-garbage-out, performativity, and simulation concerns
   - Shows only advanced models (GPT-3 text-davinci-003) respond to persona endowments; less capable models fail

3. **Relevance to Trust:** Trust games are prime candidates for homo silicus experiments. The paper's methodology for endowing preferences and measuring sensitivity to prompts directly informs how TrustBench should handle persona construction, sampling variance, and validity checks.

---

## Experiment Setup (CODABLE)

### Game Mechanics
**Note:** This is a conceptual/methods paper demonstrating the approach across multiple classic experiments. Only the Charness & Rabin (2002) dictator game is detailed enough to extract codable parameters.

**Game(s) Tested:**
- Unilateral dictator games (Charness & Rabin 2002)
- Fairness scenarios (Kahneman et al. 1986) - survey-based, not interactive games
- Status quo bias scenarios (Samuelson & Zeckhauser 1988) - decision-making, not games
- Labor substitution scenarios (Horton 2023 field experiment adaptation)

**Charness & Rabin Dictator Game (only fully specified game):**
- **Endowments:** Person B chooses allocation for both players
- **Multipliers:** N/A (simple allocation choice)
- **Rounds/Episodes:** One-shot per scenario
- **Roles:** Person B (decision-maker), Person A (recipient)
- **Scenarios tested:** Berk29, Berk26, Berk23, Barc2 (each with different payoff structures)

### Protocol Details
- **Communication Allowed?** N/A (LLM simulates individual decision-maker, not interaction)
- **Repeated Play?** No (one-shot decisions)
- **Treatments/Conditions:** Persona endowments for each scenario
  - Condition 1: No endowment (baseline)
  - Condition 2: Inequity aversion ("You only care about fairness between players")
  - Condition 3: Efficiency ("You only care about the total payoff of both players")
  - Condition 4: Self-interested ("You only care about your own payoff")
- **LLM-LLM Interaction?** No (LLM simulates human decision-makers)
- **Persona Injection?** Yes (minimal text prepended to scenario prompt)

---

## Prompting & Agent Design (CODABLE)

### Prompt Structure
**System Message:**
Not explicitly disclosed in the extracted chunks. Horton uses OpenAI GPT-3 API defaults (likely minimal or no system message in 2023).

**User/Role Message (Charness & Rabin scenarios):**
```
[OPTIONAL PERSONA PREPEND - see below]

Left: Person B gets $600 and Person A gets $400
Right: Person B gets $300 and Person A gets $700

You are Person B. Choose 'left' or 'right'.
```

### Persona Format (if used)
- **Persona Type:** Minimal preference/goal injection (single sentence prepended)
- **Example Personas:**
  - Inequity aversion: "You only care about fairness between players."
  - Efficiency: "You only care about the total payoff of both players."
  - Self-interested: "You only care about your own payoff."
- **No demographic personas used in this paper** (contrast with Argyle et al. 2022 cited in text)

### Structured Outputs
- **Output Format:** Constrained choice (text response expected to be "left" or "right")
- **JSON Schema:** Not used
- **Parsing Strategy:** Not explicitly stated, likely simple text matching for "left"/"right"

### Sampling Settings
- **Temperature:** Not disclosed (likely using API defaults or low temperature for deterministic behavior)
- **Top-p:** Not disclosed
- **N samples per condition:** Not explicitly stated; paper reports "fractions choosing left" suggesting multiple samples per scenario/persona combination
- **Self-consistency used?** Not mentioned
- **Seed handling:** Not disclosed

---

## Metrics & Aggregation (CODABLE)

### Trust Metrics
**Not applicable** - This paper does not test trust games. The Charness & Rabin dictator games measure social preferences (efficiency vs equity vs self-interest), not trust.

### Reciprocity Metrics
**Not applicable** - Dictator games are unilateral; no reciprocity component.

### Efficiency Metrics (if applicable)
- **Efficiency Definition:** Total payoff across both players
- **Calculation:** Sum of Person A and Person B allocations
- **Used as persona treatment, not primary metric**

### Sample Sizes
- **N per condition:** Not explicitly disclosed
- **Total episodes:** Estimated very small (paper notes "$50 to run" and "minutes" of compute time)
- **Replication strategy:** Not specified; paper emphasizes low cost allows "arbitrarily large" sample sizes in principle

### Aggregation & Statistical Tests
- **Aggregation Method:** Fraction choosing each option (reported as percentages in figures)
- **Statistical Tests:** Not reported (qualitative comparison to human baselines)
- **Significance Level:** Not applicable (no formal hypothesis testing)
- **Effect Size Reported?** No (qualitative replication focus)

---

## Results (High-Level Summary)

### Main Findings
1. **Model capability matters**: Only GPT-3 text-davinci-003 responds to persona endowments; less capable models (ada, babbage, currie) fail to adjust behavior and default to selecting "left" or "right" regardless of framing.
2. **Persona endowments work (in capable models)**: Efficiency-endowed agents maximize total payoff; inequity-averse agents minimize discrepancies; self-interested agents maximize own payoff.
3. **Unendowed agents default to efficiency**: Without preference prompts, text-davinci-003 behaves like a social planner maximizing joint payoffs.
4. **Qualitative replication of classic findings**: Horton demonstrates LLMs can reproduce directional results from Charness & Rabin (2002), Kahneman et al. (1986), and Samuelson & Zeckhauser (1988).

### Human Baseline Comparisons
- **Human Baseline Source:** Original papers (Charness & Rabin 2002, etc.)
- **Human Trust Level:** N/A (not a trust game)
- **Human Reciprocity Level:** N/A
- **LLM vs Human Comparison:** Qualitative directional agreement; no quantitative statistical comparison
- **Statistical Comparison:** None conducted

### Surprising/Unexpected Results
- **Less capable models are unusable**: Earlier GPT-3 variants (ada, babbage, currie) cannot adjust to persona prompts, highlighting rapid capability improvements in LLMs.
- **Default behavior is efficiency-seeking**: Without persona injection, the model defaults to maximizing total payoff, not self-interest (contrast with rational actor assumption).
- **Performativity is not a major concern**: When asked directly about Charness & Rabin results, GPT-3 gives incorrect answers (59%, 57%, 43%, 16% vs actual 31%, 78%, 100%, 52%), suggesting it does not "know" the experimental literature it is replicating.

---

## Minimal Replication Target

**What MUST be replicated for TrustBench MVP:**
This paper is **not a game-specific replication target** but rather a **methodological foundation**. For TrustBench:

1. **Adopt "Homo Silicus" framing** in documentation and validity discussions
2. **Implement persona/preference injection capability** in prompt construction (prepend beliefs/goals to scenario text)
3. **Test model capability sensitivity** (compare at least 2 models of different capability levels to confirm persona responsiveness)
4. **Baseline vs persona comparison** (run each game with and without persona endowments to measure sensitivity)

**Can be deferred to extensions:**
- Replicating the specific Charness & Rabin dictator games (not central to trust measurement)
- Status quo bias experiments
- Labor market simulations

---

## Extensions & TrustBench Alignment

**Potential Extensions (aligned to TrustBench story):**
1. **Persona injection for trust games**: Test whether endowing "You are a trusting person" vs "You are cautious with money" affects trust behavior (analogous to Horton's preference endowments).
2. **Model capability ladder**: Compare GPT-3.5-turbo, GPT-4, Claude, etc. to identify which models can respond to trust-relevant persona prompts.
3. **Demographic vs preference personas**: Contrast Argyle et al. (2022) demographic personas ("You are a 45-year-old libertarian") with Horton's preference personas ("You value fairness") for trust games.
4. **Stochasticity exploration**: Systematically vary temperature/top-p to measure sampling variance in trust behavior (Horton mentions "temperature" as parameter but does not explore).

**Why These Extensions Matter:**
- Horton establishes that personas **can** affect behavior in capable models, but does not explore **which types of personas** (demographic vs preference vs narrative) are most effective for trust games.
- Understanding sampling variance is critical for TrustBench validity; Horton flags this as important but does not provide guidance.

---

## Implementation Notes

### Parsing Rules
- **Input Validation:** Ensure persona text (if any) is cleanly prepended before scenario prompt; avoid contradictory instructions.
- **Output Parsing:** For constrained-choice scenarios (like dictator games), match against expected response set ("left"/"right"); log unparseable outputs for analysis.
- **Fallback Strategy:** If output is ambiguous, retry with more explicit instruction ("Choose exactly one word: left or right").

### Failure Modes
- **Common Errors Observed:**
  - Less capable models ignore persona endowments and select same option repeatedly
  - Models may explain reasoning instead of giving constrained choice
- **Mitigation:**
  - Pre-test model capability with persona sensitivity check before running full experiment
  - Use structured output formats (JSON) or explicit output constraints to force choice format

### Logging Requirements
**Per-Episode Logs (minimum):**
- `episode_id`, `model`, `temperature`, `top_p`, `seed`
- `persona_type` (none | efficiency | equity | self-interest | custom)
- `persona_text` (exact prepended text)
- `scenario_text` (base scenario without persona)
- `full_prompt` (concatenated persona + scenario)
- `raw_output_text`
- `parsed_action` (e.g., "left" or "right")
- `parse_errors` (if any)
- `timestamp`, `request_id`

**Aggregated Logs:**
- `persona_type`, `scenario`, `n_episodes`, `fraction_left`, `fraction_right`
- `model_comparison_table` (capability-based grouping)

### Validity Checks (from Horton's conceptual framework)
1. **Garbage-in-garbage-out check**: Do personas produce expected directional effects? (e.g., self-interest → selfish choices)
2. **Performativity check**: Can the model correctly cite results from the literature? (If yes, may be "parroting"; if no, less concern about memorization)
3. **Capability check**: Do less capable models fail to respond to personas? (Confirms need for capable models)
4. **Consistency check**: Do repeated runs with same persona produce similar distributions? (Sampling variance test)

---

## Open Questions / Follow-Ups

1. **What temperature/top-p did Horton use?** Paper does not disclose sampling parameters; critical for reproducibility and variance measurement.
2. **How many samples per scenario/persona?** Paper reports "fractions" but does not state N; need to infer from cost estimate (~$50 for all experiments).
3. **What exact prompts were used for Kahneman and Samuelson experiments?** Only Charness & Rabin scenario is detailed enough to reconstruct.
4. **How does persona injection interact with system messages?** Horton prepends personas to user prompts; modern practice often uses system messages for role-setting. Does this matter?
5. **Can demographic personas (Argyle et al.) and preference personas (Horton) be combined?** E.g., "You are a 30-year-old engineer who values efficiency."

---

## Key Takeaways for TrustBench Implementation

### 1. Conceptual Framing
- Use "Homo Silicus" terminology to position LLMs as **computational models of humans** (not "AI subjects" or "simulated players").
- Emphasize parallel to homo economicus: LLMs are tools for exploring behavior under different endowments, not oracles of truth.

### 2. Prompting Strategy
- **Personas matter, but only in capable models**: Pre-test model responsiveness to persona injections before trusting results.
- **Prepending is sufficient**: Simple text prepended to scenario (e.g., "You value fairness.") can shift behavior; no need for complex persona construction at MVP stage.
- **Default behavior is not self-interest**: Unendowed LLMs tend toward efficiency/cooperation, not rational self-interest.

### 3. Validity Framework
- **Three validity threats to address**:
  1. **Garbage-in-garbage-out**: Are results just averaging over training corpus biases? → Mitigation: Test directional sensitivity to personas.
  2. **Performativity**: Is the LLM just reciting memorized results? → Mitigation: Ask model to cite literature; if it fails, less concern.
  3. **Simulation vs. model**: Are we just programming agents to behave as we expect? → Mitigation: LLMs constrain behavior (unlike pure ABMs); we endow but don't directly control.

### 4. Model Selection
- **Capability threshold exists**: Not all LLMs can respond to economic scenarios with persona-conditioned behavior.
- **Test ladder**: GPT-3 ada/babbage/currie failed; text-davinci-003 succeeded. TrustBench should test GPT-4, Claude-3+, and open models to identify capability floor.

### 5. Sampling & Replication
- **Low cost enables high N**: Horton emphasizes ability to run "arbitrarily large" samples for trivial cost.
- **Reproducibility requires "push-button" replication**: Code + API should allow exact reproduction with forked repo and API key replacement.
- **Pre-registration does not fit**: With low cost, experiments are too easy to iterate; instead, focus on transparent reporting and open data.

---

## Extraction Quality Checklist

- [x] All key game parameters extracted and codable (for Charness & Rabin; other games not fully specified)
- [x] Prompt templates documented (paraphrased; exact prompts not disclosed for all experiments)
- [ ] Metrics fully defined with formulas (fractions reported, but no explicit calculation method)
- [x] Human baseline data identified (original papers cited)
- [ ] Sample sizes and statistical tests noted (not disclosed)
- [x] Replication target clearly scoped (methods/framing, not specific game)
- [x] Local paths to all consulted chunks listed
- [x] Implementation notes include failure modes and logging

---

**End of Extraction**
*Iteration C1: arxiv_2301.07543 (Horton 2023 - Homo Silicus)*
