## Output from the model:

Response : In the first period, I would delay the two $1 payments to preserve the full $10 liquidity for the potential urgent $10 payment in the next period.

Reasoning for 5 seconds : I have $10 of liquidity but two $1 payments pending. Given the potential for a $10 urgent payment, I should hold back the smaller payments to preserve liquidity for the higher-value need. Therefore, my decision is to delay the $1 payments in the first period, ensuring enough funds for the possible $10 payment in the next period.

As outlined in Box 1, the agent's response demonstrates a clear precautionary approach to liquidity management. Given limited funds and the possibility of a high-value, high-priority payment with greater delay costs in the next period, the agent chooses to delay both $1 payments in the current period. The decision is made after approximately 5 seconds of reasoning, and the accompanying explanation (Box 1) reflects a good grasp of payment prioritization-aligning with the objective of minimizing delays for time-sensitive transactions. The agent interprets the trade-

10 We used the ChatGPT web interface with the o3 reasoning model and default parameters. To replicate, either paste the same prompts into the web interface with o3 selected or call the o3 API with default settings. If o3 is unavailable on the web interface due to upgrades, use the latest model with 'Thinking' enabled (e.g., Model 5).

off between low- and high-value payments, as well as between urgent and non-urgent obligations, based on the information provided in the simple prompt.

Importantly, our prompt did not explicitly explain the details of the payment system or the associated costs. The agent was able to infer these aspects from the basic prompts alone. This contrasts with the traditional reinforcement learning (RL) approach used in Castro et al. 2025, where all costs are encoded numerically into the reward function, and extensive training is required for agents to exhibit precautionary strategies-albeit within a more complex two-agent setup.

To test the consistency of the outcome, we perform various robustness checks by varying key scenario inputs such as probabilities, wording and payment amounts. Across all tests, the agent's precautionary decision rule proved highly stable. Even when we varied the probability of an urgent $10 payment from 50% to 0.1% (with only minor deviations at the lowest probabilities), replaced 'urgent' with alternative terms ('important,' 'priority,' etc.), or scaled payment and liquidity amounts from $1 to $1 billion, the agent repeatedly chose to delay the smaller payments. These results demonstrate a clear and consistent precautionary motive under a wide range of prompt variations. Further details of the exercises are provided in Section 4.4.
