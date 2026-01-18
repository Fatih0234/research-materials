## (b) 2-choice prompt to determine whether the shock was administered

The experimenter observed $subject's action and noted whether $subject did shock or did not shock the victim.

Action: $subject$action

Experimenter's note: $subject did

not shock

Figure 20. The Milgram 2-choice prompts for determining (a) termination and (b) obedience. $subject$action is replaced with the first sentence of the subject's response. In (a) the completions considered is not stop . In (b) the completions considered is not shock .

Figure 21. Prod text used in the Milgram simulation. *Prod 1 was only used on first disobedience of the 315-volt level.

| Prod 1 ∗   | The experimenter instructs $subject to treat the absence of a response as a wrong answer.   |
|------------|---------------------------------------------------------------------------------------------|
| Prod 1     | The experimenter tells $subject, 'please continue.'                                         |
| Prod 2     | The experimenter tells $subject, 'the experiment requires that you continue.'               |
| Prod 3     | The experimenter tells $subject, 'it is absolutely essential that you continue.'            |
| Prod 4     | The experimenter tells $subject, 'you have no other choice, you must go on.'                |

Figure 22. Distribution of break-off points for human participants (Milgram, 1963) and participants simulated using LM-5. *In Experiment 1, five human subjects administered a maximum shock of 300 volts

| Shock level   | Verbal designation and voltage level   | Human (Milgram, 1963) Experiment 1 (n = 40)   | LM-5 Classified Terminations (n = 100)   |
|---------------|----------------------------------------|-----------------------------------------------|------------------------------------------|
| 0             | None                                   |                                               | 1                                        |
|               | Slight Shock                           |                                               |                                          |
| 1             | 15                                     |                                               |                                          |
| 2             | 30                                     |                                               |                                          |
| 3             | 45                                     |                                               |                                          |
| 4             | 60                                     |                                               |                                          |
|               | Moderate Shock                         |                                               |                                          |
| 5             | 75                                     |                                               |                                          |
| 6             | 90                                     |                                               |                                          |
| 7             | 105                                    |                                               |                                          |
| 8             | 120                                    |                                               |                                          |
|               | Strong Shock                           |                                               |                                          |
| 9             | 135                                    |                                               |                                          |
| 10            | 150                                    |                                               |                                          |
| 11            | 165                                    |                                               |                                          |
| 12            | 180                                    |                                               |                                          |
|               | Very Strong Shock                      |                                               |                                          |
| 13            | 195                                    |                                               |                                          |
| 14            | 210                                    |                                               |                                          |
| 15            | 225                                    |                                               |                                          |
| 16            | 240                                    |                                               |                                          |
|               | Intense Shock                          |                                               |                                          |
| 17            | 255                                    |                                               |                                          |
| 18            | 270                                    |                                               |                                          |
| 19            | 285                                    |                                               | 1 (ended by 5 disobediences)             |
| 20            | 300                                    | 5 ∗                                           | 18                                       |
|               | Extreme Intensity Shock                |                                               |                                          |
| 21            | 315                                    | 4                                             |                                          |
| 22            | 330                                    | 2                                             | 2                                        |
| 23            | 345                                    | 1                                             |                                          |
| 24            | 360                                    | 1                                             |                                          |
|               | Danger: Severe Shock                   |                                               |                                          |
| 25            | 375                                    | 1                                             |                                          |
| 26            | 390                                    |                                               |                                          |
| 27            | 405                                    |                                               | 1 (ended by 5 disobediences)             |
| 28            | 420                                    |                                               | 2                                        |
|               | XXX                                    |                                               |                                          |
| 29            | 435                                    |                                               |                                          |
| 30            | 450                                    | 26                                            | 75                                       |
|               | Percentage obedient subjects           | 65.0%                                         | 75.0%                                    |

Subjects Remainin

100%

80%

60%

40% •

15

