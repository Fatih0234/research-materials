## 4 Efficiency

Naïve implementations of constrained decoding add overhead to the standard LM inference process, including a per-step mask computation and an optional one-time grammar compilation. However, several optimizations can significantly reduce this overhead. For instance, mask computation can run in parallel with the LM's forward pass, and grammar compilation can be performed concurrently with pre-filling computations [Guidance AI, 2023; Dong et al., 2024]. Other optimizations such as grammar caching and constraint-based speculative decoding [GuidanceAI, 2024b; Beurer-Kellner et al., 2023; Kurt, 2024a] can further reduce overhead.

Metrics We break down the efficiency evaluation into the following components:

- Grammar Compilation Time (GCT): The time spent on grammar compilation, if applicable.
- Time to First Token (TTFT): Time from the start of generation to the production of the first token.
- Time per Output Token (TPOT): Average time to generate each output token after the first.
