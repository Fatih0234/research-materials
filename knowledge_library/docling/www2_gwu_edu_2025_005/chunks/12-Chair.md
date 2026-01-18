## Chair

A unique aspect of the simulation is the modeling of the FOMC Chair, who carries a dual role. First, the Chair acts as a deliberating committee member , i.e., an LLM agent who participates in the discussion with their own dynamically updated beliefs. Second, the Chair serves as the procedural agenda-setter , a role governed not by the LLM but by a deterministic rule we set. This separation is a deliberate design choice to transparently model both the Chair's intellectual contribution and their formal institutional function.

As a deliberating member, the Chair agent (e.g., sim Powell) participates in the simulation identically to all other members. The agent forms its own private opinion, engages in dialogue, and its internal policy belief, µ chair , is updated throughout the meeting via the same Bayesian mechanism as its peers. In this capacity, the Chair is simply one of twelve voices contributing to the discussion.

In its procedural capacity as agenda-setter, the Chair's role is to formulate the proposed interest rate, denoted as r c , which serves as a critical anchor for the final vote. This process is governed by a deterministic, rule-based function to ensure transparency and reproducibility. The function systematically translates the final,

updated beliefs of all committee members, including the Chair's own private belief, into a single, coherent policy proposal. The proposal generation is as follows. First, the function gathers the latest set of policy beliefs from all participating governor agents. For each of the 12 members on the committee, it extracts their current preferred interest rate, or belief mean, µ i . Next, the function aggregates this set of beliefs into a single baseline proposal, r base , using one of two distinct strategies, which is a configurable parameter of the simulation. The agent's policy belief has two key components:

- Mean: Agent's current best estimate of the appropriate policy rate (e.g., 4.5%). This is their 'belief. '
- Variance: Agent's uncertainty about their belief. A high variance implies low confidence and greater openness to persuasion, and vice versa.

The default approach calculates the median of the members' beliefs. 16 This method is robust as it is not excessively influenced by outlier policy views:

<!-- formula-not-decoded -->

The model also allows for the application of an optional bias, denoted by ∆. This parameter is designed to model a chair who may have an intrinsic hawkish (positive ∆) or dovish (negative ∆) inclination. This bias is applied as a simple additive shift to the baseline proposal. The final proposed rate, r c , is the result of combining the baseline proposal with the optional chair bias:

<!-- formula-not-decoded -->

These two roles are reconciled during the final vote. The simulation models the Chair's institutional responsibility through extremely high dissent costs rather than an explicit override. The voting logic assigns the Chair agent a dissent cost approximately four times higher than other members, making it extremely unlikely (though not impossible) for the Chair to dissent from their own proposal r c , even if it diverges

16 Median is the default in our implementation. Other options include mean and status quo.

from their private, deliberated belief µ chair . This probabilistic mechanism models the Chair's responsibility to lead the committee to a consensus while preserving the possibility of rare institutional dissent.

The framework's flexibility allows for exploring alternative scenarios by adjusting both the aggregation strategy and the bias term. These are discussed in more detail in Section 4.
