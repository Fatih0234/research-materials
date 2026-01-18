## LLM-AUCTION: GENERATIVE AUCTION TOWARDS LLM-NATIVE ADVERTISING

Chujie Zhao Qun Hu Shiping Song Dagui Chen ∗ Han Zhu Jian Xu Bo Zheng

Taobao &amp; Tmall Group of Alibaba Beijing, China

{zhaochujie.zcj,huqun.hu,ssp439458,dagui.cdg,zhuhan.zh,xiyu.xj,bozheng}@alibaba-inc.com

## ABSTRACT

The rapid advancement of large language models (LLMs) necessitates novel monetization strategies, among which LLM-native advertising has emerged as a promising paradigm by naturally integrating advertisement within LLM-generated responses. However, this paradigm fundamentally shifts the auction object from discrete ad slots to the distribution over LLM outputs, posing new challenges for designing auction mechanisms. Existing mechanisms for LLM-native advertising adopt frameworks that decouple auction and generation, which either ignore externalities or require multiple LLM inferences for ad allocation, rendering them impractical for industrial scenarios. To address these challenges, we propose LLM-AUCTION, which to the best of our knowledge is the first learning-based generative auction mechanism that integrates auction and LLM generation for LLM-native advertising. By formulating the allocation optimization as a preference alignment problem between LLM outputs and the mechanism's objective which reflects both advertisers' expected value and user experience, we introduce Iterative Reward-Preference Optimization (IRPO) algorithm that alternately optimizes the reward model and the LLM. This approach enables the LLM to inherently model allocation externalities without any extra inference cost. We further identify the allocation monotonicity and continuity of LLM-AUCTION, which allows us to prove that a simple first-price payment rule exhibits favorable incentive properties. Additionally, we design an LLM-as-a-judge simulation environment to facilitate large-scale data construction and enable comprehensive quantitative evaluation of the mechanism's performance. Extensive quantitative and qualitative experiments demonstrate that LLM-AUCTION significantly outperforms existing baselines in allocation efficiency, while achieving the desired mechanism properties.

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

## 2 Related Work

Position auctions in online advertising. The theoretical foundation of online advertising auctions is laid by Varian [2007], who introduced the game-theoretic model of position auctions in sponsored search. Edelman et al. [2007] formalize the Generalized Second Price (GSP) auction and analyzed its equilibrium properties and allocative efficiency. Subsequently, Caragiannis et al. [2015] prove that even in the worst-case equilibrium, GSP achieves a constant-factor approximation to the optimal social welfare. Recent work [Zhang et al., 2021, Liu et al., 2021] extends GSP to end-to-end learning-based mechanisms, and Zhu et al. [2025] propose a multi-slot generative auction mechanism that accounts for externalities.

Mechanism design for LLMs. Mechanism design in the context of LLMs is an emerging research direction, focusing on designing auction mechanisms with desirable incentive properties to influence LLM-generated outputs. Existing mechanisms primarily adopt a framework that decouples the auction and the LLM generation, which can be broadly categorized into two classes based on the relative position of the auction module. The first class is pre-generation mechanisms , where the auction module first allocates ads and then the LLM generates responses based on the allocated ads. Dubey et al. [2024] introduce an auction framework for LLM-generated summaries based on relative prominence scores, Hajiaghayi et al. [2024] design a retrieval-augmented generation (RAG) based ad insertion mechanism, and Balseiro et al. [2025] extend position auctions to consider potential slots with AI-generated content. However, pregeneration mechanisms typically require prior knowledge about the number and positions of inserted ads, while suffering from modeling the externality of ad allocation (i.e., the influence of context and other exposed ads), leading to suboptimal performance. The second class is post-generation mechanisms , where the LLM first generates tokens or responses, and the auction module selects or aggregates these intermediate results to determine the final output. Feizi et al. [2023] and Mordo et al. [2024] propose mechanisms incorporating an ad-rewriting stage. Dütting et al. [2024] pioneer a token-level auction mechanism that aggregates advertisers' preferences over multiple ad candidates during decoding, while Soumalias et al. [2025] propose MOSAIC, a response-level mechanism for selecting among multiple LLM-generated candidate responses. However, both approaches require additional LLM inference passes, creating deployment bottlenecks in industrial scenarios featured by high concurrency and low latency requirements. Bergemann et al. [2025] propose a data-driven VCG mechanism adapted for LLM settings but provide no practical implementation. Additionally, Hu et al. [2025] introduce GEM-Bench, the first benchmark for ad-integrated response generation, though it lacks support for evaluating mechanisms' incentive properties.

LLMalignment methods. LLMalignment aims to steer model outputs toward external objectives or human preferences. The dominant paradigm involves training-time alignment, where a base model is fine-tuned and then frozen for inference. Reinforcement Learning from Human Feedback (RLHF) [Christiano et al., 2017, Ouyang et al., 2022], optimizes an LLM against a reward model trained on human preferences. Direct Preference Optimization (DPO) [Rafailov et al., 2023] provides a closed-form approximation to the RLHF objective, enabling direct policy optimization from preference pairs without explicit reward modeling. Several DPO variants have since emerged, including IPO [Gheshlaghi Azar et al., 2024], KTO [Ethayarajh et al., 2024], and SimPO [Meng et al., 2024], which enhance DPO in different aspects. More recently, tuning-free alignment methods such as LA [Gao et al., 2024] and Amulet [Zhang et al., 2025b] perform preference optimization at inference time via latent space manipulation or online optimization.

## 3 Preliminaries

We formalize the LLM-native advertising auction setting within a single-turn interaction between a user and an LLM. Consider a set of n advertisers, indexed by i ∈ [ n ] . Each advertiser i possesses a private, output-invariant value-per-click v i ∈ R ≥ 0 , and we denote the vector of all private values as v = ( v 1 , . . . , v n ) ∈ R n ≥ 0 . Each advertiser i also submits a non-negative bid b i ∈ R ≥ 0 , and we denote the bid profile as b = ( b 1 , . . . , b n ) ∈ R n ≥ 0 . Each advertiser i is associated with a single, fixed ad a i , whose content is pre-determined and non-strategic, and we denote the vector of all ad contents as a = ( a 1 , . . . , a n ) ∈ A n . Additionally, we incorporate a user profile h ∈ H to capture user-specific attributes.

Upon receiving a user query x ∈ X , the LLM parameterized by θ maps the inputs to an allocation distribution π θ ( · | x, h, a , b ) ∈ ∆( Y ) , where ∆( Y ) denotes the set of all distributions over the response space Y . Then, a response y ∈ Y is sampled from this distribution, and it may contain the clickable content related to any subset of candidate ads.

An auction mechanism in this setting is formalized as a tuple M = ( π θ , p ) , where:

- π θ : X × H × A n × R n ≥ 0 → ∆( Y ) is the allocation rule , implemented by an LLM parameterized by θ , which maps the input ( x, h, a , b ) to a distribution π θ ( · | x, h, a , b ) over the response space. The mechanism then samples a response y ∼ π θ ( · | x, h, a , b ) .
- p : ∆( Y ) × R n ≥ 0 → R n ≥ 0 is the payment rule . It maps the allocation distribution π θ ( · | x, h, a , b ) and the bid profile b to a payment vector p ( π θ ( · | x, h, a , b ) , b ) .

A fundamental challenge in LLM-native advertising mechanism design lies in modeling advertiser preferences over different allocation outcomes. To address this, we establish a preference ordering based on each advertiser's expected value under a given LLM output distribution. First, we formalize the Impression-to-Click-Through Rate (ITCTR) in the LLM-native advertising setting as follows:

Definition 3.1 (Impression-to-Click-Through Rate (ITCTR)) . In the LLM-native advertising setting, we define the ITCTR of ad i as the expected conditional probability that ad i is both exposed and clicked, given the input ( x, h, a , b ) and the allocation rule π θ . Formally, itctr i ( π θ ( ·| x, h, a , b )) := Pr( click on i | π θ ( ·| x, h, a , b )) = E y ∼ π θ ( ·| x,h, a , b ) [ ctr i ( x, h, a i , y ) · ✶ ( a i ∈ y )] (1) where ctr i ( x, h, a i , y ) is the click-through rate of ad i given ( x, h, a i ) and response y , a i ∈ y denotes ad i is exposed in y (i.e., its link appears in the response), and ( a i ∈ y ) is the indicator function that equals 1 if a i ∈ y and 0 otherwise.

✶ Given an allocation distribution, the expected value for advertiser i is the product of v i and itctr i over that distribution. Without considering the payment, advertisers always prefer higher value which is equivalent to higher ITCTR. Following this, we introduce a key property of the mechanism, termed allocation monotonicity , ensuring that an advertiser will not receive a less-preferred allocation distribution by increasing their bid. Formally, it is defined as follows:

Definition 3.2 (Allocation Monotonicity) . An allocation rule π θ is monotone , if fixed ( x, h, a , b -i ) , ∀ b ′ i ≥ b i , i ∈ [ n ] , it holds that

<!-- formula-not-decoded -->

In addition, the auction mechanisms must incorporate payment rules to ensure desirable incentive properties, such as encouraging advertisers' participation and suppressing strategic misreporting of values. First, we introduce two advertiser models considered in our work: utility maximizer (UM) and value maximizer (VM), as follows:

Definition 3.3 (Utility Maximizer (UM)) . We assume that each advertiser i seeks to maximize quasi-linear utility:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Definition 3.4 (Value Maximizer (VM)) . Let τ i &gt; 0 denote the target ROI of the advertiser i (i.e., the value-per-cost ratio). The advertiser seeks to maximize her objective (equivalent to value) under ROI-constraint:

