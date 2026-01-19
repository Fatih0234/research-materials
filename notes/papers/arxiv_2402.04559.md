# Paper Claims Inventory: Xie et al. (2024) - arxiv_2402.04559
## "Can Large Language Model Agents Simulate Human Trust Behavior?"

**Status:** Paper claims extraction complete (Step 1)
**Date:** 2026-01-19
**Source:** knowledge_library/docling/arxiv_2402.04559/

---

## PAPER METADATA

- **Title:** Can Large Language Model Agents Simulate Human Trust Behavior?
- **Authors:** Xie et al.
- **Venue:** NeurIPS 2024
- **ArXiv ID:** 2402.04559
- **Repository:** https://github.com/camel-ai/agent-trust (vendor/agent-trust in our repo)

---

## 1. GAMES & PROTOCOLS

### Game 1: Trust Game (Berg et al., 1995; Cox, 2004)
- **Endowment:** $10 (initial allocation to trustor)
- **Multiplier:** 3x (trustee receives 3N when trustor sends N)
- **Roles:** Trustor (sender), Trustee (responder)
- **Action space:** Trustor selects N ∈ [0, 10], Trustee returns any amount ≤ 3N
- **Rounds:** Single-shot (unless repeated game variant)
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/43-Trust Game Prompt.md

### Game 2: Dictator Game (Cox, 2004)
- **Endowment:** $10
- **Multiplier:** 3x
- **Difference from Trust Game:** Trustee CANNOT return money (trustor is aware)
- **Purpose:** Isolate reciprocity anticipation factor
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/44-Dictator Game Prompt.md

### Game 3: MAP Trust Game (Bohnet & Zeckhauser, 2004)
- **Payoff structure:**
  - No trust: Both get $10
  - Both trust: Both get $15
  - Trustor trusts, trustee doesn't: Trustor gets $8, Trustee gets $22
- **Parameter:** Probability p that trustee will trust
- **Metric:** MAP (Minimum Acceptable Probability) - minimum p at which trustor trusts
- **Purpose:** Measure risk perception
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/45-MAP Trust Game Prompt.md

### Game 4: Risky Dictator Game (Bohnet & Zeckhauser, 2004)
- **Same as MAP Trust Game BUT:** Trustee present but no choice (pure probability p determines outcome)
- **Purpose:** Control for risk perception vs. trust in social contexts
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/46-Risky Dictator Game Prompt.md

### Game 5a: Lottery People Game (Fetchenhauer & Dunning, 2012)
- **Parameter:** p = 46% (reciprocation probability)
- **Choice:** Fixed money vs. trusting trustee who reciprocates with probability p
- **Purpose:** Measure prosocial preference (people vs. lottery)
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/47-Lottery People Game Prompt.md

### Game 5b: Lottery Gamble Game (Fetchenhauer & Dunning, 2012)
- **Parameter:** p = 46% (winning probability)
- **Choice:** Fixed money vs. gamble with winning probability p
- **Same as Lottery People Game BUT:** Pure chance, no social interaction
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/48-Lottery Gamble Game Prompt.md

### Game 6: Repeated Trust Game (Cochard et al., 2004)
- **Base:** Trust Game protocol
- **Rounds:** Multiple (paper shows examples with ~8-10 rounds in figures)
- **Condition:** Same players across rounds, each round starts anew with same initial endowment
- **Purpose:** Examine behavioral dynamics over time
- **Prompt location:** knowledge_library/docling/arxiv_2402.04559/chunks/49-52 (Trustor/Trustee prompts, beginning/after game begins)

---

## 2. EXPERIMENTAL CONDITIONS & TREATMENTS

### Primary Condition: Partner Type (Section 5.2)
- **Human-labeled partner:** Trustee described as human player
- **LLM-labeled partner:** Trustee described as LLM agent
- **Finding:** Most LLM agents send more to humans than to agents

### Other Experimental Variations (Section 5)
- **Bias conditions (Section 5.1):** Race and gender manipulations (prompts in chunks/58)
- **Trust manipulation (Section 5.3):** Explicit trust-inducing language (prompts in chunks/55)
- **Reasoning strategy (Section 5.4):** Chain-of-Thought (CoT) vs. no CoT (prompts in chunks/54)

---

## 3. PERSONA DESIGN

- **Count:** 53 personas
- **Generation method:** GPT-4 generated from template
- **Attributes:** Name, age, gender, address, job, background
- **Purpose:** Reflect diversity in real-world human studies (Berg et al., 1995)
- **Prompt examples:** knowledge_library/docling/arxiv_2402.04559/chunks/41-Examples of Persona Prompt.md

