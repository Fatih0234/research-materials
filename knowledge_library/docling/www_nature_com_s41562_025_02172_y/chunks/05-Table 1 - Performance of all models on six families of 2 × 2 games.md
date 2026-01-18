## Table 1 | Performance of all models on six families of 2 × 2 games

| Gamefamily   |   Llama2 |   Claude2 |   davinci-002 |   davinci-003 |   GPT-4 |
|--------------|----------|-----------|---------------|---------------|---------|
| Second best  |    0.486 |     0.735 |         0.473 |         0.692 |   0.763 |
| Biased       |    0.632 |     0.794 |         0.629 |         0.761 |   0.798 |
| Cyclic       |    0.634 |     0.749 |         0.638 |         0.793 |   0.806 |
| Unfair       |    0.641 |     0.812 |         0.683 |         0.833 |   0.836 |
| PDfamily     |    0.731 |     0.838 |         0.807 |         0.841 |   0.871 |
| Win-win      |    0.915 |     0.878 |         0.988 |         0.972 |   0.992 |
| Overall      |    0.697 |     0.814 |         0.73  |         0.839 |   0.854 |

Model score divided by maximum score achievable under ideal conditions. The best- performing model is marked in bold. PD, Prisoner's Dilemma.

To analyse the different LLMs' performance, we calculated, for each game, their achieved score divided by the total score that could have been achieved under ideal conditions, that is, if both players had played such that the player we are analysing would have gained the maximum possible outcomes on every round. The results of this simulation are shown across all game types in Table 1. We can see that all models perform reasonably well. Moreover, we observe that larger LLMs generally outperform smaller LLMs. In particular, GPT-4 performs best overall, outperforming Claude 2 ( t (287) = 3.34, P &lt; 0.001, Cohen's d = 0.20, 95% confidence interval (CI) 0.08-0.31, Bayes factor (BF) 14.8), davinci-003 ( t (287) = 6.29, P &lt; 0.001, d = 0.37, 95% CI 0.25-0.49, BF &gt;100), davinici-002 ( t (287) = 8.45, P &lt; 0.001, d = 0.70, 95% CI 0.520.89, BF &gt;100) and Llama 2 ( t (287) = 7.27, P &lt; 0.001, d = 0.43, 95% CI 0.31-0.43, BF &gt;100).

We can use these results to take a glimpse at the strengths of the different LLMs. That LLMs are generally performing best in win-win games is not surprising, given that there is always an obvious best choice in such games. What is, however, surprising is that they also perform well in the Prisoner's Dilemma family of games, which is known to be challenging for human players 23 . We can also use these results to look at the weaknesses of the different LLMs. Seemingly, all the LLMs perform worse in situations in which what is the best choice is not aligned with their own preferences. Because humans commonly solve such games via the formation of conventions, we will look at a canonical game of convention formation, the Battle of the Sexes, in more detail below.
