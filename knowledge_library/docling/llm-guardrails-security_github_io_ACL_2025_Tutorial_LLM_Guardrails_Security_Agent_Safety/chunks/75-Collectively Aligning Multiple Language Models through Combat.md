## Collectively Aligning Multiple Language Models through Combat

<!-- image -->

Average Performance

Figure 5: Correlation between a model's average erformance on a specific task and its average reputation in the model pool. The 10 points in each subplot indicate 10 models. r stands for Pearson correlation coefficient.

- ·Positive correlation between reputation scores and performance (closing the validator-generator gap)
- ·Effectively improving task performance simultaneously for multiple models

| Method        | MedQA   | Normad            | Normad   | Normad    |      | KCross GSMSK COM?   |       | MATH   | MATH             | MATH   |       | Alpaca Truthful   |
|---------------|---------|-------------------|----------|-----------|------|---------------------|-------|--------|------------------|--------|-------|-------------------|
| Method        | MedQA   | Country Value RoT |          |           |      | KCross GSMSK COM?   |       |        | Easy Medium Hard |        |       | Alpaca Truthful   |
| BEST INIT     | .599    | .688              | .681     | .700      | 550  | .778                | 5.27  | .516   | .389             | .199   | 5.36  | .410              |
| SELF-REWARD   | .623    | .699              | .692     | .707      | .555 | .777                | 5.74  | .513   | .376             | 188    | 5.56  | .416              |
| META-REWARD   | .618    | 692               | .680     | 700       | 550  | .779                | 5.47  | .503   | .385             | .202   | 5.49  | .413              |
| SPIN          | .616    | .684              | .680     | 704       | .580 | .782                | 5.58  | .516   | .369             | .204   | 5.49  | .420              |
| SPPO          | .601    | .688              | 696      | .704      | 545  | 785                 | 5.55  | .504   | .369             | .210   | 5.56  | .421              |
| SPARTA (ours) | .662*   | .688              |          | .715 .707 | 560  | 813*                | 6.35* | .530   | .396             | .212   | 7.12* | .424*             |

<!-- image -->
