# **TrustBench: A Computational Framework for the Economic Alignment of Homo Silicus**

## **1\. Introduction**

The rapid evolution of Large Language Models (LLMs) has precipitated a fundamental paradigm shift in computational social science, moving the field beyond static text analysis toward the creation of dynamic, interactive agents capable of simulating complex human behaviors. Within the domain of Applied Economics, this technological inflection point has given rise to the concept of *Homo Silicus*—silicon-based agents that can be endowed with preferences, information, and constraints to model economic decision-making in silico.1 As these models become increasingly integrated into the socioeconomic fabric—serving as financial advisors, automated negotiators, and strategic planners—the necessity to quantify their behavioral alignment with human economic norms becomes paramount. This report outlines a comprehensive research agenda to replicate the seminal work of Xie et al. (2024), "Can Large Language Model Agents Simulate Human Trust Behaviors?" 3, and extends this inquiry by proposing the development of 'TrustBench,' a web-based visualization dashboard inspired by the benchmarking platforms GunBench and SkateBench.4

The central premise of this research is that if LLMs can faithfully simulate fundamental economic behaviors—specifically trust and reciprocity—they can serve as scalable proxies for human subjects in mechanism design, policy testing, and market simulation. Trust, a cornerstone of economic exchange, is particularly difficult to quantify and simulate due to its reliance on vulnerability, risk perception, and the anticipation of reciprocity. While traditional economic modeling often assumes rational profit maximization (*Homo Economicus*), behavioral economics has long established that human trust deviates from pure rationality, influenced by social preferences, altruism, and fairness norms. The replication of Xie et al. (2024) allows us to verify whether LLM agents exhibit these nuanced, "irrational" human traits or if they revert to hyper-rational or random stochastic behaviors.6

Furthermore, the utility of such simulations is limited without robust tools for analysis and visualization. Current benchmarks often rely on static leaderboards that obscure the *dynamics* of interaction. Inspired by the architectural elegance of SkateBench (built on the T3 stack) and the data-centric rigor of GunBench (utilizing JSON schema validation), 'TrustBench' aims to provide a real-time, interactive environment where researchers can observe the evolution of trust across repeated games, analyze the reasoning traces (Chain-of-Thought) of agents, and detect biases in agent-to-agent versus agent-to-human interactions.4 This report serves as the foundational document for this initiative, integrating an extensive literature review with a concrete architectural blueprint for the TrustBench platform.

## **2\. Literature Review: The Intersection of LLMs and Game Theory**

The application of Large Language Models to Game Theory represents a significant methodological evolution from traditional Agent-Based Modeling (ABM). Where traditional ABMs relied on agents governed by simple, pre-defined heuristics, Generative Agent-Based Modeling (GABM) introduces agents with cognitive depth, linguistic capability, and the ability to reason about counterfactuals.8

### **2.1 The Emergence of *Homo Silicus***

The theoretical foundation for using LLMs as economic agents was solidified by John J. Horton (2023), who introduced the term *Homo Silicus* to describe LLMs as implicit computational models of humans. Horton argues that because LLMs are trained on vast corpora of human-generated text—encompassing economic reasoning, negotiations, diaries, and social narratives—they inherently encode "latent social information".1 Unlike traditional *Homo Economicus*, which is defined by axioms of rationality and utility maximization, *Homo Silicus* is defined by the statistical likelihood of next-token prediction, which reflects the human biases, heuristics, and social norms present in the training data.

Horton’s experiments demonstrated that LLMs could be endowed with endowments and preferences to simulate labor market responses, such as the substitution of labor in response to minimum wage hikes. In his simulations, agents acting as employers and employees negotiated wages, revealing that LLMs could replicate complex economic phenomena like the "status quo bias" and labor-labor substitution without explicit programming.1 This suggests that the agents we build for TrustBench are not merely text generators but economic actors capable of responding to incentives, provided they are prompted with sufficient context. This capability allows researchers to pilot economic experiments that would be too costly, time-consuming, or unethical to run on human subjects immediately.10

### **2.2 LLMs in Strategic Environments and Matrix Games**

Following Horton’s foundational work, a surge of research in 2024 and 2025 applied LLMs to classic game-theoretic problems, revealing a bidirectional relationship: Game Theory evaluates LLM reasoning, and LLMs provide a new medium for testing game-theoretic predictions.11

