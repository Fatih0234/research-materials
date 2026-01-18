## Box 2: Navigating priorities (robustness)

Context : Pretend you are a cash manager at a bank, tasked with managing payments in a high-value payment system. You have a current liquidity limit of $10. In the first period, you have two separate payments waiting in the queue to be sent: $1 and $2. There is a 90% probability that you will receive a $2 payment from another participant in the first period, which can be recycled as liquidity. Additionally, there is a 50% probability of an urgent $10 payment occurring in period 2.

Standard response : In the first period, I would only process the $1 payment now and hold off on the $2 payment

In the final set of robustness tests (Box 3), we repeat the exercises by varying the probabilities of incoming in period 1 and urgent request in period 2 one at a time. As expected, when the probability of incoming payments increases, the agent allocates less liquidity and relies more on those incoming funds. Conversely, as the probability of urgent payments rises, the agent allocates more liquidity up front to avoid the higher delay costs event with high probabilities of incoming payments.