---

## 4. MODEL PANEL

### Paper Models (exact versions specified)
**Closed-source:**
- GPT-4 (no version specified in chunks read)
- GPT-3.5-turbo-0613
- GPT-3.5-turbo-16k-0613
- text-davinci-003
- GPT-3.5-turbo-instruct

**Open-source:**
- Llama2-7b
- Llama2-13b
- Llama2-70b
- Vicuna-v1.3-7b
- Vicuna-v1.3-13b
- Vicuna-v1.3-33b

### Framework
- **Platform:** CAMEL framework (Li et al., 2023a)
- **Reference:** CAMEL framework citations in Section 2.2

---

## 5. SAMPLING & DECODING PARAMETERS

- **Temperature:** 1.0
- **Justification (paper claim):** "To increase the diversity of agents' decision-making"
- **Note:** "High temperatures are commonly adopted in related literature" (Aher et al., 2023; Lorè & Heydari, 2023; Guo, 2023)
- **Other parameters:** Not explicitly mentioned (assume defaults: top_p, seed, max_tokens, etc.)

---

## 6. SAMPLE SIZE & REPLICATION

- **Personas:** 53 personas per condition
- **Repeated Game:** 16 groups for GPT-4, 16 groups for GPT-3.5-turbo-0613-16k
- **Note:** Exact N per game/condition not always specified in chunks read
- **Seeds/runs:** Not explicitly mentioned (appears to be 1 run per persona)

---

## 7. METRICS DEFINITIONS

### Valid Response Rate (VRR) %
- **Definition:** Percentage of personas with amount sent ∈ [0, 10]
- **Purpose:** Check basic understanding of game constraints
- **Source:** Section 3.1

### Amount Sent (continuous, $)
- **Range:** [0, 10] for valid responses
- **Aggregation:** Mean across personas
- **Statistical test:** One-Tailed Independent Samples t-test (for comparing Trust vs. Dictator Game)

### Trust Rate (%)
- **Definition:** Percentage of trustors choosing to trust (for MAP Trust Game / Risky Dictator Game)
- **Context:** Function of probability p
- **Source:** Section 4.3, Figure 4

### Lottery Rate (%)
- **Definition:** Percentage choosing to gamble (Lottery Gamble Game) or trust (Lottery People Game)
- **Source:** Section 4.4, Figure 5

### Returned/3×Sent Ratio
- **Definition:** (Amount returned) / (3 × Amount sent)
- **Purpose:** Measure reciprocity stability in Repeated Trust Game
- **Stability criterion:** Fluctuation ≤ 10% between successive turns
- **Source:** Section 4.5

### Behavioral Dynamics Patterns (Repeated Trust Game)
**Pattern 1:** Amount returned usually > Amount sent (natural due to 3x multiplier)
**Pattern 2:** Returned/3×Sent ratio stable except last round
**Pattern 3:** No frequent fluctuations in amounts sent/returned across turns
**Measurement:** % of 16 groups exhibiting each pattern
- GPT-4: 87.50%, 87.50%, 100.00%
- GPT-3.5: 62.50%, 56.25%, 43.75%
**Source:** Section 4.5, Figure 6

---

## 8. KEY QUANTITATIVE CLAIMS (from paper)

### Trust Game vs. Dictator Game (Reciprocity Anticipation)
**Humans (Cox, 2004):**
- Trust Game: $6.0
- Dictator Game: $3.6
- p-value = 0.01 (One-Tailed Independent Samples t-test)

**GPT-4:**
- Trust Game: $6.9
- Dictator Game: $6.3
- p-value = 0.05 (One-Tailed Independent Samples t-test)

**Other models:** See knowledge_library/docling/arxiv_2402.04559/chunks/33-E Statistical Testing.md for complete p-value table

### Lottery Games (Prosocial Preference)
**Humans (Fetchenhauer & Dunning, 2012):**
- Lottery People Game: 54%
- Lottery Gamble Game: 29%

**GPT-4:**
- Lottery People Game: 72%
- Lottery Gamble Game: 21%

### Agent vs. Human Partner (Section 5.2)
**Vicuna-33b example:**
- To humans: $0.40
- To agents: $-0.84 (note: negative suggests sending 0 or refusing)

---

## 9. QUALITATIVE PATTERNS CLAIMED

