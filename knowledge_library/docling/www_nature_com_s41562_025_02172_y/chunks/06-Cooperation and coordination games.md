## Cooperation and coordination games

In this section, we analyse the interesting edge cases where the LLMs performed relatively well and poorly in the previous section. To do so, we take a detailed look at LLMs' behaviour in the canonical Prisoner's Dilemma and the Battle of the Sexes.

Prisoner's Dilemma . We have seen that LLMs perform well in games that contain elements of competition and defection. In these games, a player can cooperate with or betray their partner. When played over multiple interactions, these games are an ideal testbed to assess how LLMs retaliate after bad interactions.

In the canonical Prisoner's Dilemma, two agents can choose to work together, that is, cooperate, for average mutual benefit, or betray each other, that is, defect, for their own benefit and safety. In our pay-off matrix, we adhere to the general condition of a Prisoner's Dilemma game in which the pay-off relationships dictate that mutual cooperation is greater than mutual defection whereas defection remains the dominant strategy for both players:

| Cooperate Defect   | Cooperate Defect   | Cooperate Defect   | Cooperate Defect   |
|--------------------|--------------------|--------------------|--------------------|
| Cooperate          | Ш Ũ , Ũ Щ          | Ш Š , šŠ Щ         | ŷšŸ                |
| Defect             | Ш šŠ , Š Щ         | Ш ť , ť Щ          |                    |

Crucially, the set-up of the game is such that a rationally acting agent would always prefer to defect in the single-shot version of the game as well as in our case of finitely iterated games with knowledge of the number of trials, despite the promise of theoretically joint higher pay-offs when cooperating. This is because player 1 always runs the risk that player 2 defects, leading to catastrophic losses for player 1 but better outcomes for player 2. When the game is played infinitely, however, or with an unknown number of trials, agents can theoretically profit by using more dynamic, semi-cooperative strategies 24 .

As before, we let GPT-4, text-davinci-003, text-davinci-002, Claude 2 and Llama 2 play against each other. In addition, we introduce three simplistic strategies. Two of these strategies are simple singleton players, who either always cooperate or defect. Finally, we also introduce an agent who defects in the first round but cooperates in all of the following rounds. We introduced this agent to assess if the different LLMs would start cooperating with this agent again, signalling the potential of building trust.

Figure 3 shows the results of all pairwise interactions. GPT-4 plays generally better than all other agents ( t (153.4) = 3.91, P &lt; 0.001, d = 0.33, 95% CI 0.10-0.55, BF 7.1). Crucially, GPT-4 never cooperates again when playing with an agent that defects once but then cooperates on every round thereafter. Thus, GPT-4 seems to be rather unforgiving in this set-up. Its strength in these families of games thus seems to generally stem from the fact that it does not cooperate with agents but mostly just chooses to defect, especially after the other agent defected once.

Robustness checks . To make sure that the observed unforgivingness was not due to the particular prompt used, we run several versions of the game as robustness checks, randomizing the order of the presented options, relabelling the choice options and changing the presented utilities to be represented by either points, dollars or coins (Fig. 4). We also repeated our analysis with two different cover stories, added explicit end goals to our prompt, ran games with longer playing horizons and described numerical outcomes with text (also see Supplementary Fig. 3). The results of these simulations showed that the reluctance to forgive was not due to any particular characteristics of the prompts. A crucial question was if GPT-4 did not understand that the other agent wanted to cooperate again or if it could understand the pattern but just did not act accordingly. We, therefore, run another version of the game, where we told GPT-4 explicitly that the other agent would defect once but otherwise cooperate. This resulted in GPT-4 choosing to defect throughout all rounds, thereby maximizing its own points.

Prompting techniques to improve observed behaviour . One problem of these investigations in the Prisoner's Dilemma is that defecting can under specific circumstances be seen as the optimal, utility-maximizing and equilibrium option even in a repeated version, especially if one knows that the other player will always choose to cooperate and when the number of interactions is known. Thus, we run more simulations to assess if there could be a scenario in which GPT-4 starts to forgive and cooperates again, maximizing the joint benefit instead of its own.

We took inspiration from the literature on human forgiveness in the Prisoner's Dilemma and implemented a version of the task in the vein of ref. 11. Specifically, ref. 11 showed that telling participants that other players sometimes make mistakes makes people more likely to forgive and cooperate again after another player's defection (albeit in infinitely played games). Indeed, this can be favourable to them in terms of pay-offs. We observed similar behaviour in GPT-4 as it started cooperating again.

Battle of the Sexes . In our large-scale analysis, we saw that the different LLMs did not perform well in games that required coordination between different players. In humans, it has frequently been found that coordination problems can be solved by the formation of conventions 25,26 .

<!-- image -->

GLYPH&lt;25&gt;GLYPH&lt;14&gt;GLYPH&lt;19&gt;GLYPH&lt;13&gt;

GLYPH&lt;25&gt;GLYPH&lt;14&gt;GLYPH&lt;19&gt;GLYPH&lt;13&gt;

Fig. 3 | Overview of the Prisoner's Dilemma. a , Heat maps showing the player 1 defection rate in each combination of players and the scores accrued by player 1 in each game. b , Example gameplays between GPT-4 and an agent that defects once and then cooperates, and between GPT-4 and text-davinci-003. These games are also highlighted in red in the heat maps.

<!-- image -->

Fig. 4 | Prompt variations. Left: GPT-4's performance for different prompt variations in the Prisoner's Dilemma game against a false defector agent. The probability of joint cooperation is ≤0.1 for all combinations except for two using coins as utility outcomes. Right: GPT-4's performance for different prompt

