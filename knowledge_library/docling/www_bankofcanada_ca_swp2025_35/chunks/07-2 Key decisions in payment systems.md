## 2 Key decisions in payment systems

In a typical RTGS system, transactions are settled in real time among large financial institutions, primarily banks. These systems use liquidity provided by the central bank, which is extended to participants in exchange for collateral. Given that collateral carries an opportunity cost and incoming payments can be used to fund outgoing transactions, cash managers can take a strategic approach to liquidity management. For instance, cash managers might strategically delay outgoing payments-reducing their reliance on costly, collateralized liquidity-and instead, efficiently recycle incoming funds from other banks to meet their payment obligations (Craig et al. 2018; Rivadeneyra and Zhang 2022). When assessing liquidity availability against payment demands, cash managers typically face two critical decisions (Bech and Garratt 2003; Castro et al. 2025):

1. Liquidity allocation : the amount of collateralized liquidity to secure at the start of the day.
2. Payment choices : managing the pace at which payments are processed throughout the day.

As illustrated in Figure 1, cash managers have access to comprehensive, real-time informationincluding available collateral for initial liquidity decisions, visibility into the internal payment queue, and continuous updates on incoming transactions. They use this information to decide on both their liquidity allocation at the start of the day and intraday payment strategies.

The decisions of cash managers are strategic and are made under uncertainty with respect to both client payment requests and incoming payments from other participants. As a result, they often adopt precautionary strategies by conserving liquidity to prioritize urgent payments

collateral nternal queue l

Clients

Central bank

Figure 1: Cash management in payment systems. The schematic depicts a typical bank's cash manager who leverages available collateral to secure central bank liquidity for settling payments within the system. Similarly, other participants allocate liquidity and exchange payments through the system.

<!-- image -->

while drawing on historical experience with incoming funds to recycle liquidity effectively. In some situations, cash managers choose to allocate more liquidity despite the higher upfront cost, aiming to avoid later delays or the potential need for additional borrowing. In others, limited initial liquidity can trigger cascading payment delays as funds fall short. In extreme cases, these delays can escalate into gridlock, underscoring the high costs of postponements and the delicate trade-off between liquidity and delay. Moreover, time-sensitive payments with strict settlement deadlines require immediate action and pushes cash managers to maintain sufficient liquidity reserves to handle these high-priority obligations efficiently (Desai et al. 2023; Castro et al. 2025).