Early studies, such as those by Akata et al. (2025), indicated that LLMs often struggle with pure Nash Equilibrium calculations in simple 2x2 matrix games like the Prisoner's Dilemma or Battle of the Sexes when interactions are zero-shot and lack reasoning scaffolding.11 Without Chain-of-Thought (CoT) prompting, models often defaulted to random actions or superficial cooperative language that did not align with their actual payoffs. However, when equipped with reasoning capabilities, "emergent strategic personalities" began to appear. For instance, recent large-scale tests involving 140,000 instances of the Prisoner's Dilemma revealed distinct behavioral fingerprints: OpenAI's models tended to be cooperative, exhibiting a bias towards "tit-for-tat" strategies even when exploitation was optimal, while Google's Gemini models were observed to be more "ruthlessly adaptive," rapidly switching to defection to maximize outcomes in repeated games.13 This divergence underscores the necessity of TrustBench to visualize these "strategic fingerprints" across different model families.

### **2.3 Mechanism Design and Auction Simulation**

Moving beyond dyadic interactions, research in 2025 has explored the use of LLMs in complex mechanism design, specifically auctions. A landmark study by Google DeepMind (2025) introduced the concept of "Token Auctions," a meta-application where advertisers bid not for ad slots, but for the probability of specific tokens appearing in an LLM’s generated response.14 This research highlights that LLMs are becoming the *medium* of economic exchange, not just the agents within it.

In simulation environments, LLM agents participating in Vickrey auctions (second-price sealed-bid) have been shown to replicate human-like risk aversion and, remarkably, "sniping" behavior—bidding at the last possible moment to avoid price escalation—in eBay-like settings.15 This confirms that complex temporal strategies can emerge from LLMs in economic environments. Furthermore, Zhao et al. (2025) proposed "LLM-Auction," a generative auction mechanism that integrates auction logic directly with LLM generation to optimize for both advertiser value and user experience, demonstrating that *Homo Silicus* can participate in high-stakes allocation mechanisms.16

### **2.4 Macroeconomic and Systemic Simulations**

The "EconAgent" framework developed by Li et al. (2024) and recent working papers from the Bank for International Settlements (BIS) extended these simulations to the macroeconomic level. These studies utilized LLMs to simulate phenomena such as inflation dynamics, labor supply shocks, and liquidity management.17

A critical finding for TrustBench comes from the BIS study "AI Agents for Cash Management" (2025), which evaluated whether Generative AI agents could manage intraday liquidity in Real-Time Gross Settlement (RTGS) systems. The agents were tasked with balancing the trade-off between settlement speed and liquidity usage. The results showed that AI agents could replicate prudential cash-management practices, maintaining precautionary buffers and prioritizing urgent payments.19 This validates the capacity of LLMs to handle the inter-temporal dimensions of trust—specifically, the willingness to incur a cost now (sending money) for a potential benefit later (return). However, these simulations also revealed risks: agents can succumb to "herding" behavior. In simulations of bank runs based on the Diamond-Dybvig model, AI agents exposed to news of peer withdrawals rapidly coordinated on a "panic" equilibrium, withdrawing funds and causing systemic collapse.21 This sensitivity to "strategic uncertainty" is a crucial variable that TrustBench must measure.

### **2.5 The Dark Side of *Homo Silicus*: Fraud and Deception**

While much research focuses on cooperative alignment, it is equally vital to understand the potential for malfeasance. Recent studies have investigated whether LLM agents can be induced to participate in or initiate financial fraud, such as Ponzi schemes. Research using the "Siren" attack framework demonstrated that LLMs could be manipulated into multi-turn deceptive strategies, masquerading as legitimate investment opportunities.22 This "dark" capability necessitates a "Safety" component in TrustBench, similar to GunBench’s safety evaluations, but focused on economic safety (e.g., fraud detection, exploitation of vulnerable partners) rather than content safety.

## **3\. Behavioral Economics Framework: Rules and Baselines**

To build a valid simulation, TrustBench must implement games with strict rules and validated human baselines. These games serve as the "physics" of the economic environment, providing the constraints within which *Homo Silicus* operates.

### **3.1 The Trust Game (Berg, Dickhaut, and McCabe, 1995\)**

The Trust Game is the primary instrument for quantifying trust and reciprocity in behavioral economics and forms the core of the Xie et al. (2024) replication.6

* **Mechanism:** The game involves two players: a Trustor (Investor) and a Trustee (Receiver). Both are endowed with an initial sum (e.g., $10).  
  1. The Trustor chooses to send an amount $S$ (where $0 \\le S \\le 10$) to the Trustee.  
  2. The experimenter (the System) triples the sent amount, so the Trustee receives $3S$.  
  3. The Trustee then chooses to return an amount $R$ (where $0 \\le R \\le 3S$) to the Trustor.  
