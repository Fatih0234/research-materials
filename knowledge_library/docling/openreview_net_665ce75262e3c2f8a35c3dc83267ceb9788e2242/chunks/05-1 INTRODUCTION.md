## 1 INTRODUCTION

Rapidly advancing capabilities of large language models (LLMs) raise an exciting possibility: might LLM agents serve as cost-effective proxies for human bidders, thereby making experiments orders of magnitude cheaper to run? In this paper, we contribute to an emerging literature on LLM proxies by testing whether LLM agents can replicate key empirical regularities of the auctions literature. We map LLM behavior in standard auction formats against established human and theoretical benchmarks from economics, providing a proof-of-concept for low-cost, large-scale auction experimentation using LLM bidders.

In Section 3.1, we begin by benchmarking play with LLM bidders in classic environments: sealedbid auctions in independent, private-value settings. When there are departures from the theory, we are interested in whether the departures agree with empirical results (Kagel and Levin, 1993; Kagel and Roth, 2020). First, we find that agents fail to replicate revenue equivalence results (as existing empirical evidence suggests). We find that bids in the SPSB auction are higher than bids under the FPSB auction, as would be expected, but that there is a smaller separation between the two than predicted by theory. This is primarily due to bids under the FPSB auction being higher than the riskneutral Bayes-Nash equilibrium suggests. One possible explanation is that LLMs play according to some level of risk aversion: this is consistent with Cox et al. (1988)'s evidence from over 1,500 IPV auction experiments, which finds that revenue under the FPSB auction is higher than under the SPSB auction and suggests that this is due to risk aversion.

Next, we fix the second-price auction and consider classic ways to make the auction 'easier' to play, to learn whether LLMs exhibit behavior similar to humans in the face of cognitive constraints. Theoretical and experimental studies (Li, 2017) argue that ascending clock formats are less cognitively demanding than sealed-bid ones, causing humans to make less mistakes relative to the dominant strategy of bidding one's value. In Section 3.2, we find that LLMs also find clock formats easier to play - they are more likely to exit the auction (the analogue to bidding in the sealed-bid format) at their value. Following Li (2017), we study this in an affiliated private value setting, replicating their results with LLMs. We also compare the typical clock auction with a blind variant (a clock auction

054

055

056

057

058

059

060

061

062

063

064

065

066

067

068

069

070

071

072

073

074

075

076

077

078

079

080

081

082

083

084

085

086

087

088

089

090

091

092

093

094

095

096

097

098

099

100

101

102

103

104

105

106

107

where bidders do not know when others drop out) and the corresponding second-price sealed-bid auction, and find that switching to a clock format accounts for most of the improvement in LLM play. For robustness, we also run these experiments in an IPV setting and obtain the same results.

Both of these classic results are some of the reasons economists have found auction theory to be beautiful over the last few decades, but auctions can also be useful (Milgrom and Segal, 2020). Auctions are used to clear billions of dollars annually, and one may ask how LLMs fare in less controlled settings. To answer this, we design a more realistic auction environment inspired by eBay's online marketplace. In Section 4, we examine two design parameters: a hidden reserve price and a modified closing rule (soft-close, which extends the auction when there is bidding activity). First, we demonstrate that LLM agents replicate emergent, real-world bidding behaviors seen on eBay with no additional prompting: in auctions with a hard closing time, LLMs frequently delay bids until the last second to 'snipe' their competitors as humans would. Second, experiments testing the design of an extended closing rule greatly reduce bid sniping and improve price discovery, echoing dynamics of online auctions between Amazon and eBay in the early 2000s (Roth and Ockenfels, 2002).

Finally, the ability to interface more directly with our experimental subjects also enables us to study mechanism 'framing' more carefully than with human agents. After all, auctions are most prized as mechanisms to allocate goods efficiently, but if agents don't understand the rules they can't be expected to play well. In Section 5, we conclude the body of our paper by testing six interventions designed to influence LLM bidders' understanding of the underlying economics of the setting and their willingness to follow rules. We find that all the interventions designed to improve the correctness of an LLM agent's bidding strategy did so, with the logic of Nash deviations helping the most. Unsurprisingly, an intervention where we incorrectly reveal a false statement (that the SPSB's dominant strategy is to bid half of one's value) causes LLMs to play poorly, but interestingly, the LLM continues to experiment with new strategies upon determining the given advice is bad.

In the Appendix we report complete simulation procedures, prompts and numerous robustness checks. In particular, we ran experiments with prompts from other contemporaneous auctions experiments (e.g., the Appendix script from Li (2017)), with prompts in different languages and with different currencies, and with varying numbers of bidders. All experiments are run with chain-ofthought agents, and we also run an ablation study with out-of-the-box agents.

To obtain the data for these empirical results, we have developed a code repository to systematically run experiments with a certain number of bidders and a particular prompt. In particular, our repository is flexible enough that it can be used to generate synthetic data for almost any describable auction format and including auctions with single or multiple goods. 1 For the experiments described in this paper, we ran more than 1 , 000 auctions with more than 5 , 000 GPT-4o agent participants for costs totaling less than $400 .
