## 1 Introduction

In recent years, the context windows of large language models (LLMs) have increased from tens of thousands to over a million tokens (Burnham and Adamczewski 2025; Liu et al. 2025). This has allowed LLMs to handle increasingly long, multi-step, long-horizon workflows, particularly when deployed in an agentic setup (Denain and Ho 2025). However, as context lengths expand, an important question arises: how does safety alignment of LLM agents scale with context size?

Prior work on LLMs with long context has focused on accuracy and efficiency, e.g., fact recall and document summarization. Performance degradation on long inputs has been thoroughly studied as 'lost in the middle' setup (Liu et al. 2024). However, very little is known about how long context influences refusal behavior and capability of LLM agents. We explore whether LLM agents become resistant to unsafe requests with longer prompts or are simply less capable overall. Previously, safety evaluations have used short prompts

Copyright © 2026, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

and static refusal testing (Andriushchenko et al. 2025; Xie et al. 2025).

We present a study of safety-capability trade-offs under long context. Building upon the AgentHarm benchmark (Andriushchenko et al. 2025), we evaluate multiple LLM-based agents in controlled setup with different context paddings. We vary context padding lengths from 1K up to 200K tokens, context type (random tokens, relevant and non-relevant text, multi-task context), and position (before or after the task description) to study how agent performance and refusal behavior are robust to those variations.

Our key findings are:

- Agentic capabilities of models with 1M-2M token context windows degrade severely already at 100K tokens, with &gt; 50% performance drops both for benign and harmful tasks.
- Refusal rates shift unpredictably: some models increase refusal while others decrease at the same context lengths.
- Padding type impacts performance: coherent text (nonrelevant/relevant) outperforms random, which outperforms multi-task.
- Padding position matters: context placed after the task description could degrade performance of the model more than before.
