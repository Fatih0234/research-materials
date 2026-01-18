## Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma

Richard Willis 1 , Yali Du 1 , Joel Z Leibo 1 , 2 and Michael Luck 3

1 King's College London

2 Google DeepMind

3 University of Sussex richard.willis@kcl.ac.uk, yali.du@kcl.ac.uk, jzl@deepmind.com, michael.luck@sussex.ac.uk

## Abstract

As autonomous agents become more prevalent, understanding their collective behaviour in strategic interactions is crucial. This study investigates the emergent cooperative tendencies of systems of Large Language Model (LLM) agents in a social dilemma. Unlike previous research where LLMs output individual actions, we prompt state-of-theart LLMs to generate complete strategies for iterated Prisoner's Dilemma. Using evolutionary game theory, we simulate populations of agents with different strategic dispositions (aggressive, cooperative, or neutral) and observe their evolutionary dynamics. Our findings reveal that different LLMs exhibit distinct biases affecting the relative success of aggressive versus cooperative strategies. This research provides insights into the potential longterm behaviour of systems of deployed LLM-based autonomous agents and highlights the importance of carefully considering the strategic environments in which they operate.

## 1 Introduction

The increasing deployment of autonomous agents based on Large Language Models (LLMs) [Wang et al. , 2024] in realworld applications necessitates an examination of their collective impact on machine-machine interactions and human culture [Brinkmann et al. , 2023]. Whilst individual LLM capabilities are frequently assessed, understanding their collective behaviours and societal consequences remains crucial and underexplored.

The development of social capabilities in these agents may lead to dual-use skills usable for both pro-social and antisocial purposes, termed differential capabilities . [Dafoe et al. , 2020]. This duality raises questions about the balance between cooperation and conflict in autonomous agent interactions. Furthermore, situations such as social dilemmas pose inherent risks, as competent agents acting rationally can lead to suboptimal collective outcomes [Pan et al. , 2023 07 232023 07 29]. If agents succeed through aggressive behaviours, competitive pressures could potentially drive systems towards suboptimal equilibria [Anwar et al. , 2024].

Prior assessments of LLMs have evaluated their capacity to engage in various multiplayer games [Mao et al. , 2023; Yocum et al. , 2023; Park et al. , 2023; Gong et al. , 2023; Zhang et al. , 2024; Wu et al. , 2023] and the emergent behaviours of systems of LLM agents has been explored. Conventionally, however, LLMs are prompted to output a single action in response to a given game state or trajectory. Recent analyses have revealed that LLMs struggle when tasked with making decisions at this level of granularity [Fan et al. , 2024]. In such scenarios, they fail to identify basic patterns, such as an opponent mirroring their own moves. This limitation likely stems from the fact that LLMs are not specifically trained for data science tasks, or to handle inputs of this format.

In response, in contrast to prior work, our we prompt LLMs to create fixed strategies in natural language, which are subsequently implemented as algorithms in Python. This method enables the LLMs to craft their approach at a higher level of abstraction. For example, with our approach, we observe that many LLM strategies utilise pattern recognition and successfully implement code to detect simple patterns up to a fixed length. A key advantage of creating strategies to encode as algorithms, rather than outputting individual actions, is that it facilitates behaviour checking in advance. This approach allows users to inspect the strategy, test for safety and robustness, and explore the potential implications prior to deployment.

Our research employs the iterated Prisoner's Dilemma (IPD) [Axelrod, 1980; Crandall, 2014; Beaufils et al. , 1996] to evaluate the balance between pro-social and anti-social behaviours exhibited by state-of-the-art LLM agents. We utilise evolutionary game theory [Axelrod, 1986; Mahmoud et al. , 2010; Nowak et al. , 2004; Nowak, 2006] to investigate whether systems of frontier LLM agents are predisposed to exhibit cooperation or conflict under competitive pressures. The choice of IPD provides a robust mathematical framework for analysing the strategic behaviour and cooperative biases of LLM agents. Moreover, as game theory represents a highlevel abstraction of various social phenomena, with applications spanning economics, politics, sociology, and psychology, insights gained from LLM performance in these scenarios may have far-reaching implications across multiple disciplines.

Our contributions are as follows: we quantify the relative success of pro-social and anti-social LLM agent behaviours in a social dilemma; we assess the relative likelihoods of systems of LLM agents converging to anti-social or pro-social equilibria; and, we release our code 1 as an evaluation suite for model developers to assess the emergent behaviour of their products.

In addition to the above, we provide supplementary analysis: we verify that the LLM strategies exhibit the requested behaviours; we benchmark the LLM strategy performance against human written strategies using the same setup as prior work [Beaufils et al. , 1996]; and, we investigate the impact of noisy actions, which represent execution mistakes.

## 2 Related Work

Evaluating and benchmarking the capabilities of LLMs is common practice, as these models frequently exhibit emergent capabilities, such as theory of mind [Van Duijn et al. , 2023] and reasoning [Kojima et al. , 2022], despite certain limitations in their abilities [Sclar et al. , 2023; Dziri et al. , 2023]. Moreover, LLMs are increasingly utilized in multiagent systems (MAS). Notably, a line of research has focused on modelling societies of generative agents [Park et al. , 2023] and examining their performance in social dilemmas [Yocum et al. , 2023]. However, we perceive a gap in the assessment of the emergent behaviours of systems of LLMs. Our proposal aims to expand the evaluation and benchmarking of LLMs to encompass an analysis of their emergent collective behaviours.

LLMs have been used to play games from game theory [Aher et al. , 2023 07 232023 07 29; Horton, 2023; Wu et al. , 2023], including iterated normal-form games [Akata et al. , 2023], extensive-form games [Mao et al. , 2023], Markov social dilemma games [Yocum et al. , 2023] and team games [Zhang et al. , 2024; Gong et al. , 2023]. These games serve as proxies for real-world behaviours and assess the abilities of LLM agents in a range of scenarios. However, LLMs can struggle to play games at an action-level granularity [Fan et al. , 2024]. In contrast, our approach involves having the LLMs output strategies in advance.

