## 1 Introduction

The rapidly developing technology of large language models (LLMs) [Zhao et al., 2023, Brown et al., 2020] has the potential to change the ecosystem of online services, such as search and recommendation [Tsai, 2023], by powering applications like chatbots and AI-driven search engines. While LLMs offer a more efficient way to acquire information, training and deploying advanced models is costly. Therefore, providing online advertising services has become a consideration for AI platforms to balance their expenses. Initial industrial efforts have predominantly adopted external ad placements, such as fixed slots appended to the model's output [Perplexity, 2024, Longo, 2024, Reid, 2023]. This paradigm fails to exploit the core capabilities of LLMs in reasoning and generation, leaving the natural integration of advertising content into the generation process an open challenge.

Unlike external ad placements, promotional content embedded in the generated response with native text style can better utilize the understanding and generation capabilities of LLM, while balancing ad revenue and user experience. This paradigm has drawn increasing attention in the research community, and we term it LLM-native advertising . In contrast to the conventional position auction setting, the object of the auction in the LLM-native advertising is no longer explicit, discrete ad slots, but rather the distribution of the LLMs' output. In this new setting, advertisers bid to influence

* Corresponding author.

Help me plan a 5-day trip from New York to Hawaii.

User Query

LLM

Candidate

Ads &amp; Bids

Auction

Traditional Mechanisms

Response

Day 1: Arrival in Honolulu take ~11 hours.

•Direct flahts from wre

• Check into your hotel in

(b) Post-Generation Mechanism

Ad-integrated Response tere's a suggested itinerary

for your Hawaii adventure:

Day 1: Arrival in Honolulu flights from NYC

• Direct take ~11 hours.

• Check-in at Hotel X:

Figure 1: Comparison of ad formats and auction mechanisms in LLM-based AI applications.

<!-- image -->

this distribution, thereby increasing the likelihood that their desired content is integrated into the generated response. This fundamental shift renders classic mechanisms derived from position auction setting, such as the Generalized Second-Price (GSP) auction [Edelman et al., 2007], no longer applicable. Consequently, there is an urgent need for new auction mechanisms tailored to the LLM-native advertising setting.

Recent pioneering work has proposed several auction mechanisms for LLM-native advertising, mainly adopting a framework that decouples the auction and the LLM generation [Dütting et al., 2024, Soumalias et al., 2025, Hajiaghayi et al., 2024, Dubey et al., 2024]. These approaches can be categorized into pre-generation and post-generation mechanisms, as shown in Figure 1. Pre-generation mechanisms first allocate ads through an auction module, and then the LLM generates a response based on the allocated ads. Such mechanisms preset the number of ads to insert and fail to account for externalities, leading to suboptimal performance. Conversely, post-generation mechanisms require the LLM to generate tokens or responses conditioned on candidate ads, followed by a selection- or aggregation-based auction on these intermediate results to determine the final output. These mechanisms incur additional LLM forward-pass inference costs that scale with the number of competing advertisers or candidate responses, rendering them impractical for large-scale industrial scenarios characterized by high concurrency and low latency requirements.

To address these challenges, we propose LLM-AUCTION, the first learning-based generative auction mechanism that integrates auction and LLM generation for LLM-native advertising. Specifically, we formulate the allocation optimization problem as a preference alignment task, where the LLM is post-trained to align its output with a mechanism's objective that balances ad revenue and user experience, conditioned on the candidate ads and their bids. We introduce an LLM-response-based click-through rate (CTR) estimation model to construct a reward model that aligns with the mechanism objective, thereby providing preference feedback for the LLM's fine-tuning. To bridge the distributional gap of allocation outputs between the pre-trained and the optimal LLM, which biases the reward model, we propose Iterative Reward-Preference Optimization (IRPO) algorithm to iteratively optimize the reward model and the LLM for better performance. Through this post-training paradigm, the LLM itself serves as the allocation rule, implicitly modeling externalities without incurring additional inference costs, making our approach highly practical. For the payment rule, we identify and leverage the property of allocation monotonicity and continuity in LLM-AUCTION, proving that a simple first-price payment rule exhibits favorable incentive properties under both utility maximizers (UM) and value maximizers (VM) with Return-on-Investment (ROI) constraints.

Additionally, inspired by the LLM-as-a-judge paradigm [Li et al., 2025], we design a simulation environment spanning from user query generation and ad-integrated response generation to user click feedback, facilitating quantitative evaluation of auction mechanisms in LLM-native advertising. It supports both training data construction and comprehensive evaluation of mechanism performance. Extensive experiments demonstrate that LLM-AUCTION significantly outperforms existing baselines in ad revenue while satisfying key mechanism properties.

Our main contributions are summarized as follows:

- Welay down general definitions and desired incentive properties of the auction mechanism design for the LLM-native advertising, establishing foundations for future work in this setting.
- We propose LLM-AUCTION, the first learning-based generative auction mechanism for the LLM-native advertising. Our mechanism aligns LLMs with mechanism's objective through a theoretically-grounded reward model, integrating ad allocation and content generation. We further identify the allocation monotonicity and continuity of LLM-AUCTION, and prove that a simple first-price payment rule exhibits favorable incentive properties.

Located just steps from

Waikiki.

User Query

(1) Decoupled Auction-Generation Mechanism

(a) Pre-Generation Mechanism

LLM

- We design an LLM-as-a-judge simulation environment for the LLM-native advertising auction mechanisms, facilitating large-scale data construction and mechanism performance evaluation.