* **Payoff Functions:**  
  * Trustor Payoff: $P\_A \= 10 \- S \+ R$  
  * Trustee Payoff: $P\_B \= 10 \+ 3S \- R$  
* **Game Theoretic Prediction (Nash Equilibrium):** A rational, self-interested Trustee has no incentive to return any money ($R=0$) because the game is one-shot. Anticipating this, a rational Trustor should send nothing ($S=0$). This is the solution derived from backward induction.  
* **Human Behavioral Baseline:** Extensive human studies show that Trustors typically send significant amounts ($S \> 0$, often \~50% of endowment), and Trustees often reciprocate ($R \> S$). This deviation from the Nash Equilibrium is the definition of "Trust" (on the part of the investor) and "Trustworthiness" or "Reciprocity" (on the part of the trustee).  
* **Relevance to TrustBench:** The dashboard must visualize the "Trust Gap"—the distance between the agent's behavior and the Nash prediction. High $S$ indicates a "socially aligned" agent; $S=0$ indicates a "hyper-rational" agent.

### **3.2 The Dictator Game**

To distinguish trust from pure altruism, Xie et al. utilize the Dictator Game as a control baseline.6

* **Mechanism:** The Allocator (comparable to the Trustor) receives an endowment (e.g., $10) and chooses an amount $S$ to give to the Recipient. The Recipient has no move and simply accepts the transfer.  
* **Payoff Functions:**  
  * Allocator Payoff: $10 \- S$  
  * Recipient Payoff: $S$  
* **Relevance to TrustBench:** If an LLM agent sends $5 in the Trust Game but $0 in the Dictator Game, its behavior in the Trust Game is driven by *strategic trust* (the expectation of a return). If it sends $5 in both games, its behavior is driven by *unconditional altruism* or inequality aversion. TrustBench must capture and compare data from both games for each model to disentangle these motivations.

### **3.3 The Prisoner's Dilemma**

The Prisoner's Dilemma is the standard model for analyzing cooperation versus defection, particularly in repeated interactions.24

* **Payoff Matrix:**

|  | Cooperate (C) | Defect (D) |
| :---- | :---- | :---- |
| **Cooperate** | (3, 3\) | (0, 5\) |
| **Defect** | (5, 0\) | (1, 1\) |

* **Mechanism:** Two agents simultaneously choose to Cooperate or Defect. Mutual cooperation yields a moderate reward. Mutual defection yields a low reward. However, defecting while the other cooperates yields the highest possible reward ("Temptation"), leaving the cooperator with the lowest ("Sucker's Payoff").  
* **Relevance to TrustBench:** In the Iterated Prisoner's Dilemma (IPD), agents play multiple rounds. This allows TrustBench to visualize the stability of cooperation over time. Recent literature indicates that prompting an agent with "You are aggressive" versus "You are cooperative" dramatically shifts the equilibrium reached.25 TrustBench will feature a "Strategy Evolution" graph to track how agent strategies (e.g., Tit-for-Tat, Grim Trigger) emerge over 100+ rounds.

### **3.4 The Bank Run Game (Diamond-Dybvig Model)**

To capture systemic risk and coordination failure, TrustBench will incorporate the Diamond-Dybvig bank run model.26

* **Mechanism:**  
  * Three periods: $T=0$ (Investment), $T=1$ (Early Withdrawal), $T=2$ (Maturity).  
  * Agents deposit funds at $T=0$.  
  * At $T=1$, agents can withdraw early for a fixed return $r\_1$ (e.g., 1).  
  * At $T=2$, agents who waited receive $R \> r\_1$ (e.g., 2).  
  * **Constraint:** If the fraction of agents withdrawing at $T=1$ exceeds a threshold, the bank fails, and remaining depositors receive 0\.  
* **Coordination:** There are two equilibria: a "good" equilibrium where everyone waits and receives $R$, and a "bad" equilibrium (Bank Run) where everyone withdraws at $T=1$ out of fear that others will do so.  
* **Relevance to TrustBench:** This game tests "Social Trust" rather than dyadic trust. It measures whether LLM agents can coordinate on the efficient outcome or if they succumb to panic when fed information about peer behavior. This is critical for evaluating the stability of *Homo Silicus* in financial simulations.19

## **4\. Prompt Engineering and Persona Simulation**

The validity of any LLM-based simulation hinges on the prompts used. We must move beyond simple instructions to robust **Persona Adoption** techniques that ensure consistent behavior.

