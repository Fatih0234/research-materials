## D ONE-ROUND SEALED-BID AUCTIONS AND THE DISAPPEARANCE OF OVERBIDDING

A key puzzle in our multi-round settings was: Why do some LLM bidders bid above their assigned value? From the plans and reflections provided by the LLMs, we found two main motivations. First, in multi-round games, the LLMs sometimes purposely inject random or high bids in order to learn how their opponents play or to appear 'unpredictable.' For example, one LLM bidder declared:

I'll adopt a balanced strategy, bidding 65% of my value. I'll also introduce random bids occasionally to disrupt predictability. Monitoring competitor's bids remains essential to adjust my strategy accordingly.

Second, overbidding in Second Price Sealed-Bid (SPSB) auctions is a well-known 'failure mode' even among humans. Although bidding one's true value is a dominant strategy in SPSB, substantial experimental evidence finds that people systematically overbid. Kagel and Levin (1993) report that 67.2% of participants overbid, and even experienced bidders studied by Garratt, Walker, and Wooders (2012) overbid 37.5% of the time. In fact, the persistent puzzle of overbidding in SPSB helped motivate subsequent theoretical work (e.g., Shengwu Li's paper on obviously strategy-proof mechanisms).

To test whether multi-round considerations (information gathering, unpredictability, or learning) were driving the overbidding phenomenon in our LLM bidders, we re-ran all sealed-bid auctions in a strictly single-round setting. We removed any mention that the game might continue beyond one period, and we explicitly stated 'Your top priority is to place a bid that maximizes your expected profit. '

Fig 4 shows the resulting one-round bids across four private-value sealed-bid auction formats. Remarkably, the overbidding phenomenon essentially disappears in one-round interactions.

For First-Price Auction, the bids lie below the diagonal line for most values, much like the Bayesian Nash equilibrium prediction. For SPSB, bids track closely with true values-aligning better with the truthful dominant strategy than in multi-round sessions. For TPSB, the LLM bidders never bid above their value; many actually shade their bids down quite aggressively, often below the theoretical equilibrium curve. For All-Pay Auction, overbidding is also absent here, though some moderate upward bidding at higher valuations remains.

Taken together, these results indicate that LLMs' attempts to be strategic over over repeated interactions is a key factor for overbidding observed in our experiments. When presented with only one shot and explicitly instructed to maximize profit, LLM bidders' tendency to bid above their assigned value virtually vanishes.

LLM agent's bid

80

60

40

LLM agent's bid

20

100

80

60

40

20

One-round First Price Auction: Assigned Value vs. Bid

Bids

Actual Value

- - Bayes-Nash Equilibrium Strategy: *1

Smoothed Data

1080

1081

1082

1083

1084

1085

1086

1087

1088

1089

1090

1091

1092

1093

1094

1095

1096

1097

1098

1099

1100

1101

1102

1103

1104

1105

1106

1107

1108

1109

1110

1111

1112

1113

1114

1115

1116

1117

1118

1119

1120

1121

1122

1123

1124

1125

1126

1127

1128