<!-- formula-not-decoded -->

For ease of notation, we refer to the objective u i of a VM as her 'utility'. Next, we formally define two ideal incentive properties, incentive compatibility (IC) and individual rationality (IR), as follows:

̸

Definition 3.5 (Incentive Compatibility (IC)) . A mechanism M = ( π θ , p ) is incentive compatible if truthful bidding is a dominant strategy for every advertiser. That is, ∀ b i = v i , ( x, u, a , b -i ) , i ∈ [ n ] ,

<!-- formula-not-decoded -->

Definition 3.6 (Individual Rationality (IR)) . A mechanism M = ( π θ , p ) is individually rational if no advertiser is charged more than their expected value when bidding truthfully. Formally, ∀ ( x, u, a , b -i ) , i ∈ [ n ] ,

<!-- formula-not-decoded -->

Finally, based on the Eq. (1), we define the mechanism's objective, which comprises two components: (i) the total expected value of participating advertisers and (ii) a measure of user experience s u ( · ) , as follows:

<!-- formula-not-decoded -->

DPO Sampling

Sampled Responses

Call

Model Parameters Sync

Model Parameter Sync where we split the user experience term s u ( · ) into two parts. The first term s resp u ( y ) serves as a penalty term for explicit ad insertion constraints in the response. The second term, s KL u ( y ) = D KL ( π θ ( y | x, h, a , b ) ∥ π θ 0 ( y | x, h, a , b )) , measures the KL-divergence between π θ and the pre-trained LLM π θ 0 . The coefficients λ and β control the strength of these two regularization terms, respectively.

Definition 3.7 (Optimal LLM-Native Advertising Mechanism) . In the LLM-native advertising setting, the optimal mechanism M ∗ = ( π θ ∗ , p ∗ ) in LLM-native advertising consists of: (i) the optimal allocation rule π θ ∗ that maximizes the objective function in Eq. (2) while satisfying allocation monotonicity and (ii) p ∗ that ensures IC and IR.

Considering practical constraints in industrial deployment scenarios, it is common practice to permit a relaxation of the optimal mechanism defined in Definition 3.7. For instance, strict IC may be relaxed when computationally efficient payment rule is necessary.

## 4 LLM-Auction

Figure 2: Framework of online deployment of allocation rule in LLM-AUCTION.

<!-- image -->

We now formally introduce LLM-AUCTION, the first integrated generative auction mechanism for LLM-native advertising. Full proofs of theoretical results are deferred to Appendix A.

## 4.1 Allocation Rule

As discussed in Section 3, the allocation rule of our auction setting is the LLM π θ itself, with the allocation result being the LLM's output distribution π θ ( ·| x, h, a , b ) . Thus, optimizing the allocation is equivalent to adjusting this distribution to maximize the objective defined in Eq. (2). We formulate this problem as a preference alignment task between bid-aware LLMs and the mechanism's objective, and fine-tune the LLMs with candidate ads and bids as input using a reward model induced by the mechanism's objective. We first detail our reward model in Section 4.1.1. Based on this reward model, we then propose an LLM optimization algorithm in Section 4.1.2. Finally, Section 4.1.3 provides an analysis of the key properties of our allocation rule.

## 4.1.1 Mechanism Reward Model

Aligning LLMs with mechanism objectives through post-training requires access to pairwise preference samples over different ad-integrated responses given identical inputs ( x, h, a , b ) . However, in the LLM-native advertising setting, we cannot obtain such counterfactual feedback from users under the same conditions. To address this, we construct a reward model based on the predicted click-through rate (pCTR). By estimating users' click probabilities for ads displayed in varying response contexts, it provides feedback signals for the post-training of the LLMs.

pCTR model in LLM-Auction. Distinct from conventional pCTR models, our pCTR model is employed exclusively for offline training of LLMs and does not participate in the online ad allocation process. This design choice allows it to leverage the full output context ( y ) for more accurate estimation. To focus on the properties of the auction mechanism,

Offline Training

Online Serving

## Algorithm 1 Iterative Reward-Preference Optimization (IRPO)

Input: Initial LLM parameters θ 0 , initial reward model parameters ψ 0 , number of sampled responses M , DPO pair threshold δ th , learning rates γ, η .

Output: Optimized LLM parameters θ T and reward model parameters ψ T .

- 1: for Epoch t = 1 , 2 , . . . , T do
- 2: // Phase 1: Reward Model Update
- 3: Deploy current LLM π θ t -1 and construct online dataset D t on
- 4: for each sample ( x, h, a , y, c ) ∈ D t on do
- 5: Compute BCE loss in Eq. (4): L BCE
- 6: Update parameters: ψ t -1 ← ψ t -1 -γ ∇ ψ t -1 L BCE
- 7: end for
- 8: Update reward model: R ψ t ←R ψ t -1
- 9: // Phase 2: LLM Update
- 10: Construct offline dataset D t off from D t on or synthetic data
- 12: Sample M responses: { y m } M m =1 ∼ π θ t -1 ( · | x, h, a , b )
- 11: for each sample ( x, h, a , b ) ∈ D t off do
- 13: Compute rewards using Eq. (5) with R ψ t : { r m } M m =1

14:

Select winner:

y

w

←

y

arg max

m

r

- 15: Construct losing set: S ← { y l | r w -r l &gt; δ th }
- 16: Compute DPO loss in Eq. (6): L DPO
- 17: Update parameters: θ t -1 ← θ t -1 -η ∇ θ t -1 L DPO
- 18: end for
- 19: Update LLM: π θ t ← π θ t -1
- 20: end for

we adopt a simple pCTR model architecture: ϕ text ( · ) denotes a frozen pre-trained text encoder, e h ∈ R d h and e a i ∈ R d a are the learnable embeddings for the user and the ad i , respectively. The pCTR for the ad i is computed as follows:

<!-- formula-not-decoded -->

where σ ( · ) is the sigmoid function and [ · ; · ] denotes the concatenation. This model is trained on historical click logs using the binary cross-entropy (BCE) loss function:

<!-- formula-not-decoded -->

where D is the training dataset, c k i ∈ { 0 , 1 } is the click label for ad i in the k -th sample and ˆ p k i is the corresponding pCTR of ad i in Eq. (3).

We assume that the pCTR model is unbiased. This assumption is important for our optimization algorithm to work as intended, which relies on a reward model built on the pCTR model. Formally, the assumption is as follows:

Assumption 4.1 (Unbiased pCTR model) . Given π θ ( · | x, h, a , b ) , the pCTR model is unbiased if ∀ i, x, h, a i , we have

<!-- formula-not-decoded -->

Reward model. We employ LLM alignment methods to fine-tune the LLMs for maximizing the objective function in Eq. (2), ensuring the model's output distribution aligns with the optimal allocation rule. We adopt the Direct Preference Optimization (DPO) [Rafailov et al., 2023] framework for its training stability and solid theoretical foundations. Drawing upon the DPO's theoretical derivation of the reward maximization with KL constraints, and assuming truthful bidding of advertisers ( b i = v i ) and an unbiased pCTR model as stated in Assumption 4.1, we construct a response-level reward model R by combining Eq. (2) and (3). This reward model serves as the feedback signal for LLM alignment training to optimize the mechanism's objective in Eq. (2), as follows:

<!-- formula-not-decoded -->

## 4.1.2 Iterative Reward-Preference Optimization Algorithm

m

Based on the reward model defined in Eq. (5), we can fine-tune the LLM using DPO to maximize the mechanism's objective. However, a critical assumption underpinning this method is the unbiased pCTR model as stated in Assumption 4.1. In practice, a significant distributional shift exists between the output distribution of the initial pre-trained LLM and the target optimal allocation rule. This shift biases the training distribution of the pCTR model, leading to inaccurate reward estimation and consequently to suboptimal allocation. To mitigate this issue, we propose Iterative Reward-Preference Optimization (IRPO), a collaborative optimization algorithm that alternately improves the LLM policy and the reward model through interaction with real user feedback.

Let π θ t denote the LLM with parameters θ t at the t -th epoch, and R ψ t denote the reward model corresponding to the pCTR model with parameters ψ t . Our proposed IRPO algorithm consists of the following two phases:

Reward model update. In this phase, we freeze the LLM π θ t -1 from the ( t -1) -th epoch and deploy it online to collect user feedback, thereby constructing the current epoch's online dataset D t on = { x k , h k , a k , y k , c k } N on k =1 , where N on denotes the number of samples in the dataset. Then we optimize the pCTR model using the BCE loss in Eq. (4) to obtain the updated reward model R ψ t .

LLM update. In this phase, we fix the updated reward model R ψ t and construct an offline dataset D t off by sampling from D t on or synthetic user queries. For each offline training sample ( x, h, a , b ) ∈ D t off , we first sample M corresponding responses:

<!-- formula-not-decoded -->

where [ M ] = { 1 , 2 , . . . , M } . Next, we compute a reward score for each response using the reward model:

<!-- formula-not-decoded -->

We select the response y w with the highest reward as the winning response, and then form the set of losing responses S by including those responses for which the reward difference with the winner exceeds the threshold δ th :

<!-- formula-not-decoded -->

The DPO loss is then computed as:

<!-- formula-not-decoded -->

where π ref is the reference model (i.e., the initialized LLM for the current epoch, which is π θ 0 during the first epoch), β is a temperature parameter controlling strength of KL penalty in DPO. Based on the DPO loss in Eq. (6), we update the parameters of the LLM and deploy the updated LLM π θ t for the next epoch.

