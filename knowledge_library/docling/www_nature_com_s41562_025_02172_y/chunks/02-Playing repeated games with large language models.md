## Playing repeated games with large language models

Received: 6 December 2023

Accepted: 12 March 2025

Published online: 8 May 2025

Check for updates

Elif Akata 1,2,3 , Lion Schulz 2 , Julian Coda-Forno 1,2 , Seong Joon Oh 3 , Matthias Bethge 3 &amp; Eric Schulz 1,2

Large language models (LLMs) are increasingly used in applications where they interact with humans and other agents. We propose to use behavioural game theory to study LLMs' cooperation and coordination behaviour. Here we let different LLMs play finitely repeated 2 × 2 games with each other, with human-like strategies, and actual human players. Our results show that LLMs perform particularly well at self-interested games such as the iterated Prisoner's Dilemma family. However, they behave suboptimally in games that require coordination, such as the Battle of the Sexes. We verify that these behavioural signatures are stable across robustness checks. We also show how GPT-4's behaviour can be modulated by providing additional information about its opponent and by using a 'social chain-of-thought' strategy. This also leads to better scores and more successful coordination when interacting with human players. These results enrich our understanding of LLMs' social behaviour and pave the way for a behavioural game theory for machines.

<!-- image -->

Large language models (LLMs) are deep learning models with billions of parameters trained on huge corpora of text 1-3 . While they can generate text that human evaluators struggle to distinguish from text written by other humans 4 , they have also shown other, emerging abilities 5 . They can, for example, solve analogical reasoning tasks 6 , program web applications 7 , use tools to solve multiple tasks 8 or adapt their strategies purely in-context 9 . Because of these abilities and their increasing popularity, LLMs are already transforming our daily lives as they permeate into many applications 10 . This means that LLMs will interact with us and other agents-LLMs or otherwise-frequently and repeatedly. How do LLMs behave in these repeated social interactions?

Measuring how people behave in repeated interactions, for example, how they cooperate 11 and coordinate 12 , is the subject of a subfield of behavioural economics called behavioural game theory 13 . While traditional game theory assumes that people's strategic decisions are rational, selfish and focused on utility maximization 14,15 , behavioural game theory has shown that human agents deviate from these principles and, therefore, examines how their decisions are shaped by social preferences, social utility and other psychological factors 16 . Thus, behavioural game theory lends itself well to studying the repeated interactions of diverse agents 17,18 , including artificial agents 19 .

In this Article, we analyse LLMs' behavioural patterns by letting them play finitely repeated games with full information and against other LLMs, simple, human-like strategies and actual human players. Finitely repeated games have been engineered to understand how agents should and do behave in interactions over many iterations. We focus on two-player games with two discrete actions, that is, 2 × 2 games (see Fig. 1 for an overview).

Analysing LLMs' performance across families of games, we find that they perform well in games that value pure self-interest, especially those from the Prisoner's Dilemma family. However, they underperform in games that involve coordination. Based on this finding, we further focus on games taken from these families and, in particular, on the currently largest LLM: GPT-4 (ref. 20). In the canonical Prisoner's Dilemma, which assesses how agents cooperate and defect, we find that GPT-4 retaliates repeatedly, even after having experienced only one defection. Because this can indeed be the equilibrium individual-level strategy, GPT-4 is good at these games because it is particularly unforgiving and selfish. However, in the Battle of the Sexes, which assesses how agents

1 Institute for Human-Centered AI, Helmholtz Munich, Oberschleißheim, Germany. 2 Max Planck Institute for Biological Cybernetics, Tübingen, Germany.

3 University of Tübingen, Tübingen, Germany. e-mail: elif.akata@helmholtz-munich.de

Fig. 1 | Playing repeated games in an example game of Battle of the Sexes. In step 1, the pay-off matrix is turned into textual game rules. In step 2, the game rules, the current game history and the query are concatenated and passed to

<!-- image -->

trade off between their own and their partners' preferences, we find that GPT-4 does not manage to coordinate with simple, human-like agents that alternate between options over trials. Thus, GPT-4 is bad at these games because it is uncoordinated. We also verify that these behaviours are not due to an inability to predict the other player's actions, and persist across several robustness checks and changes to the pay-off matrices. We point to two ways in which these behaviours can be changed. GPT-4 can be made to act more forgivingly by pointing out that the other player can make mistakes. Moreover, GPT-4 gets better at coordinating with the other player when it is first asked to predict their actions before choosing an action itself, an approach we term social chain-of-thought (SCoT) prompting. Finally, we let GPT-4 with and without SCoT-prompting play the canonical Prisoner's Dilemma and the Battle of the Sexes with human players. We find that SCoT prompting leads to more successful coordination and joint cooperation between participants and LLMs and makes participants believe more frequently that the other player is human.