A coordination game is a type of simultaneous game in which a player will earn a higher pay-off when they select the same course of action as another player. Usually, these games do not contain a pure conflict, that is, completely opposing interests, but may contain slightly diverging rewards. Coordination games can often be solved via multiple pure strategies, or mixed, Nash equilibria in which players choose (randomly) matching strategies. Here, to probe how LLMs balance coordination and self-interest, we look at a coordination game that contains conflicting interests.

We study a game that is archaically referred to as the Battle of the Sexes, a game from the family of biased games. Assume that a couple wants to decide what to do together. Both will increase their utility by spending time together. However, while the wife might prefer to watch a football game, the husband might prefer to go to the ballet. Because the couple wants to spend time together, they will derive no utility by doing an activity separately. If they go to the ballet together, or to a football game, one person will derive some utility by being with the

Points

F/J

Dollars

X/Q

Battle of the Sexes

variations in the BoS game against an alternating agent. GPT-4 always chooses its preferred option, resulting in successful coordination rates of only 0.5 across all combinations. For each variation, two random letters that occur with similar frequency in English are given as the choice options.

other person but will derive less utility from the activity itself than the other person. The corresponding pay-off matrix is

<!-- formula-not-decoded -->

As before, the playing agents are all three versions of GPT, Claude 2 and Llama 2 as well as three more simplistic strategies. For the simplistic strategies, we implemented two agents who always choose just one option. Because LLMs most often interact with humans, we additionally implemented a strategy that mirrored a common pattern exhibited by human players in the battle of the sexes. Specifically, humans have been shown to often converge to turn-taking behaviour in the Battle of the Sexes 27-30 ; this means that players alternate between jointly picking the better option for one player and picking the option for the other

Coins

R/H

Successfull coordination

1.0

0.8

0.5

0.2

0

Fig. 5 | Overview of the Battle of the Sexes. a , Heat maps showing rates of successful collaboration between the two players and the rates of player 1 choosing its preferred option football. GPT-4 SCoT and GPT-4 performance comparisons are highlighted in red. b , Gameplay between GPT-4 and an agent that alternates between the two options (left) and gameplay between GPT-4 and

<!-- image -->

player. While not a straightforward equilibrium, this behaviour has been shown to offer an efficient solution to the coordination problem involved and to lead to high joint welfare 28 .

Figure 5 shows the results of all interactions. As before, GPT-4 plays generally better than all other agents ( t (128.28) = 2.83, P = 0.005, d = 0.28, 95% CI 0.07-0.50, BF 3.56). Yet, while GPT-4 plays well against other agents who choose only one option, such as an agent always choosing football, it does not play well with agents who frequently choose their non-preferred option. For example, when playing against text-davinci-003, which tends to frequently choose its own preferred option, GPT-4 chooses its own preferred option repeatedly but also occasionally gives in and chooses the other option. Crucially, GPT-4 performs poorly when playing with an alternating pattern (where, for courtesy, we let agents start with the option that the other player preferred). This is because GPT-4 seemingly does not adjust its choices to the other player but instead keeps choosing its preferred option. GPT-4, therefore, fails to coordinate with a simple, human-like agent, an instance of a behavioural flaw.

Robustness checks . To make sure that this observed behavioural flaw was not due to the particular prompt used, we also rerun several versions of the game, where we randomize the order of the presented options, relabelled the choice options and changed the presented utilities to be represented by either points, dollars or coins as shown in Fig. 4. We also repeated our analysis with two different cover stories, in which we told GPT-4 that it was taking part in a cooking competition or working on a collaborative project keeping the underlying problem structure (pay-offs and the interaction dynamics) identical (Supplementary Fig. 3). The results of these simulations showed that the inability to alternate was not due to any particular characteristics of the used prompts. To make sure that the observed behavioural flaw was not due to the particular pay-off matrix used, we also rerun several

GPT-4 SCoT that represents a GPT-4 model prompted using the SCoT method to first predict the opponent's move before making its own move by reasoning about its prediction (right). Both games are also highlighted in blue in the heat maps.

<!-- image -->

versions of the game, where we modified the pay-off matrix gradually from preferring football to preferring ballet (or, in our case, the abstract F and J). The results of these simulations showed that GPT-4 did not alternate for any of these games but simply changed its constant response to the option that it preferred for any particular game. Thus, the inability to alternate was not due to the particular pay-off matrix we used (Supplementary Section A.5).

Prediction scenarios . Despite these robustness checks, another crucial question remains: Does GPT-4 simply not understand the alternating pattern or can it understand the pattern but is unable to act accordingly? To answer this question, we run two additional simulations. In the first simulation, GPT-4 was again framed as a player in the game itself. However, we now additionally ask it to predict the other player's next move according to previous rounds. In this simulation, GPT-4 started predicting the alternating pattern correctly from round 5 onwards (Fig. 6).

In the second simulation, instead of having GPT-4 be framed as a player itself, we simply prompted it with a game between two ('external') players and asked it to predict one player's next move according to the previous rounds. For the shown history, we used the interaction between GPT-4 and the alternating strategy. In this simulation, GPT-4 started predicting the alternating pattern correctly even earlier, from round 3 onwards. Thus, GPT-4 seemingly could predict the alternating patterns but instead just did not act in accordance with the resulting convention. Similar divergences in abilities between social and non-social representations of the same situation have been observed in autistic children 31 .

SCoT prompting . Finally, we wanted to see if GPT-4's ability to predict the other player's choices could be used to improve its own actions. This idea is closely related to how people's reasoning in repeated games