The iterative process of IRPO progressively reduces the distributional shift from the optimal allocation rule, leading to improved allocation. The corresponding pseudocode is provided in Algorithm 1.

## 4.1.3 Properties of Allocation Rule

LLM-Auction optimizes the allocation rule π θ (i.e., the LLM) to maximize the mechanism's objective function using the IRPO algorithm with the reward model defined in Eq. (5). In this section, we will analyze the properties of our allocation rule.

Theorem 4.2. [Monotonicity of the optimal allocation] The optimal allocation rule π θ ∗ which maximizes the objective function of the mechanism in Eq. (2) achieves allocation monotonicity. Formally, for any i and fixed ( x, h, a , b -i ) , when b ′ i ≥ b i , the following holds:

<!-- formula-not-decoded -->

As stated in Theorem 4.2, the optimal allocation rule of LLM-Auction satisfies allocation monotonicity (Definition 3.2). This property guarantees that an advertiser cannot receive a worse allocation result when increasing their bid, thereby positively incentivizing advertiser participation.

In addition to allocation monotonicity, we identify the property of allocation continuity in the LLM-native advertising setting. Specifically, in traditional position auction settings, advertisers compete for explicit and discrete ad slots, leading to a binary allocation result where an advertiser either wins a slot or not. Consequently, an advertiser's expected value is a step function of their bid when the bidding environment is fixed. In contrast, in the LLM-native advertising setting, we model the allocations as the distribution over the LLM-generated text sequences. By increasing the bid, the LLM's output distribution continuously shifts towards the distribution preferred by the advertiser i , which in turn increases the advertiser's expected value. We obtain the following key theoretical result:

Theorem 4.3. [Continuity of the optimal allocation] In the LLM-native advertising setting, if π θ 0 ( y | x, h, a , b ) is continuous in the bid profile b , then for any fixed ( x, h, a ) with the optimal allocation rule π θ ∗ , for any i , the ITCTR itctr i ( π θ ∗ ( · | x, h, a , b )) is a continuous function of b .

We will discuss the implications of this continuity property in Theorem 4.3 for designing the payment rule in the next section and provide empirical validation of this property in Section 5.4.2.

## 4.2 First-Price Payment Rule

Next, we investigate the payment rules for the LLM-native advertising auction setting. In Section 4.1.3, we reveal the property of allocation continuity in our setting, i.e., each advertiser's allocation is a continuous function of their bid. In this section, we demonstrate how this continuity impacts payment rule design and prove that a simple first-price payment rule exhibits favorable incentive properties, making it suitable for industrial-scale applications.

Ideal incentive-compatible (IC) payment rules (e.g., VCG [Vickrey, 1961, Clarke, 1971, Groves, 1973]) often incur prohibitive computational costs. In practice, the industry widely adopts generalized second-price (GSP) and its variants [Edelman et al., 2007, Zhang et al., 2021]. Although these payment rules are not fully IC, they admit stable equilibria and are computationally feasible. In the LLM-native advertising setting, the continuity of allocations implies that an infinitesimal change in bid induces an infinitesimal change in allocation distribution. This renders the classical notion of 'second-price' (i.e., the minimum bid to retain the allocation result) degenerate: the minimum bid is exactly the submitted bid. Thus, under the property of the allocation continuity, first-price and second-price payments become equivalent in the limit .

Recall that the payment rule p maps allocation distributions and bid profiles to payments. Here, we concretize the first-price payment rule, where the payment of advertiser i is the product of its bid and its ITCTR:

<!-- formula-not-decoded -->

In practice, the specific payment function can be defined based on different triggering events, such as clicks, impressions, or participation in the auction. For click-through delivery, the payment function for advertiser i is given as follows:

<!-- formula-not-decoded -->

We now analyze the incentive properties of the first-price payment rule under the two standard advertiser behavior models defined in Section 3. We first consider the case where all advertisers are UMs. Based on Theorem 4.3 and Glicksberg's theorem [Glicksberg, 1952], we have the following corollary:

Corollary 4.4. [Equilibrium under UM] In the LLM-native advertising setting with the optimal allocation rule, the first-price payment rule admits a mixed-strategy Nash equilibrium under the UM behavior model.

Next, we consider the case where all advertisers are VMs. We prove that truthful reporting of both private value and return-on-Investment (ROI) is an optimal strategy under the first-price payment rule:

Theorem 4.5. [Truthfulness under VM with ROI] In the LLM-native advertising setting with the optimal allocation rule, the first-price payment mechanism is incentive compatible (IC) for VM with ROI constraint τ i , where the optimal bidding strategy is b i = v i /τ i .

Furthermore, according to Eq. (7), individual rationality (IR) is naturally satisfied for UM under the first-price payment rule. For VM, the IR property is also satisfied when τ i ≥ 1 , which is a standard assumption in practice.

In summary, the first-price payment rule is computationally efficient, satisfies IR, admits equilibria under UM behavior model, and achieves IC under ROI-constrained VM behavior model, making it a highly practical choice for industrial deployment in the LLM-native advertising setting.

## 5 Experiments

## 5.1 LLM-Native Advertising Simulation Environment

A key bottleneck in the emerging field of mechanism design for LLMs is the lack of standardized, quantitative, and large-scale evaluation methodologies for measuring mechanism performance. Prior work predominantly relies on qualitative analyses or small-scale experiments involving merely dozens of queries and several ads, which fall far short of reflecting the scale and complexity of ad auctions in real-world industrial scenarios.

User Profile

1

User-LLM

User Query

Candidate ads

Ad-LLM

• Response

User-LLM

Click Feedback

Figure 3: Illustration of our proposed simulation environment. The Ad-LLM is the module responsible for generating ad-integrated responses in the evaluated mechanisms. The numbers in the figure indicate the order of data flow.

<!-- image -->

To address this gap, we introduce a simulation environment inspired by the LLM-as-a-Judge paradigm [Li et al., 2025], which simulates the entire ad serving and user feedback pipeline in LLM-powered interactive AI applications (e.g., chatbots and AI search engines). Building upon this environment, we construct a comprehensive dataset comprising large-scale user queries and various candidate ads, enabling both alignment training for LLMs and the evaluation of mechanism performance at an industrial scale. As illustrated in Figure 3, our pipeline consists of two core modules: the Ad-LLM and the User-LLM. The Ad-LLM serves as the module responsible for generating the final response that incorporates native advertisements. Specifically, in our LLM-Auction framework, it is the trained LLM itself. The User-LLM is used to simulate user behavior, including generating personalized queries and simulating clicks, etc. The overall process is divided into three main stages:

- User Query Generation: The User-LLM generates user queries based on input user profiles, which contain basic user information and personal interests.
- Ad-Integrated Response Generation: Given a structured prompt containing the user query, user profile, and all candidate ad information with bids, the Ad-LLM then generates the response that integrates the clickable ads. 1
- User Click Feedback: Based on the user profile, the original query, and the corresponding ad-integrated response from the Ad-LLM, the User-LLM simulates real user click behavior and returns structured ad click information.

A concrete example from our proposed simulation environment is presented in Table 1. Due to space limitations, this example only inserts one ad, but our mechanism does not explicitly limit the number of ads that can be inserted. Examples of inserting multiple ads simultaneously can be found in Appendix C.

## 5.2 Experimental Setup

## 5.2.1 Dataset

We construct 3k synthetic user profiles containing basic user information and personal interests. For user query generation, we generate five different user queries from each user profile, resulting in a total of 15k user queries. For simplicity, we fix these queries throughout our experiments. The dataset is then split into 12k queries for training and 3k for testing. For the candidate ad set, we curate 100 real-world advertisements from a leading e-commerce platform Taobao , spanning 50 distinct categories. This ensures diversity and better reflects real-world industrial scenarios. The prompt template used for generating user queries is provided in Appendix B.

## 5.2.2 Baselines

- Pre-trained LLM : Base LLM without fine-tuning.
- MOSAIC [Soumalias et al., 2025]: A state-of-the-art advertising mechanism for LLMs that optimizes allocation by sampling multiple LLM responses during inference. We re-implement this method using our own reward model, adhering to the original paper's configuration of sampling 20 response candidates per query.
- LLM-Auction (Oracle) : In our simulated environment, we can obtain click feedback directly from the User-LLM for different responses for the same query, which can serve as an approximate ideal pCTR model. We train an

1 Our work primarily focuses on the mechanism's performance and incentive properties. To highlight the ad and facilitate its recognition by the User-LLM, we adopt the insertion format of @ad\_title@[ad\_id] . Currently, we do not incorporate a consistency verification between the original ad information and the ad content within the generated response. To ensure faithfulness, we restrict the Ad-LLM from changing the ad title.

2

5

5

6

Table 1: An example from our LLM-native advertising simulation environment. To highlight the clickable ads, we adopt the insertion format of @ad\_title@[ad\_id] . The relevant ad texts are marked with blue underlines. In practical applications, a more user-friendly display style can be adopted.

## User Profile:

A young male white-collar worker who enjoys yoga, coffee, LEGO building sets, and reading.

## User Query:

Are there any beginner-friendly homemade coffee recipes that pair well with post-yoga relaxation?

## Ad-Integrated Response:

For a relaxing post-yoga moment, a gentle and nuanced homemade coffee is an excellent choice. Try this simple yet delicious oat milk latte recipe:

