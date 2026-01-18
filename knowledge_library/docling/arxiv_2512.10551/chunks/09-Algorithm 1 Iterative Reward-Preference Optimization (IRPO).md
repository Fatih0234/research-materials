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
