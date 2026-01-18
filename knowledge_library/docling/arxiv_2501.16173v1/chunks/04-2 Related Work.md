## 2 Related Work

Evaluating and benchmarking the capabilities of LLMs is common practice, as these models frequently exhibit emergent capabilities, such as theory of mind [Van Duijn et al. , 2023] and reasoning [Kojima et al. , 2022], despite certain limitations in their abilities [Sclar et al. , 2023; Dziri et al. , 2023]. Moreover, LLMs are increasingly utilized in multiagent systems (MAS). Notably, a line of research has focused on modelling societies of generative agents [Park et al. , 2023] and examining their performance in social dilemmas [Yocum et al. , 2023]. However, we perceive a gap in the assessment of the emergent behaviours of systems of LLMs. Our proposal aims to expand the evaluation and benchmarking of LLMs to encompass an analysis of their emergent collective behaviours.

LLMs have been used to play games from game theory [Aher et al. , 2023 07 232023 07 29; Horton, 2023; Wu et al. , 2023], including iterated normal-form games [Akata et al. , 2023], extensive-form games [Mao et al. , 2023], Markov social dilemma games [Yocum et al. , 2023] and team games [Zhang et al. , 2024; Gong et al. , 2023]. These games serve as proxies for real-world behaviours and assess the abilities of LLM agents in a range of scenarios. However, LLMs can struggle to play games at an action-level granularity [Fan et al. , 2024]. In contrast, our approach involves having the LLMs output strategies in advance.

LLMs have been suggested for use in game theoretic setting [Gemp et al. , 2024] and modelling human societies and social phenomena [Park et al. , 2023; Vezhnevets et al. , 2023 10 292023 11 01; Piatti et al. , 2024; De Zarz` a et al. , 2023; Gao et al. , 2024]. While our approach similarly utilises games to evaluate LLM behaviour, our focus diverges from improving LLM performance. Instead, we aim to critically assess the balance between aggressive and cooperative behaviours exhibited by these models, and to analyse the emergent dynamics of systems comprising multiple LLM agents with varying behavioural tendencies.

IPD has been extensively employed in various fields of study to model and analyse strategic decision-making in repeated interactions [Axelrod, 1980; Crandall, 2014; Rapoport et al. , 2015; Press and Dyson, 2012; Knight et al. , 2016; Kendall et al. , 2007; Nowak and Sigmund, 1993]. Furthermore, researchers have used IPD to study the emergence and stability of cooperative behaviours in populations: it has

1 https://github.com/willis-richard/evollm

<!-- formula-not-decoded -->

Table 1: Prisoner's Dilemma

helped explain phenomena such as reciprocal altruism and the evolution of cooperation among non-kin individuals [Axelrod, 1986; Mahmoud et al. , 2010; Nowak et al. , 2004; Nowak, 2006; Stewart and Plotkin, 2013; Hilbe et al. , 2013; Wahl and Nowak, 1999a]. The incorporation of noisy actions into IPD models [Wu and Axelrod, 1995; Wahl and Nowak, 1999b] serves a dual purpose: it simulates the uncertainty of action outcomes and represents the potential for execution errors by agents. This added complexity allows us to assess the robustness and adaptability of LLM agent behaviours under more realistic, imperfect conditions.