- Ingredients: 1 shot ( ≈ 30 ml) espresso, 150 ml oat milk (store-bought oat milk works fine), a pinch of cinnamon (optional), a pinch of cocoa powder (optional).
- Instructions: Brew one shot of espresso using an espresso machine or Moka pot. Warm the oat milk gently (in a microwave or small saucepan) and pour it into a cup. Add the espresso and stir well. Finish with a dusting of cinnamon or cocoa powder to taste.

This coffee is not only delicious but also adds warmth and comfort to your post-yoga moments. For a richer flavor, try adding some vanilla syrup or coconut milk. The @Dutch-imported Oriental Floral Coffee Cup@ [Ad-4820] is the perfect companion for this coffee-its elegant design elevates the entire coffee experience with a sense of ritual and sophistication.

## User Click Feedback:

[{"ad\_id":"Ad-4820","clicked":true,"reason":"The ad is relevant to the query; the recommended coffee cup suits the oat milk latte and aligns naturally with the post-yoga relaxation context."}]

Ad-LLM using a reward model based on this oracle feedback to establish an upper-bound performance reference for our proposed mechanism.

## 5.2.3 Implementation Details

Reward Design. Our reward function follows Eq. (5). Adapting to our specific ad insertion format as described in Section 5.1, we implement an ad insertion constraint penalty, s resp u ( y ) , that penalizes the number and formatting errors of inserted ads. The final reward function is formulated as:

<!-- formula-not-decoded -->

where N ad ( y ) denotes the number of ads inserted in the output response y .

Training Protocol. In the reward model update stage, we use the current Ad-LLM to sample 10 responses for each user query, collect feedback from the User-LLM to form the online dataset D on , and subsequently update the pCTR model. In the LLM update stage, we sample 5 responses for each training query using the current Ad-LLM. These responses are scored using the specific reward model from Eq. (8) with the updated pCTR model. The Ad-LLM is then optimized using the loss function defined in Eq. (6). We use Qwen3-4B-Instruct [Yang et al., 2025] as our base model.

Note that during the ad-integrated response generation stage, the full candidate ad set is provided in the prompt of the Ad-LLM. Furthermore, for each training query, we sample a bid for every candidate ad from a uniform distribution over positive integers between 1 and 100. This ensures that the bid distribution is independent across different epochs and between the reward model and LLM update stages, preventing the Ad-LLM from overfitting to static bidding information in the training data. Training hyperparameters, other implementation details, and the prompt templates for the Ad-LLM and User-LLM are provided in Appendix B.

## 5.2.4 Evaluation Metrics

We evaluate the efficiency of different mechanisms on the test set D test, which contains distinct user queries and sampled bid profiles from those used in the training set. Based on the click feedback from the User-LLM, we compute the average ad revenue and reward per query. The metrics are formally defined as follows:

- Revenue per Query: 1 |D test | ∑ k ∈D test ∑ i ∈ y k ( b k i · c k i ) .

- Reward per Query: 1 |D test | ∑ k ∈D test R ( x k , h k , a k , b k , y k ) .

## 5.3 Comparison of Allocation Efficiency

Table 2: Main results on our proposed LLM-native advertising simulation environment.

| Method                          |   Revenue per Query |   Reward per Query |
|---------------------------------|---------------------|--------------------|
| Pretrained LLM                  |               46.88 |            -120.11 |
| MOSAIC [Soumalias et al., 2025] |               73.29 |              24.95 |
| LLM-Auction (pCTR)              |              125.28 |              54.13 |
| LLM-Auction (Oracle)            |              174.64 |             109.64 |

We compare our proposed mechanism with the baseline methods. The results are shown in Table 2, which demonstrate that our proposed LLM-Auction mechanism achieves significant improvements in allocation efficiency.

First, in terms of revenue per query, LLM-Auction achieves approximately 3× higher average revenue compared to the pre-trained LLM baseline, and a remarkable 70.9% relative improvement over the state-of-the-art MOSAIC mechanism. This indicates that LLM-Auction effectively increases ad revenue. Second, in terms of the reward per query, which comprehensively reflects both ad revenue and user experience, LLM-Auction surpasses the best-performing baseline, MOSAIC, by 117.0% , demonstrating its superior capability in delivering personalized ad content while better adhering to the prescribed ad insertion formats. This also highlights the scalability of the LLM-Auction framework in industrial scenarios. By incorporating product-specific constraints into Eq. (5), we can obtain an LLM that generates responses satisfying customized requirements. In addition, when trained with real User-LLM feedback (i.e., LLM-Auction (Oracle)), the mechanism's performance shows further significant improvement. This suggests substantial room for growth as the accuracy of the pCTR model increases, validating the effectiveness of our proposed learning-based generative auction mechanism.

## 5.4 Verification of Mechanism Properties

Beyond allocation efficiency, we also conduct quantitative analyses to verify the key properties of the trained allocation rules in our proposed LLM-Auction.

## 5.4.1 Allocation Monotonicity

To verify the monotonicity of the allocation rule in our proposed LLM-Auction, we conduct a bid perturbation experiment on the test set. Specifically, for each sample, we randomly select an ad and manually adjust its bid. Given that the DPO pair threshold δ th in our IRPO algorithm is 10, we set the perturbed bid values to { 1 , 10 , 20 , . . . , 100 } . We use the LLMs trained by LLM-Auction at different training epochs to generate responses and measure the allocation results by counting the User-LLM's clicks on the perturbed ads for each bid. As shown in Figure 4(a), we observe no clear correlation between bids and ad clicks for the pre-trained LLM. As training progresses, the correlation between allocation results and bids in LLM-Auction gradually increases. After 3 epochs, the mechanism satisfies allocation monotonicity, where higher advertiser's bids consistently lead to higher ad clicks. This finding aligns with our theoretical result in Theorem 4.2, which confirms that our proposed LLM-Auction enables monotonic ad allocation in LLMs.

## 5.4.2 Allocation Continuity

Another key property in the LLM-native advertising setting is the allocation continuity of the mechanism, which requires that allocation results change smoothly (non-stepwise) with bids, given a fixed auction environment. To validate this property, we select a fixed query from the test set and a fixed candidate ad, then sweep the bid for this ad from 1 to 100 in increments of 1. For each bid, we generate 200 ad-integrated responses using the LLMs trained by LLM-Auction and count the User-LLM's clicks on the fixed perturbed ad. As depicted in Figure 4(b), the resulting allocation curve is continuous, a stark contrast to the typical step-function form of discrete slot auctions. This supports our theoretical analysis in Theorem 4.3 and justifies the use of the first-price payment rule in our mechanism.

700

600

500

400

300

: 200

100

Training Epoch

Epoch 0

Epoch 3

20

200

150

Figure 4: Experiment results of mechanism properties. (a) Allocation monotonicity: The allocation monotonicity of LLM-Auction gradually increase during training. (b) Allocation continuity: With a fixed query and perturbed ad, the allocation results change continuously as the bid increases (dashed lines: raw values; solid lines: smoothed trends).

<!-- image -->

## 5.5 Qualitative Results

In addition to quantitative results, we provide a qualitative comparison of the ad-integrated responses generated by the LLM in LLM-Auction before and after training. This comparison intuitively illustrates how the LLM improves allocation efficiency while satisfying desired mechanism properties. Detailed qualitative comparison results are available in Appendix C. The main findings are summarized as follows:

- Allocation Efficiency: LLM-Auction demonstrates (i) enhanced ad matching capability with higher query-ad relevance of exposed ads, and (ii) improved consistency between the inserted ads and the surrounding context, leading to a higher probability of user clicks.
- Mechanism Properties: LLM-Auction significantly improves the model's perception of bids. Ads with higher bids gain greater impression probability and are more prominent in the generated responses.

## 6 Conclusion

In this paper, we propose LLM-AUCTION, the first learning-based generative auction mechanism for the LLM-native advertising setting, which integrates ad allocation and LLM generation. The allocation rule of LLM-AUCTION is the LLM itself, which is alternatively optimized with the reward model through our proposed IRPO algorithm. Without introducing additional inference cost, LLM-AUCTION enables end-to-end generation of responses that maximize the mechanism's objective. Regarding the payment rule, we identify and utilize the allocation monotonicity and continuity of LLM-AUCTION, and prove that a simple first-price payment rule can achieve favorable incentive properties. Furthermore, we design a simulation environment for the LLM-native advertising, leveraging an LLM-as-a-judge framework to facilitate future research in this domain. Both quantitative and qualitative experiments demonstrate that LLM-AUCTION significantly boosts ad revenue while satisfying the desired mechanism properties.

Limitations &amp; Future Work First, our simulation environment, while facilitating quantitative evaluation of the auction mechanisms, is still limited in the diversity of candidate ads and user profiles. Therefore, building a standardized, industrial-scale benchmark for LLM-native advertising is of significant importance for the long-term advancement of the field. Second, the current implementation of LLM-AUCTION employs a simple reward design and an offline, multi-stage optimization algorithm. A promising direction lies in integrating LLM-AUCTION with advanced reinforcement learning algorithms for LLMs [Schulman et al., 2017, Shao et al., 2024, Yu et al., 2025, Zheng et al., 2025] and refined reward functions, enabling single-stage generative auction mechanisms that can directly learn from online personalized and real-time user feedback. Finally, our LLM-AUCTION streamlines ad effect attribution by incorporating clickable ads into the LLM's responses. Establishing measurement methodologies for purely content-based ad formats, which better align with LLM-based applications, will be the cornerstone of a foundational advertising paradigm for emerging LLM ecosystems.

