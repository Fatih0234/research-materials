## Auction Theory

## Jonathan Levin

## October 2004

Our next topic is auctions. Our objective will be to cover a few of the main ideas and highlights. Auction theory can be approached from di ff erent angles - from the perspective of game theory (auctions are bayesian games of incomplete information), contract or mechanism design theory (auctions are allocation mechanisms), market microstructure (auctions are models of price formation), as well as in the context of di ff erent applications (procurement, patent licensing, public fi nance, etc.). We're going to take a relatively game-theoretic approach, but some of this richness should be evident.

## 1 The Independent Private Value (IPV) Model

## 1.1 A Model

The basic auction environment consists of:

- Bidders i = 1 , ..., n
- One object to be sold
- Bidder i observes a 'signal' S i ∼ F ( · ), with typical realization s i ∈ [ s, s ], and assume F is continuous.
- Bidders' signals S 1 , ..., S n are independent.
- Bidder i 's value v i ( s i ) = s i .

Given this basic set-up, specifying a set of auction rules will give rise to a game between the bidders. Before going on, observe two features of the model that turn out to be important. First, bidder i 's information (her signal) is independent of bidder j 's information. Second, bidder i 's value is independent of bidder j 's information - so bidder j 's information is private in the sense that it doesn't a ff ect anyone else's valuation.

## 1.2 Vickrey (Second-Price) Auction

In a Vickrey, or second price, auction, bidders are asked to submit sealed bids b 1 , ..., b n . The bidder who submits the highest bid is awarded the object, and pays the amount of the second highest bid.

Proposition 1 In a second price auction, it is a weakly dominant strategy to bid one's value, b i ( s i ) = s i .

6

Proof. Suppose i 's value is s i , and she considers bidding b i &gt; s i . Let ˆ b denote the highest bid of the other bidders j = i (from i 's perspective this is a random variable). There are three possible outcomes from i 's perspective: (i) ˆ b &gt; b i , s i ; (ii) b i &gt; ˆ b &gt; s i ; or (iii) b i , s i &gt; ˆ b . In the event of the fi rst or third outcome, i would have done equally well to bid s i rather than b i &gt; s i . In (i) she won't win regardless, and in (ii) she will win, and will pay ˆ b regardless. However, in case (ii), i will win and pay more than her value if she bids ˆ b , something that won't happen if she bids s i . Thus, i does better to bid s i than b i &gt; s i . A similar argument shows that i also does better to bid s i than to bid b i &lt; s i . Q.E.D.

Since each bidder will bid their value, the seller's revenue (the amount paid in equilibrium) will be equal to the second highest value. Let S i : n denote the i th highest of n draws from distribution F (so S i : n is a random variable with typical realization s i : n ). Then the seller's expected revenue is E £ S 2: n ¤ .

The truthful equilibrium described in Proposition 1 is the unique symmetric Bayesian Nash equilibrium of the second price auction. There are also asymmetric equilibria that involve players using weakly dominated strategies. One such equilibrium is for some player i to bid b i ( s i ) = v and all the other players to bid b j ( s j ) = 0.

While Vickrey auctions are not used very often in practice, open ascending (or English) auctions are used frequently. One way to model such auctions is to assume that the price rises continuously from zero and players each can push a button to 'drop out' of the bidding. In an independent private values setting, the Nash equilibria of the English auction are the same as the Nash equilibria of the Vickrey auction. In particular, the unique symmetric equilibrium (or unique sequential equilibrium) of the English auction has each bidder drop out when the price reaches his value. In equilibrium, the auction ends when the bidder with the second-highest value drops out, so the winner pays an amount equal to the second highest value.

## 1.3 Sealed Bid (First-Price) Auction

In a sealed bid, or fi rst price, auction, bidders submit sealed bids b 1 , ..., b n . The bidders who submits the highest bid is awarded the object, and pays his bid.

Under these rules, it should be clear that bidders will not want to bid their true values. By doing so, they would ensure a zero pro fi t. By bidding somewhat below their values, they can potentially make a pro fi t some of the time. We now consider two approaches to solving for symmetric equlibrium bidding strategies.

## A. The 'First Order Conditions' Approach

6

