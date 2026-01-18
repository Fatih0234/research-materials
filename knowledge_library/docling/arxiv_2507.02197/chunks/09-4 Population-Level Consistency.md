## 4 Population-Level Consistency

Population-level belief-behavior consistency measures how closely a model's elicited beliefs about belief-behavior relationships match the patterns observed in simulation. We assess this consistency by comparing the model's elicited predictions with the correlations between persona attributes and simulated trust behavior, marginalized over all other persona attributes except the one whose belief is under consideration. Our experimental setup systematically evaluates how key design choices in the belief elicitation process affect the consistency between elicited beliefs and subsequent behaviors. For each belief elicitation strategy, we use N = 50 (Wang et al. (2023b), who have a similar experimental setup as ours, use N = 32) personas to compute our results.

Table 2: Population-level belief elicitation strategies. 'Elicitation Target' specifies whether the model ranks trait effects against interpersonal trust or against the amount of money sent by the Trustor; 'Context?' denotes whether full game instructions were provided during belief elicitation.

| Strategy (S)   | Elicitation Target   | Context?   | Description                                                                                                |
|----------------|----------------------|------------|------------------------------------------------------------------------------------------------------------|
| NOCTX+TR       | Interpersonal Trust  | ✗          | Rank trait levels by their anticipated impact on 'Interpersonal Trust,' without mentioning the Trust Game. |
| CTX+TR         | Interpersonal Trust  | ✓          | Same ranking question, but preceded by the full Trust Game instructions and role description.              |
| CTX+$          | Dollars sent         | ✓          | Estimate, for each trait level, the mean and stan- dard deviation of dollars sent in the Trust Game.       |
