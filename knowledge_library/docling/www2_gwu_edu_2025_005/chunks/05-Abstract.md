## Abstract

We develop a multi-agent framework for modeling the Federal Open Market Committee (FOMC) decision making process. The framework combines two approaches: an LLM-based simulation and a Monte Carlo implementation of a generalized Bayesian voting model. Both begin from identical prior beliefs about the appropriate interest rate for each committee member, formed using real-time data and member profiles. In a simulation replicating the July 2025 FOMC meeting, both tracks deliver rates near the 4.25-4.50% range's upper end (4.42% LLM, 4.38% MC). Political pressure scenario increases dissent and dispersion: the LLM track averages 4.38% and shows dissent in 88% of meetings; the MC track averages 4.39% and shows dissent in 61% of meetings. A negative jobs revision scenario moves outcomes lower: LLM at 4.30% (dissent in 74% of meeting), and MC at 4.32% (dissent in 62% of meeting), with final decisions remaining inside the 4.25-4.50% range. The framework isolates small, scenario-dependent wedges between behavioral and rational baselines, offering an in silico environment for counterfactual evaluation in monetary policy.

Keywords

: Generative AI; Multi-Agent Systems; Large Language Models,

Federal Open Market Committee; Monetary Policy; Simulations

JEL Codes

: E52, E58, C63, D83, C73

∗ Email: kazinnik@stanford.edu .

† Email: tsinc@gwu.edu .

We thank Erik Brynjolfsson, Thomas R. Cook, Seung Jung Lee, Andrew Martinez, and Daniela Puzzello, as well as the participants at the DEL brownbag series. We are grateful to the Stanford Digital Economy Lab for funding and support. All remaining errors are our own.