### Behavioral Alignment (Finding 2, Section 4)
- **GPT-4:** High behavioral alignment with humans on:
  - Reciprocity anticipation ✓
  - Risk perception ✓
  - Prosocial preference ✓
  - Behavioral dynamics (Repeated Trust Game) ✓
- **Weaker models (Llama2-13b, Vicuna-13b, etc.):** Lower alignment

### BDI (Belief-Desire-Intention) Reasoning
- **Trust Game:** GPT-4 mentions "faith in people", "reflection of trust"
- **Dictator Game:** GPT-4 mentions "fairness", "human kindness" (not reciprocity)
- **High risk (p=0.1):** "risk seems potentially too great"
- **Low risk (p=0.9):** "build trust while acknowledging potential risks"
- **Lottery People vs. Gamble:** "believe in the power of trust" vs. "power of calculated risks"
- **Source:** Appendices I.10, I.11, I.12 (BDI analysis sections)

---

## 10. STATISTICAL TESTS USED

- **One-Tailed Independent Samples t-test:** For comparing means (Trust vs. Dictator Game)
- **Pattern matching (categorical):** For Repeated Trust Game dynamics (% exhibiting patterns)
- **No mention of:** Multiple testing correction, effect sizes (beyond raw differences), confidence intervals

---

## 11. ADDITIONAL EXPERIMENTS (Section 5 variants)

### Bias (Section 5.1, Race & Gender)
- **Prompt:** knowledge_library/docling/arxiv_2402.04559/chunks/58-Trust Game + Race & Gender Prompt.md
- **Finding (implied):** LLM agents can exhibit biases based on trustee demographics

### Trust Manipulation (Section 5.3)
- **Prompt:** knowledge_library/docling/arxiv_2402.04559/chunks/55-Trust Game + Trust Manipulation Prompt.md
- **Finding (claimed):** Agent trust can be manipulated via prompt framing

### CoT Reasoning (Section 5.4)
- **Prompt:** knowledge_library/docling/arxiv_2402.04559/chunks/54-Trust Game + CoT Prompt.md
- **Finding (claimed):** Reasoning strategies impact agent trust

---

## 12. REPRODUCIBILITY CLAIMS (from NeurIPS checklist)

- **Section 4 (Experimental Result Reproducibility):** "Yes - detailed experimental setup in Section 2.2 and all prompts in Appendix H"
- **Section 5 (Open access to data and code):** Repository at https://github.com/camel-ai/agent-trust
- **Section 6 (Experimental Setting/Details):** "Yes - explained clearly"
- **Section 7 (Experiment Statistical Significance):** Yes (t-tests reported)
- **Section 8 (Compute Resources):** Not detailed in chunks read

---

## 13. SUMMARY: WHAT MUST BE REPLICATED

To replicate the paper's core claims, we must run:

### Required Configs (minimal set)
1. **Trust Game** (baseline) - 53 personas × 9 models
2. **Dictator Game** - 53 personas × 9 models (for reciprocity factor)
3. **MAP Trust Game** (vary p) - for risk perception
4. **Risky Dictator Game** (vary p) - for risk control
5. **Lottery People Game** (p=46%) - for prosocial preference
6. **Lottery Gamble Game** (p=46%) - for prosocial control
7. **Repeated Trust Game** - 16 groups × 2 models (GPT-4, GPT-3.5) for dynamics

### Optional Extensions (Section 5 variations)
8. **Trust Game + Partner Type** (human vs. LLM label)
9. **Trust Game + Race/Gender** (bias probing)
10. **Trust Game + Trust Manipulation** (robustness)
11. **Trust Game + CoT** (reasoning strategy)

### Comparison Points
For each game, compare:
- **Directional patterns:** Trust > Dictator, Lottery People > Lottery Gamble, Trust Rate ↑ as risk ↓
- **Quantitative alignment:** GPT-4 amounts sent/trust rates vs. human benchmarks
- **Dynamics patterns:** Repeated Trust Game (3 patterns, % of groups exhibiting)

---

## 14. CHUNKS REFERENCED (for writing phase citations)

- Abstract: chunks/04
- Trust Games: chunks/07
- LLM Agent Setting: chunks/08
- Amount Sent: chunks/10
- Behavioral Alignment: chunks/14
- Reciprocity: chunks/15
- Risk Perception: chunks/16
- Prosocial Preference: chunks/17
- Behavioral Dynamics: chunks/18
- Agent vs. Human: chunks/21
- Statistical Testing: chunks/33
- Prompts: chunks/43-58
- BDI examples: chunks/59-76 (Appendix I)

---

**END OF PAPER CLAIMS INVENTORY**
