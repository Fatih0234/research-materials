## 4 Discussion

In the Introduction, we formulated 7 questions aimed at understanding the strategic reasoning of artificial intelligence. Now we are ready to answer those questions based on the results of our Guess the number experiments. For each question, we provide a formal criterion for deriving an answer.

Q1. Does LLM recognize the rules of the game and act in accordance with the rules? (Yes.)

Criterion: the share of correct answers, i.e. integer numbers from 0 to 100. The higher the share of correct answers, the better LLM recognizes the rules of the game and act in accordance with the rules.

In our dataset, 100% of LLM answers are legitimate. Therefore, we conclude that LLMs do recognize and adhere to the rules.

Q2. Does LLM recognize the strategic context of the game? (Yes.)

We asked GPT-4o to classify all answers into 6 categories using the following prompt:

Task: You are given a player's answer from the 'Keynesian Beauty Contest" game. Each player picks a number between 0 and 100 and explains their reasoning. Classify the reasoning into one of six categories:

1. No explanation.
2. Uninformative or purely heuristic (e.g., 'Because I said so", 'It's sunny in Paris, so 47", '3 is a lucky number, so 33").
3. Theoretical Nash equilibrium (explicitly states everyone should choose 0, so they choose 0).
4. Level-1 reasoning (expects average/median ≈ 50, picks fraction once).
5. Finite level-k reasoning (iterates reasoning steps &gt; 1 but finite times).
6. Infinite level-k reasoning (iterates reasoning to infinity, leading to 0).
7. Output format: &lt; category number &gt; -&lt; brief explanation why &gt;

The player's answer to classify is:

Criterion: the share of answers falling into categories 3 - 6 is now regarded as a degree of recognition of the strategic context of the game.

Table 11 presents the results of the strategy classification.

| Strategy category   |   Claude Sonnet |   Gemini Flash |   GPT-4o |   GPT-4o mini |   Llama |
|---------------------|-----------------|----------------|----------|---------------|---------|
| Category 1          |               0 |              0 |        0 |             0 |       0 |
| Category 2          |               0 |              0 |        4 |            19 |       0 |
| Category 3          |               0 |             20 |       11 |             1 |      91 |
| Category 4          |              96 |             45 |      339 |           396 |      45 |
| Category 5          |             688 |            527 |      403 |           373 |     268 |
| Category 6          |              16 |            208 |       43 |            11 |     396 |

Table 11: Classification of strategy explanations.

As one can see, almost all strategies played by LLMs (except 23) included strategic level𝑘 reasoning patterns or theoretical equilibrium play. Therefore, we confirm the positive answer to question Q2: LLMs do recognize the strategic context of the game.

Q3. Are LLM's decisions in line with the expected comparative statics with respect to the parameters of the experiment? (Yes.)

For each LLM, we calculate whether

1. Their average response in Scenario 1 is lower than in Scenario 2;
2. Their average response in Scenario 7 is lower than in Scenario 6;
3. Their average response in Scenario 9 is lower than in Scenario 8;
4. Their average response in Scenario 10 is lower than in Scenario 11;
5. Their average response in Scenario 12 is lower than in Scenario 13;
6. Their average response in Scenario 16 is lower than in Scenario 14.

Criterion: the higher is the number of positive answers, the better LLM's decisions are in line with the expected comparative statics with respect to the parameters of the experiment.

Based on Tables 2 - 6, we report that each of five LLMs has 6 positive answers out of 6. Therefore, all models demonstrate expected adaptability to the changing set of parameters in our experiments.

Q4. Can LLM find an analytical solution to the game? (No.)

For scenarios with 𝑛 = 2 , we asked GPT-4o to classify all answers into 2 categories using the following prompt:

Task: You are given a player's answer from the Keynesian Beauty Contest game with 2 players. Each player chooses a number between 0 and 100 and explains their reasoning. In this game, playing 0 is a weakly dominant strategy.

Your task is to classify the player's reasoning into one of two categories:

1. Dominant strategy explanation. The reasoning explicitly explains that playing 0 is a weakly dominant strategy. It is not enough to simply mention that 0 is a Nash equilibrium. To belong to this category, the reasoning must include some explanation that playing 0 is weakly better regardless of what the opponent chooses (Example

answer in this category: 'No matter what the other player picks, playing 0 is never worse and sometimes strictly better, so 0 is the weakly dominant strategy. I will play 0.').

2. Other explanations. All other reasoning that does not meet the criteria for category 1. (Example answer in this category: 'If both players are rational, they will both choose 0 since it is a Nash equilibrium.').

The player's answer to classify is:

Criterion: the share of answers falling into category 1 shows how well LLMs identify weakly dominant strategies.

We report that none of the responses were classified as category 1. LLMs fail to identify the dominant strategy in the Guess the number game with two players.

Q5. Can LLM correctly use the analytical solution when choosing its strategy? (Indefinite.)

Deriving the dominant strategy does not guarantee that an LLM will actually play this strategy.

Criterion: for scenarios with 𝑛 = 2 , we compute the share of cases when LLM played 0 in responses that were classified as belonging to category 1 in Q5. This criterion is not applicable if no responses were classified as category 1 in Q5.

Since no strategies were classified as category 1 in Q5, we cannot assess whether LLMs are able to correctly apply the concept of a dominant strategy.

Q6. Do different LLMs perform differently? (Yes.)

For each particular scenario and any given pair of LLMs we conduct a 𝑡 -test for comparing the average numbers of the corresponding LLMs.

Criterion: if the test does not reject a hypothesis of equal averages at the 1% significance level, we give a negative response to Q6 (for the particular scenario and particular pair of LLMs).

For the sake of brevity, we do not provide all calculations that can be easily reproduced based on Tables 2-6. While some model pairs (18% of all pairs in all 16 scenarios) exhibit statistical equivalence, the results show systematic deviations, suggesting that the models adopt distinct strategies in generating numerical choices. This increased heterogeneity underscores the importance of model architecture and training background in shaping behavioral outputs.

Q7. Are LLM's strategies similar to strategies played by human players? (No.) .

For each of scenarios 1, 2, 6, 7, 8, and 9 (i.e., the scenarios in which the exact numbers played by humans are known), we conduct a 𝑡 -test to compare the average numbers of humans and LLMs for any given model.

Criterion: if the test does not reject a hypothesis of equal averages at the 1% significance level, we give a negative response to Q7 (for the particular scenario and particular LLM).

The comparison indicates that, in most experimental settings, model-generated averages significantly diverge from human results, with exact matches being relatively rare (7% of all comparisons in 6 scenarios).