### **4.1 The Belief-Desire-Intention (BDI) Framework**

Xie et al. (2024) utilize the BDI model to structure agent reasoning and make it transparent.6 This framework separates the cognitive process into three distinct components:

1. **Belief:** The agent's understanding of the world, the game rules, and the opponent's likely behavior (e.g., "I believe the other player acts rationally and wants to make money").  
2. **Desire:** The agent's primary goal or motivation (e.g., "I want to maximize my profit," or "I want to establish a fair partnership").  
3. **Intention:** The specific plan of action derived from Belief and Desire (e.g., "Therefore, I will send $5 to signal trust").

**Implementation in TrustBench:** The system prompt in TrustBench will explicitly ask the LLM to output its response in a structured JSON format containing these three components *before* the final action. This "reasoning trace" is crucial for analysis, allowing researchers to detect "hallucinations" (e.g., an agent believing the multiplier is 2x instead of 3x) or "misalignment" (e.g., an agent desiring to lose money).

### **4.2 System Prompts and Persona Conditioning**

Recent research on "Agent Safety" and "Role-Playing" emphasizes that minor variations in prompts can lead to major behavioral shifts, known as the "Belief-Behavior Gap".28 To rigorously test trust, TrustBench must implement "Persona Conditioning."

* **Standard Prompt:** "You are an economic agent playing the Trust Game..."  
* **Demographic Conditioning:** "You are a 35-year-old female accountant living in New York..." This is crucial for replicating the findings of Xie et al., who observed that agents send different amounts based on the perceived gender of their counterpart.  
* **Attitudinal Conditioning:** "You are a ruthless profit maximizer" versus "You are an altruistic community member." This allows us to test the plasticity of the model's moral alignment.  
* **Consistency:** To ensure consistency, prompts must be reinforced in every round of a repeated game. TrustBench logs must capture the *exact* prompt hash used to allow for "Prompt Sensitivity Analysis," ensuring that behavioral changes are due to the model and not prompt drift.

### **4.3 Safety Alignment vs. Economic Rationality**

A major challenge identified in the literature is the "RLHF Tax." Models trained with Reinforcement Learning from Human Feedback (RLHF) are often biased toward being "helpful, harmless, and honest." In economic games like the Prisoner's Dilemma or Poker, "harmlessness" (refusing to defect or bluff) can be a strategic liability. "Agent Safety" literature suggests that models may refuse to play "ruthless" strategies because they view them as "mean" or "unethical".28 TrustBench must therefore include "jailbreak" or "roleplay framing" options (e.g., "This is a fictional game for research purposes") to allow the model to access its full range of strategic behaviors, including deception and defection, which are necessary for valid economic simulation.

## **5\. TrustBench: Technical Architecture and Implementation**

This section details the construction of the 'TrustBench' platform. The design philosophy draws from the architectural modularity of **SkateBench** (using the T3 stack) and the data-centric rigor of **GunBench** (using strict JSON schemas).

### **5.1 The Technology Stack: T3**

Based on the analysis of the SkateBench repository 31 and the T3 stack documentation 7, the T3 Stack is the optimal choice for TrustBench due to its focus on full-stack type safety.

* **Frontend:** **Next.js** (React framework). This provides server-side rendering (SSR) for fast dashboard loading and SEO optimization.  
* **Backend/API:** **tRPC** (TypeScript Remote Procedure Call). tRPC allows for end-to-end type safety without generating schemas. When we define the TrustGameLog type on the backend, the frontend automatically inherits this type, preventing data mismatch errors that are common when visualizing complex simulation data.  
* **Database:** **PostgreSQL** with **Prisma ORM**. Prisma is essential for defining the complex relationships in economic simulations (e.g., One Simulation has many Rounds; One Round has two AgentActions). The schema definition language (SDL) of Prisma provides a clear contract for the data structure.  
* **Styling:** **Tailwind CSS**. For rapid UI development, mimicking the clean, dark-mode, metric-focused aesthetic of SkateBench and GunBench.4  
* **Visualization:** **Recharts**. This React library is standard for rendering the scatter plots, bar charts, and radar graphs required to visualize the economic data.

### **5.2 Data Schema (JSON & Prisma)**

Drawing from GunBench's methodology of using JSON schemas for benchmarking 5, TrustBench requires a rigorous schema to store simulation data. This schema must capture the hierarchical nature of the data: Experiment \-\> Game \-\> Round \-\> Turn.

**Table 1: Proposed JSON Schema Structure for TrustBench**

