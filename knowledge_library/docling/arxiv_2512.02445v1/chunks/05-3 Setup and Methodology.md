## 3 Setup and Methodology

We extend the AgentHarm benchmark to evaluate agentic capabilities and behaviors under long-context inputs for both benign and harmful tasks. AgentHarm tests capabilities for multi-step tool use. The benchmark provides manually implemented tools that simulate real-world tools (e.g., Google Search or an API to post on X) to allow full control over task execution. A brief description of the new setup can be seen in Figure 1.

The AgentHarm public test dataset contains 176 samples from 44 unique tasks across 8 categories (e.g., disinformation, fraud). Every task can be expanded with modes: a hint providing what tool should be called first and a detailed prompt with step-by-step instructions. Combining the modes gives us four modifications of each task description. For our experiments we focus on the simplest subset to reduce costs and provide an upper bound on model capabilities, ensuring capability is not the limiting factor and context length is the primary factor influencing performance (see Section A).

AgentHarm uses automatic scorer and LLM-judge evaluation (Zheng et al. 2023). We focus on two metrics: (1) Harm score : rubric-based completion score in [0, 1] on harmful tasks based on manually implemented rubrics (2) Refusal rate : fraction of samples flagged as refusals by LLM model. See Section B for details. We use Harm Score as the main metric and ignore semantic judge assuming reliable evaluation on the simplest subset of tasks. For the refusal judge, we provide small changes in the prompt and the underneath model, details in Section E.

To increase context length and have a controlled environment, we experiment with four context padding types : random padding uses tokens randomly sampled from the tokenizer; non-relevant padding uses coherent text from fiction literature (5 genres: humor, mythology, sci-fi, crime, romance) that is not related to the task category; relevant padding uses coherent text from Wikipedia articles related to the task category; and multi-task padding samples task descriptions from the validation dataset. These padding types allow us to isolate different factors: random padding provides full control over reproducibility, non-relevant and relevant padding use coherent in-distribution text, and multi-task padding tests robustness to semantically confounding context See Sections F and G for more details.

We add padding in two different positions relative to the task to study the effect of context position : before padding placed before the task description, simulating a context window filled with data from past interactions, while after padding places context entirely after the task description, simulating a user adding information after an initial task.

To have a diverse set of models, varied by context length Table 1 and capabilities, we evaluate models from different families: GPT-4.1-nano, GPT-5, DeepSeek-V3.1 and Grok 4 Fast. See Tables 2 and 3 and section E for details.

Figure 2: AgentHarm score for benign and harmful tasks (top) and refusal rate (bottom) as random padding length increases, with padding placed after the task. Error bars denote 1 σ .

<!-- image -->
