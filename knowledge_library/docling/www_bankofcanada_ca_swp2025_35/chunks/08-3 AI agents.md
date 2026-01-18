## 3 AI agents

Gen AI represents a rapidly advancing class of AI models designed to learn from extensive datasets and generate new, human-like content or data (Horton 2023; Aher et al. 2023; Korinek 2023). Leveraging substantial computational resources, Gen AI models, such as large language models (LLMs) based on Transformer architectures, have demonstrated remarkable success in generating coherent text (Vaswani et al. 2017; Chang et al. 2024). Recent advances in Gen AI have helped improve language model capabilities. Early LLMs were predominantly reactive, often struggling with complex problem-solving and logical deduction. In contrast, new models with 'reasoning' capabilities mitigate some of these limitations-to a certain extent-by employing techniques that enable step-by-step analysis (Wei et al. 2022; Korinek 2023, 2025).

A key innovation is chain-of-thought prompting, which guides models to break down lengthy,

Liquidity decision

Level 1

As a Tool

Execute end-to-end

Mange entire payments workflow

Level 5

complex queries into smaller, manageable steps that facilitate systematic reasoning. Moreover, when combined with a tree-of-thoughts approach, this technique enables models to explore multiple solution paths, detect errors, and iteratively refine their responses. These systems can also leverage external information via the Internet and internal data through retrieval-augmented generation (RAG), thereby providing access to both real-time and proprietary information to tailor their outputs (Wei et al. 2022; Wiesinger et al. 2024; Wang et al. 2024; OpenAI 2025).

The integration of reasoning, logic, and both external and internal data access in new Gen AI models embodies the concept of an Agentic AI (Wiesinger et al. 2024; Horton 2023; Wang et al. 2024; Perez Cruz and Shin 2025; Korinek 2025). These autonomous agents can proactively gather information, formulate plans, and execute actions to achieve specified goals. The advances in reasoning capabilities described above represent critical steps toward this objective, enabling AI agents to plan multi-step actions and adjust strategies based on outcomes (Ott et al. 2023; Wiesinger et al. 2024; Korinek 2025).

The literature suggests that AI agents can exhibit varying degrees of autonomy and capability and can be classified into five categories based on these characteristics (Bornet et al., 2025). Similarly, as outlined in Figure 2, we map AI agents' utility in payment systems across five levels-Tool, Assistant, Operator, Actor, and Agent-showing a progressive shift from basic rule-based automation to fully independent decision-making. This framework shows how payment systems can evolve from simple automation toward sophisticated agentic systems:

Figure 2: High-level progression framework for AI agents with an example payment-related tasks at each level.

<!-- image -->

- Level 1 (as a Tool): Simple rule-based alerts and balance queries that require cash manager intervention for every decision.

Adapt strategies dynamically

- Level 2 (as an Assistant): Data-driven recommendations for tasks like fraud alerts or liquidity transfers, where the agent proposes actions but relies on a human cash manager to execute them.
- Level 3 (as an Operator): Autonomous execution of predefined workflows, such as routing non-urgent payments under defined rules, without human triggers.
- Level 4 (as an Actor): Dynamic adaptation and strategic decision-making (e.g., adjusting payment priorities or liquidity strategies in real time based on changing conditions) while still operating within risk limits set by the cash manager.
- Level 5 (as an Agent): Fully independent orchestration of end-to-end processes, such as intraday payments and liquidity optimization, implementing decisions with minimal cash manager oversight.

These developments open new avenues for applying LLMs in payments research. Agentic AI can help simulate individual agent behavior in payment systems, enabling the study of automatic payment exchanges and responses to policy changes. By modeling interactions between autonomous AI agents, researchers can analyze how policy changes and market conditions affect transaction flows, liquidity decisions, and risk propagation in payment systems. This approach can provide insights into operational dynamics and help support the design of adaptive financial infrastructures (Korinek, 2023; Aldasoro et al., 2024; Horton, 2023; Kazinnik, 2023; Jabarian, 2024).

In this paper, we are primarily focused Level 2 (AI agents as assistants), where actions are based on patterns and other information provided via prompts. However, these models can also be trained to operate at higher levels of sophistication-such as Operators, Actors, or Agents-enabling them to execute predefined payment processes, dynamically adapt payment and liquidity management strategies, or even develop new strategies to optimize and automate the entire payments workflow.