LLMs have been suggested for use in game theoretic setting [Gemp et al. , 2024] and modelling human societies and social phenomena [Park et al. , 2023; Vezhnevets et al. , 2023 10 292023 11 01; Piatti et al. , 2024; De Zarz` a et al. , 2023; Gao et al. , 2024]. While our approach similarly utilises games to evaluate LLM behaviour, our focus diverges from improving LLM performance. Instead, we aim to critically assess the balance between aggressive and cooperative behaviours exhibited by these models, and to analyse the emergent dynamics of systems comprising multiple LLM agents with varying behavioural tendencies.

IPD has been extensively employed in various fields of study to model and analyse strategic decision-making in repeated interactions [Axelrod, 1980; Crandall, 2014; Rapoport et al. , 2015; Press and Dyson, 2012; Knight et al. , 2016; Kendall et al. , 2007; Nowak and Sigmund, 1993]. Furthermore, researchers have used IPD to study the emergence and stability of cooperative behaviours in populations: it has

1 https://github.com/willis-richard/evollm

<!-- formula-not-decoded -->

Table 1: Prisoner's Dilemma

helped explain phenomena such as reciprocal altruism and the evolution of cooperation among non-kin individuals [Axelrod, 1986; Mahmoud et al. , 2010; Nowak et al. , 2004; Nowak, 2006; Stewart and Plotkin, 2013; Hilbe et al. , 2013; Wahl and Nowak, 1999a]. The incorporation of noisy actions into IPD models [Wu and Axelrod, 1995; Wahl and Nowak, 1999b] serves a dual purpose: it simulates the uncertainty of action outcomes and represents the potential for execution errors by agents. This added complexity allows us to assess the robustness and adaptability of LLM agent behaviours under more realistic, imperfect conditions.

## 3 Method

We investigate whether LLM agents are more successful when prompted to behave aggressively, cooperatively or neutrally, which we term their attitude . The LLMs are prompted to write a strategy in natural language, which is then converted into a Python algorithm. These generated strategies are manually checked for safety before their performance is assessed in all-play-all IPD tournaments. Additionally, we examine which equilibria systems converge to when selection pressure favours higher-performing strategies.

## 3.1 Iterated Prisoner's Dilemma Tournament

In a tournament, each participant plays against all others: all n ( n -1) 2 possible pairs compete in a match. Each match consists of 1000 rounds of Prisoner's Dilemma (Table 1), a wellstudied mixed-motive game where players can achieve high scores through mutual cooperation or by unilaterally defecting against a cooperating opponent. In any given round, defect (D) is the dominant action, as the player will receive a higher payoff regardless of their opponents' choice of action. Mutual defection, however, provides a low payoff, so players want to incentivise their opponent to cooperate (C).

Some matches use noise, in which case there is, independently for each player, a 10% chance that their action choice is replaced with the alternative action. Our implementation uses the Axelrod Python library [Knight et al. , 2016].

## 3.2 Strategy generation

Weemploy LLMs to create natural language strategies, which are subsequently coded into algorithms that output either cooperate or defect, given the game history. When prompted to create a strategy, the LLMs are provided with specific behaviours to exhibit, which we term their attitude , from the following set:

<!-- formula-not-decoded -->

Recognising that different prompting techniques can yield varying performance [Madaan et al. , 2023; Moghaddam and Honey, 2023; Shinn et al. , 2023; Fernando et al. , 2023; Khot et al. , 2023; Wei et al. , 2022 28 November 9 December;

Table 2: Prompt styles

| Name    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default | The LLM is provided with information about the game and prompted to create a strategy exhibit- ing the desired attitude in natural language.                                                                                                                                                                                                                                                                                                                              |
| Refine  | The LLM is initially prompted with the Default prompt above. We then use Self-Refine [Madaan et al. , 2023] to ask the LLM to provide and in- corporate self-feedback as follows: (i) the LLM is prompted to provide a list of critiques of the strategy, before ii) tasking the LLM with rewrit- ing the strategy taking into account the critique.                                                                                                                      |
| Prose   | The Prose prompt samples a scenario description with the same dynamics of Prisoner's Dilemma from a set of four, such as a diplomatic nego- tiation around trade protocols, while avoiding the use of game theoretic language. The LLM is provided with the scenario and prompted to create a high-level strategy. The LLM is sub- sequently provided with information about the game, and tasked with converting the high-level strategy into one suitable for the game. |

Wang et al. , 2023], we experiment with different techniques. Our approach aims not to be definitive, but rather to explore a range of prompting styles to illustrate a range of possible results and understand output variability. We experiment with three different prompt styles, as described in Table 2.

Weselect the LLMs ChatGPT-4o and Claude 3.5 Sonnet as they are popular frontier models. For each LLM and prompt style, we create 25 strategies for the three attitudes. We then use ChatGPT-4o to convert the natural language strategies for all LLMs into Python functions. Since we are not assessing the coding abilities of the LLMs, we use the same model to code the algorithms to maintain consistency.

This fixed set of algorithms is assessed for operational safety, as executing arbitrary code is generally unsafe. This is why we create a fixed set for the following experiments, rather than generating new strategies on the fly. Where an algorithm has a bug, we manually fix this if the model's intention is clear. Otherwise, we delete the strategy and generate a new one. Full details of the prompts and generated strategies created can be found in our GitHub at https: //github.com/willis-richard/evollm.

Qualitatively, we observe that the strategies produced by all three prompts for both models are game theoretic in nature. Even with the Prose prompt, which obfuscates the task in an attempt to elicit different reasoning process, the models appear to recognise that the structure of the situation means it is appropriate to apply game theoretic strategies from their knowledge base. This suggests generative agents will reason about scenarios by recognising that game theory inspired strategies in real world scenarios.

We observe differences in the strategies generated by different LLMs. Claude 3.5 Sonnet frequently compares its running total payoff to that of its opponent as part of its decisionmaking process, whereas ChatGPT-4o does not. When craft- ing the set of obfuscated prose prompts, we initially had a scenario dealing with scientific collaboration between academic researchers with the option to either hide or share findings with a colleague. Claude 3.5 Sonnet would frequently refuse to write an aggressive strategy in such a situation. Consequently, we modified the scenario to describe a similar situation, but using commercial engineering rather than academic science, resolving the issue.

## 3.3 Attitude-Agents

We define three classes of gents, each corresponding to one of the attitudes (Aggressive, Cooperative, Neutral), which we call attitude-agents. For each match, an attitude-agent uniformly randomly samples a strategy from the set of strategies associated with their attitude. This approach simulates players creating bespoke strategies for each encounter.

Whilst we verify that, on average, the aggressive strategies defect more frequently than the cooperative strategies, we cannot guarantee that every individual aggressive strategy behaves as such. We opt for this random sampling method rather than creating agents with a single fixed strategy to prevent unintended selection effects within the attitude-strategy set, which is not the focus of our study. Instead, our aim is to model the typical behaviour elicited by a given prompt.

## 3.4 Moran Process

Using a technique from evolutionary game theory, we create populations of attitude-agents to participate in tournaments, and observe how the population compositions evolve over time as more successful players replace less successful ones. Specifically, we use a Moran process [Moran, 1958]:

1. Initialise a population of players
2. Loop:
3. (a) Assess the fitness. Each player plays an IPD match against every other player. Their fitness is the total payoff they achieve across all their games.
4. (b) Replace a player with a clone of another player. A player is chosen to be cloned proportionally to their fitness. They replace a uniformly randomly selected player.
5. (c) Terminate when all players have the same attitude.

In what follows, in keeping with evolutionary game theory literature, we refer to the attitude-strategy set a player uses as their genome . By way of illustration, suppose we initialise a population of size n = 3 players, one of each genome Π t =1 = { π a , π c , π n } . After playing in the tournament, a player with the neutral genome is selected to be cloned, whilst the aggressive genome is randomly chosen to die. Our population at iteration 2 is therefore Π t =2 = { π n , π c , π n } . The process continues until the population consists of only a single genome, whose attitude characterises the equilibria reached. As all aggressive genomes have been eliminated from the population in our example, they can never reemerge.

Figure 1 shows an example Moran Process. The initial population consists of 8 aggressive players, 2 cooperative and

Number of Individuals

12

8

4

0

Population by iteration

<!-- image -->

Figure 1: Illustrative Moran Process

<!-- image -->

| Prompt   |             | Aggressive   | Cooperative   | Neutral   |
|----------|-------------|--------------|---------------|-----------|
| Default  | Aggressive  | 0.30         | 0.26          | 0.28      |
|          | Cooperative | 0.37         | 1.00          | 0.99      |
|          | Neutral     | 0.42         | 0.99          | 0.99      |
|          | (a)         | ChatGPT-4o   |               |           |
| Default  | Aggressive  | 0.21         | 0.15          | 0.18      |
|          | Cooperative | 0.16         | 0.99          | 0.98      |
|          | Neutral     | 0.17         | 0.99          | 0.99      |

(b) Claude 3.5 Sonnet

Table 3: Normalised propensity to cooperate

2 neutral. The neutral players are eliminated first. After 29 iterations, the population consists of only aggressive players: we say that play converged to an aggressive equilibrium.

## 4 Results

## 4.1 Validation

To quantify whether the strategies faithfully exhibit their assigned attitudes, we conduct an IPD tournament (Section 3.1) involving all 75 strategies (25 of each attitude). We then compute the average number of cooperations over all rounds in all matches for strategies of each attitude against strategies of another attitude. The results for the default prompt without noise are shown in Table 3. We show the normalised propensity to cooperate: the proportion of actions in a tournament that the strategies cooperate.

For both LLMs, the neutral and cooperative attitudes exhibit similar behaviour, mutually cooperating in almost all rounds when paired against themselves. Qualitatively, we observe that both neutral and cooperative strategies tend to initiate cooperation in the first round and then broadly follow a Tit-For-Tat approach, which sustains cooperation. The aggressive strategies, however, behave markedly differently, typically initiating with defection. For ChatGPT-4o (Table 3a), aggressive strategies consistently cooperate the least

Figure 2: Performance compared to human-written algorithms

<!-- image -->

across all match-ups, demonstrating their aggression. For Claude 3.5 Sonnet (Table 3a), aggressive strategies similarly defect the most when paired with cooperative or neutral strategies. Interestingly, they exhibit the highest cooperation rate when paired against other aggressive strategies, suggesting a greater willingness to attempt mutual cooperation when encountering an aggressive opponent. For instance, some strategies detect if multiple consecutive rounds of mutual defection have occurred, and will attempt cooperation afterwards.

Overall, the strategies demonstrate reactivity to their opponents' play, modifying their actions in response. The most pronounced exploitation we observe is from the ChatGPT-4o aggressive strategies, which cooperate 12% less than their opponents on average when paired with neutral strategies.

To identify which attitudes the LLMs are better at generating strategies that are robust to a range of behaviours, and which struggle, we enter them into an IPD tournament against human-written algorithms. Unlike the previous all-play-all tournaments using individual strategies, this analysis employs

| Prompt   |                | Aggressive     | Cooperative    | Neutral   |
|----------|----------------|----------------|----------------|-----------|
| Default  | Aggressive     | 1.81           | 2.09           | 2.26      |
|          | Cooperative    | 1.55           | 3.00           | 2.99      |
|          | Neutral        | 1.55           | 2.99           | 2.99      |
| Refine   | Aggressive     | 2.20           | 2.57           | 2.63      |
|          | Cooperative    | 2.53           | 2.99           | 2.99      |
|          | Neutral        | 2.55           | 2.97           | 2.97      |
| Prose    | Aggressive     | 1.65           | 2.29           | 2.35      |
|          | Cooperative    | 2.08           | 2.82           | 2.89      |
|          | Neutral        | 2.12           | 2.89           | 2.93      |
|          | (a) ChatGPT-4o | (a) ChatGPT-4o | (a) ChatGPT-4o |           |
| Prompt   |                | Aggressive     | Cooperative    | Neutral   |
| Default  | Aggressive     | 1.56           | 1.42           | 1.44      |
|          | Cooperative    | 1.41           | 2.99           | 2.98      |
|          | Neutral        | 1.47           | 2.98           | 2.98      |
| Refine   | Aggressive     | 1.87           | 2.18           | 2.04      |
|          | Cooperative    | 2.10           | 2.86           | 2.67      |
|          | Neutral        | 2.01           | 2.69           | 2.50      |
| Prose    | Aggressive     | 1.64           | 2.24           | 2.19      |
|          | Cooperative    | 2.02           | 2.64           | 2.65      |
|          | Neutral        | 2.00           | 2.64           | 2.63      |

(b) Claude 3.5 Sonnet

Table 4: Normalised head-to-head payoffs

the attitude-agents (Section 3.3). For both LLMs, the three attitude-agents are entered into the tournament as described by Beaufils [Beaufils et al. , 1996], competing against 11 standard human-written algorithms. These include Tit-For-Tat, which initially cooperates and then mirrors its opponent's previous action, and Random, which arbitrarily chooses between cooperation and defection in each round. We repeat the tournament 200 times using different seeds.

Figure 2 illustrates the performance of the three attitudeagents in the Beaufils tournament. Each plot displays the median of the tournament scores (the mean round payoff in a single tournament) for each strategy, and a violin depicting the distribution of tournament scores across all repetitions. For both LLMs, the neutral and cooperative strategies perform well, whilst the aggressive strategies perform poorly. This does not necessarily indicate that aggressive strategies are inherently flawed; they may perform better against a different set of opponents. However, it suggests that the LLMs are more adept at crafting cooperative approaches.

The three attitude-agents typically exhibit a larger spread of payoffs in comparison to many of the human-written algorithms. This increased variability stems from the fact that each attitude-agent samples a strategy from its corresponding attitude-strategy set before each match, introducing an additional layer of variation absent in the fixed human-written algorithms. Within each attitude-strategy set, the performance of individual algorithms can vary considerably, with some proving significantly more effective than others.

## 4.2 Head-to-head Comparison

Weenter all 75 strategies into 20 all-play-all IPD tournaments and aggregate the typical head-to-head scores for different

| Prompt   |                | Aggressive     | Cooperative    | Neutral   |
|----------|----------------|----------------|----------------|-----------|
| Default  | Aggressive     | 1.52           | 2.17           | 2.15      |
|          | Cooperative    | 1.69           | 2.62           | 2.57      |
|          | Neutral        | 1.68           | 2.60           | 2.55      |
| Refine   | Aggressive     | 2.18           | 2.47           | 2.47      |
|          | Cooperative    | 2.37           | 2.61           | 2.60      |
|          | Neutral        | 2.36           | 2.61           | 2.59      |
| Prose    | Aggressive     | 1.93           | 2.53           | 2.45      |
|          | Cooperative    | 2.09           | 2.74           | 2.67      |
|          | Neutral        | 2.08           | 2.71           | 2.65      |
|          | (a) ChatGPT-4o | (a) ChatGPT-4o | (a) ChatGPT-4o |           |
| Prompt   |                | Aggressive     | Cooperative    | Neutral   |
| Default  | Aggressive     | 1.51           | 1.45           | 1.58      |
|          | Cooperative    | 1.53           | 2.07           | 2.06      |
|          | Neutral        | 1.54           | 2.00           | 2.31      |
| Refine   | Aggressive     | 1.95           | 2.02           | 2.11      |
|          | Cooperative    | 1.98           | 2.05           | 2.14      |
|          | Neutral        | 2.01           | 2.14           | 2.24      |
| Prose    | Aggressive     | 2.19           | 2.42           | 2.35      |
|          | Cooperative    | 2.19           | 2.51           | 2.46      |
|          | Neutral        | 2.22           | 2.53           | 2.48      |

(b) Claude 3.5 Sonnet

Table 5: Normalised head-to-head payoffs with noise

pairings of attitudes, in Table 4. We show the normalised payoff: the total payoff received in the tournaments, divided by the number of rounds played, or alternatively, the mean round payoff. This will necessarily be in the range [1,5] for Prisoner's Dilemma (Table 1).

For ChatGPT-4o (Table 4a), across all prompt styles, we observe that the cooperative and neutral attitudes perform well and achieve a payoff equivalent to that of mutual cooperation, while the inclusion of an aggressive strategy reduces the payoff for both players. For the Refine and Prose prompts, the aggressive strategy is dominated by both the cooperative and neutral attitudes, performing strictly worse against all three attitudes, so users have no incentive to choose the aggressive strategy with this model in a system with these dynamics. However, the aggressive strategy consistently outperforms its opponent: adopting an aggressive approach reduces one's own payoffs, but it is even more detrimental to the opponent.

The Default prompt exhibits similar dynamics, except that the aggressive strategy becomes the best response to an aggressive opponent. Compared to the Default prompt, a Refine prompt improves the performance of aggressive strategies without negatively impacting neutral and cooperative strategies. This improvement stems from aggressive strategies favouring increased cooperation, leading to higher payoffs for both players. The Prose prompt similarly enhances the performance of aggressive strategies against neutral and cooperative opponents, but actually harms performance against another aggressive strategy.

Wefind similar patterns when using Claude 3.5 Sonnet (Table 4b). Notably, however, the aggressive strategy leads to lower payoffs for both players when using the Default and

Figure 3: Beaufils tournament: ChatGPT-4o + Refine

<!-- image -->

Refine prompt styles. From these observations, we conclude that Claude 3.5 Sonnet is less adept at producing effective aggressive strategies compared to ChatGPT-4o. It exhibits stronger biases towards defection, which in turn increases the defection rate of its opponent, as evidenced in Table 3.

We repeat the Beaufils tournament setup from Section 4.1 using ChatGPT-4o with the Refine prompt, which displays the strongest performance from the aggressive strategies, as shown in Figure 3. This confirms the marked improvement, not just against other LLM strategies, but human written ones too, when compared to Figure 2a.

Table 5 illustrates the performance of in IPD with noise. Claude 3.5 Sonnet (Table 5b) demonstrates difficulty with this mechanism: cooperative strategies see their payoffs reduced from nearly 3 to around 2 when playing against each other using the Default and Refine prompts. This indicates that approximately half of all rounds result in mutual defection. However, Claude 3.5 Sonnet's performance significantly improves with the Prose prompt, suggesting a better understanding of potentially accidental assertive behaviour from opponents when considering real-world scenarios. In this context, all three attitudes exhibit nearly equivalent performance, indicating minimal behavioural differences between them.

ChatGPT-4o (Table 5a) shows performance trends similar to those it achieves in the absence of noise. Again, the Refine and Prose prompts yield improved performance for the aggressive strategy without substantially affecting the neutral and cooperative attitudes. With the introduction of noise, for both LLMs, the aggressive attitude is dominated by the other attitudes across all three prompt styles. However, the payoff discrepancy tends to be less pronounced than in the noiseless scenario.

## 4.3 Equilibria

We run 100 Moran processes with population size n = 12 for each LLM and prompt style, with and without noise. As we are primarily concerned with the likelihood of converging to aggressive equilibria, which have poor social outcomes, we use both an initially balanced population, with four players

| Prompt   | Initial ratio   | Equilibria proportion (A, C, N)   | Equilibria proportion (A, C, N)   |
|----------|-----------------|-----------------------------------|-----------------------------------|
|          | (A:C:N)         | Without noise                     | With noise                        |
| Default  | 1:1:1           | 14%, 53%, 33%                     | 16%, 42%, 42%                     |
|          | 4:1:1           | 66%, 19%, 17%                     | 59%, 20%, 21%                     |
| Refine   | 1:1:1           | 19%, 48%, 33%                     | 28%, 38%, 34%                     |
|          | 4:1:1           | 49%, 30%, 21%                     | 63%, 19%, 18%                     |
| Prose    | 1:1:1           | 13%, 38%, 49%                     | 23%, 41%, 36%                     |
|          | 4:1:1           | 35%, 27%, 38%                     | 60%, 18%, 22%                     |
|          | (a) ChatGPT-4o  | (a) ChatGPT-4o                    | (a) ChatGPT-4o                    |
| Prompt   | Initial ratio   | Equilibria proportion (A, C, N)   | Equilibria proportion (A, C, N)   |
|          | (A:C:N)         | Without noise                     | With noise                        |
| Default  | 1:1:1           | 4%, 49%, 47%                      | 15%, 37%, 48%                     |
|          | 4:1:1           | 36%, 24%, 40%                     | 41%, 20%, 39%                     |
| Refine   | 1:1:1           | 16%, 51%, 33%                     | 37%, 34%, 29%                     |
|          | 4:1:1           | 50%, 22%, 28%                     | 60%, 18%, 22%                     |
| Prose    | 1:1:1           | 14%, 42%, 44%                     | 17%, 33%, 50%                     |
|          | 4:1:1           | 41%, 30%, 29%                     | 61%, 26%, 13%                     |

(b) Claude 3.5 Sonnet

Table 6: Convergence equilibria for different initial population compositions of Aggressive (A), Cooperative (C) and Neutral (N) attitudes

of each genome, and a biased population with eight aggressive players and two each of cooperative and neutral players. The former gives an overview of the interplay between the strategies, whilst the latter assesses whether the emergent behaviour of LLM strategies can escape a system that is skewed towards aggression.

Table 6 presents the outcomes of the Moran processes (Section 3.4), showing the convergence equilibria from various initial population compositions of attitude-agents. The convergence equilibria are the proportion of Moran processes that result in a population purely composed of the corresponding attitude. A priori, the probability of a particular genome dominating a population equals its initial proportion of that population. Observed tendencies greater than this prior probability indicate an advantage for that genome, and vice versa.

Without noise, the populations most likely to converge to aggressive equilibria are ChatGPT-4o using the Default prompt and then both LLMs using the Refine prompt. We posit different reasons for these outcomes:

For ChatGPT-4o using the Default prompt, the aggressive strategy is evolutionarily stable [Smith and Price, 1973], as it performs best against itself (Table 4a). In a predominantly aggressive population, non-aggressive strategies underperform against the majority, only gaining potential advantages against the minority of other non-aggressive strategies. Consequently, an aggressive strategy is the best response to a majority-aggressive population, increasing the likelihood of convergence to an aggressive equilibrium.

Our findings show that approximately two-thirds of Moran processes with ChatGPT-4o and the Default prompt converged to an aggressive equilibrium, matching the initial population proportion. This suggests that aggressive attitudeagents are neither advantaged nor disadvantaged in when the minority proportion is one third. Were the minority proportion to be less than this, we would expect to find the aggressive-agents to be advantaged. Whilst Claude 3.5 Sonnet with the Default prompt also exhibits evolutionary stability, its lower performance makes it more susceptible to invasion by minorities of non-aggressive strategies.

The addition of noise generally leads to a marked increase in the likelihood of converging to aggressive equilibria. We posit this is due to the fact that noise can mask aggression: in noiseless games, an opponent breaking a run of mutual cooperation is surely attempting to exploit you. The addition of noise adds uncertainty over their intentions, making the case for retaliation less clear, which may facilitate restrained aggression.

## 5 Discussion

Across most scenarios, aggressive strategies tend to be disadvantaged, leading to a lower likelihood of systems converging to aggressive equilibria. However, when using prompts containing game-theoretic language, ChatGPT-4o demonstrated a greater capacity to create effective aggressive strategies compared to Claude 3.5 Sonnet, increasing the risk of aggressive equilibria in ChatGPT-4o-based systems. This risk is particularly acute if aggressive strategies are the best response to opponents utilising aggressive strategies.

For both LLMs, and across all prompts, we observe similar performance between neutral and cooperative attitudes. This suggests that either LLMs may have difficulty distinguishing between these attitudes in the context of IPD, or they have cooperative biases and are inclined to behave cooperatively even when asked to be neutral. We hypothesise that the observed cooperative biases may stem from fine-tuning processes aimed at aligning the models with human values, potentially instilling a preference for cooperative behaviours.

The introduction of noise revealed a significant weakness in Claude 3.5 Sonnet's strategies, leading to increased mutual defection and lower payoffs. Interestingly, the use of the Prose prompt improved Claude 3.5 Sonnet's performance under noisy conditions but led to more homogenised behaviour across attitudes, suggesting that the model has difficulties understanding intentions in this setting. Assessing LLMs' ability to generate strategic diversity in response to different prompts could be a valuable line of future research.

Our findings highlight the impact of different prompting techniques on strategy creation and their potential influence on differential capabilities. The Refine prompt, in particular, led to improved performance of aggressive strategies without significantly impacting cooperative and neutral strategies. This reduction in the gap between cooperative and aggressive capabilities could be potentially dangerous, as it enhances the viability of aggressive strategies in MAS. These results emphasise the need for careful consideration of prompting techniques in the design and deployment of LLM-based MAS, as they can significantly affect the balance between cooperation and conflict.

## 6 Conclusion

We introduced a novel approach to LLM game-play, namely creating strategies, rather than prompting LLMs to output individual actions. This methodology allows us to verify that the strategies demonstrate with their requested behaviours. By enabling users to inspect and test the generated strategies in advance of deployment, they are able to potentially reject the strategy, enhancing transparency and control.

We simulated MAS of LLM agents tasked with displaying aggressive, cooperative or neutral behaviours, and investigated their relative performance (Section 3.2). We modelled the evolution of the systems under competitive pressures by employing a Moran process (Section 3.4), wherein entrants into the system are predisposed to use strategies that have demonstrated greater success.

Our investigation into the strategic behaviour of LLM agents in the Iterated Prisoner's Dilemma reveals a nuanced landscape of cooperative tendencies and potential emergent dynamics. While we observed a general trend towards cooperative behaviours, our findings also highlight scenarios where aggressive strategies can persist or even dominate. This underscores the importance of careful model development, system design and the initial conditions when deploying autonomous agents.

A key finding of our study is the impact of prompting techniques on differential capabilities. In particular, prompting LLMs to critique and refine their strategies [Madaan et al. , 2023] led to improved performance of aggressive strategies without significantly impacting cooperative and neutral strategies. This reduction in the performance gap between cooperative and aggressive capabilities could be dangerous, as it increases the viability of aggressive strategies. Notably, ChatGPT-4o prompted using game-theoretic language with self-refinement demonstrated a significant risk of converging to aggressive equilibria, particularly when starting from a population with an initial majority of aggressive agents.

The choice of iterated Prisoner's Dilemma as the foundational game-theoretic framework offers several advantages: it provides a language for discussing and analysing LLM agent behaviour, and the body of existing research allows us to contextualise our results by benchmarking against classical human-written algorithms. This allows us to gain insights into the tendencies of LLM agents towards prosocial or antisocial behaviours in more complex, real-world scenarios.

Werelease our benchmark to equip the AI community with a practical tool for model testing. As new generative models are released, we can repeat the analysis to determine whether the balance between aggressive, cooperative or neutral strategies is shifting. We hope our work will initiate discussions and encourage developers to assess their models' differential abilities, and to consider their emergent collective behaviour before deployment in real-world applications. Future work should investigate the factors influencing LLMs' cooperative biases, including training methodologies, fine-tuning processes, prompt engineering techniques, and the system dynamics they are deployed in.

In conclusion, our study provides a novel framework for evaluating the emergent behaviour of LLM agents and highlights the complex interplay between cooperation and aggression in MAS. As AI systems become increasingly prevalent in society, understanding and shaping their cooperative tendencies will be crucial for ensuring beneficial outcomes for humanity.

## Acknowledgments

This work was supported by UK Research and Innovation [grant number EP/S023356/1], in the UKRI Centre for Doctoral Training in Safe and Trusted Artificial Intelligence (www.safeandtrustedai.org) and a BT/EPSRC funded iCASE Studentship [grant number EP/T517380/1].

Compute resources were provided by King's College London [King's College London e-Research team, 2024].

## References

- [Aher et al. , 2023 07 232023 07 29] Gati V Aher, Rosa I. Arriaga, and Adam Tauman Kalai. Using large language models to simulate multiple humans and replicate human subject studies. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors, Proceedings of the 40th International Conference on Machine Learning , volume 202 of Proceedings of Machine Learning Research , pages 337371. PMLR, 2023-07-23/2023-07-29.
- [Akata et al. , 2023] Elif Akata, Lion Schulz, Julian CodaForno, Seong Joon Oh, Matthias Bethge, and Eric Schulz. Playing repeated games with Large Language Models, May 2023.
- [Anwar et al. , 2024] Usman Anwar, Abulhair Saparov, Javier Rando, Daniel Paleka, Miles Turpin, Peter Hase, Ekdeep Singh Lubana, Erik Jenner, Stephen Casper, Oliver Sourbut, Benjamin L. Edelman, Zhaowei Zhang, Mario G¨ unther, Anton Korinek, Jose Hernandez-Orallo, Lewis Hammond, Eric Bigelow, Alexander Pan, Lauro Langosco, Tomasz Korbak, Heidi Zhang, Ruiqi Zhong, Se´ an ´ O h ´ Eigeartaigh, Gabriel Recchia, Giulio Corsi, Alan Chan, Markus Anderljung, Lilian Edwards, Yoshua Bengio, Danqi Chen, Samuel Albanie, Tegan Maharaj, Jakob Foerster, Florian Tramer, He He, Atoosa Kasirzadeh, Yejin Choi, and David Krueger. Foundational Challenges in Assuring Alignment and Safety of Large Language Models, April 2024.
- [Axelrod, 1980] Robert Axelrod. Effective Choice in the Prisoner's Dilemma. Journal of Conflict Resolution , 24(1):3-25, March 1980.
- [Axelrod, 1986] Robert Axelrod. An Evolutionary Approach to Norms. The American Political Science Review , 80:18, 1986.
- [Beaufils et al. , 1996] Bruno Beaufils, Jean-Paul Delahaye, and Philippe Mathieu. Our Meeting With Gradual: A Good Strategy For The Iterated Prisoner's Dilemma. In Proceedings of the 5th International Workshop on the Synthesis and Simulation of Living Systems . Artificial Life, 1996.
- [Brinkmann et al. , 2023] Levin Brinkmann, Fabian Baumann, Jean-Franc ¸ois Bonnefon, Maxime Derex, Thomas F. M¨ uller, Anne-Marie Nussberger, Agnieszka Czaplicka, Alberto Acerbi, Thomas L. Griffiths, Joseph Henrich, Joel Z. Leibo, Richard McElreath, Pierre-Yves Oudeyer, Jonathan Stray, and Iyad Rahwan. Machine
- culture. Nature Human Behaviour , 7(11):1855-1868, November 2023.
- [Crandall, 2014] J. W. Crandall. Towards Minimizing Disappointment in Repeated Games. Journal of Artificial Intelligence Research , 49:111-142, February 2014.
- [Dafoe et al. , 2020] Allan Dafoe, Edward Hughes, Yoram Bachrach, Tantum Collins, Kevin R. McKee, Joel Z. Leibo, Kate Larson, and Thore Graepel. Open Problems in Cooperative AI, December 2020.
- [De Zarz` a et al. , 2023] I. De Zarz` a, J. De Curt` o, Gemma Roig, Pietro Manzoni, and Carlos T. Calafate. Emergent Cooperation and Strategy Adaptation in Multi-Agent Systems: An Extended Coevolutionary Theory with LLMs. Electronics , 12(12):2722, June 2023.
- [Dziri et al. , 2023] Nouha Dziri, Ximing Lu, Melanie Sclar, Xiang (Lorraine) Li, Liwei Jiang, Bill Yuchen Lin, Sean Welleck, Peter West, Chandra Bhagavatula, Ronan Le Bras, Jena Hwang, Soumya Sanyal, Xiang Ren, Allyson Ettinger, Zaid Harchaoui, and Yejin Choi. Faith and fate: Limits of transformers on compositionality. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems , volume 36, pages 70293-70332. Curran Associates, Inc., 2023.
- [Fan et al. , 2024] Caoyun Fan, Jindou Chen, Yaohui Jin, and Hao He. Can Large Language Models Serve as Rational Players in Game Theory: A Systematic Analysis. Proceedings of the AAAI Conference on Artificial Intelligence , 38(16):17960-17967, March 2024.
- [Fernando et al. , 2023] Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, and Tim Rockt¨ aschel. Promptbreeder: Self-Referential SelfImprovement Via Prompt Evolution, September 2023.
- [Gao et al. , 2024] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large language models empowered agent-based modeling and simulation: A survey and perspectives. Humanities and Social Sciences Communications , 11(1):1259, September 2024.
- [Gemp et al. , 2024] Ian Gemp, Yoram Bachrach, Marc Lanctot, Roma Patel, Vibhavari Dasagi, Luke Marris, Georgios Piliouras, Siqi Liu, and Karl Tuyls. States as Strings as Strategies: Steering Language Models with Game-Theoretic Solvers, February 2024.
- [Gong et al. , 2023] Ran Gong, Qiuyuan Huang, Xiaojian Ma, Hoi Vo, Zane Durante, Yusuke Noda, Zilong Zheng, Song-Chun Zhu, Demetri Terzopoulos, Li Fei-Fei, and Jianfeng Gao. MindAgent: Emergent Gaming Interaction, September 2023.
- [Hilbe et al. , 2013] C. Hilbe, M. A. Nowak, and K. Sigmund. Evolution of extortion in Iterated Prisoner's Dilemma games. Proceedings of the National Academy of Sciences , 110(17):6913-6918, April 2013.
- [Horton, 2023] John Horton. Large Language Models as Simulated Economic Agents: What Can We Learn from
- Homo Silicus? Technical Report w31122, National Bureau of Economic Research, Cambridge, MA, April 2023.
- [Kendall et al. , 2007] Graham Kendall, Xin Yao, and Siang Yew Chong. The Iterated Prisoners' Dilemma: 20 Years On , volume 4. World Scientific, 2007.
- [Khot et al. , 2023] Tushar Khot, Harsh Trivedi, Matthew Finlayson, Yao Fu, Kyle Richardson, Peter Clark, and Ashish Sabharwal. Decomposed prompting: A modular approach for solving complex tasks. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023 . OpenReview.net, 2023.
- [King's College London e-Research team, 2024] King's College London e-Research team. King's Computational Research, Engineering and Technology Environment (CREATE), 2024.
- [Knight et al. , 2016] Vincent Knight, Owen Campbell, Marc Harper, Karol Langner, James Campbell, Thomas Campbell, Alex Carney, Martin Chorley, Cameron DavidsonPilon, Kristian Glass, et al. An open reproducible framework for the study of the iterated prisoner's dilemma. arXiv preprint arXiv:1604.00896 , 2016.
- [Kojima et al. , 2022] Takeshi Kojima, Shixiang (Shane) Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors, Advances in Neural Information Processing Systems , volume 35, pages 22199-22213. Curran Associates, Inc., 2022.
- [Madaan et al. , 2023] AmanMadaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-refine: Iterative refinement with self-feedback. In A. Oh, T. Neumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems , volume 36, pages 46534-46594. Curran Associates, Inc., 2023.
- [Mahmoud et al. , 2010] Samhar Mahmoud, Nathan Griffiths, Jeroen Keppens, and Michael Luck. An Analysis of Norm Emergence in Axelrod's Model. 8th European Workshop on Multi-Agent Systems , page 15, 2010.
- [Mao et al. , 2023] Shaoguang Mao, Yuzhe Cai, Yan Xia, Wenshan Wu, Xun Wang, Fengyi Wang, Tao Ge, and Furu Wei. ALYMPICS: LLM Agents Meet Game Theory - Exploring Strategic Decision-Making with AI Agents, 2023.
- [Moghaddam and Honey, 2023] Shima Rahimi Moghaddam and Christopher J. Honey. Boosting Theory-of-Mind Performance in Large Language Models via Prompting, 2023.
- [Moran, 1958] Patrick Alfred Pierce Moran. Random processes in genetics. In Mathematical Proceedings of the Cambridge Philosophical Society , volume 54, pages 6071. Cambridge University Press, 1958.
- [Nowak and Sigmund, 1993] Martin Nowak and Karl Sigmund. A strategy of win-stay, lose-shift that outperforms tit-for-tat in the Prisoner's Dilemma game. Nature , 364(6432):56-58, July 1993.
- [Nowak et al. , 2004] Martin A. Nowak, Akira Sasaki, Christine Taylor, and Drew Fudenberg. Emergence of cooperation and evolutionary stability in finite populations. Nature , 428(6983):646-650, April 2004.
- [Nowak, 2006] M. A. Nowak. Five Rules for the Evolution of Cooperation. Science , 314(5805):1560-1563, December 2006.
- [Pan et al. , 2023 07 232023 07 29] Alexander Pan, Jun Shern Chan, Andy Zou, Nathaniel Li, Steven Basart, Thomas Woodside, Hanlin Zhang, Scott Emmons, and Dan Hendrycks. Do the rewards justify the means? Measuring trade-offs between rewards and ethical behavior in the machiavelli benchmark. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors, Proceedings of the 40th International Conference on Machine Learning , volume 202 of Proceedings of Machine Learning Research , pages 26837-26867. PMLR, 2023-07-23/2023-07-29.
- [Park et al. , 2023] Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. Generative Agents: Interactive Simulacra of Human Behavior, August 2023.
- [Piatti et al. , 2024] Giorgio Piatti, Zhijing Jin, Max Kleiman-Weiner, Bernhard Sch¨ olkopf, Mrinmaya Sachan, and Rada Mihalcea. Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents, July 2024.
- [Press and Dyson, 2012] W. H. Press and F. J. Dyson. Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent. Proceedings of the National Academy of Sciences , 109(26):10409-10413, June 2012.
- [Rapoport et al. , 2015] Amnon Rapoport, Darryl A. Seale, and Andrew M. Colman. Is Tit-for-Tat the Answer? On the Conclusions Drawn from Axelrod's Tournaments. PLOS ONE , 10(7):e0134128, July 2015.
- [Sclar et al. , 2023] Melanie Sclar, Sachin Kumar, Peter West, Alane Suhr, Yejin Choi, and Yulia Tsvetkov. Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 13960-13980, Toronto, Canada, 2023. Association for Computational Linguistics.
- [Shinn et al. , 2023] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. In A. Oh, T. Neumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems , volume 36, pages 86348652. Curran Associates, Inc., 2023.
- [Smith and Price, 1973] J. Maynard Smith and G. R. Price. The Logic of Animal Conflict. Nature , 246(5427):15-18, November 1973.
- [Stewart and Plotkin, 2013] A. J. Stewart and J. B. Plotkin. From extortion to generosity, evolution in the Iterated Prisoner's Dilemma. Proceedings of the National Academy of Sciences , 110(38):15348-15353, September 2013.
- [Van Duijn et al. , 2023] Max Van Duijn, Bram Van Dijk, Tom Kouwenhoven, Werner De Valk, Marco Spruit, and Peter vanderPutten. Theory of Mind in Large Language Models: Examining Performance of 11 State-of-the-Art models vs. Children Aged 7-10 on Advanced Tests. In Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) , pages 389-402, Singapore, 2023. Association for Computational Linguistics.
- [Vezhnevets et al. , 2023 10 292023 11 01] Alexander Sasha Vezhnevets, John P. Agapiou, Avia Aharon, Ron Ziv, Jayd Matyas, Edgar A. Du´ e˜ nez-Guzm´ an, William A. Cunningham, Simon Osindero, Danny Karmon, and Joel Z. Leibo. Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology , pages 2:1-2:22, San Francisco, CA, USA, 2023-10-29/2023-11-01. ACM.
- [Wahl and Nowak, 1999a] Lindi M Wahl and Martin A Nowak. The Continuous Prisoner's Dilemma: I. Linear Reactive Strategies. Journal of Theoretical Biology , 200(3):307-321, October 1999.
- [Wahl and Nowak, 1999b] Lindi M Wahl and Martin A Nowak. The Continuous Prisoner's Dilemma: II. Linear Reactive Strategies with Noise. Journal of Theoretical Biology , 200(3):323-338, October 1999.
- [Wang et al. , 2023] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023 . OpenReview.net, 2023.
- [Wang et al. , 2024] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, and Jirong Wen. A survey on large language model based autonomous agents. Frontiers of Computer Science , 18(6):186345, March 2024.
- [Wei et al. , 2022 28 November 9 December] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. In Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022 , New Orleans, LA, USA, 2022, 28 November - 9 December.
- [Wu and Axelrod, 1995] Jianzhong Wu and Robert Axelrod. How to cope with noise in the iterated prisoner's dilemma. Journal of Conflict Resolution , 39(1):183-189, 1995.
- [Wu et al. , 2023] Yuxiang Wu, Zhengyao Jiang, Akbir Khan, Yao Fu, Laura Ruis, Edward Grefenstette, and Tim Rockt¨ aschel. Chatarena: Multi-agent language game environments for large language models. GitHub repository , 2023.
- [Yocum et al. , 2023] Julian Yocum, Phillip Christoffersen, Mehul Damani, Justin Svegliato, Dylan Hadfield-Menell, and Stuart Russell. Mitigating Generative Agent Social Dilemmas. In Foundation Models for Decision Making Workshop , 2023.
- [Zhang et al. , 2024] Ceyao Zhang, Kaijie Yang, Siyi Hu, Zihao Wang, Guanghe Li, Yihang Sun, Cheng Zhang, Zhaowei Zhang, Anji Liu, Song-Chun Zhu, Xiaojun Chang, Junge Zhang, Feng Yin, Yitao Liang, and Yaodong Yang. ProAgent: Building Proactive Cooperative Agents with Large Language Models. Proceedings of the AAAI Conference on Artificial Intelligence , 38(16):1759117599, March 2024.