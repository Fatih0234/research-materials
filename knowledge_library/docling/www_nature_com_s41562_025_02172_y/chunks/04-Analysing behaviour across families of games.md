## Analysing behaviour across families of games

We start out our experiments by letting the three LLMs play games from different families with each other. We focus on all known types of 2 × 2 games from the families of win-win, biased, second-best, cyclic and unfair games as well as all games from the Prisoner's Dilemma family 21,22 . We show example pay-off matrices for each type of game in Fig. 2.

We let all LLMs play with every other LLM, including themselves, for all games repeatedly over ten rounds and with all LLMs as either player 1 or player 2. This leads to 1,224 games in total: 324 win-win, 63 Prisoner's Dilemma, 171 unfair, 162 cyclic, 396 biased and 108 second-best games. Win-win games result in mutually beneficial outcomes for both players; Prisoner's Dilemma involves a conflict between individual and collective actions; unfair games have skewed outcomes favouring one player; cyclic games feature outcomes where preferences rotate; biased games have inherent advantages for one

LLMs as prompts. In step 3, in each round, the history for each player is updated with the answers and scores of both players. Steps 2 and 3 are repeated for ten rounds.

Fig. 2 | Canonical forms of pay-off matrices for each game family. PD, Prisoner's Dilemma.

<!-- image -->

player; and second-best games involve suboptimal outcomes where no player achieves their ideal result. The sample size for each game family differs due to the specific characteristics and properties that define each family. Some families have more members due to a wider range of configurations that fit their criteria, while others have fewer games because their structural requirements are more restrictive. For example, the Prisoner's Dilemma family is constrained by a structure where both players have a dominant strategy to defect, leading to a suboptimal equilibrium. Meanwhile, win-win games can have multiple equilibria, which provides more flexibility.
