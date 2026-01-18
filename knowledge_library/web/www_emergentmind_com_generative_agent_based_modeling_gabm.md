[ ](https://www.emergentmind.com/)
[ Trending Papers ](https://www.emergentmind.com/ "Trending Papers") [ Open Problems ](https://www.emergentmind.com/open-problems "Open Problems") [ Email Digest ](https://www.emergentmind.com/subscribe "Email Digest") [ Pricing ](https://www.emergentmind.com/pricing "Plans & Pricing") [ Log in ](https://www.emergentmind.com/users/sign_in "Log in") [ Sign up ](https://www.emergentmind.com/users/sign_up?redirect_to=https%3A%2F%2Fwww.emergentmind.com%2Ftopics%2Fgenerative-agent-based-modeling-gabm "Sign up") [ Discord Discord Logo Streamline Icon: https://streamlinehq.com  ](https://discord.gg/BhfTC4mTXq) [ Updates ](https://updates.emergentmind.com/ "Updates")
[ Trending Papers ](https://www.emergentmind.com/ "Trending Papers") [ Open Problems ](https://www.emergentmind.com/open-problems "Open Problems") [ Email Digest ](https://www.emergentmind.com/subscribe "Email Digest") [ Pricing ](https://www.emergentmind.com/pricing "Plans & Pricing") [ Log in ](https://www.emergentmind.com/users/sign_in "Log in") [ Sign up ](https://www.emergentmind.com/users/sign_up?redirect_to=https%3A%2F%2Fwww.emergentmind.com%2Ftopics%2Fgenerative-agent-based-modeling-gabm "Sign up") [ Discord Discord Logo Streamline Icon: https://streamlinehq.com  ](https://discord.gg/BhfTC4mTXq)
Generative Agent-Based Modeling (GABM)
Papers
Topics
Lightbulb On Streamline Icon: https://streamlinehq.com
Authors
Recent
[View all](https://www.emergentmind.com/history)
Magnifying Glass Streamline Icon: https://streamlinehq.com
2000 character limit reached 
[ Sponsor Information Square Streamline Icon: https://streamlinehq.com  ](https://www.emergentmind.com/sponsorship)
[ ![](https://assets.emergentmind.com/assets/sponsors/paperpile-logo-w343-d7fd7c8c33d166ed3ac6f5bb45f26f8b89eca7f00c1e1433295e91ce6a7d2fae.png) ](https://www.paperpile.com?utm_source=emergentmind&utm_medium=sidebar-image)
Organize your preprints, BibTeX, and PDFs with Paperpile.
[ Get 30 days free ](https://www.paperpile.com?utm_source=emergentmind&utm_medium=sidebar-text)
Chrome Extension
Enhance arXiv with our new Chrome Extension.
[ Chrome Extension ](https://chromewebstore.google.com/detail/emergent-mind-%E2%80%94-arxiv-int/hgmnadjffdiipehljmhagdgpaoiiklml)
#  Generative Agent-Based Modeling (GABM) 
Updated 11 July 2025 
  * Generative Agent-Based Modeling (GABM) is an agent-based simulation paradigm that leverages deep generative and language models for context-sensitive, adaptive agent behavior.
  * It advances classic models by enabling agents to generate dynamic actions, decisions, and communications through probabilistic and deep learning techniques.
  * GABM finds practical applications in population synthesis, social dynamics, epidemic modeling, digital economies, and public administration research.


Generative [Agent-Based Modeling](https://www.emergentmind.com/topics/agent-based-modeling-abm) (GABM) is an [agent-based simulation](https://www.emergentmind.com/topics/agent-based-simulation) paradigm in which agents generate actions, decisions, and communications using large-scale machine learning models, most notably LLMs and deep generative architectures. Unlike classic [agent-based models](https://www.emergentmind.com/topics/agent-based-models-abms) (ABMs), in which agent behavior is typically defined by hardcoded rules or heuristics, GABM endows agents with the capacity for context-dependent reasoning, flexible adaptation, natural language interaction, and emergent pattern formation. The deployment of generative models in [agent-based frameworks](https://www.emergentmind.com/topics/agent-based-frameworks) has enabled new levels of realism, scalability, and interpretability in simulating complex systems, notably in population synthesis, social dynamics, human-in-the-loop experimentation, digital economy simulations, and public administration modeling.
## 1. Foundations and Theoretical Frameworks
At the core of GABM is the integration of probabilistic and deep generative modeling techniques with multi-agent simulation. In traditional population synthesis—a key input for large-scale modeling of transport and social systems—[deep generative models](https://www.emergentmind.com/topics/deep-generative-models) such as [Variational Autoencoders](https://www.emergentmind.com/topics/variational-autoencoders) ([VAEs](https://www.emergentmind.com/topics/variational-autoencoders-vaes)) are used to learn the full joint distribution of agent attributes, thereby overcoming limitations of classic methods like Iterative Proportional Fitting (IPF), Gibbs sampling, and Bayesian networks in high-dimensional settings ([Borysov et al., 2018](https://www.emergentmind.com/papers/1808.06910)). VAEs compress high-dimensional attribute vectors X=(X1,…,Xn)X=(X_1,\ldots,X_n)X=(X1​,…,Xn​) into a compact latent space ZZZ, yielding scalable and flexible generation of realistic agents by sampling from the learned latent distribution.
GABM extends this approach by embedding generative models within autonomous agents who interact within mechanistic simulation environments. Each agent's behavior—be it in physical, social, or digital domains—is dynamically generated by prompting a LLM or deep network with contextual information, personality, memory, and environmental feedback ([Vezhnevets et al., 2023](https://www.emergentmind.com/papers/2312.03664), [Ghaffarzadegan et al., 2023](https://www.emergentmind.com/papers/2309.11456)).
A canonical GABM agent comprises:
  * **Profile/State:** Personalized agent attributes (e.g., demographics, interests, skills).
  * **Memory:** Structured as both short-term and long-term stores, with mechanisms for semantic recall and temporal encoding ([Xiao et al., 2023](https://www.emergentmind.com/papers/2311.06957), [Vezhnevets et al., 2023](https://www.emergentmind.com/papers/2312.03664)).
  * **Reasoning Module:** Executes context-sensitive decision-making, often via [chain-of-thought prompting](https://www.emergentmind.com/topics/chain-of-thought-prompting-cotp) and multi-step evaluation ([Ghaffarzadegan et al., 2023](https://www.emergentmind.com/papers/2309.11456), [Xu et al., 5 Jun 2025](https://www.emergentmind.com/papers/2506.04699)).
  * **Interaction Interface:** Enables natural language exchanges with other agents, digital environments, or game-master coordinators ([Vezhnevets et al., 2023](https://www.emergentmind.com/papers/2312.03664), [Ferraro et al., 2024](https://www.emergentmind.com/papers/2411.16031)).


## 2. Generative Mechanisms and Mathematical Formalisms
Deep generative models provide the mathematical underpinning for agent synthesis, action production, and memory handling. In VAEs, the generative process is as follows:
  * Encode agent attributes into latent variables: μk,σk=Encoder(xk)\mu_k, \sigma_k = \text{Encoder}(x_k)μk​,σk​=Encoder(xk​)
  * Sample latent representation: zk=μk+σk⊙ϵk,ϵk∼N(0,I)z_k = \mu_k + \sigma_k \odot \epsilon_k, \; \epsilon_k \sim \mathcal{N}(0,I)zk​=μk​+σk​⊙ϵk​,ϵk​∼N(0,I)
  * Decode to reconstruct attributes: x^k=Decoder(zk)\hat{x}_k = \text{Decoder}(z_k)x^k​=Decoder(zk​)


The objective combines quantitative reconstruction and regularization:
L(θ,ϕ)=∑k[∥xk−x^k∥num+∥xk−x^k∥cat+βDKL[N(μk,σk)∥N(0,I)]]L(\theta, \phi) = \sum_k \left[ \| x_k - \hat{x}_k \|_{\text{num}} + \| x_k - \hat{x}_k \|_{\text{cat}} + \beta D_{KL}[\mathcal{N}(\mu_k, \sigma_k) \Vert \mathcal{N}(0, I)] \right]L(θ,ϕ)=k∑​[∥xk​−x^k​∥num​+∥xk​−x^k​∥cat​+βDKL​[N(μk​,σk​)∥N(0,I)]]
where DKLD_{KL}DKL​ is the [Kullback-Leibler divergence](https://www.emergentmind.com/topics/kullback-leibler-divergence) ensuring latent structure regularity ([Borysov et al., 2018](https://www.emergentmind.com/papers/1808.06910)).
For [LLM-driven agents](https://www.emergentmind.com/topics/llm-driven-agents), actions at each step are sampled as:
at∼p(⋅∣fa(zt)),a_t \sim p(\cdot \mid f^a(z_t)),at​∼p(⋅∣fa(zt​)),
where fa(zt)f^a(z_t)fa(zt​) formats the agent's current state and memory into a prompt; ata_tat​ is the LLM-generated action ([Vezhnevets et al., 2023](https://www.emergentmind.com/papers/2312.03664)). Many implementations rely on an external "Game Master" (GM) to translate agent intentions into state transitions and to resolve conflicts or enable digital tool integrations ([Vezhnevets et al., 2023](https://www.emergentmind.com/papers/2312.03664)).
Memory operations in [generative agents](https://www.emergentmind.com/topics/generative-agents-smallville) are handled via vector embeddings (e.g., using BERT or similar models) and temporal encoding:
  * Memory vector: v=BERT(d)v = \text{BERT}(d)v=BERT(d), where ddd is memory description
  * Temporally-weighted: Vtime−aware=v×TencodedV_{time-aware} = v \times T_{encoded}Vtime−aware​=v×Tencoded​


Retrieval combines semantic and temporal similarity for contextually relevant recall, critical for rich, adaptive agent behavior ([Xiao et al., 2023](https://www.emergentmind.com/papers/2311.06957)).
## 3. Practical Applications Across Domains
GABM frameworks have been demonstrated in a wide variety of research domains:
  * **Population Synthesis:** VAEs enable fitting the full joint distribution of hundreds of socio-demographic or behavioral variables, allowing generation of synthetic agents for urban, transport, and epidemiological simulation at unprecedented scale and resolution ([Borysov et al., 2018](https://www.emergentmind.com/papers/1808.06910)).
  * **Epidemiological Modeling:** LLM-enhanced agents in epidemic simulations reason about personal health, risk, and social context, producing behaviors such as self-isolation, quarantine, and adaptation to public health messaging. This approach yields emergent epidemic curves, multiple waves, and feedback-sensitive social dynamics ([Williams et al., 2023](https://www.emergentmind.com/papers/2307.04986), [Choi et al., 10 Jun 2025](https://www.emergentmind.com/papers/2506.13783)).
  * **Social Phenomena:** By integrating social psychology with generative reasoning, GABMs capture complex effects such as social norm diffusion, echo chamber formation, polarization in online networks, and the friendship paradox in large-scale social simulations ([Ghaffarzadegan et al., 2023](https://www.emergentmind.com/papers/2309.11456), [Ferraro et al., 2024](https://www.emergentmind.com/papers/2411.16031), [Orlando et al., 9 Feb 2025](https://www.emergentmind.com/papers/2502.05919)).
  * **Digital Economy and MMO Simulations:** [LLM-based agents](https://www.emergentmind.com/topics/llm-based-agents) model market behaviors including bargaining, specialization, coalition formation, and price-setting with realism that rule-based or RL agents cannot achieve. These systems support studies of policy, taxation, and emergent economic phenomena in synthetic societies ([Dizaji, 2024](https://www.emergentmind.com/papers/2411.17724), [Xu et al., 5 Jun 2025](https://www.emergentmind.com/papers/2506.04699)).
  * **Public Administration and Crisis Simulation:** GABM is used for modeling government response to crises, such as water pollution events, allowing integration of agent memory, reflection, and public event dynamics entirely in natural language environments ([Xiao et al., 2023](https://www.emergentmind.com/papers/2311.06957)).
  * **Human-Assistant Interaction Design:** Generative agents simulate human subjects in studies of assistant systems, enabling scalable, privacy-preserving, and reproducible evaluations of design scenarios previously restricted to costly human-in-the-loop experiments ([Xuan et al., 15 May 2025](https://www.emergentmind.com/papers/2505.09938)).


## 4. Model Validation, Calibration, and Limitations
A central challenge in GABM is the validation and calibration of generatively empowered agents. While subjective believability, human expert review, and text similarity measures (e.g., cosine similarity of embeddings) are commonly used, these do not establish operational validity across the intended domain ([Larooij et al., 4 Apr 2025](https://www.emergentmind.com/papers/2504.03274)).
Limitations identified in the literature include:
  * **Computational Cost:** GABMs amplify traditional ABM complexity, as the cost of simulating nnn LLM-driven agents grows with C(n)∝n2×LLMcostC(n) \propto n^2 \times \text{LLM}_{\text{cost}}C(n)∝n2×LLMcost​ ([Larooij et al., 4 Apr 2025](https://www.emergentmind.com/papers/2504.03274)).
  * **Interpretability:** The black-box nature of LLMs obscures causal mechanisms underlying emergent phenomena, complicating causal inference and theory-building.
  * **Reproducibility and Stochasticity:** Variability inherent in LLM outputs challenges consistent experimental replication.
  * **Bias and Hallucination:** Generative agents risk unintended propagation of social or factual biases, and hallucinated reasoning or actions.


Efforts are ongoing to develop better calibration protocols, standardized benchmarks, and hybrid modeling that combines simplicity and theoretical clarity with generative depth ([Larooij et al., 4 Apr 2025](https://www.emergentmind.com/papers/2504.03274), [Navarro et al., 2024](https://www.emergentmind.com/papers/2411.07038)).
## 5. Advances, Toolkits, and Implementation Patterns
The field has seen the development of specialized libraries and methodologies for GABM:
  * **Concordia:** A flexible open-source framework enabling construction of generative simulations in physical, social, and digital spaces. Agents interact via LLMs and associative/memory components, with a GM orchestrating the environment and resolving actions or [API](https://www.emergentmind.com/topics/geospatial-application-programming-interface-api) calls ([Vezhnevets et al., 2023](https://www.emergentmind.com/papers/2312.03664), [Navarro et al., 2024](https://www.emergentmind.com/papers/2411.07038)).
  * **GIDEA:** A modular platform for conducting large-scale, fully simulated human-assistant interaction research, supporting structured experimental protocols, dynamic persona creation, and environment configuration ([Xuan et al., 15 May 2025](https://www.emergentmind.com/papers/2505.09938)).
  * **Simulation Design Patterns:** Modern workflows in GABM emphasize separation between scenario specification (via JSON or similar structured formats), detailed memory and state management, and batch experimental runs with HTML or tabular logging for downstream analysis ([Navarro et al., 2024](https://www.emergentmind.com/papers/2411.07038)).


Detailed experimental protocols now include assignment of personality parameters (often according to the Big Five model), long- and short-term memory structures, and execution modules that define the round-based progression of the simulation ([Navarro et al., 2024](https://www.emergentmind.com/papers/2411.07038), [Xiao et al., 2023](https://www.emergentmind.com/papers/2311.06957)).
## 6. Interdisciplinary Impact and Research Directions
GABM's integration of generative models with agent-based frameworks has had a significant cross-disciplinary impact:
  * **Complex Systems Science:** GABMs are applied in network science (network formation, influence dynamics), social dynamics (opinion and polarization), and behavioral epidemiology ([Lu et al., 2024](https://www.emergentmind.com/papers/2408.09175), [Orlando et al., 9 Feb 2025](https://www.emergentmind.com/papers/2502.05919)).
  * **Experimental Design:** The grammar of generative mechanisms enables modular assembly of hybrid models, simulation-based power analysis, and design optimization in biology, epidemiology, and economics ([Sankaran et al., 2022](https://www.emergentmind.com/papers/2208.06011)).
  * **Policy and Governance:** GABMs serve as testbeds for economic policy, public administration crisis response, and the exploration of institutional design effects in agent collectives ([Xiao et al., 2023](https://www.emergentmind.com/papers/2311.06957), [Dizaji, 2024](https://www.emergentmind.com/papers/2411.17724)).


Ongoing research focuses on:
  * Standardizing benchmarks and validation metrics for operational validity
  * Improving interpretability and reducing computational overhead
  * Exploring bias reduction and model robustness to prompt and population [diversity](https://www.emergentmind.com/topics/diversity-beta-recall)
  * Hybrid approaches combining generative and rule-based agents for scalable, robust systems ([Larooij et al., 4 Apr 2025](https://www.emergentmind.com/papers/2504.03274), [Lu et al., 2024](https://www.emergentmind.com/papers/2408.09175))


## 7. Summary
GABM represents a significant methodological advance in computational modeling, coupling the expressive, adaptable reasoning of generative models with agent-based simulation frameworks. This enables nuanced, context-sensitive modeling of complex systems across physical, social, and digital domains, with emerging use in social science, epidemiology, economics, and human–computer interaction. Critical scientific challenges remain in operational validation, interpretability, and resource scaling, but the ongoing development of specialized libraries, validation protocols, and interdisciplinary methods is expanding the scope and rigor of GABM research.
[ File Document Download Save Streamline Icon: https://streamlinehq.com  PDF ](https://www.emergentmind.com/users/sign_up?redirect_to=https%3A%2F%2Fwww.emergentmind.com%2Farticles%2Fgenerative-agent-based-modeling-gabm) [ File Document Download Save Streamline Icon: https://streamlinehq.com  Markdown ](https://www.emergentmind.com/users/sign_up?redirect_to=https%3A%2F%2Fwww.emergentmind.com%2Farticles%2Fgenerative-agent-based-modeling-gabm) [ Chat Bubble Oval Streamline Icon: https://streamlinehq.com  Chat (Pro) ](https://www.emergentmind.com/pricing)
Definition Search Book Streamline Icon: https://streamlinehq.com
References (15)
1. 
[Scalable Population Synthesis with Deep Generative Modeling](https://www.emergentmind.com/papers/1808.06910) (2018)
2. 
[Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia](https://www.emergentmind.com/papers/2312.03664) (2023)
3. 
[Generative Agent-Based Modeling: Unveiling Social System Dynamics through Coupling Mechanistic Models with Generative Artificial Intelligence](https://www.emergentmind.com/papers/2309.11456) (2023)
4. 
[Simulating Public Administration Crisis: A Novel Generative Agent-Based Simulation System to Lower Technology Barriers in Social Science Research](https://www.emergentmind.com/papers/2311.06957) (2023)
5. 
[Empowering Economic Simulation for Massively Multiplayer Online Games through Generative Agent-Based Modeling](https://www.emergentmind.com/papers/2506.04699) (2025)
6. 
[Agent-Based Modelling Meets Generative AI in Social Network Simulations](https://www.emergentmind.com/papers/2411.16031) (2024)
7. 
[Epidemic Modeling with Generative Agents](https://www.emergentmind.com/papers/2307.04986) (2023)
8. 
[Infected Smallville: How Disease Threat Shapes Sociality in LLM Agents](https://www.emergentmind.com/papers/2506.13783) (2025)
9. 
[Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations?](https://www.emergentmind.com/papers/2502.05919) (2025)
10. 
[Incentives to Build Houses, Trade Houses, or Trade House Building Skills in Simulated Worlds under Various Governing Systems or Institutions: Comparing Multi-agent Reinforcement Learning to Generative Agent-based Model](https://www.emergentmind.com/papers/2411.17724) (2024)
11. 
[Design and Evaluation of Generative Agent-based Platform for Human-Assistant Interaction Research: A Tale of 10 User Studies](https://www.emergentmind.com/papers/2505.09938) (2025)
12. 
[Do Large Language Models Solve the Problems of Agent-Based Modeling? A Critical Review of Generative Social Simulations](https://www.emergentmind.com/papers/2504.03274) (2025)
13. 
[Designing Reliable Experiments with Generative Agent-Based Modeling: A Comprehensive Guide Using Concordia by Google DeepMind](https://www.emergentmind.com/papers/2411.07038) (2024)
14. 
[Generative Agent-Based Models for Complex Systems Research: a review](https://www.emergentmind.com/papers/2408.09175) (2024)
15. 
[Generative Models: An Interdisciplinary Perspective](https://www.emergentmind.com/papers/2208.06011) (2022)
### Sponsor
[ ![](https://assets.emergentmind.com/assets/sponsors/paperpile-logo-w343-d7fd7c8c33d166ed3ac6f5bb45f26f8b89eca7f00c1e1433295e91ce6a7d2fae.png) ](https://www.paperpile.com?utm_source=emergentmind&utm_medium=inline-logo)
Organize your preprints, BibTeX, and PDFs with Paperpile.
[ Get 30 days free ](https://www.paperpile.com?utm_source=emergentmind&utm_medium=inline-button)
[ ![Paperpile](https://assets.emergentmind.com/assets/sponsors/paperpile-on-laptop-caa897b8bd2dbb1dedf34da417761efa97093c381f939bf194fee6ef94a9b446.png) ](https://www.paperpile.com?utm_source=emergentmind&utm_medium=inline-screenshot)
### Whiteboard
[![](https://emergentmind-storage-cdn-c7atfsgud9cecchk.z01.azurefd.net/ai-images/0086397980089462cfe2d189bc47afab.webp)](https://emergentmind-storage-cdn-c7atfsgud9cecchk.z01.azurefd.net/ai-images/0086397980089462cfe2d189bc47afab.webp)
### Topic to Video (Beta)
Generate a video overview of this topic.
[ Ai Sparkles Streamline Icon: https://streamlinehq.com  Sign Up to Generate ](https://www.emergentmind.com/users/sign_up?redirect_to=https%3A%2F%2Fwww.emergentmind.com%2Farticles%2Fgenerative-agent-based-modeling-gabm)
### Follow Topic
Get notified by email when new papers are published related to **Generative Agent-Based Modeling (GABM)**.
[ Add Bell Notification Streamline Icon: https://streamlinehq.com  Sign Up to Follow Topic by Email ](https://www.emergentmind.com/users/sign_up?redirect_to=%2Ftopics%2Fgenerative-agent-based-modeling-gabm)
### Continue Learning
  1. [How do Generative Agent-Based Models handle the trade-off between expressive agent behavior and computational scalability, particularly in large populations?](https://www.emergentmind.com/search?q=In+the+context+of+Generative+Agent-Based+Modeling+%28GABM%29%2C+how+do+Generative+Agent-Based+Models+handle+the+trade-off+between+expressive+agent+behavior+and+computational+scalability%2C+particularly+in+large+populations%3F)
  2. [In what ways have memory architectures for generative agents improved the realism and adaptability of simulated social interactions?](https://www.emergentmind.com/search?q=In+the+context+of+Generative+Agent-Based+Modeling+%28GABM%29%2C+in+what+ways+have+memory+architectures+for+generative+agents+improved+the+realism+and+adaptability+of+simulated+social+interactions%3F)
  3. [What are the current best practices for validating and calibrating GABMs to ensure reliable emergent behaviors, compared to classic ABMs?](https://www.emergentmind.com/search?q=In+the+context+of+Generative+Agent-Based+Modeling+%28GABM%29%2C+what+are+the+current+best+practices+for+validating+and+calibrating+GABMs+to+ensure+reliable+emergent+behaviors%2C+compared+to+classic+ABMs%3F)
  4. [How do GABMs integrate domain knowledge or existing empirical findings, given the stochastic and black-box nature of generative models like LLMs?](https://www.emergentmind.com/search?q=In+the+context+of+Generative+Agent-Based+Modeling+%28GABM%29%2C+how+do+GABMs+integrate+domain+knowledge+or+existing+empirical+findings%2C+given+the+stochastic+and+black-box+nature+of+generative+models+like+LLMs%3F)
  5. [Find recent papers about validation and benchmarking methods in Generative Agent-Based Modeling.](https://www.emergentmind.com/search?q=Find+recent+papers+about+validation+and+benchmarking+methods+in+Generative+Agent-Based+Modeling.)


### Related Topics
  1. [Agent-Based Simulation](https://www.emergentmind.com/topics/agent-based-simulation)
  2. [LLM-based Simulation Methods](https://www.emergentmind.com/topics/llm-based-simulation-methods)
  3. [Socially Intelligent Generative Agents](https://www.emergentmind.com/topics/socially-intelligent-generative-agents)
  4. [Generative Social Simulation](https://www.emergentmind.com/topics/generative-social-simulation)
  5. [Multi-Agent Generative Simulacra Overview](https://www.emergentmind.com/topics/multi-agent-generative-simulacra)
  6. [LLM-Driven Generative Agents](https://www.emergentmind.com/topics/llm-driven-generative-agents)
  7. [Generative Social Simulations](https://www.emergentmind.com/topics/generative-social-simulations)
  8. [LLM-Augmented Agent-Based Modeling](https://www.emergentmind.com/topics/llm-augmented-agent-based-modeling)
  9. [LLM Empowered Agent-Based Modeling](https://www.emergentmind.com/topics/large-language-models-empowered-agent-based-modeling)
  10. [Agent Behavioral Models Overview](https://www.emergentmind.com/topics/agent-behavioral-models)


Content
[ Overview ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#topic-content) [ References ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#references) [ Whiteboard ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#whiteboard) [ Topic to Video ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#video) [ Follow Topic ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#follow-topic) [ Continue Learning ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#continue-learning) [ Related Topics ](https://www.emergentmind.com/topics/generative-agent-based-modeling-gabm#related-topics-generative-agent-based-modeling-gabm)
Stay informed about trending AI/ML papers: 
[About](https://www.emergentmind.com/about) [Updates](https://updates.emergentmind.com/) [Chrome Extension](https://chromewebstore.google.com/detail/emergent-mind-%E2%80%94-arxiv-int/hgmnadjffdiipehljmhagdgpaoiiklml) [Paper Prompts](https://www.emergentmind.com/paper-prompts) [Sponsorship](https://www.emergentmind.com/sponsorship) [API](https://www.emergentmind.com/docs/api) [Terms](https://www.emergentmind.com/terms) [Privacy](https://www.emergentmind.com/privacy) [RSS](https://www.emergentmind.com/feeds/rss) [Contact](https://www.emergentmind.com/contact) [Twitter](https://twitter.com/EmergentMind) [ Discord ](https://discord.gg/BhfTC4mTXq) 