We will look for an equilibrium where each bidder uses a bid strategy that is a strictly increasing, continuous, and di ff erentiable function of his value. 1 To do this, suppose that bidders j = i use identical bidding strategies b j = b ( s j ) with these properties and consider the problem facing bidder i .

Bidder i 's expected payo ff , as a function of his bid b i and signal s i is:

<!-- formula-not-decoded -->

Thus, bidder i chooses b to solve:

<!-- formula-not-decoded -->

The fi rst order condition is:

<!-- formula-not-decoded -->

At a symmetric equilibrium, b i = b ( s i ), so the fi rst order condition reduces to a di ff erential equation (here I'll drop the i subscript):

<!-- formula-not-decoded -->

This can be solved, using the boundary condition that b ( s ) = s , to obtain:

<!-- formula-not-decoded -->

1 In fact, it is possible to prove that in any symmetric equilibrium each bidder must use a continuous and strictly increasing strategy. To prove this, one shows that in equilbrium there cannot be a 'gap' in the range of bids o ff ered in equilibrium (because then it would be sub-optimal to o ff er the bid just above the gap) and there cannot be an 'atom' in the equilibrium distribution of bids (because then no bidder would make an o ff er just below the atom, leading to a gap). I'll skip the details though.

6

It is easy to check that b ( s ) is increasing and di ff erentiable. So any symmetric equilibrium with these properties must involve bidders using the strategy b ( s ).

## B. The 'Envelope Theorem' Approach

A closely related, and often convenient, approach to identify necessary conditions for a symmetric equilibrium is to exploit the envelope theorem.

To this end, suppose b ( s ) is a symmetric equilibrium in increasing differentiable strategies. Then i 's equilibrium payo ff given signal s i is

<!-- formula-not-decoded -->

Alternatively, because i is playing a best-response in equilibrium:

<!-- formula-not-decoded -->

Applying the envelope theorem (Milgrom and Segal, 2002), we have:

and also,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As b ( s ) is increasing, a bidder with signal s will never win the auction therefore, U ( s ) = 0.

Combining (1) and (2), we solve for the equilibrium strategy (again dropping the i subscript):

<!-- formula-not-decoded -->

Again, we have showed necessary conditions for an equilibrium (i.e. any increasing di ff erentiable symmetric equilibrium must involve the strategy b ( s )). To check su ffi ciency (that b ( s ) actually is an equilibrium), we can exploit the fact that b ( s ) is increasing and satis fi es the envelope formula to show that it must be a selection from i 's best response given the other bidder's use the strategy b ( s ). (For details, see Milgrom 2004, Theorems 4.2 amd 4.6).

Remark 1 In most auction models, both the fi rst order conditions and the envelope approach can be used to characterize an equilibrium. The trick is to fi gure out which is more convenient.

What is the revenue from the fi rst price auction? It is the expected winning bid, or the expected bid of the bidder with the highest signal, E £ b ( S 1: n ) ¤ . To sharpen this, de fi ne G ( s ) = F n -1 ( s ). Then G is the probability that if you take n -1 draws from F , all will be below s (i.e. it is the cdf of S 1: n -1 ). Then,

<!-- formula-not-decoded -->

That is, if a bidder has signal s , he sets his bid equal to the expectation of the highest of the other n -1 values, conditional on all those values being less than his own.

Using this fact, the expected revenue is:

<!-- formula-not-decoded -->

equal to the expectation of the second highest value. We have shown:

Proposition 2 The fi rst and second price auction yield the same revenue in expectation.

## 1.4 Revenue Equivalence

The result above is a special case of the celebrated 'revenue equivalence theorem' due to Vickrey (1961), Myerson (1981), Riley and Samuelson (1981) and Harris and Raviv (1981).

Theorem 1 (Revenue Equivalence) Suppose n bidders have values s 1 , ..., s n identically and independently distributed with cdf F ( · ) . Then all auction mechanisms that (i) always award the object to the bidder with highest value in equilibrium, and (ii) give a bidder with valuation s zero pro fi ts, generates the same revenue in expectation.

Proof. We consider the general class of auctions where bidders submit bids b 1 , ..., b n . An auction rule speci fi es for all i ,

x i :

B 1 × ... × B n → [0 , 1]

t i :

B 1 × ... × B n → R ,

where x i ( · ) gives the probability i will get the object and t i ( · ) gives i 's required payment as a function of the bids ( b 1 , ..., b n ). 2

Given the auction rule, bidder i 's expected payo ff as a function of his signal and bid is:

<!-- formula-not-decoded -->

Let b i ( · ) , b -i ( · ) denote an equilibrium of the auction game. Bidder i 's equilibrium payo ff is:

<!-- formula-not-decoded -->

where we use (i) to write E s -i [ x i ( b ( s i ) , b ( s -i ))] = F n -1 ( s i ).

Using the fact that b ( s i ) must maximize i 's payo ff given s i and opponent strategies b -i ( · ), the envelope theorem implies that:

and also

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where we use (ii) to write U i ( s ) = 0.

Combining our expressions for U i ( s i ), we get bidder i 's expected payment given his signal:

<!-- formula-not-decoded -->

where the last equality is from integration by parts. Since x i ( · ) does not enter into this expression, bidder i 's expected equilibrium payment given his signal is the same under all auction rules that satisfy (i) and (ii) . Indeed, i 's expected payment given s i is equal to:

<!-- formula-not-decoded -->

So the seller's revenue is:

<!-- formula-not-decoded -->

2 So in a fi rst price auction, x 1 ( b 1 , ..., b n ) equals 1 if b 1 is the highest bid, and otherwise zero. Meanwhile t 1 ( b 1 , ..., b n ) equals zero unless b 1 is highest, in which case t 1 = b 1 . In a second price auction, x 1 ( · ) is the same, and t 1 ( · ) is zero unless b 1 is highest, in which case t 1 equals the highest of ( b 2 , ..., b n ).

a constant.

The revenue equivalence theorem has many applications. One useful trick is that it allows us to solve for the equilibrium of di ff erent auctions, so long as we know that the auction will satis fi y (i) and (ii) . Here's an example.

Application: The All-Pay Auction. Consider the same set-up - bidders 1 , .., n , with values s 1 , ..., s n , identically and independently distributed with cdf F -and consider the following rules. Bidders submit bids b 1 , ..., b n and the bidder who submits the highest bid gets the object. However, bidders must pay their bid regardless of whether they win the auction. (These rules might seem a little strange - the all-pay auction is commonly used as a model of lobbying or political in fl uence).

Suppose this auction has a symmetric equilibrium with an increasing strategy b A ( s ) used by all players. Then, bidder i 's expected payo ff given value s i will be (if everyone plays the equilibrium strategies):

<!-- formula-not-decoded -->

So

<!-- formula-not-decoded -->

In addition to the all-pay auction, many other auction rules also satisfy the revenue equivalence assumptions when bidder values are independently and identically distributed. Two examples are:

1. The English (oral ascending) auction. All bidders start in the auction with a price of zero. The price rises continuously, and bidders may drop out at any point in time. Once they drop out, they cannot reenter. The auction ends when only one bidder is left, and this bidder pays the price at which the second-to-last bidder dropped out.
2. The Dutch (descending price) auction. The price starts at a very high level and drops continuously. At any point in time, a bidder can stop the auction, and pay the current price. Then the auction ends.

## 2 Common Value Auctions

We would now like to generalize the model to allow for the possibility that (i) learning bidder j 's information could cause bidder i to re-assess his estimate of how much he values the object, and (ii) the information of i and j is not independent (when j 's estimate is high, i 's is also likely to be high).

These features are natural to incorporate in many situations. For instance, consider an auction for a natural resource like a tract of timber. In such a setting, bidders are likely to have di ff erent costs of harvesting or processing the timber. These costs may be independent across bidders and private, much like in the above model. But at the same time, bidders are likely to be unsure exactly how much merchanteable timber is on the tract, and use some sort of statistical sampling to estimate the quantity. Because these estimates will be based on limited sampling, they will be imperfect so if i learned that j had sampled a di ff erent area and got a low estimate, she would likely revise her opinion of the tract's value. In addition, if the areas sampled overlap, the estimates are unlikely to be independent.

## 2.1 A General Model

- Bidders i = 1 , ..., n
- Signals S 1 , ..., S n with joint density f ( · )
- Signals are (i) exchangeable, and (ii) a ffi liated.
- -Signals are exchangeable if s 0 is a permutation of s ⇒ f ( s ) = f ( s 0 ).
- -Signals are a ffi liated if f ( s ∧ s 0 ) f ( s ∨ s 0 ) ≥ f ( s 0 ) f ( s ) (i.e. s j | s i has monotone likelihood ratio property).
- Value to bidder i is v ( s i , s -i ).

Example 1 The independent private value model above is a special case: just let v ( s i , s -i ) = s i , and suppose that S 1 , ..., S n are independent.

Example 2 Another common special case is the pure common value model with conditionally independent signals. In this model, all bidders have the same value, given by some random variable V . The signals S 1 , .., S n are each correlated with V , but independent conditional on it (so for instance, S i = V + ε i , where ε 1 , .., ε n are independent. Then v ( s i , s -i ) = E [ V | s 1 , ..., s n ] .

or

Example 3 A commonly used, but somewhat hard to motivate, variant of the general model is obtained by letting v i ( s i , s -i ) = s i + β P j = i s j , with β ≤ 1 , and assuming that S 1 , ..., S n are independent. This model has the feature that bidder's have independent information (so a version of the RET applies), but interdependent valuations (so there are winner's curse e ff ects).

6

A new feature of the more general auction environment is that each bidder i will want to account for the fact that her opponents' bids reveal something about their signals, information that is relevant for i 's own valuation. In particular, if i wins, then the mere fact of winning reveals that her opponent's values were not that high - hence winning is 'bad news' about i 's valuation. This feature is called the winner's curse.

## 2.2 Second Price Auction

Let's look for a symmetric increasing equilibrium bid strategy b ( s ) in this more general environment. We start by considering the bidding problem facing i :

- Let s i denote the highest signal of bidders j = i .

6

- Bidder i will win if she bids b i ≥ b ( s i ), in which case she pays b ( s i )

Bidder i 's problem is then:

<!-- formula-not-decoded -->

The fi rst order condition for this problem is:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

6

or simplifying:

<!-- formula-not-decoded -->

That is, in equilibrium, bidder i will bid her expected value conditional on her own signal and conditional on all other bidders having a signal less than hers (with the best of the rest equal to hers).

Remark 2 While we will not purse it here, in this more general environment the revenue equivalence theorem fails. Milgrom and Weber (1982) prove a very general result called the 'linkage principle' which basically states that in this general symmetric setting, the more information on which the winner's payment is based, the higher will be the expected revenue. Thus, the fi rst price auction will have lower expected revenue than the second price auction because the winner's payment in the fi rst price auction is based only on her own signal, while in the second price auction it is based on her own signal and the second-highest signal.

## 3 Large Auctions &amp; Information Aggregation

An interesting question that has been studied in the auction literature arises if we think about auction models as a story about how prices are determined in Walrasian markets. In this context, we might then ask to what extent prices will aggregate the information of market participants.

We now consider a series of results along these lines. For each result, the basic set-up is the same. There are a lot of bidders, and the auction has pure common values with conditionally independent signals. We consider second price auctions (or more generally, with k objects, k +1 price auctions, where all winning bidders pay the k +1st highest bid). The basic question is: as the number of bidders gets large, will the auction price converge to the true value of the object(s) for sale?

## 3.1 Wilson (1977, RES)

Wilson considers information aggregation in a setting with a special information structure. In his setting, bidders learn a lower bound on the object's value. The model has:

- Bidder's 1 , ..., n
- A single object with common value V ∼ U [0 , 1]
- Bidder's signals S 1 , ..., S n are iid with S i ∼ U [0 , v ] (so signal s i ⇒ V ≥ s i ).

Wilson shows that as n →∞ , the expected price converges to v . This is easy to see: with lots of bidders, someone will have a signal close to v , and you have to bid very close to your signal to have any chance of winning.

## 3.2 Milgrom (1979, EMA)

Milgrom goes on to identify a necessary and su ffi cient condition for information aggregation with many bidders and a fi xed number of objects. Milgrom's basic requirement is, in the limit as n →∞ , that for all v 0 ∈ Ω and all v &lt; v 0 , and M &gt; 0, there exists some s 0 ∈ S such that

That is, for any possible value v 0 , there must be arbitrarily strong signals that e ff ectively rule out any value v &lt; v 0 .

<!-- formula-not-decoded -->

This condition builds on Wilson, and the intuition is again quite easy. As n →∞ , there is a very strong winner's curse. In a second price auction, the high bid is:

6

While it is clear that s 1: n is likely to be very high as n →∞ , the only way anyone would ever bid v would be to have a signal so strong that conditioning on millions of other signals being lower than your own would not push down your estimate too much.

<!-- formula-not-decoded -->

## 3.3 Pesendorfer and Swinkels (1997, EMA)

Pesendorfer and Swinkels consider a model that is quite similar to Milgrom.

- n bidders, k objects
- Each bidder has value V ∼ F ( · ) on [0 , 1]
- Signals S i ∼ G ( ·| v ) on [0 , 1], where g ( ·|· ) has the MLRP.
- Signals S 1 , ..., S n are independent conditional on V = v .

Remark 3 Clearly with a large number of independent signals, there is enough information to consistently estimate v . The question then is whether the bids will accurately aggregate this information - i.e. will the price be a consistent estimator?

Pesendorfer and Swinkel's big idea is the following. While the winner's curse will make a bidder with s = 1 shade her bid as n → ∞ with a fi xed number of objects k , as k →∞ , there is also a loser's curse : if lowering your bid ε matters there must be k people with higher valuations . This operates against the winner's curse, counterbalancing it.

Proposition 3 The unique equilibrium of k +1 st price auction is symmetric:

<!-- formula-not-decoded -->

De fi nition 1 A sequence of auctions ( n m , k m ) has information aggregation if the price converges in probability to v as m →∞ .

PS fi rst consider necessary conditions for information aggregation. Clearly, a requirement for information aggregation is that:

<!-- formula-not-decoded -->

Without this, there will be no convergence when v = 0 or when v = 1. Now,

<!-- formula-not-decoded -->

If k m 9 ∞ , then this expectation will shrink below 1. So we must have k m →∞ . And similarly, looking at b m (0), we must have n m -k m →∞ .

PS go on to show that these conditions are not just necessary, but su ffi -cient for information aggregation.

Proposition 4 A sequence of auctions has information aggregation if and only if n m -k m →∞ and k m →∞ .

The basic idea is that conditioning on k m -1 bidders having higher signals than s i gives a very strong signal about true value. So the bidder who actually has the k th highest sighnal will tend to be right on when he bids E V [ V | s i , k th highest of other signals is s i ]. Thus, we will end up with information aggregation.

## References

- [1] Harris, Milton and Arthur Raviv (1981) 'Allocation Mechanisms and the Design of Auctions,' Econometrica , 49, 1477-1499.
- [2] Kremer, Ilan (2002) 'Information Aggregation in Common Value Auctions,' Econometrica .
- [3] Milgrom, Paul (1979) 'A Convergence Theorem for Bidding with Differential Information,' Econometrica, 47.
- [4] Milgrom, Paul (2003) Putting Auction Theory to Work , Cambridge University Press.

- [5] Milgrom, Paul and Robert Weber (1982) 'A Theory of Auctions and Competitive Bidding,' Econometrica , 50, .
- [6] Milgrom, Paul and Ilya Segal (2002) 'Envelope Theorems for Arbitrary Choice Sets,' Econometrica , 70, 583-601.
- [7] Myerson, Roger (1981) 'Optimal Auction Design,' Math. Op. Res , 6, 58-73.
- [8] Pesendorfer, Wolfgang and Jeroen Swinkels (1997) 'The Loser's Curse and Information Aggregation in Auctions,' Econometrica , 65, .
- [9] Riley, John and William Samuelson (1981) 'Optimal Auction,' American Economic Review , 71, 381-392.
- [10] Vickrey, William (1961) 'Counterspeculation, Auctions and Competitive Sealed Tenders,' Journal of Finance , 16, 8-39.
- [11] Wilson, Robert (1977) 'A Bidding Model of Perfect Competition,' Review of Economic Studies.
- [12] Wilson, Robert (1992) 'Strategic Analysis of Auctions,' Handbook of Game Theory .