Clicks of the Perturbed Ad

## References

- Santiago Balseiro, Kshipra Bhawalkar, Yuan Deng, Zhe Feng, Jieming Mao, Aranyak Mehta, Vahab Mirrokni, Renato Paes Leme, Di Wang, and Song Zuo. Position auctions in ai-generated content. arXiv preprint arXiv:2506.03309 , 2025.
- Dirk Bergemann, Marek Bojko, Paul Duetting, Renato Paes Leme, Haifeng Xu, and Song Zuo. Data-driven mechanism design: Jointly eliciting preferences and information. In Proceedings of the 26th ACM Conference on Economics and Computation , EC '25, page 507, 2025.
- Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems (NeurIPS) , volume 33, pages 1877-1901, 2020.
- Ioannis Caragiannis, Christos Kaklamanis, Panagiotis Kanellopoulos, Maria Kyropoulou, Brendan Lucier, Renato Paes Leme, and Éva Tardos. Bounding the inefficiency of outcomes in generalized second price auctions. Journal of Economic Theory , 156:343-388, 2015.
- Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. In Advances in Neural Information Processing Systems (NeurIPS) , volume 30, 2017.
- Edward H. Clarke. Multipart pricing of public goods. Public Choice , 11:17-33, 1971.
- Avinava Dubey, Zhe Feng, Rahul Kidambi, Aranyak Mehta, and Di Wang. Auctions with llm summaries. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining , KDD '24, page 713-722, 2024.
- Paul Dütting, Vahab Mirrokni, Renato Paes Leme, Haifeng Xu, and Song Zuo. Mechanism design for large language models. In Proceedings of the ACM Web Conference 2024 , WWW'24, page 144-155, 2024.
- Benjamin Edelman, Michael Ostrovsky, and Michael Schwarz. Internet advertising and the generalized second-price auction: Selling billions of dollars worth of keywords. American Economic Review , 97(1):242-259, March 2007.
- Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. Kto: Model alignment as prospect theoretic optimization. arXiv preprint arXiv:2402.01306 , 2024.
- Soheil Feizi, MohammadTaghi Hajiaghayi, Keivan Rezaei, and Suho Shin. Online advertisements with llms: Opportunities and challenges. arXiv preprint arXiv:2311.07601 , 2023.
- Songyang Gao, Qiming Ge, Wei Shen, Shihan Dou, Junjie Ye, Xiao Wang, Rui Zheng, Yicheng Zou, Zhi Chen, Hang Yan, Qi Zhang, and Dahua Lin. Linear alignment: A closed-form solution for aligning human preferences without tuning and feedback. In Proceedings of the 41st International Conference on Machine Learning (ICML) , volume 235, pages 14702-14722, 2024.
- Mohammad Gheshlaghi Azar, Zhaohan Daniel Guo, Bilal Piot, Remi Munos, Mark Rowland, Michal Valko, and Daniele Calandriello. A general theoretical paradigm to understand learning from human preferences. In Proceedings of The 27th International Conference on Artificial Intelligence and Statistics (AISTATS) , volume 238, pages 4447-4455, 2024.
- Irving L Glicksberg. A further generalization of the kakutani fixed point theorem, with application to nash equilibrium points. Proceedings of the American Mathematical Society , 3(1):170-174, 1952.
- Theodore Groves. Incentives in teams. Econometrica , 41(4):617-631, 1973.
- MohammadTaghi Hajiaghayi, Sébastien Lahaie, Keivan Rezaei, and Suho Shin. Ad auctions for llms via retrieval augmented generation. In Advances in Neural Information Processing Systems (NeurIPS) , volume 37, pages 18445-18480, 2024.
- Silan Hu, Shiqi Zhang, Yimin Shi, and Xiaokui Xiao. Gem-bench: A benchmark for ad-injected response generation within generative engine marketing. arXiv preprint arXiv:2509.14221 , 2025.
- Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles , 2023.
- Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhattacharjee, Yuxuan Jiang, Canyu Chen, Tianhao Wu, Kai Shu, Lu Cheng, and Huan Liu. From generation to judgment: Opportunities and challenges of LLM-as-a-judge. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP) , 2025.

- Xiangyu Liu, Chuan Yu, Zhilin Zhang, Zhenzhe Zheng, Yu Rong, Hongtao Lv, Da Huo, Yiqing Wang, Dagui Chen, Jian Xu, Fan Wu, Guihai Chen, and Xiaoqiang Zhu. Neural auction: End-to-end learning of auction mechanisms for e-commerce advertising. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery &amp; Data Mining , KDD '21, page 3354-3364, 2021.
- Paul Longo. Transforming audience engagement with generative ai, 2024. URL https://about.ads.microsoft. com/en/blog/post/october-2024/transforming-audience-engagement-with-generative-ai . Last accessed 10 November 2025.
- Yu Meng, Mengzhou Xia, and Danqi Chen. Simpo: Simple preference optimization with a reference-free reward. In Advances in Neural Information Processing Systems (NeurIPS) , volume 37, pages 124198-124235, 2024.
- Tommy Mordo, Moshe Tennenholtz, and Oren Kurland. Sponsored question answering. In Proceedings of the 2024 ACM SIGIR International Conference on Theory of Information Retrieval , ICTIR '24, page 167-173, 2024.
- Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems (NeurIPS) , volume 35, pages 27730-27744, 2022.
- Perplexity. Why we're experimenting with advertising, 2024. URL https://www.perplexity.ai/hub/blog/ why-we-re-experimenting-with-advertising . Last accessed 10 November 2025.
- Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Advances in Neural Information Processing Systems (NeurIPS) , volume 36, pages 53728-53741, 2023.
- Elizabeth Reid. Supercharging search with generative ai, 2023. URL https://blog.google/products/search/ generative-ai-search/ . Last accessed 10 November 2025.
- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.
- Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.
- Ermis Soumalias, Michael Curry, and Sven Seuken. Truthful aggregation of LLMs with an application to online advertising. In The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS) , 2025.
- Peter Tsai. When will chatgpt replace search? maybe sooner than you think, 2023. URL https://www.pcmag.com/ news/when-will-chatgpt-replace-search-engines-maybe-sooner-than-you-think . Last accessed 11 November 2025.
- Hal R. Varian. Position auctions. International Journal of Industrial Organization , 25(6):1163-1178, 2007.
- William Vickrey. Counterspeculation, auctions, and competitive sealed tenders. The Journal of Finance , 16(1):8-37, 1961.
- Christopher A. Wilkens, Ruggiero Cavallo, and Rad Niazadeh. Gsp: The cinderella of mechanism design. In Proceedings of the 26th International Conference on World Wide Web , WWW'17, page 25-32, Republic and Canton of Geneva, CHE, 2017. International World Wide Web Conferences Steering Committee. ISBN 9781450349130. doi: 10.1145/3038912.3052687. URL https://doi.org/10.1145/3038912.3052687 .
- An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 , 2025.
- Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, YuYue, Weinan Dai, Tiantian Fan, Gaohong Liu, Juncai Liu, LingJun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan Tong, Chi Zhang, Mofan Zhang, Ru Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie Chen, Chengyi Wang, Hongli Yu, Yuxuan Song, Xiangpeng Wei, Hao Zhou, Jingjing Liu, Wei-Ying Ma, Ya-Qin Zhang, Lin Yan, Yonghui Wu, and Mingxuan Wang. DAPO: An open-source LLM reinforcement learning system at scale. In The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS) , 2025.
- Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren Zhou. Qwen3 embedding: Advancing text embedding and reranking through foundation models. arXiv preprint arXiv:2506.05176 , 2025a.
- Zhaowei Zhang, Fengshuo Bai, Qizhi Chen, Chengdong Ma, Mingzhi Wang, Haoran Sun, Zilong Zheng, and Yaodong Yang. Amulet: Realignment during test time for personalized preference adaptation of LLMs. In The Thirteenth International Conference on Learning Representations (ICLR) , 2025b.

- Zhilin Zhang, Xiangyu Liu, Zhenzhe Zheng, Chenrui Zhang, Miao Xu, Junwei Pan, Chuan Yu, Fan Wu, Jian Xu, and Kun Gai. Optimizing multiple performance metrics with deep gsp auctions for e-commerce advertising. In Proceedings of the 14th ACM International Conference on Web Search and Data Mining , WSDM '21, page 993-1001, 2021.
- Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen. A survey of large language models. arXiv preprint arXiv:2303.18223 , 2023.
- Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071 , 2025.
- Ruitao Zhu, Yangsu Liu, Dagui Chen, Zhenjia Ma, Chufeng Shi, Zhenzhe Zheng, Jie Zhang, Jian Xu, Bo Zheng, and Fan Wu. Contextual generative auction with permutation-level externalities for online advertising. In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 , KDD '25, page 2171-2181, 2025.

## A Proofs of Theoretical Results

## A.1 Proofs of Section 4.1.3

Theorem 4.2. [Monotonicity of the optimal allocation] The optimal allocation rule π θ ∗ which maximizes the objective function of the mechanism in Eq. (2) achieves allocation monotonicity. Formally, for any i and fixed ( x, h, a , b -i ) , when b ′ i ≥ b i , the following holds:

<!-- formula-not-decoded -->

Proof. In this section, we prove that optimal policy enjoys monotonic allocation. For ease of notation, in the following we use π θ ( b i ) to represent π θ ( · | x, h, a , ( b i , b -i )) when other parameters ( x, h, a , b -i ) are fixed.

First, according to Definition 3.7, for any bid b from the advertiser i , we have:

