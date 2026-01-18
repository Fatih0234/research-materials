## 2 EVALUATING LLMS IN GAME-BASED PLAYGROUND

The integration of LLMs into game-based environments has emerged as a powerful avenue for evaluating their cognitive and decision-making capabilities. In contrast to traditional evaluation paradigms that emphasize linguistic competence, game-based evaluations reveal deeper dimensions of LLM behavior, such as human-like decision-making, uncertainty management, and strategic interaction. This section explores the growing role of games as playgrounds for LLM assessment: Subsection 2.1 analyzes the observable behaviors of LLMs when deployed as agents in games, highlighting decision-making patterns and interactive dynamics. Subsection 2.2 focuses on the approaches to strengthen the strategic reasoning capabilities of LLMs, including prompting techniques, fine-tuning, and tool integration. Together, these provide a comprehensive perspective on how games serve as both behavioral probes and enhancement platforms for LLMs.

Manuscript submitted to ACM

Table 1. A Summary of LLM-based Agents' Behavioral Features in Various Game Categories.

| Game Category                                                                        | Information         | Nature        | Interaction            | Structure              |
|--------------------------------------------------------------------------------------|---------------------|---------------|------------------------|------------------------|
| Basic Matrix Games §2.1.1 e.g. , Prisoner's Dilemma, Ultimatum Game, RPS [12, 35-38] | Perfect / Imperfect | Comp. / Coop. | Single-turn / Repeated | Symmetric / Asymmetric |

Spotlight: LLMs exhibit strong pro-social biases ( e.g., fairness, cooperation) often deviating from game-theoretic rationality. They struggle with probabilistic reasoning and approximating mixed-strategy Nash equilibria, showing high sensitivity to prompt framing.

| Identity Games §2.1.2 e.g. , Avalon, Werewolf, Jubensha [13, 20, 39, 40]   | Imperfect   | Comp. / Coop.   | Multi-turn, Social   | Asymmetric   |
|----------------------------------------------------------------------------|-------------|-----------------|----------------------|--------------|

Spotlight: Capable of recursive reasoning and social modeling ( e.g., influencing teammates). However, they lack strategic reliability, failing to maintain role consistency and logical coherence under pressure, and are prone to hallucinations.

Negotiation &amp; Coordination

§2.1.3

e.g. , Bargaining, Overcooked, Hanabi

[19, 41-44]

Imperfect

Comp. / Coop.

Multi-turn, Communicative

Symmetric / Asymmetric

Spotlight: Demonstrate recognizable negotiation tactics (bluffing, anchoring) and emerging Theory of Mind (ToM). Yet, robust coordination is limited; they often regress to selfish or inconsistent strategies in complex scenarios without social scaffolding.

| Economic Games §2.1.4 e.g. , Bertrand Competition, Auctions [15, 45-47]   | Imperfect   | Comp.   | Multi-turn Repeated   | Symmetric   |
|---------------------------------------------------------------------------|-------------|---------|-----------------------|-------------|

Spotlight: Display adaptive economic strategies, such as tacit collusion in pricing games. Performance is bounded by imperfect reasoning and fragile risk assessment, often failing to achieve equilibrium strategies consistently.

```
Board & Card Games §2.1.5 e.g. , Chess, Go, Poker [48-51] Perfect / Imperfect Comp. Multi-turn Symmetric
```

Spotlight: Baseline models show significant strategic deficiencies. They struggle with deep calculation, logical consistency, and managing uncertainty information, often producing invalid or strategically incoherent moves without specialized fine-tuning.
