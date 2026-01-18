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