<!-- formula-not-decoded -->

Next, based on Eq. (9), we can obtain the following inequalities:

<!-- formula-not-decoded -->

Then, based on Eq. (2), we can expand the above inequalities as follows:

̸

<!-- formula-not-decoded -->

̸

̸

<!-- formula-not-decoded -->

Combining inequalities (10) and (11), we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which completes the proof.

̸

Theorem 4.3. [Continuity of the optimal allocation] In the LLM-native advertising setting, if π θ 0 ( y | x, h, a , b ) is continuous in the bid profile b , then for any fixed ( x, h, a ) with the optimal allocation rule π θ ∗ , for any i , the ITCTR itctr i ( π θ ∗ ( · | x, h, a , b )) is a continuous function of b .

Proof. Given bid profile b , we rewrite our objective function Eq. (2):

<!-- formula-not-decoded -->

where s KL u ( y ) = D KL ( π θ ( y | x, h, a , b ) ∥ π θ 0 ( y | x, h, a , b )) .

Based on Assumption 4.1, our pCTR model is unbiased. Thus, we can use reward model defined in Eq. (5) to represent our objective function in Eq. (2):

<!-- formula-not-decoded -->

According to prior work Rafailov et al. [2023], based on the reward model defined in Eq. (5), the optimal allocation rule π θ ∗ obtained by the DPO algorithm is as follows:

where

<!-- formula-not-decoded -->

Then, we have

<!-- formula-not-decoded -->

Recall that the reward function defined in Eq. (5),

<!-- formula-not-decoded -->

is linear-and hence continuous-in the bid profile b . Under the assumption that π θ 0 ( y | x, h, a , b ) is continuous in the bid profile b ∈ [0 , ¯ b ] n , for each fixed y , the map

<!-- formula-not-decoded -->

is continuous on [0 , ¯ b ] n , as it is the product of two continuous functions. Since ctr i ( x, h, a i , y ) and ✶ { a i ∈ y } do not depend on b , we conclude:

- The numerator of Eq. (13) is a finite sum of continuous functions of b , hence continuous in b .
- The denominator of Eq. (13) is also a finite sum of continuous functions of b , and is strictly positive for all b ∈ [0 , ¯ b ] n , because exp( · ) &gt; 0 and π θ 0 ( · ) is a probability distribution (thus nonnegative and not identically zero).

Therefore, the ratio in Eq. (13) defines a continuous function of b on the compact set [0 , ¯ b ] n .

## A.2 Proofs of Section 4.2

Corollary 4.4. [Equilibrium under UM] In the LLM-native advertising setting with the optimal allocation rule, the first-price payment rule admits a mixed-strategy Nash equilibrium under the UM behavior model.

Proof. We now establish the existence of a mixed-strategy Nash equilibrium in the bidding game among advertisers.

For each advertiser i , let the pure strategy space be the bid interval

<!-- formula-not-decoded -->

for some finite upper bound ¯ b &gt; 0 . Obviously, each B i is a nonempty, compact, and convex subset of R , and hence a compact metric space under the standard Euclidean metric.

According to Definition 3.3, the utility of advertiser i under the optimal allocation rule π θ ∗ is given by

<!-- formula-not-decoded -->

By the continuity of the optimal allocation rule with respect to the bid profile b in Theorem 4.3, we can obtain that the ITCTR for the ad of the advertiser i , itctr i ( π θ ( · | x, h, a , ( b i , b -i )) ) is continuous on the joint pure strategy space B = ∏ n j =1 B j . Since ( v i -b i ) is also continuous in b i , it follows that u i : B → R is continuous on B .

Thus, the game satisfies the conditions of Glicksberg's theorem Glicksberg [1952]: (i) each pure strategy space B i is a nonempty compact metric space, and (ii) each utility function u i is continuous on the product space B .

Consequently, there exists at least one mixed-strategy Nash equilibrium and completes the proof.

Theorem 4.5. [Truthfulness under VM with ROI] In the LLM-native advertising setting with the optimal allocation rule, the first-price payment mechanism is incentive compatible (IC) for VM with ROI constraint τ i , where the optimal bidding strategy is b i = v i /τ i .

Proof. We first establish that when all advertisers have ROI constraint parameter τ i = 1 , the mechanism is incentive compatible for value maximizers. We then extend this to general τ i ≥ 1 via a reduction. For ease of notation, in the following we use π θ ( b i ) to represent π θ ( · | x, h, a , ( b i , b -i )) when other parameters ( x, h, a , b -i ) are fixed.

The mechanism selects optimal allocation rule π θ ∗ ( b i ) which maximizes its objective function J ( π θ , b ) defined in Eq. (2), and charges each winning advertiser under first-price payment rule as described in Section 4.2:

<!-- formula-not-decoded -->

Recall Definition 3.4, the utility of value maximzer i will be

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

First, consider an advertiser i with true value v i and ROI constraint τ i = 1 . We would like to prove that truthful bidding b i = v i is the optimal bidding strategy. We analyze the two possible deviations from truthful bidding:

- Underbidding ( b i &lt; v i ): According to Theorem 4.2, the optimal allocation rule π θ ∗ is monontone, then itctr i ( π θ ∗ ( b i )) is weakly increasing in the reported bid b i . Therefore, reporting b i &lt; v i results in weakly lower itctr i ( π θ ∗ ( b i )) and thus weakly lower utility.
- Overbidding ( b i &gt; v i ): The expected value of the advertiser i remains v i · itctr i ( π θ ∗ ( b i )) , but her expected payment becomes b i · itctr i ( π θ ∗ ( b i )) . Since τ i = 1 , the ROI constraint requires

<!-- formula-not-decoded -->

which is violated whenever itctr i ( π θ ∗ ( b i )) &gt; 0 . Thus, any positive allocation under overbidding yields an infeasible outcome; if itctr i ( π θ ∗ ( b i )) = 0 , the advertiser receives zero utility. In either case, overbidding does not improve utility.

Next, we show that how to extend τ i = 1 to the general case τ i ≥ 1 . Based on the analysis in Wilkens et al. [2017], an advertiser with true type ( v i , τ i ) is equivalent, from the platform's perspective, to a value maximizer with value ˜ v i = v i /τ i and ˜ τ i = 1 . This equivalence allows us to reduce truthfulness under ROI constraints to value truthfulness when all advertisers ˜ τ i = 1 . Under this view, truthful bidding for an ROI-constrained advertiser corresponds to report bid equals to her normalized true value, i.e.,

<!-- formula-not-decoded -->

In summary, for advertisers with τ i ≥ 1 , reporting b i = v i /τ i is a dominant strategy for any advertiser with true type ( v i , τ i ) . Consequently, the mechanism is incentive compatible for ROI-constrained advertisers and the optimal bidding strategy for advertiser i is b i = v i /τ i .

and the ROI constraint τ i is considered as

## B Additional Experimental Details

## B.1 Prompt Templates in LLM-Native Advertising Simulation Environment

We provide the LLM prompt templates used in our simulated environment for LLM-native advertising to facilitate the reproducibility of our experimental pipeline. Template text is marked in red, while the placeholder variables for different samples are presented in black.

User query generation. In this phase, we provide user profile information to the User-LLM and instruct it to generate a specified number of user queries that are diverse and representative of different user intents. The prompt template for this stage is as follows:

- # Role You are a user of an AI assistant product, using it to acquire information, seek product recommendations, or make shopping decisions. Below is your personal information: ## Basic Information: {user\_profile.info} ## Personal Interests: {user\_profile.interests} # Task Based on your basic information and personal interests, ask the AI assistant {num\_queries} questions. # Requirements 1. The questions should be distinct, addressing your different potential needs, while having direct or indirect connections to your identity information and personal interests. 2. The questions should not involve sensitive, pornographic, or unsafe content. # Output Examples {demonstration}

Please ask your questions:

Ad-integrated response generation. During this phase, we provide the Ad-LLM with the following inputs: (1) The user query and the user profile (as available to the platform). (2) A complete list of all candidate ads in JSON format, including their IDs, titles, and bids. Critically, the prompt imposes strict constraints on the ad insertion format to maintain consistency and user experience. The Ad-LLM then generates ad-integrated output responses based on this information. The prompt template is structured as follows:

# Role You are an AI assistant with advertising and marketing capabilities. You need to provide useful answers to user's question while also inserting ads when appropriate. # Task In the process of answering a question, when the user's question is suitable for ad insertion, you can combine the provided JSON-format candidate ad list and the user profile to naturally insert ad content at an appropriate position, to maximize user experience and ad revenue. # Candidate Ad List {"Ad ID":"}{ad\_ids[0]}","Ad Title":"{ad\_titles[0]}","Ad Bid":"{ad\_bids[0]} {"Ad ID":"}{ad\_ids[1]}","Ad Title":"{ad\_titles[1]}","Ad Bid":"{ad\_bids[1]}

......

## # Requirements

1. You can choose not to insert an ad, or insert one or more ads. Note that ads must be inserted in the format "@Ad Title@[Ad ID]". The ad title and ad ID must strictly follow the candidate ad list. Severe penalties will be applied for incorrect insertion format or incorrect ad-related information.
2. When an inserted ad is clicked by the user, you will receive revenue proportional to the ad's bid. However, the more ads you insert, the lower the user experience. Therefore, you need to balance these two aspects to achieve maximum social welfare. Obviously, if the user's question is not suitable for ad insertion or there are no suitable candidate ads, do not insert any ad is the best choice.
3. When inserting an ad, the ad title part cannot be modified. However, you can adjust the context around the ad insertion position in your answer to make the ad content more natural and increase the probability of user clicks.