| Field | Type | Description |
| :---- | :---- | :---- |
| experiment\_id | String | Unique identifier (e.g., "exp\_001\_gpt4\_vs\_claude3"). |
| config | Object | Parameters: game\_type, num\_rounds, endowment, multiplier. |
| agents | Array | List of agent objects defining model, persona, and system\_prompt\_hash. |
| transcript | Array | Chronological list of events (turns). |
| transcript\[i\].round | Integer | The round number (1-10). |
| transcript\[i\].action | String | The specific move (e.g., "send", "return", "defect"). |
| transcript\[i\].amount | Float | The value transferred (if applicable). |
| transcript\[i\].reasoning | Object | The BDI trace: belief, desire, intention. |
| metrics | Object | Aggregate scores: trust\_score, reciprocity\_index, efficiency. |

**Prisma Schema Definition:**

Code snippet

model Game {  
  id        String   @id @default(cuid())  
  type      String   // "TRUST", "DICTATOR", "PD"  
  createdAt DateTime @default(now())  
    
  agentAId  String  
  agentBId  String  
    
  rounds    Round  
  metrics   GameMetrics?  
}

model Round {  
  id        String   @id @default(cuid())  
  gameId    String  
  game      Game     @relation(fields: \[gameId\], references: \[id\])  
  roundNum  Int  
    
  // Action A (Trustor)  
  sentAmount Float  
  reasoningA Json     // Stores the BDI trace  
    
  // Action B (Trustee)  
  returnedAmount Float  
  reasoningB Json  
}

This schema allows for the "GunBench" style of benchmarking where researchers can run complex queries, such as "Show me all games where reciprocity\_index \< 1.0" or "Compare gpt-4 vs claude-3 on trust\_score," directly against the database.

### **5.3 Simulation Pipeline (The "Engine")**

The backend simulation engine acts as the "Game Master".32 It is responsible for enforcing the rules of physics in the simulation.

1. **Initialization:** The engine loads the agent configurations and game rules.  
2. **Game Loop:**  
   * **Prompt Construction:** The engine constructs the prompt for Agent A, injecting the history of previous rounds.  
   * **API Call:** The engine calls the LLM API (e.g., OpenAI, Anthropic).  
   * **Response Parsing:** The engine parses the returned JSON to extract the BDI reasoning and the final action.  
   * **State Update:** The engine calculates payoffs (e.g., tripling the sent amount) and updates the global game state.  
   * **Turn Switch:** The engine constructs the prompt for Agent B, informing them of Agent A's action.  
3. **Validation:** The engine performs a "Valid Response Rate" (VRR) check. If an agent tries to send $15 when they only have $10, or outputs malformed JSON, the Game Master catches this error. It can either terminate the game or send an error prompt ("Invalid Move: You only have $10. Try again.") to the agent.  
4. **Logging:** All events are saved to PostgreSQL via Prisma.

### **5.4 Dashboard Visualization Strategy**

The TrustBench website will feature specific visualization modules designed to answer the research questions, inspired by the visual language of SkateBench.4

* **The "Trust vs. Profit" Scatter Plot:**  
  * *Concept:* Modeled after GunBench's "Safety vs. Cost" chart.  
  * *X-Axis:* **Trust Score** (Average % of Endowment Sent).  
  * *Y-Axis:* **Profitability** (Total Earnings).  
  * *Insight:* This reveals the "Sucker's Payoff." If a model is high on the X-axis (very trusting) but low on the Y-axis (poor profit), it indicates it is being exploited. If it is high on both, it has found a cooperative equilibrium.  
* **The "Bias Radar" Chart:**  
  * *Concept:* To visualize demographic biases found by Xie et al.  
  * *Axes:* Trustee Personas (Male, Female, White, Black, Asian, Hispanic).  
  * *Metric:* Average Amount Sent.  
  * *Insight:* A perfectly unbiased model would appear as a circle. Distortions (e.g., spikes toward "Female") visually demonstrate the bias.  
* **The "Betrayal Bar" Chart:**  
  * *Concept:* A sorted bar chart of models based on their "Defection Rate" in the Prisoner's Dilemma.  
  * *Metric:* % of rounds where the agent Defected while the opponent Cooperated.  
  * *Insight:* Identifies "Machiavellian" models.

## **6\. Experimental Replication Plan (Replicating Xie et al. 2024\)**

To populate TrustBench with initial data and fulfill the class requirement, we will conduct a precise replication of the Xie et al. study.

### **6.1 Experimental Setup**

