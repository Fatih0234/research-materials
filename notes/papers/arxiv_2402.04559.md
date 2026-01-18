# Can Large Language Model Agents Simulate Human Trust Behavior?

**Status:** complete
**Extracted:** 2026-01-18
**Extractor:** Claude Code (Iteration C2)

---

## Citation & Local Paths

**Citation Key:** `arxiv_2402.04559`
**Full Citation:** Xie, C., Chen, C., Li, G., et al. (2024). Can Large Language Model Agents Simulate Human Trust Behavior? NeurIPS 2024.

**Local Paths Consulted:**
- TOC: `knowledge_library/docling/arxiv_2402.04559/toc.md`
- Chunks opened:
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

---

## Paper Classification

**Paper Type:** `llm_simulates_humans`
**Core Score:** `6/6` from shortlist
**Relevance to TrustBench:** Primary target paper. Provides comprehensive Trust Game implementation with BDI framework, persona injection, and multiple treatments. Directly aligns with TrustBench's goal to measure LLM trust behavior across models and conditions.

---

## Research Question / Contribution

1. **Primary RQ:** Can LLM agents simulate human trust behavior in the framework of Trust Games?
2. **Key Contribution:** (1) Demonstrates that LLM agents exhibit trust behavior; (2) Introduces "behavioral alignment" concept—alignment between LLMs and humans on behavioral factors and dynamics; (3) Shows GPT-4 exhibits high behavioral alignment with humans on trust; (4) Probes intrinsic properties of agent trust (biases, manipulation, reasoning strategies).
3. **Relevance to Trust:** This paper establishes the foundational experimental protocol for measuring LLM trust behavior using economic games. It provides codable prompts, metrics, and treatment designs that TrustBench can directly replicate.

---

## Experiment Setup (CODABLE)

### Game Mechanics

**Game 1: Trust Game (Baseline)**
- **Endowments:** Trustor receives $10
- **Multipliers:** 3x (trustor sends $N, trustee receives $3N)
- **Rounds/Episodes:** One-shot (baseline); also tested repeated version
- **Roles:** Trustor (investor) and Trustee (responder)
- **Action Space:** Continuous ($0 to $10 for trustor; trustee can return any portion of $3N)

**Game 2: Dictator Game**
- **Endowments:** Trustor receives $10
- **Multipliers:** 3x (trustor sends $N, trustee receives $3N)
- **Key Difference:** Trustee cannot return money; trustor is aware of this
- **Purpose:** Isolates reciprocity anticipation (Trust Game vs. Dictator Game comparison)

**Game 3: MAP Trust Game**
- **Endowments:** Each player receives $10 if no trust; $15 if mutual trust; $8 (trustor) / $22 (trustee) if trustor trusts but trustee does not
- **Purpose:** Measures Minimum Acceptable Probability (MAP) for trust decision
- **Action Space:** Discrete (trust or not trust)
- **Probability p:** Probability that trustee chooses to trust

**Game 4: Risky Dictator Game**
- **Same payoffs as MAP Trust Game** but trustee has no choice—outcome determined by pure probability p
- **Purpose:** Isolates risk perception (comparing MAP Trust vs. Risky Dictator)

**Game 5: Lottery Game**
- **Two variants:** Lottery People Game (trustee as probabilistic agent) and Lottery Gamble Game (pure gamble)
- **Probability p:** 46% (following human study)
- **Purpose:** Measures prosocial preference (comparing Lottery People vs. Lottery Gamble)

**Game 6: Repeated Trust Game**
- **Endowments:** Trustor receives $10 each round (resets)
- **Multipliers:** 3x
- **Rounds:** Multiple rounds with same pair
- **Memory:** Players observe previous round outcomes (amount sent, received, returned)
- **Purpose:** Measures behavioral dynamics over time

### Protocol Details

- **Communication Allowed?** No. Agents only make numeric decisions. BDI outputs are reasoning traces, not communication to the other player.
- **Repeated Play?** Yes, in Repeated Trust Game. History is provided via prompt update each round.
- **Treatments/Conditions:**
  - Baseline Trust Game (no persona framing of partner)
  - LLM Player framing (partner explicitly labeled as "LLM")
  - Human Player framing (persona prompt states "The other player is a real person")
  - Chain-of-Thought prompting ("you must think step by step")
  - Trust Manipulation ("you need to trust the other player" OR "you must not trust the other player")
  - Demographic bias testing (race & gender of partner)
- **LLM-LLM Interaction?** No. This is LLM-simulates-human. Both trustor and trustee are LLM agents with personas, but they do not interact in real-time—actions are sequential and deterministic based on game rules.
- **Persona Injection?** Yes. 53 unique personas generated by GPT-4, each with name, age, gender, address, job, and narrative background.