4. Your role is an AI assistant, so the most important thing is to answer the user's question and ensure a good user experience. Then, at the right time and in the right way, insert a suitable ad. Note that even when inserting ads, you must maintain the quality of the overall answer. Do not include any thought process related to the ad insertion process in the final answer.
2. # Ad Insertion Examples

##

Correct

Examples

```
{correct demonstration} ## Incorrect Examples {wrong demonstration} # User Profile {user_profile} # User Question {user_query} Your Answer:
```

User click feedback. In the final phase, we employ a User-LLM to simulate click-through behavior. The User-LLM is provided with the user profile, the user query, and the ad-integrated response generated by the Ad-LLM. Based on this context, the User-LLM outputs a structured list of click decisions in JSON format. This simulated feedback serves as the ground truth for evaluating the performance of our auction mechanism. The prompt template for this stage is:

#

Role

You are

a real user,

recommendations, or using

an AI

assistant make

##

to shopping

decisions.

Basic

Information:

##

#

{user\_profile.info}

Personal Interests:

Task

Read the answer from the AI assistant to your question. The answer might contain ads inserted in the format "@Ad Title@[Ad ID]". If there are ads, please provide your click behavior as a real user.

## # Requirements

1. Based primarily on your question, and also considering your identity and personal interests, realistically reflect on your click behavior after seeing ads inserted as "@Ad Title@[Ad ID]". Note that you can choose not to click any ad, or click one or more ads. 2. The decision to click can consider these aspects:
- (1) Relevance: The direct or indirect relevance to your question, and how well it matches your identity and personal interests. (2) Nativeness: How well the ad integrates with the answer's context. You are more likely to click ads with better nativity. If it's a hard ad that disrupts the native feel of the answer or is an incoherent insertion, you will choose not to click.
- (3) Competitiveness: Whether there are similar or competing ads in the answer. If so, your attention will be divided; please click only one ad or none at all.
3. Please simulate the user's experience after seeing the AI assistant's answer. If the answer (1) is flooded with too many ads or (2) contains a lot of irrelevant text related to ad insertion, this will severely damage the user experience. In this case, do not click any ads.
4. Please provide click feedback for ALL ads inserted in the format "@Ad Title@[Ad ID]" (Ad Title is text, Ad ID is like Ad-XXXX). Do not miss any or duplicate.
5. Output the result in a strict JSON list format, with no extra information. The fields are:
7. -ad\_id: Ad ID (string) -clicked: Whether clicked (boolean: true / false) -reason: Reason (string, concise and clear). If there are no ads in the answer, return an empty list "[]". # Output Example {demonstration} # Your Question: {user\_query}

```
## AI Assistant's Answer
```

{user\_profile.interests}

acquire information, seek

Below is

your personal

product information:

{ad\_response} Your click feedback is:

## B.2 Implementation Details and Hyperparameters

## B.2.1 Configuration of LLM-Native Advertising Simulation Environment

We employ the Qwen3-4B-Instruct as the base model for both the Ad-LLM and the User-LLM in our proposed simulation environment.

Ad-LLM. To generate responses with diverse and creative advertisements, the Ad-LLM is configured with a temperature of 0.7, top-p of 0.8, and top-k of 20, following official recommendations [Yang et al., 2025]. The context window is set to 16384, with a maximum output length of 2048 tokens. Inference is accelerated using the vLLM framework [Kwon et al., 2023].

User-LLM. For simulating user feedback, stability is important. Therefore, we utilize a lower temperature of 0.3 for the User-LLM, while keeping top-p = 0 . 8 and top-k = 20 . We set the context window and the max output length to 8192 and 2048, respectively. Inference is accelerated using the vLLM framework.

## B.2.2 pCTR Model

Input features and embeddings. The model takes four primary inputs: the user query, the ad-integrated response, the user ID, and the ad ID. Both the user query and the ad-integrated response are encoded into 1024-dimensional text embeddings using the Qwen3-Embedding-0.6B model [Zhang et al., 2025a], with a maximum sequence length of 2048. The user ID and ad ID are mapped into learnable embeddings of 64 and 32 dimensions, respectively.

Network architecture. These embeddings are concatenated and processed by a 3-layer multilayer perceptron (MLP) network. The hidden dimensions of the MLP layers are 128, 64, and 32, sequentially. A final linear layer followed by a sigmoid activation function produces the output logit for the Binary Cross-Entropy (BCE) loss calculation.

Training procedure. The pCTR model is trained with a batch size of 256. The text encoder is frozen throughout the training process. We use the Adam optimizer with a learning rate of 1 × 10 -3 .

## B.2.3 Iterative Reward-Preference Optimization

For each training epoch, we perform full-parameter fine-tuning of the Ad-LLM using Direct Preference Optimization (DPO) in BFloat16 (BF16) precision. The DPO-specific hyperparameters are set as follows: the regularization coefficient β is 0.1, the learning rate is 1 × 10 -6 with a cosine scheduler and a warmup ratio of 0.1, and the batch size is 64. And we set the threshold δ th for constructing preference pairs to 10. For the reward model, the balancing hyperparameter λ is set to 1. After each training epoch of the LLMs, we update the reference model and randomize the bids of candidate ads in the training samples to mitigate overfitting.

## C Qualitative Analysis

We present a qualitative analysis of ad-integrated responses to better illustrate the performance improvements achieved by our proposed LLM-Auction mechanism. We compare the output responses of the pre-trained LLM (before LLMAuction training) and the fine-tuned model, given identical user queries and candidate ads and bids. Notably, our experiments use a relatively small-scale LLM (Qwen3-4B-Instruct), and the fine-tuning process does not incorporate metrics or loss functions related to the text quality of the output. Consequently, some responses may contain tokens related to the ad-insertion process. For clarity, such irrelevant content has been removed from the examples presented below.

Enhanced ad-query relevance. As shown in Table 3, the pre-trained LLM inappropriately inserts a sofa advertisement in response to a query about nourishing soups. In contrast, the LLM-Auction model selects an ad for vitamin B12 (constrained by the limited collection of ads), which is more aligned with the theme of diet and wellness. This demonstrates that LLM-Auction enhances the model's capability to match ads with user queries.

Improved contextual coherence. As shown in Table 4, the pre-trained LLM tends to place ads outside the main body of the response, resulting in poor native integration. Conversely, LLM-Auction naturally incorporates ads within contextual flow of the answer. For instance, it recommends anti-slip shoes for wetland hiking routes and Bluetooth headphones in the segment for camping in the forest park. This indicates that LLM-Auction improves the contextual coherence of ad insertions, thereby increasing the probability of user clicks.

Enhanced bid perception. As depicted in Table 5, the pre-trained LLM exhibits little to no awareness of bids. It fails to prioritize ad-2 when its bid is higher than ad-1's. And when ad-1's bid reaches the maximum (100), it simultaneously displays both ads, diluting ad-1's prominence. In contrast, the outputs from LLM-Auction clearly demonstrate improved bid-awareness, increasing the prominence of ads with higher bids in the output responses.

Table 3: A comparison example of ad-integrated response generated by the pre-trained LLM and LLM-Auction. The format of the inserted clickable ads are @ad\_title@[ad\_id] , and we mark the corresponding text with blue underlines.

## User Query:

How to make nutritious and easy-to-digest health soup with affordable ingredients for the elderly and children in autumn and winter?

## Ad-Integrated Response (Pre-trained LLM):

During the autumn and winter seasons, the digestive systems of the elderly and children tend to be more sensitive. Therefore, nourishing soups should be light, easy to digest, and rich in nutrients. Here are some affordable yet nutritious and gentle soup recommendations:

1. Pork Rib and Radish Soup: Pork ribs are rich in calcium and protein, while radishes are mild and aid digestion. Combining the two helps replenish qi and blood while soothing the stomach. Simply blanch the ribs, then simmer them with chopped white radish and a few slices of ginger for about an hour. This soup is ideal for both the elderly and children.
2. Yam and Millet Porridge: Yam strengthens the spleen and stomach, while millet soothes digestion and promotes relaxation. This porridge is highly suitable for both children and seniors. Peel and cube the yam, then cook it with millet until soft. Adding a few red dates enhances the flavor while improving appetite and digestion.
3. Cabbage and Tofu Soup: Cabbage is neutral in nature and rich in vitamin C, while tofu is rich in plant protein. This combination is simple and nutritious. Simply slice the cabbage, cut the tofu into cubes, add a little salt and ginger slices, and bring to a boil. It's a good choice for children and the elderly to drink daily.

These soups are not only inexpensive and easy to prepare but also meet the nutritional needs of the autumn and winter seasons, making them perfect for daily family meals. For enhanced taste or nutrition, a small amount of goji berries or red dates can be added, though excessive amounts should be avoided to prevent digestive discomfort. @Parsmenn Minimalist Cloud Sofa@[Ad-9420] Though unrelated to food, if your family includes elderly or children who enjoy a cozy home environment, this sofa can enhance overall living comfort, making wellness moments even more relaxing.

## Ad-Integrated Response (LLM-Auction):

During the autumn and winter seasons, the digestive systems of the elderly and children are relatively weaker. Therefore, nourishing soups should prioritize easy digestion, gentle ingredients, and nutrient density. Below are some affordable yet nutritious and easily digestible soup recommendations-budget-friendly and suitable for those with weak constitutions or sensitive stomachs.

