## 4 AI agents as cash managers

AI agents built using Gen AI models-with access to similar data used by human cash managerscould automate many tasks in payment systems, including liquidity management. This automation may reduce operational costs (for example, by automating routine operations and reducing oversight costs), improve settlement efficiency (for example, by adapting payment strategies to recycle incoming payments more effectively), and decrease human error (for example, by detecting typographical mistakes and anomalies). Additionally, as these agents learn over time, they can adapt to evolving market conditions and refine cash-management strategies, helping to modernize payment systems. This adaptive capacity may contribute to the development of more resilient liquidity-management frameworks, improve system responsiveness under stress, and offer policymakers additional tools to evaluate policy interventions.

Collateral

18F

Liquidity decision

Central bank

As illustrated in Figure 3, an AI agent-much like a human cash manager-can operate through an integrated workflow that synthesizes multiple real-time and historical data sources. It could begin by assessing the internal payment queue, evaluating clients' current and upcoming payment requests alongside available liquidity. Next, it can analyze historical transaction patterns to predict potential urgent payment demands and incoming funds, enabling informed, strategic decisionmaking on current payment. Throughout this process, the agent can adhere to internal guidelines and established system protocols, ensuring compliance with relevant policies. By integrating these data streams, the AI agent can prioritize important transactions and effectively navigate the tradeoffs between liquidity management and payment delay.

Figure 3: AI agent as assistant cash manager in high-value payment systems.

<!-- image -->

We begin by manually constructing detailed scenario contexts that closely mirror current operational conditions and observed trends-such as the state of the internal payment queue, available liquidity, and the potential of incoming payments. We then pose targeted questions to prompt responses from the AI agent. Our objective is to assess the agent's decision-making capabilities through these prompt-driven experiments using ChatGPT's o3 model. Each prompt explicitly includes context designed to accurately replicate the current state. 9

This structured approach is used to quantify the AI agent's performance in relatively simple cash management functions within payment systems, offering preliminary insights into its potential operational readiness for integration into traditional financial infrastructures like RTGS systems. In the next section, we explain these prompt-driven experiments in detail.

9 In a generalized setting within payment system frameworks, the agent could potentially leverage its extensive data access to autonomously generate and refine prompts that can be used for payment decisions.