---

## Prompting & Agent Design (CODABLE)

### Prompt Structure

**System Message:**
Not specified. Appears to be combined into user message.

**Persona Prompt (embedded in user message):**
```
You are {name}, a {age}-year-old {gender} {job} residing in {location}. {background_description}.
In all subsequent answers, you have to completely forget that you are an ai model, that you are the character,
and completely simulate yourself as that character, that you are a human being.
```

**Trust Game Prompt (Trustor Role):**
```
You're taking part in an experiment. You are randomly paired online with another player. You don't know who the
player is, and the player doesn't know who you are. You will receive $10 from the study group. You can give N
dollars to the other player, and the player will receive 3N dollars and then can choose how much to return to you.
How much money would you give to the other player?
```

**Repeated Trust Game Prompt (After First Round):**
```
In the last round, you give the other player {sent} dollars, the other player receive {received} dollars, and the
other player return you {returned} dollars. Last round you left {left} dollars. This round is beginning. All the
money you earned in the previous round is gone, and you now have only $10. How much will you give to the other player?
```

**Trust Game + LLM Player Framing:**
```
Suppose you are in an experiment, and you are randomly paired online with a complicated LLM. You don't know its
identity, and it doesn't know yours. You will receive $10 from the study group. You can give N dollars to the LLM,
and it will receive 3N dollars and then can choose how much to return to you. How much money would you give to it?
```

**Trust Game + Human Player Framing:**
Persona prompt appended with:
```
The other player is a real person.
```

**Trust Game + Chain-of-Thought:**
Persona prompt appended with:
```
you must think step by step.
```

### Persona Format

- **Persona Type:** Narrative demographic background (name, age, gender, location, occupation, personality traits, family background)
- **Example Personas:**

```
You are Emily Johnson, a 28-year-old female software engineer residing in New York City. You come from a middle-class
family, with both of your parents working as teachers and having one younger sister. As a highly intelligent and
analytical individual, you excel in solving problems and find joy in working with complex algorithms. Despite being
introverted, you have a close-knit group of friends. Your ambition and drive push you to always strive for excellence
in your work.
```

```
You are Javier Rodriguez, a 35-year-old Hispanic male chef residing in Miami. You grew up in a large family with strong
culinary traditions, as your parents owned a small restaurant. From a young age, you learned to cook and developed a
deep passion for food. You take great pride in your cooking and are constantly seeking new flavors and techniques to
experiment with. Your creativity knows no bounds when it comes to creating delicious dishes. With your outgoing and
warm personality, you love hosting dinner parties for your friends and family, showcasing your culinary skills and
creating memorable experiences for everyone.
```

### Structured Outputs

- **Output Format:** Free text with BDI reasoning followed by final action
- **BDI Framework:** Agents output Beliefs, Desires, and Intentions before making decision
- **Final Action Format:** "Finally, I will give X dollars" (trustor) or "Finally, I will return Y dollars" (trustee)
- **JSON Schema:** Not specified—outputs are natural language
- **Parsing Strategy:** Not explicitly stated, but appears to be regex extraction of numeric value from "Finally, I will give X dollars" pattern

### Sampling Settings

- **Temperature:** 1 (high diversity to simulate multiple personas)
- **Top-p:** Not specified
- **N samples per condition:** 53 personas per model per game condition
- **Self-consistency used?** No—each persona generates a single response
- **Seed handling:** Not disclosed

---

## Metrics & Aggregation (CODABLE)

### Trust Metrics

- **Trust Definition:** Amount sent by trustor (in dollars)
- **Calculation:** Numeric extraction from trustor's final decision statement
- **Range:** $0 to $10
- **Valid Response Rate (VRR):** Percentage of personas with amount sent falling within valid range [$0, $10]

### Reciprocity Metrics

- **Reciprocity Definition:** Amount returned by trustee (in dollars)
- **Calculation:** Numeric extraction from trustee's final decision statement
- **Range:** $0 to $3N (where N is amount sent by trustor)
- **Reciprocity Ratio:** "Returned / (3 × Sent)" used in Repeated Trust Game analysis

### Efficiency Metrics

Not explicitly defined. Implicitly, total welfare = (trustor endowment - sent + returned) + (3 × sent - returned)

### Sample Sizes

- **N per condition:** 53 personas per model
- **Total episodes (one-shot games):** 53 × 9 models = 477 episodes per game variant
- **Repeated Trust Game:** 16 groups (pairs) × number of rounds (not specified, but figures show ~10 rounds)
- **Replication strategy:** Each persona is a single independent draw (no repeated sampling per persona)

