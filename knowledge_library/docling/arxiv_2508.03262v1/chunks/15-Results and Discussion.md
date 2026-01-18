## Results and Discussion

In this section, we analyzes the experimental results regarding two conditions and inter-model comparisons, discussing the similarity and agreement between humans and LLMs.

Effect of Interaction Condition: Comparing the performance differences between the two interaction conditions,

Figure 2: Response distribution in Sequential Condition

Human

Human

12

12 6

GPT

0

GPT

LLaMA 0

LLaMA 0

Qwen

0

Qwen 0

6

36

36

0

3t

7

0

0

139

139

134

336

23

23

141

183

259

44

44

1

14

251

275

5

77

1

Table 1: LLM performance across experimental conditions for music performance (M) and art (A) domains.

|                                                  | Sequential                                       | Sequential                                       | Sequential                                       | Human-guided                                     | Human-guided                                     | Human-guided                                     |
|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| Metric                                           | GPT                                              | Llama                                            | Qwen                                             | GPT                                              | Llama                                            | Qwen                                             |
| A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       |
| M Q1                                             | 62.26                                            | 60.15                                            | 61.11                                            | 62.07                                            | 63.60                                            | 62.26                                            |
| M Q2                                             | 57.28                                            | 78.54                                            | 75.10                                            | 70.50                                            | 80.84                                            | 76.82                                            |
| M Q2.1                                           | 5.43                                             | 22.25                                            | 9.78                                             | 15.65                                            | 26.41                                            | 33.74                                            |
| M Q3                                             | 11.36                                            | 0.00                                             | 0.00                                             | 31.86                                            | 9.73                                             | 29.20                                            |
| TF Total                                         | 44.06                                            | 53.83                                            | 46.17                                            | 45.98                                            | 55.36                                            | 45.79                                            |
| M total                                          | 6.90                                             | 11.49                                            | 4.79                                             | 6.70                                             | 11.11                                            | 15.13                                            |
| A Q1                                             | 64.75                                            | 37.55                                            | 66.28                                            | 65.13                                            | 55.17                                            | 65.71                                            |
| A Q2                                             | 67.82                                            | 62.84                                            | 64.75                                            | 76.44                                            | 73.37                                            | 65.71                                            |
| A Q2.1                                           | 16.23                                            | 9.6                                              | 4.28                                             | 28.44                                            | 23.24                                            | 24.16                                            |
| A Q3                                             | 16.73                                            | 0.19                                             | 0.13                                             | 0.00                                             | 35.38                                            | 36.41                                            |
| TF Total                                         | 45.59                                            | 32.95                                            | 46.55                                            | 44.44                                            | 42.72                                            | 40.04                                            |
| A total                                          | 12.45                                            | 5.94                                             | 1.72                                             | 17.05                                            | 16.09                                            | 13.79                                            |
| Total Acc                                        | 4.60                                             | 0.77                                             | 0.77                                             | 4.02                                             | 0.96                                             | 4.41                                             |
| B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) |
| CSA                                              | 0.62                                             | 0.55                                             | 0.66                                             | 0.72                                             | 0.86                                             | 0.76                                             |
| SSA                                              | 0.86                                             | 0.83                                             | 0.72                                             | 0.93                                             | 0.90                                             | 0.86                                             |
| Jaccard                                          | 0.43                                             | 0.00                                             | 0.27                                             | 0.67                                             | 0.57                                             | 0.20                                             |

the Human-guided Condition showed overall superior prediction performance compared to the Sequential Condition. This was somewhat expected, as the Human-guided condition is designed to allow LLMs to reference actual human response flows for each question, enabling reasoning to proceed in a manner closer to human judgment pathways. These results suggest that providing actual human responses as examples may produce effects similar to few-shot prompting, providing a foundation for exploring the effectiveness of various prompting techniques in RQ2.

As shown in Table 1, the Human-guided condition demonstrated higher accuracy than the Sequential condition in terms of individual-level accuracy. The difference between conditions was particularly pronounced in subjective or open-ended questions compared to binary-choice items. For example, in Qwen's case, the accuracy for subjective questions ( Q2.1 ) was only 9.78% and 4.28% in the Sequential condition, but improved significantly to 33.74% and 24.16% in the Human-guided condition. This suggests that when LLMs rely on their own generated response flows (Sequential Condition), errors may accumulate or reasoning may proceed in directions that diverge from human response patterns. However, we can confirm that the Overall Accuracy was generally very low across all models. Meanwhile, analysis of group-level tendencies showed that both conditions performed well overall, with the Human-guided condition consistently showing higher prediction accuracy compared to the Sequential condition. The Human-guided condition scored higher across all major indicators including CSA, SSA, and Jaccard index.

These results provide two major findings. First, in Human-guided condition, actual human responses were provided as context for each item, enabling LLMs to form more

2

2

0

28

28

2

2

11

11

2

2

0

0

Figure 3: Response distribution in Human-Guided condition

<!-- image -->

coherent reasoning pathways, which led to higher prediction accuracy at both group and individual levels. This demonstrates that providing actual response examples is effective for improving LLMs' behavioral prediction accuracy, suggesting the validity of example-based approaches such as few-shot. Second, while LLMs still showed difficulties in precisely replicating individual human choices, they demonstrated similar tendencies to humans at the group level.

Comparison Models: Based on the results from Table 1, Figures 9 and 10 when comparing accuracy across models, GPT-4o showed consistently high performance in both item-level accuracy ( M Q1 62.07%, M Q2 70.50%, A Q1 65.13%, A Q2 76.44%) and group-level similarity indicators (CSA 0.72, SSA 0.93, Jaccard 0.67) in the Humanguided condition, demonstrating the most human-like patterns in both choice outcomes and variable structures. LLaMA achieved the highest variable direction agreement (0.86) in the Human-guided condition. But overall accuracy was only 0.96%. This suggests that while the model excels at identifying the direction of variable influence, it lacks consistency in translating this understanding into individual choice predictions. Qwen showed similar Overall Accuracy to GPT-4o at 4.41% in the Human-guided condition, but had a low Jaccard score of 0.20, indicating that its important variable set differed significantly from humans.

Figures 9 and 10 reveal particularly notable model differences in response distribution in terms of price ( Q2.1 ). Figure 9 shows that human responses have high diversity, while LLM responses tend to cluster at specific price points. In Figure 10, this clustering pattern becomes even more pronounced, with LLMs showing much more concentrated response distributions compared to the diverse human response patterns. For instance, in Sequential condition, Figure 9 show that Qwen provided response distributions with some variance similar to humans, but when switched to Human-guided condition, the response distribution became much more concentrated at specific price points. Nevertheless, the accuracy for the same questions increased significantly, as shown in the transition from Figure 9 to 10. This demonstrates that actual human responses had a positive im- pact on the model's prediction performance, though at the cost of response diversity.