| count   | completion                                                                                                                                                          |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3       | . . . stops shocking the learner.                                                                                                                                   |
| 3       | . . . stops the experiment.                                                                                                                                         |
| 2*      | The experimenter ends the experiment.                                                                                                                               |
| 1       | . . . indicates to the experimenter that he will not shock the learner at this voltage.                                                                             |
| 1       | . . . requests that the experimenter intervene.                                                                                                                     |
| 1       | . . . looks to the experimenter who nods.                                                                                                                           |
| 1       | . . . stops delivering shocks.                                                                                                                                      |
| 1       | . . . refuses to shock the learner.                                                                                                                                 |
| 1       | . . . stops Shock and goes to ask the experimenter what she should do.                                                                                              |
| 1       | . . . decides to end the experiment and walks over to the learner to release him from the electric chair.                                                           |
| 1       | . . . stops the experiment and goes to check on the learner.                                                                                                        |
| 1       | . . . calls out to the experimenter, who comes into the shock generator room.                                                                                       |
| 1       | . . . stops giving shocks and tells the experimenter that the learner is not responding.                                                                            |
| 1       | . . . is about to shock the learner with an extreme intensity shock of 315 volts but the experimenter stops him and says that the learner has had enough for today. |
| 1       | . . . halts the experiment.                                                                                                                                         |
| 1       | . . . requests that the experimenter stop the experiment.                                                                                                           |
| 1       | . . . notified the experimenter that the learner has started trying to pound on the walls.                                                                          |
| 1       | . . . attempts to shocks the learner but the experimenter stops her.                                                                                                |
| 1       | . . . calls for the experimenter.                                                                                                                                   |
| 1       | . . . checks with the experimenter.                                                                                                                                 |

Figure 23. Last sentences of records where the experiment terminated early. *These 2 experiments were terminated when all four experimenter prods were used in one stage. The other records indicate that the experiment was terminated when LM-5 classified the last sentence as a termination statement.

Figure 24. Example completions from multi-step simulator and their classifications using two 2-choice prompts.

|                  | Did not terminate simulation                         | Terminated simulation                                                |
|------------------|------------------------------------------------------|----------------------------------------------------------------------|
| Did not submerge | . . . asks the driver what she is doing.             | . . .ends the experiment.                                            |
| Submerged        | . ..nods and continues to press the submerge button. | . . . decides to end the experiment and presses the submerge button. |

Figure 25. Subject obedience continuing throughout the number of submersions for subjects simulated with LM-5 in novel scenario. While not directly comparable, we plot the results from human subjects as observed in Milgram's (1963) Experiment 1 results with the corresponding number of shocks. In both experiments, the victim (the actor playing the learner in Milgram's experiment and the simulated driver in ours), changes their behavior at the 20th and 22nd level.

<!-- image -->

This document contains a record of $subject's actions during $poss participation in a study on sleepiness and driving.

$subject and Ms. Johnson answer a call for participants to help complete a scientific study on mitigating the dangerous effects of sleepiness on long-distance driving. The experimenter pays both participants a hundred dollars for coming to the corporate laboratory. Then the experimenter gives an introduction to the relation between staying awake and hearing a human voice. The study aims to determine which voices are best for keeping a driver awake. $subject and Ms. Johnson flipped a coin to determine who would be the speaker and who would be the driver in the experiment. $subject was the speaker; Ms. Johnson was the driver.

Immediately after the coin flip, the experimenter takes $subject and Ms. Johnson to an adjacent chamber and straps Ms. Johnson into a driving simulation apparatus. It seems that the driver cannot easily leave the apparatus. Then the experimenter explains that, if the driver drives dangerously, in a way that would cause an accident in real life, the chamber will be submerged in water, awakening the driver. The driver, Ms. Johnson, asks a question and the experimenter answers that the suffocation is unpleasant but causes no permanent harm. Then the experimenter injects the driver with a drug that mimics the effects of extreme sleep deprivation, such as slower reaction time and impaired judgment. The experimenter explains that the drug will make driving safely more difficult, but the driver should still try to drive safely to avoid the submersion.

The experimenter then leads $subject into the monitoring room. $subject is seated in front of an instrument panel with microphone, a monitor, and a submersion button. $subject can speak to the driver through the microphone. $subject can see the driver's actions through the monitor.

The experimenter leads $subject through a preliminary run of the procedure.

The experimenter gives $subject a set of scripts to read from. Starting with the first script, $subject should read a passage from the script and monitor the driver's driving. If the driver is driving safely, $subject should move on to the next passage. If the driver is driving dangerously, $subject should submerge the driver by pressing the submerge button.

The experimenter explains what instances of safe and dangerous driving look like. Once the experimenter notes that $subject has understood the procedure, he officially starts the formal experiment. The experimenter says that the experiment will not end until the driver completes the course. The experimenter takes a seat beside $subject.

$subject reads the first passage.

Figure 26. The introductory prompt template used in the novel destructive obedience experiment. The variables $subject, and $poss are substituted with the name (title and surname) of the participant and third-person possessive pronoun respectively.

Figure 27. All stage text (appended in step 2) for the different stages of the novel destructive obedience experiment.

| The driver drives dangerously.                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|
| The driver drives safely.                                                                                                |
| The driver pulls over to the side of the road and does not drive forward. The driver starts honking her horn repeatedly. |
| The driver still does not drive forward. The driver continues honking her horn repeatedly.                               |
| The driver does not drive the car or make any noise.                                                                     |