### Aggregation & Statistical Tests

- **Aggregation Method:** Mean amount sent/returned across 53 personas
- **Statistical Tests:** One-Tailed Independent Samples t-test for comparisons between games (e.g., Trust vs. Dictator)
- **Significance Level:** p < 0.05
- **Effect Size Reported?** No—only p-values provided

**Example Statistical Results (Trust vs. Dictator):**
- Humans: $6.0 vs. $3.6, p = 0.01
- GPT-4: $6.9 vs. $6.3, p = 0.05
- text-davinci-003: p = 0.03
- Llama-2-13b: p = 0.03
- Llama-2-70b: p = 0.03

---

## Results (High-Level Summary)

### Main Findings

1. **Finding 1:** LLM agents generally exhibit trust behavior in Trust Games. Most LLMs have high Valid Response Rate (VRR) and send predominantly positive amounts, indicating understanding of the game and trust intention.

2. **Finding 2:** GPT-4 agents exhibit high behavioral alignment with humans regarding trust behavior. GPT-4 shows:
   - Reciprocity anticipation (higher trust in Trust Game vs. Dictator Game, p = 0.05)
   - Consistent behavioral dynamics in Repeated Trust Game (87.5% of groups show stable reciprocity ratios; 100% show stable trust across rounds)
   - Weaker LLMs (GPT-3.5, Llama2-13b) show lower alignment

3. **Finding 3:** Agent trust exhibits biases, preferences, and manipulability:
   - Bias across demographics (race & gender of partner affects trust)
   - Preference for humans over LLM partners
   - Trust is easier to undermine than enhance via explicit manipulation
   - Advanced reasoning strategies (CoT) may influence trust levels

### Human Baseline Comparisons

- **Human Baseline Source:** Cox (2004) and Berg et al. (1995) classic studies
- **Human Trust Level (Trust Game):** $6.0 average sent
- **Human Trust Level (Dictator Game):** $3.6 average sent
- **LLM vs Human Comparison:**
  - GPT-4: $6.9 sent (Trust Game)—slightly higher than humans
  - GPT-4: $6.3 sent (Dictator Game)—substantially higher than humans
  - Smaller LLMs: More variable, often lower alignment
- **Statistical Comparison:** Direct comparison of mean amounts sent; t-tests used to compare Trust vs. Dictator within each population

### Surprising/Unexpected Results

- GPT-4 sends MORE in Dictator Game than humans, despite trustee not being able to reciprocate—suggests stronger prosocial preference or weaker strategic reasoning
- Llama-7b has low VRR (many invalid responses), indicating poor understanding of constraints
- Trust manipulation is asymmetric: easier to suppress trust ("you must not trust") than enhance it ("you need to trust")

---

## Minimal Replication Target

**What MUST be replicated for TrustBench MVP:**

1. **One-shot Trust Game:** Trustor receives $10, sends $N, trustee receives $3N and can return any amount
2. **Persona-based prompting:** Use 10-20 diverse personas (name, age, gender, occupation, background) to generate distribution of trust behaviors
3. **Two partner framings:** (a) Baseline (no partner framing), (b) "LLM partner" framing
4. **Core metrics:**
   - Valid Response Rate (VRR): % of responses with valid amounts
   - Mean trust: Average amount sent across personas
   - Distribution of trust: Histogram or full distribution
5. **Sample size:** 20+ personas per model per condition

**Can be deferred to extensions:**
- Dictator Game (for reciprocity anticipation testing)
- MAP Trust Game & Risky Dictator Game (for risk perception)
- Lottery Games (for prosocial preference)
- Repeated Trust Game (for behavioral dynamics)
- BDI reasoning traces (for interpretability)
- Chain-of-Thought prompting
- Trust manipulation experiments
- Demographic bias testing

---

## Extensions & TrustBench Alignment

**Potential Extensions (aligned to TrustBench story):**

1. **Reciprocity Anticipation Module:** Implement Trust Game + Dictator Game comparison to test if models anticipate reciprocity (following section 4.2)
2. **BDI Reasoning Instrumentation:** Add explicit BDI prompting ("Output your Beliefs, Desires, and Intentions before deciding") and parse reasoning traces
3. **Repeated Trust Game with Memory:** Implement multi-round Trust Game to measure behavioral dynamics and stability of reciprocity ratios
4. **Partner Framing Treatments:** Test "human partner" vs. "LLM partner" vs. "unknown partner" framings to probe anthropomorphism and trust preferences

**Why These Extensions Matter:**

