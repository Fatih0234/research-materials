## Related Work

Recent research has increasingly focused on evaluating how precisely LLMs can replicate human-like social and psychological behaviors. We categorize these studies into three types: persona-free attempts, attempts with simulated personas, and those with real personas.

Persona-free Investigation with Social Psychology: To quantitatively assess LLM social behaviors, studies have adopted established social game paradigms including the Public Goods Game, Ultimatum Game, and organizational collaboration scenarios to evaluate cooperative tendencies, altruism, and strategic capabilities (Sreedhar et al. 2025a,b). These approaches assign specific roles to models or structure cooperative frameworks through prompts, simulating human-like teamwork and decision-making patterns. While significant in demonstrating that LLMs can modulate behavior based on contextual conditions, most analyses focus on aggregate group trends, showing multi-agent systems approximate human cooperative distributions better than single models. However, findings remain limited to group-level statistical similarities, leaving individual persona-level predictive precision largely unexamined.

Evaluation Attempts with Simulated Personas: Based on the information type provided to the model, these personas fall into three categories: personality-based, demographic-based, and narrative-based. Some researchers attempted to input personality-based personas from social psychology as prompts to induce distinct behavioral patterns (Zhang et al. 2024; Ashery, Aiello, and Baronchelli 2025). For example, Zhang et al. examined how agents with different personality traits engage in negotiation and debate. Other researchers attempted to design demographic-based personas for simulating variation in attitudes toward social issues (Piao et al. 2025; Kim et al. 2025). For example, Piao et al. injected demographic profiles into over 10,000 LLM agents to analyze decision-making distributions in contexts such as basic income policies and disaster response. Moreover, another group of researchers attempted to utilize narrative-based personas including specific memories, goals, and daily routines to simulate long-term and personalized interactions (Park et al. 2023; Xie et al. 2024a). Park et al. provided LLM agents with background stories and tracked their autonomous behaviors within a virtual town, demonstrating the potential for sustained, agent-specific behavioral patterns. While these approaches have been effective in diversifying LLM behavior through persona injection, they remain limited by the synthetic nature of the input. That is, the personas are not grounded in real human data, and thus miss achieving a one-to-one correspondence with actual human attitudes and contextual experience.

Evaluation Attempts with Real Personas: While simulated personas have effectively induced behavioral variation in LLMs, they offer limited precision in predicting individual behavior. More recently, Park et al. (2024) evaluated LLM-human alignment using real persona data from interviews, comparing outputs across the General Social Survey, Big Five traits, and simple economic games. However, this work focused primarily on attitudinal surveys, not high-stakes economic decisions involving monetary consequences-contexts requiring higher-order reasoning shaped by budget constraints, opportunity costs, and cultural norms. Furthermore, it did not examine how different persona injection methods impact predictive accuracy.

Though previous studies identified valuable insights us- aLe

M

® Cultural Education Experience (9 items)

Institution Satisfaction (4 items)

Basic Demographic Information (11 itmes)

Cultural Participation (6 items)

Music Performance

Q1. Are you willing to attend this performances at the regular price?

Figure 1: Overview of persona information categories and experimental question form.

<!-- image -->

ing different personas, no existing studies have systematically evaluated LLMs' ability to predict realistic economic consumption choices. In addition, they have less analyzed how variations in persona construction and injection strategies influence behavioral alignment. To address these gaps, investigating whether LLMs can simulate economic human behavior with real-world persona is required. To conduct such a simulation, we adopt a human experiment about willingness-to-pay, as illustrated in the next section.
