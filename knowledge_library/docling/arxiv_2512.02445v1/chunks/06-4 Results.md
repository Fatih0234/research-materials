## 4 Results

Majority of tested agents show clear signs of performance degradation when the context length increases. As shown in Figure 2, for many tested agents we observe gradual capability degradation and sometimes quick degradation when padding length exceeds 100K tokens. Different agents show different velocity of degradation, but the trend remains strong.

Grok 4 Fast shows strong degradation after 50K tokens, even on benign tasks, deteriorating to zero at 200K. Despite the declared 2M tokens context window, for both benign and harmful tasks we observe a severe drop between 50K and 100K tokens of context padding. This cannot be explained by the refusal rate, as it exhibits a similar trend.

GPT-4.1-nano shows a decrease in performance both for benign and harmful tasks. The refusal rate, lowest across all models for the no padding case, starts to quickly increase after 10K tokens of padding and reaches nearly 40% for 200K random padding. Also, for this padding we observe a threefold decrease in performance for harmful tasks. This can't be solely attributed to refusal rate increase, as we observe a similar picture for benign tasks, where performance was cut

Table 1: Input context length for tested models.

| Model         | Input context length   |
|---------------|------------------------|
| GPT-4.1-nano  | 1M tokens              |
| GPT-5         | 400K tokens            |
| DeepSeek-V3.1 | 128K tokens            |
| Grok 4 Fast   | 2M tokens              |

Figure 3: Performance comparison across different padding types (Random, Multi-task, Non-relevant, Relevant) for harmful tasks, with padding placed after the task. Shows GPT-4.1nano and Grok 4 Fast. Error bars denote 1 σ .

<!-- image -->

in half, dropping from 80% to 40%. Additionally, capabilities continue to degrade at 800K tokens, despite a decrease in the refusal rate compared to 200K padding.

Compared to other models, the DeepSeek-V3.1 model shows greater robustness to random padding. For benign tasks, the model's performance decreases by 10 percentage points when comparing runs with no padding to those with 200K tokens of random padding. For harmful tasks, we even observe an increase in scores for padding between 0 and 50K tokens, which could be attributed to a slight decrease in the refusal rate observed with this padding. However, as we approach the model's maximum context length, we see a jump in the refusal rate and a decrease in performance to a score similar to that in the no-padding run.

The GPT-5 model shows a very high refusal rate that does not decrease with increasing context padding. With such a consistently high refusal rate, we observe a slight decrease in performance on harmful tasks, but the initially low harm score prevent us from drawing strong conclusions. We do not further explore benign tasks with context padding longer than 10K tokens because of the initial stability of the results and the high cost of running experiments.

Context padding type could significantly impact performance. As shown in Figure 3, different padding types exhibit varying impacts. For GPT-4.1-nano, we observe

Figure 4: Impact of padding position on harmful task performance: before vs. after the task description, for GPT-4.1-nano and Grok 4 Fast with random padding. Error bars denote 1 σ .

<!-- image -->

higher scores for non-relevant padding, followed by relevant padding, then random, and finally multi-task padding performing worst. Due to the high refusal rate, Grok 4 Fast does not demonstrate a similar pattern, and its score for different padding oscillates near the no padding result. Similar to the previous observation, between 50K and 100K, Grok 4 Fast demonstrates behavior similar to mode collapse and the performance of different padding types tends to converge to the same value.

Padding position influences model performance. Figure 4 shows how the position of the padding could influence capability degradation rate. For both GPT-4.1-nano and Grok 4 Fast, placing padding before the task description slows degradation compared to placing it after . This likely occurs because with before padding, the task description and task execution are closer together, allowing attention mechanisms to operate more in-distribution. Modern attention mechanisms (e.g., sliding window, RoPE) may not handle attention to very distant tokens as well, since such patterns are uncommon in training. When padding is placed after , the model must attend across a large gap between instruction and execution, potentially explaining the more severe degradation.

Refusal rates shift unexpectedly with increasing context length. Figure 2 shows unexpected shifts in refusal rates with increased context. GPT-4.1-nano and Grok 4 Fast show opposite behavior with random padding. GPT-4.1-nano's initially low refusal rate increases after 50K tokens, rising considerably at 200K tokens compared to no padding. Grok 4 Fast shows different behavior: its initially high refusal rate of 80% gradually decreases after 5K tokens, becoming half as high at 200K tokens.

Agents with context length up to 1 million tokens show severe degradation already at 100K tokens. GPT-4.1-nano and Grok 4 Fast models claim an input context window of up to 1 million and 2 million tokens respectively. Neverthe- less, even with 200K tokens we observe severe performance degradation. Compared to the gradual score observed in GPT4.1-nano, Grok 4 Fast exhibits a rapid behavioral change between 50K and 100K tokens. For 800K-context random padding (80% of maximum context window capacity) GPT4.1-nano shows similar performance on both harmful and benign tasks, indicating comparable capability degradation despite initial differences.