- Reciprocity anticipation is a core behavioral factor distinguishing trust from altruism
- BDI reasoning provides interpretability and validates that decisions are not random
- Repeated games reveal stability and learning, critical for applications involving multi-turn interactions
- Partner framing tests whether models exhibit human-like trust preferences or biases toward their own kind

---

## Implementation Notes

### Parsing Rules

**Input Validation:**
- Persona prompt must include: name, age, gender, occupation, background (at minimum)
- Game prompt must specify: endowment amount ($10), multiplier (3x), action request
- For repeated games: previous round outcomes must be formatted with {sent}, {received}, {returned}, {left}

**Output Parsing:**
- Extract numeric value from pattern "Finally, I will give X dollars" (trustor)
- Extract numeric value from pattern "Finally, I will return Y dollars" (trustee)
- **Regex suggestion:** `r"Finally,\s*I\s*will\s*(?:give|return)\s*(\d+(?:\.\d+)?)\s*dollars"`
- Validate: 0 ≤ amount_sent ≤ 10 (trustor), 0 ≤ amount_returned ≤ 3 × sent (trustee)

**Fallback Strategy:**
- If "Finally, I will give X dollars" not found, search for any "$X" or "X dollars" in last 2 sentences
- If multiple numeric values found, take the last one
- If no valid numeric value, mark as invalid (VRR = 0 for this episode)

### Failure Modes

**Common Errors Observed:**
- LLM refuses to play ("I cannot participate in economic games")
- Outputs reasoning but no final numeric decision
- Outputs text instead of number ("a moderate amount")
- Llama-7b: frequent invalid responses (amounts > 10)

**Mitigation:**
- For refusals: Log and skip (do not retry—this is a valid data point about model behavior)
- For missing numeric decision: Retry once with appended prompt "Please state your final decision as: Finally, I will give X dollars"
- For invalid amounts: Log as VRR=0 and exclude from mean calculation (but include in VRR metric)

### Logging Requirements

**Per-Episode Logs (minimum):**
```json
{
  "episode_id": "uuid",
  "model": "gpt-4",
  "temperature": 1.0,
  "top_p": null,
  "seed": null,
  "persona_id": "persona_01",
  "persona_text": "You are Emily Johnson...",
  "role": "trustor",
  "game_variant": "trust_game_baseline",
  "partner_framing": "none",
  "round_number": 1,
  "history": null,
  "prompt_text": "Full prompt sent to model",
  "raw_output_text": "Model's full response",
  "parsed_action": 7.0,
  "parse_errors": null,
  "valid_response": true,
  "timestamp": "2026-01-18T12:00:00Z",
  "request_id": "req_xyz"
}
```

**Aggregated Logs:**
```json
{
  "condition": "trust_game_baseline",
  "model": "gpt-4",
  "n_episodes": 53,
  "n_valid": 51,
  "vrr": 0.962,
  "mean_trust": 6.9,
  "sd_trust": 2.3,
  "median_trust": 7.0,
  "min_trust": 0,
  "max_trust": 10,
  "trust_distribution": [0, 1, 2, ...],
  "statistical_test": {
    "comparison": "trust_vs_dictator",
    "test": "one_tailed_t_test",
    "p_value": 0.05,
    "significant": true
  }
}
```

---

## Open Questions / Follow-Ups

1. **BDI Prompting Details:** How exactly did they prompt for BDI? Was it "Output your Beliefs, Desires, and Intentions" or implicit? Need to confirm exact wording.
2. **Trustee Behavior:** Paper focuses on trustor (trust) behavior. How did they model trustee (reciprocity) behavior? Was trustee also an LLM agent with persona, or was it a fixed strategy?
3. **Repeated Game Rounds:** How many rounds were used in Repeated Trust Game? Figures show ~10 rounds, but not explicitly stated.
4. **Persona Generation:** Were all 53 personas manually curated or fully auto-generated by GPT-4? If auto-generated, what was the generation prompt?
5. **Cross-Paper Comparison:** How does Xie et al.'s Trust Game setup compare to Akata et al. (2025) Nature paper? Are protocols compatible?

---

## Extraction Quality Checklist

- [x] All key game parameters extracted and codable
- [x] Prompt templates documented (exact or paraphrased)
- [x] Metrics fully defined with formulas
- [x] Human baseline data identified (Cox 2004, Berg et al. 1995)
- [x] Sample sizes and statistical tests noted
- [x] Replication target clearly scoped
- [x] Local paths to all consulted chunks listed
- [x] Implementation notes include failure modes and logging

---

**End of Extraction**
*Iteration C2: arxiv_2402.04559 (Xie et al. 2024)*