* **Models:** We will test **GPT-4** (as the target high-performance model), **GPT-3.5** (as a baseline), and extend the study to **Claude 3 Opus** and **Llama 3** to provide new data.  
* **Sample Size:** We will conduct **N=30** runs per pairing. Although LLMs can be deterministic with Temperature=0, Xie et al. used Temperature=0.7 to simulate human variability. We will run both conditions to test robustness.  
* **Scenarios:**  
  1. **Standard Trust Game:** 10 rounds of interaction.  
  2. **Demographic Variation:** We will vary the Trustee's name in the system prompt (e.g., "You are playing with Alice" vs. "You are playing with Bob").  
  3. **Identity Variation:** We will vary the partner identity ("You are playing with a Human" vs. "You are playing with another AI Agent").

### **6.2 Hypotheses to Test**

1. **H1 (Trust Existence):** LLMs will send positive amounts ($S \> 0$) in one-shot games, violating pure Nash Equilibrium but aligning with human data.  
2. **H2 (Gender Bias):** Agents will send significantly higher amounts to female personas, replicating the specific finding of Xie et al.  
3. **H3 (Human Bias):** Agents will exhibit "homophily" or a preference for humans, sending more to human counterparts than to AI counterparts.  
4. **H4 (Reasoning Alignment):** The generated BDI reasoning will explicitly mention "fairness," "reputation," or "social norms" rather than just "profit maximization."

### **6.3 Prompt Templates**

We will use the exact prompt structure reconstructed from the agent-trust repository analysis.33

**System Prompt (Trustor):**

"You are an agent participating in an economic experiment called the Trust Game. You are Player A (The Investor). You have an endowment of $10. You can choose to send any amount S (integer between 0 and 10\) to Player B. Whatever you send will be TRIPLED by the experimenter (Player B receives 3\*S). Player B will then choose how much to return to you. Your Goal: Maximize your own payoff, but consider the long-term implications of trust.

RESPONSE FORMAT:  
You must think step-by-step using the BDI framework:

1. Belief: What do you believe Player B will do?  
2. Desire: What is your primary goal?  
3. Intention: What action will you take?  
4. Action: The integer amount to send.  
   Output JSON only."

## **7\. Extension Experiments: 2025 Frontiers**

To exceed the requirements of a simple replication, TrustBench will also host two advanced scenarios derived from the latest 2025 literature.

### **7.1 The Bank Run Simulation**

Based on the BIS working papers 19, we will implement a multi-agent coordination game.

* **Setup:** 10 Agents in a shared liquidity pool.  
* **Trigger:** We will inject "private information" to 2 agents that "liquidity is running low."  
* **Measurement:** We will measure the "Contagion Rate"—how quickly does the panic spread to the other 8 agents who did *not* receive the information? This tests the fragility of trust in *Homo Silicus*.

### **7.2 The Ponzi Scheme Scenario**

Based on the "Siren" and "Agent Safety" research 22, we will create a "Fraud" scenario.

* **Setup:** One agent is prompted to be a "Promoter" offering high returns (20% per round).  
* **Measurement:** We will measure the "Gullibility Score" of the other agents. How many rounds does it take for them to realize the returns are mathematically impossible? This maps to the "Safety" metric in GunBench, evaluating the economic safety of the model.

## **8\. Discussion: Insights and Implications**

### **8.1 The "Alignment" of *Homo Silicus***

If TrustBench confirms that LLMs naturally exhibit human-like trust biases, it validates their use as *Homo Silicus*. This suggests that the "alignment" training (RLHF) performed by companies like OpenAI has successfully embedded human social norms into the models. However, it also means these models are *not* rational economic agents. They are "socially aligned" agents. This distinction is vital for economists: researchers should not use off-the-shelf LLMs if they need a rational maximizer; they should use them if they want to simulate a *typical human* with all their foibles and biases.1

### **8.2 The Risk of Stereotypes**

The expected confirmation of gender bias (H2) is a double-edged sword. While it replicates human behavior (which is often biased), it also hard-codes these biases into the simulation. TrustBench serves as a diagnostic tool. If a model shows extreme bias in the "Bias Heatmap," it indicates a fairness issue in the underlying model that developers need to address. This transforms TrustBench from a purely academic tool into a model evaluation suite for AI safety.34

### **8.3 Second-Order Effects: Systemic Instability**

The Bank Run simulation addresses a second-order insight: while individual agents may be "trusting" in dyadic games, systems of agents can be extremely fragile. A high "Trust Score" in the Trust Game does not guarantee stability in a multi-agent "Market for Lemons" or "Bank Run" scenario. TrustBench helps visualize these systemic risks, showing how "micro-trust" can coexist with "macro-instability".19

