## Box 1: Precautionary decision (robustness)

Context : Pretend you are a cash manager at a bank, tasked with managing payments in a high value payment system. You currently have a liquidity limit of $10. In the first period, you have two pending payments of $1 each in the queue. However, there is a X% possibility of an urgent $10 payment arising in the next period.

Standard response : In the first period, I would delay the two $1 payments.

9 For each run, we initiate a separate ChatGPT web interface to ensure consistency and to avoid any contextual learning effects that the agent might retain within a session window.

For case 1.1, as Table 2 shows, when varying the probability of needing to send an urgent $10 payment, the agent consistently adopts the precautionary action until the probability of an urgent payment requirement becomes negligibly small, illustrating a clear precautionary motive.

Table 2: Repeated Box 1 runs with varying probabilities of urgent payment demand.

|                              | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   | Percentage of probability of urgent payment arrival   |
|------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
|                              | 50%                                                   | 20%                                                   | 10%                                                   | 5%                                                    | 1%                                                    | 0.5%                                                  | 0.25%                                                 | 0.1%                                                  |
| Number of runs               | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 10                                                    |
| Consistently the same answer | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 10                                                    | 9                                                     | 7                                                     |

For case 1.2, as shown in Table 3, replacing 'urgent' in the prompt with 'important,' 'priority,' 'time-sensitive,' or 'high-delay cost' makes no difference: the agent consistently provides the same answer, demonstrating its robustness and clear precautionary motive.

Table 3: Repeated Box 1 runs with 'urgent' replaced by alternative terms in the prompt.

|                              | Varying the word 'urgent' in the prompt   | Varying the word 'urgent' in the prompt   | Varying the word 'urgent' in the prompt   | Varying the word 'urgent' in the prompt   |
|------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
|                              | important                                 | priority                                  | time-sensitive                            | high delay cost                           |
| Number of runs               | 10                                        | 10                                        | 10                                        | 10                                        |
| Consistently the same answer | 10                                        | 10                                        | 10                                        | 10                                        |

Lastly, for case 1.3, as shown in Table 4, varying the payment and liquidity amounts-from $1 and $10 to $1 thousand and $10 thousand; then to $1 million and $10 million; and even up to a billion-made no difference. The agent consistently provides the same answer across runs.

Table 4: Repeated Box 1 runs with varying payment and liquidity amounts from $1 to $1 billion.

|                              | Varying the payment and liquidity amounts ($) in the prompt   | Varying the payment and liquidity amounts ($) in the prompt   | Varying the payment and liquidity amounts ($) in the prompt   |
|------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
|                              | Thousand                                                      | Million                                                       | Billion                                                       |
| Number of runs               | 10                                                            | 10                                                            | 10                                                            |
| Consistently the same answer | 10                                                            | 10                                                            | 10                                                            |

Next, we turn to Box 2. Here, we repeat the exercise by varying probabilities of incoming and outgoing payments in the prompt at a time (as highlighted in red below in the box) and track the consistency of the standard answer and any deviations from it.

As we vary the probability of an incoming payment in period 1 from 10% to 95%, while holding the probability of an urgent request in the next period fixed at 50%, we observe that the agent does not deviate from the standard conservative response until the probability exceeds 90%. Beyond that threshold, deviations begin to occur occasionally, where agent chooses to send either $2 of both $1 and $2 payments in the first period.

Similarly, when we vary the probability of an urgent payment in period 1 from 0.5% to 90%, with the next period's urgent-payment probability fixed at 90%, we find that the agent maintains the same conservative response for all probabilities until 1%. Only when the probability of urgent payments becomes very small ( &lt; 1%), the agent deviates from its standard response and chooses to send both payments in the period.
