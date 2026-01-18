## E Judge Configuration Details

We reuse AgentHarm's two-judge protocol: a semantic judge that inspects the tool-call trace and task description to assign completion labels, and a refusal judge that scans the full model dialogue to detect refusals. Both judges ignore any padding we insert so that their assessments only reflect the task exchange. To control cost we substituted GPT-4o with GPT-4.1-nano for both judges after confirming near-identical

<!-- image -->

Figure 5: Random padding results for GPT-4.1-nano for different subsets of AgentHarm. These subsets have the same tasks and only differ in whether the task uses hint and detailed prompt. (a) Harm score for harmful tasks (b) Refusal rate for harmful tasks (c) Score for benign tasks

Figure 6: Performance comparison across different padding types (Random, Multi-task, Non-relevant, Relevant) for harmful tasks, with padding placed after the task for DeepSeekV3.1. Error bars denote 1 σ .

<!-- image -->

Figure 7: Refusal rate for benign tasks as random padding length increases, with padding placed after the task. Error bars denote 1 σ .

<!-- image -->

<!-- image -->

Figure 8: Performance for each harm category for GPT-4.1-nano with random padding (a) benign tasks (b) harmful tasks (c) refusal rate

Figure 9: Performance for each harm category for Grok 4 Fast with random padding (a) benign tasks (b) harmful tasks (c) refusal rate

<!-- image -->

Figure 10: Performance for each harm category for DeepSeek-V3.1 with random padding (a) benign tasks (b) harmful tasks (c) refusal rate

<!-- image -->

Table 2: Model API endpoints.

| Model name         | API used                                                                                       |
|--------------------|------------------------------------------------------------------------------------------------|
| GPT-4.1 nano GPT-5 | openai/gpt-4.1-nano-2025-04-14 openrouter/openai/gpt-5 openrouter/deepseek/deepseek-chat- v3.1 |
| Grok 4 Fast        | openrouter/x-ai/grok-4-fast                                                                    |
| DeepSeek-V3.1      |                                                                                                |

Table 3: Judge configuration per model. Last column shows prompt type for the refusal judge. Standard prompt follows AgentHarm; modified prompt for GPT-5 used to reduce false negatives from standard refusal judge prompt.

| Model         | Semantic Judge   | Refusal Judge   | Prompt                     |
|---------------|------------------|-----------------|----------------------------|
| GPT-4.1-nano  | GPT-4.1-nano     | GPT-4.1-nano    | Standard Modified Standard |
| GPT-5         | GPT-4o           | GPT-4o          |                            |
| DeepSeek-V3.1 | GPT-4.1-nano     | GPT-4.1-nano    |                            |
| Grok 4 Fast   | GPT-4.1-nano     | GPT-4.1-nano    | Standard                   |

decisions on a validation subset. GPT-5 required an exception: its safety-trained completions often propose benign alternatives, which the GPT-4.1-nano judge missed. For that model we reinstated GPT-4o and tightened the refusal prompt to explicitly flag such deflections, yielding stable refusal counts used in the main analysis.