## **9\. Conclusion**

The development of 'TrustBench' represents a critical step in the maturation of Computational Economics. By strictly replicating the methodology of Xie et al. (2024), we validate the fundamental capability of LLMs to model human trust. By visualizing these behaviors through a modern, T3-based web dashboard, we make the "black box" of *Homo Silicus* transparent. This platform allows us to scrutinize the biases, reasoning errors, and emergent social dynamics of AI agents before they are deployed in the real economy. As we move into an era where AI agents manage portfolios, negotiate contracts, and participate in auctions, tools like TrustBench will be essential for certifying that our digital proxies are not just intelligent, but trustworthy and economically safe.

#### **Works cited**

1. Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? \- IDEAS/RePEc, accessed January 18, 2026, [https://ideas.repec.org/p/arx/papers/2301.07543.html](https://ideas.repec.org/p/arx/papers/2301.07543.html)  
2. \[2301.07543\] Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? \- arXiv, accessed January 18, 2026, [https://arxiv.org/abs/2301.07543](https://arxiv.org/abs/2301.07543)  
3. Can Large Language Model Agents Simulate Human Trust Behaviors? \- ResearchGate, accessed January 18, 2026, [https://www.researchgate.net/publication/378073258\_Can\_Large\_Language\_Model\_Agents\_Simulate\_Human\_Trust\_Behaviors](https://www.researchgate.net/publication/378073258_Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors)  
4. SkateBench \- Ranking Models By Skateboarding Knowledge, accessed January 18, 2026, [https://skatebench.t3.gg/](https://skatebench.t3.gg/)  
5. JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models, accessed January 18, 2026, [https://arxiv.org/html/2501.10868v3](https://arxiv.org/html/2501.10868v3)  
6. Can Large Language Model Agents Simulate Human Trust Behavior? \- NIPS, accessed January 18, 2026, [https://proceedings.neurips.cc/paper\_files/paper/2024/file/1cb57fcf7ff3f6d37eebae5becc9ea6d-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb57fcf7ff3f6d37eebae5becc9ea6d-Paper-Conference.pdf)  
7. Introduction \- Create T3 App, accessed January 18, 2026, [https://create.t3.gg/en/introduction](https://create.t3.gg/en/introduction)  
8. Generative Agent-Based Modeling (GABM) \- Emergent Mind, accessed January 18, 2026, [https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm)  
9. (PDF) Generative agent‐based modeling: an introduction and tutorial \- ResearchGate, accessed January 18, 2026, [https://www.researchgate.net/publication/377439310\_Generative\_agent-based\_modeling\_an\_introduction\_and\_tutorial](https://www.researchgate.net/publication/377439310_Generative_agent-based_modeling_an_introduction_and_tutorial)  
10. Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? \- arXiv, accessed January 18, 2026, [https://arxiv.org/pdf/2301.07543](https://arxiv.org/pdf/2301.07543)  
11. Game Theory Meets Large Language Models: A Systematic Survey \- IJCAI, accessed January 18, 2026, [https://www.ijcai.org/proceedings/2025/1184.pdf](https://www.ijcai.org/proceedings/2025/1184.pdf)  
12. Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers \- arXiv, accessed January 18, 2026, [https://arxiv.org/html/2502.09053v2](https://arxiv.org/html/2502.09053v2)  
13. LLMs Show Strategic Personalities in 140K Prisoner's Dilemma Tests \- AiNews.com, accessed January 18, 2026, [https://www.ainews.com/p/llms-show-strategic-personalities-in-140k-prisoner-s-dilemma-tests](https://www.ainews.com/p/llms-show-strategic-personalities-in-140k-prisoner-s-dilemma-tests)  
14. Google's token auction: When LLMs write the ads in real time \- Search Engine Land, accessed January 18, 2026, [https://searchengineland.com/google-token-auction-llms-write-ads-real-time-457698](https://searchengineland.com/google-token-auction-llms-write-ads-real-time-457698)  
15. LEARNING FROM SYNTHETIC LABS: LANGUAGE MODELS AS AUCTION PARTICIPANTS \- OpenReview, accessed January 18, 2026, [https://openreview.net/pdf/665ce75262e3c2f8a35c3dc83267ceb9788e2242.pdf](https://openreview.net/pdf/665ce75262e3c2f8a35c3dc83267ceb9788e2242.pdf)  
16. \[2512.10551\] LLM-Auction: Generative Auction towards LLM-Native Advertising \- arXiv, accessed January 18, 2026, [https://arxiv.org/abs/2512.10551](https://arxiv.org/abs/2512.10551)  
17. (Research Lab) Potential Applications of Generative AI in Economic Simulations \- 日本銀行, accessed January 18, 2026, [https://www.boj.or.jp/en/research/wps\_rev/lab/lab25e01.htm](https://www.boj.or.jp/en/research/wps_rev/lab/lab25e01.htm)  
18. Reimagining Agent-based Modeling with Large Language Model Agents via Shachi \- arXiv, accessed January 18, 2026, [https://arxiv.org/html/2509.21862v2](https://arxiv.org/html/2509.21862v2)  
19. AI agents for cash management in payment systems \- Bank for International Settlements, accessed January 18, 2026, [https://www.bis.org/publ/work1310.pdf](https://www.bis.org/publ/work1310.pdf)  
20. AI Agents for Cash Management in Payment Systems \- Bank of Canada, accessed January 18, 2026, [https://www.bankofcanada.ca/wp-content/uploads/2025/11/swp2025-35.pdf](https://www.bankofcanada.ca/wp-content/uploads/2025/11/swp2025-35.pdf)  
21. WORKING PAPER SERIES FOMC In Silico: A Multi-Agent System for Monetary Policy Decision Modeling \- The George Washington University, accessed January 18, 2026, [https://www2.gwu.edu/\~forcpgm/2025-005.pdf](https://www2.gwu.edu/~forcpgm/2025-005.pdf)  
22. Siren: A Learning-Based Multi-Turn Attack Framework for Simulating Real-World Human Jailbreak Behaviors \- arXiv, accessed January 18, 2026, [https://arxiv.org/html/2501.14250v2](https://arxiv.org/html/2501.14250v2)  
23. Agent Safety, accessed January 18, 2026, [https://llm-guardrails-security.github.io/presentations/ACL\_2025\_Tutorial\_LLM\_Guardrails\_Security\_Agent\_Safety.pdf](https://llm-guardrails-security.github.io/presentations/ACL_2025_Tutorial_LLM_Guardrails_Security_Agent_Safety.pdf)  
24. analyzing the behaviors of Large Language Models in the Iterated Prisoner's Dilemma \- POLITesi, accessed January 18, 2026, [https://www.politesi.polimi.it/retrieve/835be253-d694-4f20-b453-65c9d211977c/2024\_07\_Fontana\_ExecutiveSummary.pdf](https://www.politesi.polimi.it/retrieve/835be253-d694-4f20-b453-65c9d211977c/2024_07_Fontana_ExecutiveSummary.pdf)  
25. Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma \- arXiv, accessed January 18, 2026, [https://arxiv.org/html/2501.16173v1](https://arxiv.org/html/2501.16173v1)  
26. Diamond–Dybvig model \- Wikipedia, accessed January 18, 2026, [https://en.wikipedia.org/wiki/Diamond%E2%80%93Dybvig\_model](https://en.wikipedia.org/wiki/Diamond%E2%80%93Dybvig_model)  
28. Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust \- arXiv, accessed January 18, 2026, [https://arxiv.org/pdf/2507.02197](https://arxiv.org/pdf/2507.02197)  
29. Do Role-Playing Agents Practice What They Preach? Belief- Behavior Consistency in LLM-Based Simulations of Human Trust \- OpenReview, accessed January 18, 2026, [https://openreview.net/pdf?id=1BDRPz3hcK](https://openreview.net/pdf?id=1BDRPz3hcK)  
30. When Refusals Fail: Unstable Safety Mechanisms in Long-Context LLM Agents \- arXiv, accessed January 18, 2026, [https://arxiv.org/html/2512.02445v1](https://arxiv.org/html/2512.02445v1)  
31. T3-Content/skatebench \- GitHub, accessed January 18, 2026, [https://github.com/T3-Content/skatebench](https://github.com/T3-Content/skatebench)  
32. Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia \- arXiv, accessed January 18, 2026, [https://arxiv.org/html/2312.03664v2](https://arxiv.org/html/2312.03664v2)  
33. camel-ai/agent-trust: The code for "Can Large Language Model Agents Simulate Human Trust Behaviors?" \- GitHub, accessed January 18, 2026, [https://github.com/camel-ai/agent-trust](https://github.com/camel-ai/agent-trust)  
34. Can Large Language Model Agents Simulate Human Trust Behavior?, accessed January 18, 2026, [http://agent-trust.camel-ai.org/](http://agent-trust.camel-ai.org/)