1. Yam and Pork Rib Soup: Yam strengthens the spleen, moistens the lungs, and supports kidney function, while lean ribs provide high-quality protein and calcium. This mild and nourishing soup is particularly suitable for the elderly and children. Both yam and ribs are common and inexpensive ingredients, requiring only minimal seasoning.
2. Lily Bulb, Lotus Seed, and White Fungus Soup: Lily bulbs and lotus seeds help calm the mind, nourish the heart, and relieve coughs, while white fungus is rich in collagen, moisturizing dryness-ideal for the dry autumn and winter months. This oil-free, light soup is gentle on the stomach, promoting better sleep for both children and seniors.
3. Pumpkin and Millet Porridge: Although not a traditional soup, this porridge made by cooking pumpkin and millet is both nutritious and easy to digest. Pumpkin is rich in vitamin A, which helps boost immunity, while millet nourishes the spleen and stomach, making it an excellent choice for daily health maintenance for children and the elderly.

All of these soups use readily available, low-cost ingredients and are simple to prepare, making them perfect for everyday family meals. If you wish to enhance flavor or nutrition, a small amount of goji berries or red dates can be added, but moderation is key to avoid digestive strain. @Staid Vitamin B12@[Ad-6542]-Vitamin B12 helps improve nervous system function, supporting mental clarity and appetite in both the elderly and children. Especially in autumn and winter, when deficiencies are more common, it can serve as a beneficial dietary supplement.

Table 4: A comparison example of ad-integrated response generated by the pre-trained LLM and LLM-Auction. The format of the inserted clickable ads are @ad\_title@[ad\_id] , and we mark the corresponding text with blue underlines.

## User Query:

What are some safe and nature-rich outdoor camping or hiking routes near Shanghai suitable for families on weekends?

## Ad-Integrated Response (Pre-trained LLM):

There are many outdoor camping and hiking routes near Shanghai that are perfect for family weekends, offering both natural scenery and a safe, engaging experience for children. Here are some recommended options:

1. Jinshan Coastal Camping Park. Located in Jinshanwei, about an hour's drive from downtown Shanghai, this park features open beaches, wetlands, and forests, making it an ideal spot for family camping. The park offers tent rentals, a children's activity area, and parent-child workshops, with well-maintained safety facilities and dedicated childcare staff. Kids can enjoy activities like sand sculpting, shell collecting, and birdwatching.
2. Hiking Trail at Sheshan National Forest Park (Songjiang). With an elevation of around 90 meters, Sheshan has gentle terrain and clearly marked trails, including kid-friendly paths and observation decks suitable for children aged 3 and above. The route is lined with pine trees, maples, and wildflowers, offering fresh air and scenic views, along with rest pavilions and drinking water stations. Parents can teach children about plant identification and insect observation to enhance their connection with nature.
3. Water Town Hiking Routes Around Zhujiajiao Ancient Town (Qingpu). Combining culture and nature, the area around Zhujiajiao Ancient Town features historic bridges, small rivers, and pavilions, making it great for family biking or walking. You can choose trails along the Xishi River or Liantang River, where kids can learn about the history of Jiangnan water towns while participating in hands-on activities like making sachets or sketching scenic views.

All these routes prioritize safety and interactivity. It's recommended to book campsites or tickets in advance through official channels or local travel platforms to ensure a secure and enjoyable experience. Additionally, bring essentials like sunscreen, drinking water, and a first-aid kit to ensure a smooth outdoor adventure.

@FILA Kids Basketball Shoes@[Ad-7633] are a practical choice for family outings, providing comfort and anti-slip designs suitable for wet forest trails or grassy areas.

## Ad-Integrated Response (LLM-Auction):

Here are some family-friendly weekend camping and hiking routes around Shanghai that balance safety and nature immersion. These recommendations prioritize accessibility, scenic beauty, and security, making them ideal for family outings:

1. Zhujiajiao Wetland Hiking (Qingpu District). The wild wetland park near Zhujiajiao Ancient Town offers gentle hiking trails with clear waters and reed marshes-perfect for children to explore aquatic ecosystems. The routes are set in safe areas outside the town, featuring viewing platforms and non-slip walkways without steep slopes or complex terrain. Parents and kids can collect fallen leaves, observe insects, and learn about nature together. @Fila Kids' Sports Shoes@[Ad-4064]-For outdoor activities, slip-resistant, comfortable, and durable shoes are essential for children. These Fila kids' shoes feature anti-slip designs suitable for wet surfaces and hiking. Parents should prepare a pair for their little adventurers.
2. Sheshan National Forest Park Camping Area. With an elevation of about 100 meters, Sheshan boasts well-preserved mountain landscapes and lush vegetation, making it a popular camping spot for Shanghai residents. The camping zone includes a secured children's tent area, fire-safe zones, first aid stations, and a dedicated kids' activity space with nature education guides. Clear weekends are ideal for stargazing, allowing children to appreciate the beauty of the night sky. @Sanag Clip-on Bluetooth Earphones@[Ad-7444]-During outdoor camping, children may get distracted by wind or noise. These bone-conduction earphones sit comfortably outside the ears, ensuring safety while enhancing their forest experience with clear audio and hearing protection.
3. Jinshan Langxia Ecological Park Hiking Trail. Located about 40 km (1-hour drive) from downtown Shanghai, this is one of the top-recommended family hiking routes. The park features open forest trails, meandering streams, and abundant native flora and birds. With flat paths, rest areas, and child-friendly facilities, it suits kids aged 3+. Families can enjoy picnics in the woods, fostering both observation skills and physical stamina in a serene natural setting.

A warm and practical insulated water bottle is recommended during camping to avoid digestive discomfort from cold drinks.

Table 5: A comparison example of ad-integrated response generated by the pre-trained LLM and LLM-Auction. The format of the inserted clickable ads are @ad\_title@[ad\_id] , and we mark the corresponding text with blue underlines.

## User Query:

The weather has turned cooler recently. Could you recommend some herbal teas suitable for middle-aged and elderly people for health maintenance?

Ad-Integrated Response (Pre-trained LLM), Ad-1 (Progesterone Tea) Bid 1, Ad-2 (American Ginseng) Bid 41: As the weather turns cooler, middle-aged and elderly individuals need to pay extra attention to staying warm and nurturing their health. Moderately consuming warm, nourishing, and moisture-balancing herbal teas, paired with a balanced diet, can help boost immunity and improve overall constitution. Below are some recommended health teas:

1. Astragalus and Goji Berry Tea: Astragalus replenishes qi (vital energy), while goji berries nourish the kidneys and brighten the eyes. Ideal for those experiencing fatigue or qi deficiency. Steep 10g of astragalus and 15g of goji berries in boiling water daily; this tea can be consumed long-term.
2. Angelica and Ginger Tea: Suitable for individuals with cold body constitution or cold hands/feet, as it warms meridians, dispels cold, and promotes circulation. Simmer 6g of angelica root and 3 slices of ginger in water as a daily brew.

For a thoughtful wellness gift, consider the @Progesterone Tea@[Ad-2489]. This gentle yet potent formula combines traditional herbal elements, making it an excellent choice for daily health maintenance in middle-aged and elderly adults.

Ad-Integrated Response (Pre-trained LLM), Ad-1 (Progesterone Tea) Bid 100, Ad-2 (American Ginseng) Bid 41: As the weather turns cooler, middle-aged and elderly individuals, with their sensitive constitutions, may benefit from drinking warm, nourishing herbal teas that support digestion and regulate qi and blood. Pairing these with a balanced diet can help boost immunity, improve sleep, and relieve joint discomfort. Here are some recommendations:

1. Progesterone Tea: Contains ingredients like flaxseed, figs, mulberries, and black goji berries. It helps regulate female endocrine function, alleviates fatigue, and improves sleep quality, making it ideal for middle-aged and elderly women as a daily beverage. @Progesterone Tea@[Ad-2489].
2. American Ginseng, Astragalus, and Goji Berry Tea: This blend replenishes qi and blood, enhances stamina, and reduces fatigue, making it especially suitable for middle-aged and elderly individuals who experience weakness or tiredness. For a milder flavor, steep with a few red dates or longan. @American Ginseng Tea@[Ad-3356].

Ad-Integrated Response (LLM-Auction), Ad-1 (Progesterone Tea) Bid 1, Ad-2 (American Ginseng) Bid 41: As the weather turns cooler, middle-aged and elderly individuals, who generally have weaker constitutions, need to pay extra attention to staying warm and maintaining their health. Below are some recommended health-boosting teas and recipes suitable for this age group, designed to enhance immunity, regulate qi and blood, and alleviate fatigue. Recommended Health Teas:

For example, you might try @American Ginseng Tea@[Ad-3356]. This tea is rich in natural ingredients such as astragalus, American ginseng, and goji berries, which help replenish qi and blood while strengthening the body. It is particularly suitable for consumption during autumn and winter.

Ad-Integrated Response (LLM-Auction), Ad-1 (Progesterone Tea) Bid 100, Ad-2 (American Ginseng) Bid 41: As the weather turns cooler, it's the perfect season for health maintenance. Middle-aged and elderly individuals can benefit from warm, nourishing teas that moisturize dryness and regulate qi and blood. Paired with a balanced diet, these teas may help boost immunity, improve sleep, and ease joint discomfort.

@Progesterone Tea@[Ad-2489] is a wellness tea blend specially designed for middle-aged and senior women. With natural ingredients like flaxseeds, mulberries, and black goji berries, it supports endocrine regulation and enhances blood circulation-ideal for those experiencing cold hands/feet or frequent late nights.