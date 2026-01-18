## Pay What LLM Wants:

## Can LLM Simulate Economics Experiment with 522 Real-human Persona?

Junhyuk Choi 1 † , Hyeonchu Park 1 , Haemin Lee 2 Hyebeen Shin 1 , Hyun Joung Jin 3 , Bugeun Kim 1 ∗

1

Department of Artificial Intelligence, Chung-Ang University 84 Heukseok-ro, Dongjak-gu, Seoul 06912, Republic of Korea { chlwnsgur129,phchu0429,hyebeens819,bgnkim } @cau.ac.kr

2 Department of Arts and Cultural Management, Chung-Ang University 84 Heukseok-ro, Dongjak-gu, Seoul 06912, Republic of Korea wplhm@cau.ac.kr

3 School of Economics, Chung-Ang University

84 Heukseok-ro, Dongjak-gu, Seoul 06912, Republic of Korea hyunjjin@cau.ac.kr

## Abstract

Recent advances in Large Language Models (LLMs) have generated significant interest in their capacity to simulate human-like behaviors, yet most studies rely on fictional personas rather than actual human data. We address this limitation by evaluating LLMs' ability to predict individual economic decision-making using Pay-What-You-Want (PWYW) pricing experiments with real 522 human personas. Our study systematically compares three state-of-the-art multimodal LLMs using detailed persona information from 522 Korean participants in cultural consumption scenarios. We investigate whether LLMs can accurately replicate individual human choices and how persona injection methods affect prediction performance. Results reveal that while LLMs struggle with precise individual-level predictions, they demonstrate reasonable group-level behavioral tendencies. Also, we found that commonly adopted prompting techniques are not much better than naive prompting methods; reconstruction of personal narrative nor retrieval augmented generation have no significant gain against simple prompting method. We believe that these findings can provide the first comprehensive evaluation of LLMs' capabilities on simulating economic behavior using real human data, offering empirical guidance for persona-based simulation in computational social science.

## Introduction

Recent advances in Large Language Models (LLMs) have sparked growing interest in their ability to reproduce social and psychological behaviors, leading to active research on simulating human-like judgment and choice patterns (Park et al. 2024, 2023; Wang et al. 2023; Cheng, Piccardi, and Yang 2023; Huang et al. 2024; Choi et al. 2025). Of particular note is the approach of injecting personas into LLMs to mimic human attitudes, personality traits, value judgments, and choice behaviors. However, most prior studies have focused on evaluating general tendencies without precise behavioral comparisons with actual humans, employing methods such as generating fictional personas to simulate human social phenomena, creating personas using demographic information, or extracting personas from existing QA datasets

(Horton 2023; Hewitt et al. 2024; Leng and Yuan 2023; Ross, Kim, and Lo 2024; Leng 2024a; Xie et al. 2024b).

To our knowledge, Park et al. (2024) is the only study analyzing actual human behavior, achieving 85% accuracy in reproducing General Social Survey responses from interview data. However, this study focused on psychological surveys rather than economic decision-making involving monetary costs. Simple attitudinal survey can elicit idealistic responses without realistic constraints, making it difficult to reflect actual decision making. Economic decision-making requiring willingness to pay involves complex cognitive processes where budget constraints, opportunity costs, and cultural interact, providing a more precise foundation for evaluating LLMs' human-like behavior reproduction.

To bridge this gap, we designed economic decisionmaking experiment using Pay-What-You-Want (Kim, Natter, and Spann (2009); PWYW) pricing, where consumers voluntarily determine payment amounts. This involves complex psychological factors including willingness to pay, income, cultural values, and individual value systems (Kim, Natter, and Spann 2009; Gerpott 2017), providing a valid framework for analyzing individual decision-making and evaluating how sophisticatedly LLMs can simulate actual individual human choices. Unlike previous studies evaluating general tendencies with fictional personas, we apply identical experimental structures to LLMs using detailed persona information from 522 actual participants and their decisionmaking data, analyzing how persona structure affects LLM choices and evaluating both group-level choice tendencies and individual-level prediction consistency. Therefore, this study evaluates how precisely LLMs can predict individual behaviors based on actual human personas within PWYW contexts. We systematically examine LLMs' human-like behavior reproduction using various models and persona injection methods through two key research questions.

- RQ1. Can LLMs predict economic decision of human individual in sequential or human-guided condition?

The first research question examines whether LLMs can reproduce decision-making patterns similar to correspond- ing human participants when injected with individual persona information. We construct individualized personas encompassing each participant's educational background, cultural experiences, value systems, and consumption tendencies, then input these into various LLMs to predict willingness-to-pay amounts and choice behaviors for the same cultural products. Based on prior studies (Lampinen et al. 2022; Wei et al. 2025) showing that errors may accumulate as LLMs construct subsequent judgments based on previous responses, we analyze the impact of response accumulation on prediction performance. We establish two experimental conditions: 1) Sequential Condition, where LLMs maintain their previous responses and answer all items sequentially, and 2) Human-guided Condition, where actual human responses are inserted into the conversation history to inform subsequent questions. Through this design, we directly compare LLMs' predictions with actual human responses and quantitatively evaluate both individual-level accuracy and group-level tendencies.

- RQ2. How do persona formats and prompting methods affect LLMs' ability in simulating human behavior?

The second research question analyzes how LLMs' prediction performance varies depending on persona composition and injection methods. While previous studies show LLMs respond sensitively to contextual changes (Sclar et al. 2023; Zhuo et al. 2024; Razavi et al. 2025), no systematic comparison exists regarding which methods are more effective for predicting human behavior. This study establishes persona injection along two axes: (1) Format: Survey vs. Storytelling (i.e., biographical narratives), and (2) Prompting Methods: base prompt, CoT (Wei et al. 2022), RAG (Lewis et al. 2020), and Few-shot Prompting (Brown et al. 2020). By applying identical conditions across different models, we analyze performance differences between models and evaluate how method variations are reflected in individual-level accuracy and group-level tendencies.

Based on this research design, this study provides two major contributions. First, we systematically validate the extent to which LLMs can precisely mimic individual human decision-making at both group and individual levels, based on sophisticated persona and decision-making data collected from actual human participants. This represents one of the first studies to evaluate LLMs' ability to predict specific humans' actual choice behaviors, advancing the precision of LLM human simulation research to the next level. Second, by comparing how LLMs' behavioral prediction performance varies according to persona composition and injection methods even with identical information, we provide empirical evidence for appropriate LLM utilization methods for future human-like behavior generation and simulation.

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

## Human Experiment

This section describes the human experiment that provides the baseline data for evaluating LLMs' individual behavioral prediction capabilities. The experiment is based on data collected from Anonymous (2023). In this section, we briefly introduce (1) the overall design of conducted PWYW experiment, (2) the collected persona items and components, and (3) the questions for inspecting economic decision-making.

## Pay What You Want

This study adopted Pay-What-You-Want (PWYW) method to measure participants' economic choices and willingness to pay. PWYW is a participatory pricing mechanism where consumers voluntarily determine payment amounts based on their perceived value rather than fixed prices, and has been widely used as a representative experimental tool for behaviorally measuring willingness to pay in economics and consumer behavior research (Kim, Natter, and Spann 2009; Gerpott 2017). This method goes beyond simple product selection, requiring consumers to comprehensively consider various internal factors such as their preferences, economic constraints, fairness perceptions, social norms, and value systems when determining payment amounts. PWYW effectively implements experimental decision-making situations where these complex factors interact to influence willingness to pay. Particularly, by applying the PWYW context to cultural product consumption situations, Anonymous (2023)

designed the experiment to observe how participants' cultural tastes, experiences, knowledge, educational levels, and so-called cultural capital are reflected in actual consumption decisions. This enables collection of more realistic and coherent economic choice data rather than simple preference responses, providing experimental conditions suitable for evaluating LLMs' ability on simulating human behavior.

## Persona Information

Anonymous (2023) collected personas from 522 Korean adults (Male 254, Female 268; Ages between 30-39). As shown in Figure 1, they investigated a total of 65 items including: basic demographic information, attitudes and preferences toward cultural arts, cultural arts knowledge level, cultural education experience, institutional usage experience and satisfaction, social norms and attitudes, and family background information. Through this comprehensive approach, they constructed personas that holistically reflect each individual's cultural capital level and socioeconomic background. We asked the authors and received the data. For detailed persona questionnaire, see supplementary material.

## Question Form

To construct realistic PWYW decision-making situations for cultural products, this study designed two scenarios: art exhibitions and music performances. Each scenario was structured to precisely measure participants' willingness to pay and choice behaviors, as presented in Figure 1. Specifically, three key questions were used to elicit participants' economic decision-making in each scenario. First, a binary question asking whether they are willing to attend the performance at the regular price. Second, a binary question asking whether they are willing to attend by paying their desired price. Third, for those who expressed willingness to attend in the second question, an open-ended numerical question asking how much they are willing to pay specifically. Additionally, multiple-choice questions were presented to identify reasons for unwillingness to attend, enabling analysis of how accurately LLMs can predict individual responses across various question formats. For the original korean questionnaire, refer to Supplementary Material.

## Statistical Tests Conducted in the Experiment

Group-level human tendencies were estimated using the Heckman two-step model (Heckman 1976). In the first step, a probit regression was conducted with the second yes/no items for each scenario ( Q2 ) as dependent variables and persona attributes as independent variables to estimate the probability of viewing intention. In the second step, a linear regression was performed using the willingness-to-pay amounts ( Q2.1 ) as dependent variables, limited to participants agreed in Q2 . The inverse Mills ratio calculated from the first stage was incorporated to correct for self-selection bias. The model accounts for potential correlation between error terms in both stages, and sample selection bias occurs when this correlation is non-zero. For detailed definitions, see supplementary material.

## RQ1 : Sequential vs Human-guided

Using the above experiment, this section investigates whether LLMs can accurately predict individual human decisions under Sequential versus Human-guided interaction conditions. We address the detailed experimental procedures for validating this question, the characteristics of models used for evaluation, analytical methods, and results of each model's prediction performance against human responses.

## Experiment Setup

We evaluated LLMs' human simulation performance by completely replicating the structure of the human experiment. Each LLM was provided with real persona information of actual human participants, and all elements of the questionnaire used in the human experiment were presented identically. Specifically, we provided all contextual information identical to humans, including survey introductions, detailed descriptions of exhibitions and performances, images provided to human participants, and hypothetical situation settings. Given that all participants in this study were Korean, and considering prior research (Leng 2024b; Verma et al. 2023) showing that linguistic variations can affect results, we used all survey items, system prompts, and questions input to LLMs in their original Korean form. The specific experimental procedure involved first presenting each participant's persona information to the LLM as a System Prompt, appending the instruction 'Think of yourself as a person of a given persona and answer' in Korean, and then asking questions in the same order as provided to humans.

To analyze the impact of previous responses on subsequent answers, we established two experimental conditions. The first was the Sequential Condition , where previous responses generated by the LLM were maintained as-is, allowing all questions to proceed sequentially with LLM responses accumulating. The second was the Human-guided Condition , where we inserted the actual responses of the corresponding human participants into the conversation log from the second question onward to replace the LLM's previous responses. This ensured that the LLM's response to each question was based on actual human responses rather than its own previous answers, enabling measurement of more independent and accurate prediction performance.

## Evaluation

We evaluated whether LLMs can predict human behavior with two aspects: individual-level accuracy and group-level tendencies . First, individual-level accuracy measures how accurately LLMs predicted individual participants' choices. Typically, the accuracy is measured with the proportion of cases where human responses and LLM responses completely match. Specifically, we calculate: (1) accuracy rate for each individual item, (2) accuracy rate for all binary items ( Q1 and Q2 ), and (3) Overall accuracy for correctly answering all three items, providing a multifaceted evaluation of LLM prediction performance.

Second, group-level tendencies measures the overall similarity between human data and simulated data by LLMs. Typically, we compared patterns of two regression models in estimating the influence of persona variables. Three metrics are used for this purpose: (1) Coefficient Sign Agreement (CSA) is the proportion of regression coefficients whose signs are matched, showing how similarly two models judged the direction of variable influence. (2) Statistical Significance Agreement (SSA) is the proportion of variables that are statistically significant in both models or insignificant in both, indicating the degree of agreement in important variable selection. (3) Jaccard Index (Jaccard 1908) calculates the overlap between two models using the set of significant variables, expressing how much the important variable sets themselves overlap as a value.

## Models

In this experiment, we selected three state-of-the-art multimodal LLMs capable of simultaneously processing text and images as evaluation targets: GPT-4o (Hurst et al. 2024), Llama-3.2-90B-Vision-Instruct (Dubey et al. 2024), and Qwen2.5-VL-72B-Instruct (Bai et al. 2025). All models are based on multimodal architectures that can integratively process images and text, and also demonstrate good performance in processing Korean, the experimental language of this study. Particularly, on a popular Korean benchmark, Hae-Rae benchmark (Son et al. 2023), these models achieved good scores: GPT-4o (0.836), Llama-3.2 (0.738), and Qwen2.5 (0.636), respectively. GPT-4o was accessed through the official OpenAI API, while the other two models were accessed through the OpenRouter API. To ensure response consistency, the temperature was fixed at 0 for all.

## Results and Discussion

In this section, we analyzes the experimental results regarding two conditions and inter-model comparisons, discussing the similarity and agreement between humans and LLMs.

Effect of Interaction Condition: Comparing the performance differences between the two interaction conditions,

Figure 2: Response distribution in Sequential Condition

Human

Human

12

12 6

GPT

0

GPT

LLaMA 0

LLaMA 0

Qwen

0

Qwen 0

6

36

36

0

3t

7

0

0

139

139

134

336

23

23

141

183

259

44

44

1

14

251

275

5

77

1

Table 1: LLM performance across experimental conditions for music performance (M) and art (A) domains.

|                                                  | Sequential                                       | Sequential                                       | Sequential                                       | Human-guided                                     | Human-guided                                     | Human-guided                                     |
|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| Metric                                           | GPT                                              | Llama                                            | Qwen                                             | GPT                                              | Llama                                            | Qwen                                             |
| A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       |
| M Q1                                             | 62.26                                            | 60.15                                            | 61.11                                            | 62.07                                            | 63.60                                            | 62.26                                            |
| M Q2                                             | 57.28                                            | 78.54                                            | 75.10                                            | 70.50                                            | 80.84                                            | 76.82                                            |
| M Q2.1                                           | 5.43                                             | 22.25                                            | 9.78                                             | 15.65                                            | 26.41                                            | 33.74                                            |
| M Q3                                             | 11.36                                            | 0.00                                             | 0.00                                             | 31.86                                            | 9.73                                             | 29.20                                            |
| TF Total                                         | 44.06                                            | 53.83                                            | 46.17                                            | 45.98                                            | 55.36                                            | 45.79                                            |
| M total                                          | 6.90                                             | 11.49                                            | 4.79                                             | 6.70                                             | 11.11                                            | 15.13                                            |
| A Q1                                             | 64.75                                            | 37.55                                            | 66.28                                            | 65.13                                            | 55.17                                            | 65.71                                            |
| A Q2                                             | 67.82                                            | 62.84                                            | 64.75                                            | 76.44                                            | 73.37                                            | 65.71                                            |
| A Q2.1                                           | 16.23                                            | 9.6                                              | 4.28                                             | 28.44                                            | 23.24                                            | 24.16                                            |
| A Q3                                             | 16.73                                            | 0.19                                             | 0.13                                             | 0.00                                             | 35.38                                            | 36.41                                            |
| TF Total                                         | 45.59                                            | 32.95                                            | 46.55                                            | 44.44                                            | 42.72                                            | 40.04                                            |
| A total                                          | 12.45                                            | 5.94                                             | 1.72                                             | 17.05                                            | 16.09                                            | 13.79                                            |
| Total Acc                                        | 4.60                                             | 0.77                                             | 0.77                                             | 4.02                                             | 0.96                                             | 4.41                                             |
| B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) |
| CSA                                              | 0.62                                             | 0.55                                             | 0.66                                             | 0.72                                             | 0.86                                             | 0.76                                             |
| SSA                                              | 0.86                                             | 0.83                                             | 0.72                                             | 0.93                                             | 0.90                                             | 0.86                                             |
| Jaccard                                          | 0.43                                             | 0.00                                             | 0.27                                             | 0.67                                             | 0.57                                             | 0.20                                             |

the Human-guided Condition showed overall superior prediction performance compared to the Sequential Condition. This was somewhat expected, as the Human-guided condition is designed to allow LLMs to reference actual human response flows for each question, enabling reasoning to proceed in a manner closer to human judgment pathways. These results suggest that providing actual human responses as examples may produce effects similar to few-shot prompting, providing a foundation for exploring the effectiveness of various prompting techniques in RQ2.

As shown in Table 1, the Human-guided condition demonstrated higher accuracy than the Sequential condition in terms of individual-level accuracy. The difference between conditions was particularly pronounced in subjective or open-ended questions compared to binary-choice items. For example, in Qwen's case, the accuracy for subjective questions ( Q2.1 ) was only 9.78% and 4.28% in the Sequential condition, but improved significantly to 33.74% and 24.16% in the Human-guided condition. This suggests that when LLMs rely on their own generated response flows (Sequential Condition), errors may accumulate or reasoning may proceed in directions that diverge from human response patterns. However, we can confirm that the Overall Accuracy was generally very low across all models. Meanwhile, analysis of group-level tendencies showed that both conditions performed well overall, with the Human-guided condition consistently showing higher prediction accuracy compared to the Sequential condition. The Human-guided condition scored higher across all major indicators including CSA, SSA, and Jaccard index.

These results provide two major findings. First, in Human-guided condition, actual human responses were provided as context for each item, enabling LLMs to form more

2

2

0

28

28

2

2

11

11

2

2

0

0

Figure 3: Response distribution in Human-Guided condition

<!-- image -->

coherent reasoning pathways, which led to higher prediction accuracy at both group and individual levels. This demonstrates that providing actual response examples is effective for improving LLMs' behavioral prediction accuracy, suggesting the validity of example-based approaches such as few-shot. Second, while LLMs still showed difficulties in precisely replicating individual human choices, they demonstrated similar tendencies to humans at the group level.

Comparison Models: Based on the results from Table 1, Figures 9 and 10 when comparing accuracy across models, GPT-4o showed consistently high performance in both item-level accuracy ( M Q1 62.07%, M Q2 70.50%, A Q1 65.13%, A Q2 76.44%) and group-level similarity indicators (CSA 0.72, SSA 0.93, Jaccard 0.67) in the Humanguided condition, demonstrating the most human-like patterns in both choice outcomes and variable structures. LLaMA achieved the highest variable direction agreement (0.86) in the Human-guided condition. But overall accuracy was only 0.96%. This suggests that while the model excels at identifying the direction of variable influence, it lacks consistency in translating this understanding into individual choice predictions. Qwen showed similar Overall Accuracy to GPT-4o at 4.41% in the Human-guided condition, but had a low Jaccard score of 0.20, indicating that its important variable set differed significantly from humans.

Figures 9 and 10 reveal particularly notable model differences in response distribution in terms of price ( Q2.1 ). Figure 9 shows that human responses have high diversity, while LLM responses tend to cluster at specific price points. In Figure 10, this clustering pattern becomes even more pronounced, with LLMs showing much more concentrated response distributions compared to the diverse human response patterns. For instance, in Sequential condition, Figure 9 show that Qwen provided response distributions with some variance similar to humans, but when switched to Human-guided condition, the response distribution became much more concentrated at specific price points. Nevertheless, the accuracy for the same questions increased significantly, as shown in the transition from Figure 9 to 10. This demonstrates that actual human responses had a positive im- pact on the model's prediction performance, though at the cost of response diversity.

## RQ2 : Prompt Injection Methology

While RQ1 demonstrated LLMs' potential to reproduce human-like choices, it revealed limitations in accurately predicting individual-level. The improved performance in the Human-guided condition suggests that persona presentation and prompt structure significantly impact LLM prediction performance. Therefore, RQ2 systematically analyzes how different persona composition methods and prompt engineering affect LLMs' human behavior prediction.

## Experiment Setup

Based on RQ1 results showing superior performance of Human-guided condition, RQ2 adopted this as the baseline setting for testing various persona composition and injection methods. All experimental conditions remained identical to RQ1, including models, API settings, and temperature parameters. The experiment examined two main axes. First, Persona Format included Survey Format (presenting the 65 collected persona items in structured form) and Storytelling Format (reconstructing the same information into biographical narratives). Second, Prompting Methods included na¨ ıve prompts (Base), CoT, RAG, and Few-shot Prompting (providing three response examples from similar personas). This resulted in seven experimental combinations: four techniques for Survey and three for Storytelling.

## Result and Discussion

The RQ2 experimental results reveal several key patterns according to different persona format and prompting methods. For detailed results, refer to Table 2.

Effect of Persona Format Analysis of the overall results reveals that Survey Format consistently outperformed Storytelling Format across most conditions. Specifically, Survey Format demonstrated higher Overall Accuracy than Storytelling Format across the majority of models and prompting methods. For instance, GPT-4o recorded 4.02% in Survey Format compared to 0.19% in storytelling Format under Base conditions, while Qwen showed a substantial difference with 4.41% versus 1.34%, respectively. These findings suggest that structured information presentation better supports LLMs' ability in information processing.

At the individual item level, Survey Format exhibited marginally higher accuracy on binary questions compared to Storytelling Format. GPT-4o demonstrated slightly superior performance in Survey Format for Q2 (70.50%, 76.44%) relative to Storytelling Format (69.16% and 74.52%, respectively). Despite these modest differences at the item level, the formats produced substantial disparities in Overall Accuracy, indicating that cumulative effects across multiple decision points significantly amplify performance differences.

We suspect that the different Persona Format may hinder clarity of persona items. Specifically, Survey Format appears to facilitate LLMs' ability to understand persona information and establish clear connections to decision-making processes. In contrast, Storytelling Format may introduce atten- tional dispersion, diverting focus from decision-relevant information. This effect was particularly pronounced in shortanswer response items, where GPT-4o showed comparable performance between Survey Format ( M Q2.1 : 15.65%) and Storytelling Format (16.38%), yet differed substantially in overall consistency.

Effect of Prompting Methods The most notable finding is that prompting methods demonstrated only limited improvements compared to the Base approach. In the Survey Format, Few-shot prompting yielded mixed results: while it improved accuracy on specific items (GPT-4o showed improvement from 15.65% to 20.05% on M Q2.1 from Base to Few-shot), Overall Accuracy decreased in most cases (Base 4.02% vs Few-shot 1.72%). This suggests that providing additional examples may enhance performance on zero-shot Base method but fails to translate into comprehensive prediction accuracy across the complete decision-making process. Similarly, CoT and RAG techniques failed to provide consistent improvements. CoT occasionally resulted in performance degradation (GPT-4o Overall accuracy declined from Base 4.02% to CoT 2.49%), indicating that explicit reasoning steps may introduce additional sources of error rather than enhancing prediction capability. RAG maintained intermediate performance levels but showed no clear enhancement over the Base approach.

These findings collectively demonstrate that current prompting methods exhibit limited effectiveness in complex human behavior prediction tasks, suggesting that the challenge of persona-based behavioral simulation may require fundamentally different approaches beyond conventional prompting method.

Note on low Jaccard index The most critical finding is the consistently low Jaccard Index across both formats. Survey Format showed Jaccard scores ranging from 0.2-0.67, while Storytelling Format exhibited similar levels at 0.170.67. The Storytelling Format was originally designed to integrate persona information as a narrative, encouraging LLMs to consider comprehensive character backgrounds rather than isolated attributes. The intention was to prevent excessive focus on specific variables and promote more balanced persona understanding. However, the consistently low Jaccard Index across both formats suggests that LLMs possess fundamentally different abilities in variable selection and weighting compared to humans.

This finding extends beyond information presentation methods, revealing intrinsic limitations in current LLM architectures; they have low ability to understand and reproduce the complex and contextual characteristics of human decision-making processes. Regardless of whether information is presented in structured or narrative form, LLMs heavily rely on limited and biased portion of the given persona, exposing the inherent constraints of current technology in persona-based behavioral simulation. While LLMs can capture directional tendencies and statistical significance at the group level to some extent, their ability to identify decisionmaking factors that humans actually consider important remains unimproved despite modifications in persona format and prompting methods. So, the challenge of achieving

Table 2: LLM performance across prompting strategies and interaction formats for music performance (M) and art (A) tasks.

|                                                  | Basic Prompt                                     | Basic Prompt                                     | Basic Prompt                                     | CoT Prompt                                       | CoT Prompt                                       | CoT Prompt                                       | RAG Prompt                                       | RAG Prompt                                       | RAG Prompt                                       | Few-Shot                                         | Few-Shot                                         | Few-Shot                                         |
|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| Metric                                           | GPT                                              | Llama                                            | Qwen                                             | GPT                                              | Llama                                            | Qwen                                             | GPT                                              | Llama                                            | Qwen                                             | GPT                                              | Llama                                            | Qwen                                             |
| Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    | Survey Format                                    |
| A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       |
| M Q1                                             | 62.07                                            | 63.60                                            | 62.26                                            | 65.13                                            | 63.03                                            | 65.71                                            | 62.07                                            | 60.15                                            | 62.26                                            | 66.09                                            | 60.15                                            | 64.56                                            |
| M Q2                                             | 70.50                                            | 80.84                                            | 76.82                                            | 74.90                                            | 78.35                                            | 78.74                                            | 72.41                                            | 80.27                                            | 71.65                                            | 70.69                                            | 78.74                                            | 73.37                                            |
| M Q2 1                                           | 15.65                                            | 26.41                                            | 33.74                                            | 21.27                                            | 12.96                                            | 22.74                                            | 15.40                                            | 31.78                                            | 33.99                                            | 20.05                                            | 6.85                                             | 20.05                                            |
| M Q3                                             | 31.86                                            | 9.73                                             | 29.20                                            | 31.86                                            | 23.01                                            | 28.32                                            | 31.86                                            | 28.32                                            | 27.43                                            | 32.74                                            | 14.16                                            | 24.78                                            |
| TF Total                                         | 45.98                                            | 55.36                                            | 45.7                                             | 55.56                                            | 53.83                                            | 51.34                                            | 47.32                                            | 47.51                                            | 48.28                                            | 49.43                                            | 52.68                                            | 51.72                                            |
| M total                                          | 6.70                                             | 11.11                                            | 15.13                                            | 8.24                                             | 5.17                                             | 9.96                                             | 5.75                                             | 12.84                                            | 15.13                                            | 9.58                                             | 4.98                                             | 9.00                                             |
| A Q1                                             | 65.13                                            | 55.17                                            | 65.71                                            | 66.86                                            | 54.98                                            | 65.33                                            | 64.75                                            | 64.94                                            | 67.05                                            | 67.62                                            | 56.9                                             | 68.01                                            |
| A Q2                                             | 76.44                                            | 73.37                                            | 65.71                                            | 75.86                                            | 73.37                                            | 72.80                                            | 74.52                                            | 71.65                                            | 68.20                                            | 71.84                                            | 64.94                                            | 72.41                                            |
| A Q2 1                                           | 28.44                                            | 23.24                                            | 24.16                                            | 28.75                                            | 22.32                                            | 24.46                                            | 29.97                                            | 16.51                                            | 23.85                                            | 22.32                                            | 15.29                                            | 14.68                                            |
| A Q3                                             | 0.00                                             | 35.38                                            | 36.41                                            | 35.38                                            | 24.10                                            | 30.77                                            | 34.87                                            | 36.92                                            | 38.46                                            | 27.69                                            | 6.15                                             | 38.97                                            |
| TF Total                                         | 44.44                                            | 42.72                                            | 40.04                                            | 45.49                                            | 42.15                                            | 42.91                                            | 42.72                                            | 44.44                                            | 43.30                                            | 51.15                                            | 37.36                                            | 50.00                                            |
| A total                                          | 17.05                                            | 16.09                                            | 13.79                                            | 18.39                                            | 15.52                                            | 12.64                                            | 15.52                                            | 12.26                                            | 16.09                                            | 13.03                                            | 6.90                                             | 12.26                                            |
| Overall Acc                                      | 4.02                                             | 0.96                                             | 4.41                                             | 2.49                                             | 0.57                                             | 1.53                                             | 3.07                                             | 1.92                                             | 3.26                                             | 1.72                                             | 0.77                                             | 0.77                                             |
| B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) |
| CSA                                              | 0.72                                             | 0.86                                             | 0.76                                             | 0.86                                             | 0.83                                             | 0.86                                             | 0.83                                             | 0.69                                             | 0.69                                             | 0.72                                             | 0.86                                             | 0.86                                             |
| SSA                                              | 0.93                                             | 0.90                                             | 0.86                                             | 0.86                                             | 0.97                                             | 0.90                                             | 0.90                                             | 0.86                                             | 0.86                                             | 0.86                                             | 0.90                                             | 0.86                                             |
| Jaccard                                          | 0.67                                             | 0.57                                             | 0.20                                             | 0.20                                             | 0.80                                             | 0.57                                             | 0.50                                             | 0.20                                             | 0.33                                             | 0.20                                             | 0.50                                             | 0.20                                             |
| Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              | Storytelling Format                              |
| A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       | A. Accuracy by Question (Individual-level)       |
| M Q1                                             | 59.58                                            | 59.96                                            | 59.77                                            | 59.58                                            | 44.06                                            | 61.69                                            | 59.96                                            | 60.54                                            | 59.96                                            |                                                  |                                                  |                                                  |
| M Q2                                             | 69.16                                            | 78.35                                            | 78.54                                            | 79.69                                            | 78.35                                            | 79.31                                            | 75.10                                            | 78.54                                            | 80.08                                            |                                                  |                                                  |                                                  |
| M Q2.1                                           | 16.38                                            | 21.52                                            | 33.74                                            | 25.92                                            | 17.85                                            | 22.98                                            | 18.83                                            | 33.74                                            | 33.99                                            |                                                  |                                                  |                                                  |
| M Q3                                             | 31.86                                            | 9.73                                             | 36.28                                            | 31.86                                            | 9.73                                             | 30.97                                            | 31.86                                            | 27.43                                            | 27.43                                            |                                                  |                                                  |                                                  |
| TF Total                                         | 52.87                                            | 52.49                                            | 53.07                                            | 53.26                                            | 28.35                                            | 53.45                                            | 53.64                                            | 48.85                                            | 53.26                                            |                                                  |                                                  |                                                  |
| M1 total                                         | 3.07                                             | 7.09                                             | 15.71                                            | 9.77                                             | 9.58                                             | 8.81                                             | 5.56                                             | 16.67                                            | 16.28                                            |                                                  |                                                  |                                                  |
| A Q1                                             | 59.96                                            | 54.79                                            | 62.45                                            | 65.52                                            | 44.64                                            | 65.52                                            | 61.30                                            | 58.81                                            | 62.07                                            |                                                  |                                                  |                                                  |
| A Q2                                             | 74.52                                            | 74.33                                            | 68.97                                            | 73.56                                            | 73.37                                            | 74.41                                            | 74.52                                            | 70.88                                            | 69.54                                            |                                                  |                                                  |                                                  |
| A Q2.1                                           | 27.22                                            | 19.27                                            | 26.61                                            | 24.46                                            | 24.46                                            | 24.77                                            | 28.75                                            | 20.49                                            | 21.41                                            |                                                  |                                                  |                                                  |
| A Q3                                             | 36.41                                            | 24.10                                            | 36.41                                            | 36.41                                            | 26.15                                            | 27.69                                            | 33.33                                            | 34.36                                            | 38.86                                            |                                                  |                                                  |                                                  |
| TF Total                                         | 42.34                                            | 42.53                                            | 46.36                                            | 44.83                                            | 39.46                                            | 45.98                                            | 42.15                                            | 41.57                                            | 44.83                                            |                                                  |                                                  |                                                  |
| A2 total                                         | 16.86                                            | 13.98                                            | 16.67                                            | 17.24                                            | 12.64                                            | 15.13                                            | 16.28                                            | 12.45                                            | 15.13                                            |                                                  |                                                  |                                                  |
| Overall Acc                                      | 0.19                                             | 0.38                                             | 1.34                                             | 1.34                                             | 0.57                                             | 1.34                                             | 0.96                                             | 1.92                                             | 1.72                                             |                                                  |                                                  |                                                  |
| B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) | B. Coefficient Similarity to Human (Group-level) |
| CSA                                              | 0.72                                             | 0.69                                             | 0.76                                             | 0.69                                             | 0.93                                             | 0.62                                             | 0.83                                             | 0.83                                             | 0.86                                             |                                                  |                                                  |                                                  |
| SSA                                              | 0.93                                             | 0.93                                             | 0.93                                             | 0.93                                             | 0.93                                             | 0.83                                             | 0.90                                             | 0.90                                             | 0.86                                             |                                                  |                                                  |                                                  |
| Jaccard                                          | 0.6                                              | 0.67                                             | 0.67                                             | 0.6                                              | 0.67                                             | 0.17                                             | 0.4                                              | 0.5                                              | 0.4                                              |                                                  |                                                  |                                                  |

human-like behavioral simulation may require fundamental advances in model architecture and training paradigms, rather than incremental improvements in persona format or prompting method. The heavy reliance on limited portion of persona indicates that current LLMs may lack the humanlike mechanisms necessary for authentic persona-based decision modeling, highlighting a crucial area for future research in developing more sophisticated approaches to human behavior simulation.

## Conclusion

This study presents the first comprehensive evaluation of LLMs' ability to simulate individual human economic decision-making using real 522 human persona data in PayWhat-You-Want (PWYW) pricing experiments. Our find- ings reveal that while LLMs demonstrate reasonable grouplevel tendencies, they struggle significantly with precise individual-level accuracy, achieving overall accuracy rates below 5% across all tested models and conditions. Notably, commonly adopted advanced prompting method such as CoT, RAG, and Few-shot prompting showed no substantial improvements over na¨ ıve baseline methods, and structured survey format consistently outperformed narrative storytelling approaches. The consistently low Jaccard indices across all experimental conditions suggest fundamental limitations in current LLM architectures' ability to identify and weigh decision-making factors that humans actually consider important in their decision making.

These results provide crucial empirical evidence for the current boundaries of LLM-based human behavior simulation and highlight the need for fundamental advances in model architecture and training paradigms rather than incremental improvements in prompt engineering. However, this study has two limitations. First, we did not conduct detailed analysis of which specific persona components among the 65 collected items most significantly influence prediction performance. Second, we did not explore advanced technical modeling approaches such as ensemble methods or fine-tuning that could potentially improve accuracy. Despite these two limitations, this work establishes a rigorous methodological framework for evaluating LLM's ability in persona-based simulation and emphasizes the importance of realistic expectations for current LLM technology in individual human behavior modeling.

## References

Anonymous. 2023. Title omitted for double-blind review.

Ashery, A. F.; Aiello, L. M.; and Baronchelli, A. 2025. Emergent social conventions and collective bias in LLM populations. Science Advances , 11(20): eadu9368.

Bai, S.; Chen, K.; Liu, X.; Wang, J.; Ge, W.; Song, S.; Dang, K.; Wang, P.; Wang, S.; Tang, J.; et al. 2025. Qwen2. 5-vl technical report. arXiv preprint arXiv:2502.13923 .

Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.; Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell, A.; et al. 2020. Language models are few-shot learners. Advances in neural information processing systems , 33: 18771901.

Cheng, M.; Piccardi, T.; and Yang, D. 2023. CoMPosT: Characterizing and evaluating caricature in LLM simulations. arXiv preprint arXiv:2310.11501 .

Choi, J.; Hong, Y.; Kim, M.; and Kim, B. 2025. Examining Identity Drift in Conversations of LLM Agents. arXiv:2412.00804.

Dubey, A.; Jauhri, A.; Pandey, A.; Kadian, A.; Al-Dahle, A.; Letman, A.; Mathur, A.; Schelten, A.; Yang, A.; Fan, A.; et al. 2024. The llama 3 herd of models. arXiv e-prints , arXiv-2407.

Gerpott, T. J. 2017. Pay-what-you-want pricing: An integrative review of the empirical research literature. Management Science Letters , 7(1): 35-62.

Heckman, J. J. 1976. The common structure of statistical models of truncation, sample selection and limited dependent variables and a simple estimator for such models. In Annals of economic and social measurement, volume 5, number 4 , 475-492. NBER.

Hewitt, L.; Ashokkumar, A.; Ghezae, I.; and Willer, R. 2024. Predicting results of social science experiments using large language models. Preprint .

Horton, J. J. 2023. Large language models as simulated economic agents: What can we learn from homo silicus? Technical report, National Bureau of Economic Research.

Huang, J.; Wang, W.; Li, E. J.; Lam, M. H.; Ren, S.; Yuan, Y.; Jiao, W.; Tu, Z.; and Lyu, M. R. 2024. On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs. In Proceedings of the Twelfth International Conference on Learning Representations (ICLR) .

Hurst, A.; Lerer, A.; Goucher, A. P.; Perelman, A.; Ramesh, A.; Clark, A.; Ostrow, A.; Welihinda, A.; Hayes, A.; Radford, A.; et al. 2024. Gpt-4o system card. arXiv preprint arXiv:2410.21276 .

Jaccard, P. 1908. Nouvelles recherches sur la distribution florale. Bull. Soc. Vaud. Sci. Nat. , 44: 223-270.

Kim, J.; Kwon, J.; Vecchietti, L. F.; Oh, A.; and Cha, M. 2025. Exploring Persona-dependent LLM Alignment for the Moral Machine Experiment. arXiv:2504.10886.

Kim, J.-Y.; Natter, M.; and Spann, M. 2009. Pay what you want: A new participative pricing mechanism. Journal of marketing , 73(1): 44-58.

Lampinen, A. K.; Dasgupta, I.; Chan, S. C.; Matthewson, K.; Tessler, M. H.; Creswell, A.; McClelland, J. L.; Wang, J. X.; and Hill, F. 2022. Can language models learn from explanations in context? arXiv preprint arXiv:2204.02329 .

Leng, Y. 2024a. Can LLMs Mimic Human-Like Mental Accounting and Behavioral Biases? In Proceedings of the 25th ACM Conference on Economics and Computation , EC '24, 581. New York, NY, USA: Association for Computing Machinery. ISBN 9798400707049.

Leng, Y. 2024b. Can LLMs mimic human-like mental accounting and behavioral biases? Available at SSRN 4705130 .

Leng, Y.; and Yuan, Y. 2023. Do LLM Agents Exhibit Social Behavior? arXiv preprint arXiv:2312.15198 .

Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.; Goyal, N.; K¨ uttler, H.; Lewis, M.; Yih, W.-t.; Rockt¨ aschel, T.; et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in neural information processing systems , 33: 9459-9474.

Park, J. S.; O'Brien, J.; Cai, C. J.; Morris, M. R.; Liang, P.; and Bernstein, M. S. 2023. Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th annual acm symposium on user interface software and technology , 1-22.

Park, J. S.; Zou, C. Q.; Shaw, A.; Hill, B. M.; Cai, C.; Morris, M. R.; Willer, R.; Liang, P.; and Bernstein, M. S. 2024. Generative agent simulations of 1,000 people. arXiv preprint arXiv:2411.10109 .

Piao, J.; Yan, Y.; Zhang, J.; Li, N.; Yan, J.; Lan, X.; Lu, Z.; Zheng, Z.; Wang, J. Y.; Zhou, D.; Gao, C.; Xu, F.; Zhang, F.; Rong, K.; Su, J.; and Li, Y. 2025. AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society. arXiv:2502.08691.

Razavi, A.; Soltangheis, M.; Arabzadeh, N.; Salamat, S.; Zihayat, M.; and Bagheri, E. 2025. Benchmarking prompt sensitivity in large language models. In European Conference on Information Retrieval , 303-313. Springer.

Ross, J.; Kim, Y.; and Lo, A. W. 2024. Llm economicus? mapping the behavioral biases of llms via utility theory. arXiv preprint arXiv:2408.02784 .

Sclar, M.; Choi, Y.; Tsvetkov, Y.; and Suhr, A. 2023. Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting. arXiv preprint arXiv:2310.11324 .

Son, G.; Lee, H.; Kim, S.; Kim, H.; Lee, J.; Yeom, J. W.; Jung, J.; Kim, J. W.; and Kim, S. 2023. Hae-rae bench: Evaluation of korean knowledge in language models. arXiv preprint arXiv:2309.02706 .

Sreedhar, K.; Cai, A.; Ma, J.; Nickerson, J. V.; and Chilton, L. B. 2025a. Simulating Cooperative Prosocial Behavior with Multi-Agent LLMs: Evidence and Mechanisms for AI Agents to Inform Policy Decisions. In Proceedings of the 30th International Conference on Intelligent User Interfaces , IUI '25, 1272-1286. New York, NY, USA: Association for Computing Machinery. ISBN 9798400713064.

Sreedhar, K.; Cai, A.; Ma, J.; Nickerson, J. V.; and Chilton, L. B. 2025b. Simulating Cooperative Prosocial Behavior with Multi-Agent LLMs: Evidence and Mechanisms for AI Agents to Inform Policy Decisions. In Proceedings of the 30th International Conference on Intelligent User Interfaces , IUI '25, 1272-1286. New York, NY, USA: Association for Computing Machinery. ISBN 9798400713064.

Verma, Y.; Jangra, A.; Kumar, R.; and Saha, S. 2023. Large scale multi-lingual multi-modal summarization dataset. arXiv preprint arXiv:2302.06560 .

Wang, Z. M.; Peng, Z.; Que, H.; Liu, J.; Zhou, W.; Wu, Y.; Guo, H.; Gan, R.; Ni, Z.; Yang, J.; et al. 2023. Rolellm: Benchmarking, eliciting, and enhancing roleplaying abilities of large language models. arXiv preprint arXiv:2310.00746 .

Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Xia, F.; Chi, E.; Le, Q. V.; Zhou, D.; et al. 2022. Chain-ofthought prompting elicits reasoning in large language models. Advances in neural information processing systems , 35: 24824-24837.

Wei, Z.; Wang, S.; Rong, X.; Liu, X.; and Li, H. 2025. Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs. arXiv preprint arXiv:2505.16894 .

Xie, C.; Chen, C.; Jia, F.; Ye, Z.; Lai, S.; Shu, K.; Gu, J.; Bibi, A.; Hu, Z.; Jurgens, D.; Evans, J.; Torr, P.; Ghanem, B.; and Li, G. 2024a. Can Large Language Model Agents Simulate Human Trust Behavior? In The Thirty-eighth Annual Conference on Neural Information Processing Systems .

Xie, C.; Chen, C.; Jia, F.; Ye, Z.; Lai, S.; Shu, K.; Gu, J.; Bibi, A.; Hu, Z.; Jurgens, D.; et al. 2024b. Can Large Language Model Agents Simulate Human Trust Behavior? In The Thirty-eighth Annual Conference on Neural Information Processing Systems .

Zhang, J.; Xu, X.; Zhang, N.; Liu, R.; Hooi, B.; and Deng, S. 2024. Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View. In Ku, L.-W.; Martins, A.; and Srikumar, V., eds., Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , 14544-14607. Bangkok, Thailand: Association for Computational Linguistics.

Zhuo, J.; Zhang, S.; Fang, X.; Duan, H.; Lin, D.; and Chen, K. 2024. ProSA: Assessing and understanding the prompt sensitivity of LLMs. arXiv preprint arXiv:2410.12405 .

## A Detailed Persona Information

This section provides the full list of 65 items in persona questionnaire collected from participants, categorized into seven thematic groups. Each item is presented in English translation first, followed by its original Korean version.

## A.1 Basic Demographic Information (11 items)

- Q1. What is your gender? 성 별 은 무 엇 입 니 까 ?
- ① Male ( 남 자 ) ② Female ( 여 자 )
- Q2. What is your age? 연 령 은 어 떻 게 되 십 니 까 ? Age: ( 만 세 )
- Q3. What is your marital status? 결 혼 유 무 는 어 떻 게 되 십 니 까 ?
- ① Married ( 기 혼 )
- ② Single ( 미 혼 )
- ③ Divorced, Bereaved, etc. ( 이 혼 , 사 별 등 )
- Q4. How many people currently live with you (including yourself)?

현 재 함 께 거 주 하 고 있 는 가 구 원 수 는 몇 명 입 니 까 ? ( 본 인을 포 함 )

Number of household members: ( 명 )

- Q5. Who do you live with? (Select all that apply) 귀 하 의 가 구구 성 은 어 떻 게 되 십 니 까 ? (* 중 복 응 답 )
- ① Grandparent(s) ( 조 부 또 는 조 모 )
- ② Parent(s) ( 부 또 는 모 )
- ③ Sibling(s) ( 형 제 / 자 매 )
- ④ Relative(s) ( 친 척 )
- ⑤ Spouse ( 배 우 자 )
- ⑥ Son(s)/Daughter(s) ( 아 들 / 딸 )
- ⑦ Alone ( 혼 자 )
- ⑧ Others ( 기 타 )
- Q6. What is your education level? 학 력 은 어 떻 게 되 십 니 까 ?
- ② High school graduate ( 고 등 학 교 졸 업 ) → Q7
- ① Middle school or less ( 중 학 교 졸 업 이 하 ) → Q7
- ③ Currently in university ( 대 학 교 재 학 ) → Q6-1
- ⑤ Currently in graduate school ( 대 학 원 재 학 ) → Q6-1
- ④ University graduate ( 대 학 교 졸 업 ) → Q6-1
- ⑥ Graduate school graduate ( 대 학 원 졸 업 ) → Q6-1
- Q6-1. What is your university major? 대 학 교 전 공 은 어 떻 게 되 십 니 까 ?
- ① Humanities ( 인 문 계 열 )
- ② Social sciences ( 사 회 계 열 )
- ③ Business ( 경 상 계 열 )
- ④ Education ( 교 육 계 열 )
- ⑤ Engineering ( 공 학 계 열 )
- ⑥ Natural sciences ( 자 연 계 열 )
- ⑦ Arts/Physical Education ( 예 체 능 계 열 )
- ⑧ Other ( 기 타 )
- Q7. What is your occupation? 직 업 은 어 떻 게 되 십 니 까 ?
- ① Office worker ( 사 무 직 )
- ② Civil servant ( 공 무 원 )
- ③ Professional ( 전 문 직 )
- ④ Sales/service ( 판 매 / 서 비 스 직 )
- ⑤ Executive/Assembly member ( 고 위임 원 / 의 회 의 원 )
- ⑥ Agriculture/Fishery worker ( 농 업 / 어업 종 사 자 )
- ⑦ Technician ( 기 술 공 )
- ⑧ Manual labor ( 단 순 노 무 )
- ⑨ Self-employed ( 자 영 업 )
- ⑩ Housewife ( 전 업 주 부 )
- ⑪ Other ( 기 타 )
- Q8. What is your father's education level? 아 버 지 의 학 력 은 어 떻 게 되 십 니 까 ?
- ① Middle school or less ( 중 학 교 졸 업 이 하 )
- ② High school graduate ( 고 등 학 교 졸 업 )
- ③ University graduate ( 대 학 교 졸 업 )
- ④ Graduate school graduate ( 대 학 원 졸 업 )
- Q9. What is your mother's education level? 어 머 니 의 학 력 은 어 떻 게 되 십 니 까 ?
- ① Middle school or less ( 중 학 교 졸 업 이 하 )
- ② High school graduate ( 고 등 학 교 졸 업 )
- ③ University graduate ( 대 학 교 졸 업 )
- ④ Graduate school graduate ( 대 학 원 졸 업 )
- Q10. What is your average monthly personal income (before taxes and insurance)?
- 지 난 1 년 간 세 금 및보 험 을 제 하 기 전 월 평 균 개 인 소 득 은 어 떻 게 되 십 니 까 ? ( 가 구 전 체 합 산 아 님 )
- ① Not applicable ( 해 당 없 음 )
- ② Less than 1 million won (100 만 원 미 만 )
- ③ 1-2 million won (100-200 만 원 )
- ④ 2-3 million won (200-300 만 원 )
- ⑤ 3-4 million won (300-400 만 원 )
- ⑥ 4-5 million won (400-500 만 원 )
- ⑦ 5-6 million won (500-600 만 원 )
- ⑧ 6-7 million won (600-700 만 원 )
- ⑨ Over 7 million won (700 만 원 이 상 )
- Q11. What is your average monthly personal expenditure? 월 평 균 개 인 지 출 은 어 떻 게 되 십 니 까 ?
- ※ 월 세 , 세 금 , 차 량 유 지 비 , 교 통 비 등 고 정 비 제 외 . 식 비 , 쇼 핑 , 문 화 및 여 가 비 포 함 .
- ※ Excludes fixed expenses such as rent, taxes, vehicle maintenance, and transportation. Includes food, shopping, cultural and leisure expenses.
- ① Less than 500,000 won (50 만 원 미 만 )
- ② 500,000-1 million won (50-100 만 원 미 만 )
- ③ 1-1.5 million won (100-150 만 원 미 만 )
- ④ 1.5-2 million won (150-200 만 원 미 만 )
- ⑤ 2-2.5 million won (200-250 만 원 미 만 )
- ⑥ 2.5-3 million won (250-300 만 원 미 만 )
- ⑦ 3-3.5 million won (300-350 만 원 미 만 )
- ⑧ 3.5-4 million won (350-400 만 원 미 만 )
- ⑨ 4-4.5 million won (400-450 만 원 미 만 )
- ⑩ 4.5-5 million won (450-500 만 원 미 만 )
- ⑪ Over 5 million won (500 만 원 이 상 )

## A.2 Cultural Participation (6 items)

In the past year (from September 1, 2020 to August 31, 2021), have you participated in the following activities? If yes, how many times?

귀 하 는 지 난 1 년 간 (2020 년 9 월 1 일 -2021 년 8 월 31 일 ) 다 음의 활 동 을 하 신 적 이있 습 니 까 ? 하 셨 다 면 얼 마 나 하 셨 습 니 까 ?

- Q1. Attended an art exhibition

미

술

전

시

회

관

람

- ① No ( 없 다 ) ② Yes ( 있 다 ): ( ) times ( 회 )
- Q2. Attended a classical music concert or opera 클 래 식 음 악 회 , 오 페 라 공 연 관 람
- ① No ( 없 다 ) ② Yes ( 있 다 ): ( ) times ( 회 )
- Q3. Read literary works

문

학

작

품

읽

기

- ① No ( 없 다 ) ② Yes ( 있 다 ): ( ) times ( 회 )
- Q4. Attended a play 연 극관 람
- ① No ( 없 다 ) ② Yes ( 있 다 ): ( ) times ( 회 )
- Q5. Attended a musical
- 뮤 지 컬 관 람
- ① No ( 없 다 ) ② Yes ( 있 다 ): ( ) times ( 회
- )
- Q6. Attended a dance performance (ballet, modern dance, Korean traditional dance)
- 무 용 공 연 관 람 -발 레 , 현 대 무 용 , 한 국 무 용
- ① No ( 없 다 ) ② Yes ( 있 다 ): ( ) times ( 회 )

## A.3 Cultural Arts Attitudes (19 items)

Please respond based on your usual thoughts.

평 소 귀 하 께 서 생 각 하 시 는 것 을 토 대 로 응 답 해 주 십시 오 .

Response scale: ① Strongly Disagree ( 전 혀 그 렇 지 않 다 ), ② Disagree ( 그 렇 지 않 다 ), ③ Neutral ( 보 통 이 다 ), ④ Agree ( 그 렇 다 ), ⑤ Strongly Agree ( 매 우 그 렇 다 )

- Q7. I enjoy beautiful things. 나 는 아 름 다 운 것 들 을 즐 긴 다 .
- Q8.
- I believe having good manners is important. 나 는 좋 은 매 너 를 갖 는 것 이 필 요 하 다 고 생 각 한 다 .
- Q9. I believe culture is more important than material wealth. 나 는 물 질 적 부 보 다 문 화 가 더 중 요 하 다 고 생 각 한 다 .
- Q10. I enjoy things related to cultural arts. 나 는 문 화 예 술 과 관 련 된 것 들 을 즐 긴 다 .
- Q11. I consider myself cultured in terms of cultural arts. 나 는 문 화 예 술 측 면 에 서 교 양 있 는 사 람 이 라 고 생 각 한 다 .
- Q12. People think I have a taste for consuming cultural arts. 사 람 들 은 나 를 문 화 예 술 을 소 비 하 는 취 향 을 가 진 사 람 으 로 생 각 한 다 .
- Q13. I try to participate in activities related to cultural arts. 나 는 문 화 예 술 과 관 련 된 활 동 에 참 여 하 려 고 노 력 한 다 .
- Q14. I try to develop tastes related to cultural arts. 나 는 문 화 예 술 과 관 련 된 취 향 을 가 지 려 고 노 력 한 다 .
- Q15. I try to refine myself by consuming cultural arts. 나 는 문 화 예 술 을 소 비 함 으 로 써 고 상 해 지 려 고 노 력 한 다 .
- Q16. I prefer classical music performances. 나 는 클 래 식 공 연 관 람 을 선 호 한 다 .
- Q17. I prefer opera performances. 나 는 오 페 라 공 연 관 람 을 선 호 한 다 .

Q18.

I prefer dance performances.

나

는

무

용

공

연

관

람

을

선

호

한

다

.

- Q19. I prefer art exhibitions. 나 는 미 술 전 시 회 관 람 을 선 호 한 다 .
- Q20. I prefer traditional music performances. 나 는 전 통 음 악 공 연 관 람 을 선 호 한 다 .
- Q21. I have a positive view of classical musicians' professions. 나 는 클 래 식 음 악연 주 자의 직 업 을 긍 정적 으 로 생 각 한 다 .
- Q22. I have a positive view of vocal artists such as opera singers. 나 는 오 페 라 와 같 은 성 악 가 의 직 업 을 긍 정적 으 로 생 각 한 다 .
- Q23. I have a positive view of dancers' professions. 나 는 무 용 가 의 직 업 을 긍 정적 으 로 생 각 한 다 .
- Q24. I have a positive view of artists' professions. 나 는 미 술 가 의 직 업 을 긍 정적 으 로 생 각 한 다 .
- Q25. I have a positive view of traditional musicians' professions. 나 는 전 통 음 악 가 의 직 업 을 긍 정적 으 로 생 각 한 다 .

## A.4 Cultural Arts Knowledge Level (4 items)

Please answer based on your current knowledge. These questions are meant to assess your level of cultural arts knowledge.

문 화 예 술 지 식 을 측 정 하 기 위 한 질 문 이 니 정 확 한 측 정 을 위 해 평 소 아 시 는 것 을 토 대 로 응 답 해 주 십시 오 .

- Q26. Who is the composer of the classical piece, Symphony 'Fate'?
- 클 래 식 곡 , 교 향 곡 ' 운 명 ' 의작 곡가 는누 구 입 니 까 ?
- ① Mozart ( 모 차 르 트 )
- ② Bach ( 바 흐 )
- ③ Beethoven ( 베 토 벤 )
- ④ Chopin ( 쇼 팽 )
- ⑤ I don't know ( 모 름 )
- Q27. Who is the composer of the opera 'Rigoletto'? 클 래 식 곡 , 오 페 라 ' 리 골 레 토 ' 의작 곡가 는누 구 입 니 까 ?
- ① Mozart ( 모 차 르 트 )
- ② Verdi ( 베 르 디 )
- ③ Puccini ( 푸 치 니 )
- ④ Wagner ( 바 그 너 )
- ⑤ I don't know ( 모 름 )
- Q28. Who is the painter of the artwork 'Mona Lisa'? 미 술 작 품 ' 모 나 리 자 ' 의작 가 는누 구 입 니 까 ?
- ① Van Gogh ( 반 고 흐 )
- ② Claude Monet ( 클 로 드 모 네 )
- ③ Pablo Picasso ( 파 블 로 피 카 소 )
- ④ Leonardo da Vinci ( 레 오 나 르 도 다 빈 치 )
- ⑤ I don't know ( 모 름 )
- Q29. Who is the painter of the artwork 'The Scream'? 미 술 작 품 ' 절 규 ' 의작 가 는누 구 입 니 까 ?
- ① Edvard Munch ( 에 드 바 르 뭉 크 )
- ② Paul Gauguin ( 폴 고갱 )
- ③ Edgar Degas ( 에 드 가 드 가 )
- ④ Paul C´ ezanne ( 폴 세 잔 )
- ⑤ I don't know ( 모 름 )

## A.5 Cultural Education Experience (9 items)

Please answer the following questions regarding your experience with cultural and arts education.

다 음의 설 문 에 응 답 해 주 십시 오 .

- Q1. Before age 18, did you receive education related to classical music, opera, or musical theatre at school (elementary, middle, high school)? 만 18 세 이 전 학 교 내 ( 초 , 중 , 고 등 학 교 ) 에 서 클 래 식 음 악 , 오 페 라 , 뮤 지 컬 과 관 련 된 교 육을 받 은 경 험 이 있으 십 니 까 ?
- ① No ( 없 다 )
- ② Yes ( 있 다 )
- Q2. Before age 18, did you receive education related to art or exhibitions at school? 만 18 세 이 전 학 교 내 에 서 미 술 , 전 시 와 관 련 된 교 육을

## 받 은 경 험 이있으 십 니 까 ?

- ①
- No ( 없 다 ) ② Yes ( 있 다 )
- Q3. Before age 18, did you receive education related to classical music, opera, or musicals outside of school (e.g., private institutes, cultural centers, private lessons, clubs)?

만 18 세 이 전 학 교 외 에 서 클 래 식 음 악 , 오 페 라 , 뮤 지 컬 과 관 련 된 교 육을 받 은 경 험 이있으 십 니 까 ? ( 학 교 외 는 사 설 학 원 , 문 화 센 터 , 개 인 레 슨 , 동 호 인 모 임 등 을 의 미 합 니다 .)

- ① No ( 없 다 )
- ② Yes ( 있 다 )
- Q4. Before age 18, did you receive art or exhibition-related education outside of school?
- 만 18 세 이 전 학 교 외 에 서 미 술 , 전 시 와 관 련 된 교 육을 받 은 경 험 이있으 십 니 까 ? ( 학 교 외 는 사 설 학 원 , 문 화 센 터 , 개 인 레 슨 , 동 호 인 모 임 등 을의 미 합 니다 .)
- ① No ( 없 다 )
- ② Yes ( 있 다 )
- Q5. After age 19 and before September 1, 2020, did you receive classical music, opera, or musical education outside of school?
- 만 19 세 이 후 부 터 과거 1 년 전 까 지 (2020 년 9 월 1 일 ) 학 교 외 에 서 클 래 식 음 악 , 오 페 라 , 뮤 지 컬 과 관 련 된 교 육을 받 은 경 험 이있으 십 니 까 ? ( 학 교 외 는 사 설 학 원 , 문 화 센 터 , 개 인 레 슨 , 동 호 인 모 임 등 을의 미 합 니다 .)
- ① No ( 없 다 )
- ② Yes ( 있 다 )
- Q6. After age 19 and before September 1, 2020, did you receive art or exhibition-related education outside of school?
- 만 19 세 이 후 부 터 과거 1 년 전 까 지 (2020 년 9 월 1 일 ) 학 교 외 에 서 미 술 , 전 시 와 관 련 된 교 육을 받 은 경 험 이 있으 십 니 까 ? ( 학 교 외 는 사 설 학 원 , 온 라 인 교 육 , 과 외 , 방 송 교 육 등 을의 미 합 니다 .)
- ① No ( 없 다 )
- ② Yes ( 있 다
- )
- Q7. Between September 1, 2020 and August 31, 2021, did you receive classical music, opera, or musical education outside of school?
- 지 난 1 년 전 부 터 현 재 까 지 (2020 년 9 월 1 일 -2021 년 8 월 31 일 ) 학 교 외 에 서 클 래 식 음 악 , 오 페 라 , 뮤 지 컬 연 관 된 교 육을 받 은 경 험 이있으 십 니 까 ? ( 학 교 외 는 사 설 학 원 , 온 라 인 교 육 , 과 외 , 방 송 교 육 등 을의 미 합 니다 .)
- ① No ( 아 니 오 )
- ② Yes ( 예 )
- Q8. Between September 1, 2020 and August 31, 2021, did you receive art or exhibition-related education outside of school?
- 지 난 1 년 전 부 터 현 재 까 지 (2020 년 9 월 1 일 -2021 년 8 월 31 일 ) 학 교 외 에 서 미 술 , 전 시 와 관 련 된 교 육을 받 은 경 험 이있으 십 니 까 ? ( 학 교 외 는 사 설 학 원 , 온 라 인 교 육 , 과 외 , 방 송 교 육 등 을의 미 합 니다 .)
- ① No ( 아 니 오 )
- ② Yes ( 예 )
- Q9. Did you graduate from an arts high school majoring in art or music, or did you major in an art- or music-related

field at university?

예 술 계고 등 학 교 에 서 미 술 또 는 음 악 분 야 를 전 공 으 로 졸 업 하 거 나 , 대 학 교 에 서 미 술 또 는 음 악 관 련 학 과 를 전 공 하 셨 습 니 까 ?

Art-related majors: Painting, Photography, Sculpture, Craft, Cartoon, Design, etc.

- -미 술 분 야 전 공 : 회화 , 사 진 , 조 각 , 공 예 , 만 화 , 디 자인 등

Music-related majors: Classical music, Korean traditional music, popular music, etc

- -음 악 분 야 전 공 : 클 래 식 음 악 , 국 악 , 대 중 음 악 등
- ① No ( 아 니 오 )
- ② Yes ( 예 )

## A.6 Institution Satisfaction (4 items)

- Q30. Have you ever visited the National Museum of Korea? 귀 하 께 서 는 국 립 중 앙 박 물 관 에 방 문 하 신 경 험 이 있 습 니 까 ?
- ② Yes ( 예 ) → Go to Q30-1
- ① No ( 아 니 오 ) → Skip to Q31
- Q30-1. How satisfied were you overall with your visit to the National Museum of Korea?

## 귀 하 께 서 국 립 중 앙 박 물 관 에 방 문 후 느 꼈 던 전 반 적 인 만 족 도 는 어 떠 십 니 까 ?

- ① Very dissatisfied ( 매 우 불 만 족 스 럽 다 )
- ② Dissatisfied ( 불 만 족 스 럽 다 )
- ③ Neutral ( 보 통 이 다 )
- ④ Satisfied ( 만 족 스 럽 다 )
- ⑤ Very satisfied ( 매 우 만 족 스 럽 다 )
- Q31. Have you ever visited the Seoul Arts Center ( 예 술 의 전 당 )?
- 귀 하 께 서 는 예 술 의 전 당 에 방 문 하 신 경 험 이있 습 니 까 ?
- ② Yes ( 예 ) → Go to Q31-1
- ① No ( 아 니 오 ) → Skip to Section VI
- Q31-1. How satisfied were you overall with your visit to the Seoul Arts Center?
- 귀 하 께 서 예 술 의 전 당 에 방 문 후 느 꼈 던 전 반 적 인 만 족 도 는 어 떠 십 니 까 ?
- ① Very dissatisfied ( 매 우 불 만 족 스 럽 다 )
- ② Dissatisfied ( 불 만 족 스 럽 다 )
- ③ Neutral ( 보 통 이 다 )
- ④ Satisfied ( 만 족 스 럽 다 )
- ⑤ Very satisfied ( 매 우 만 족 스 럽 다 )

## A.7 Social Norms and Attitudes (10 items)

Please respond based on your usual thoughts.

평 소 귀 하 께 서 생 각 하 시 는 것 을 토 대 로 응 답 해 주 십시 오 .

Response scale: ① Strongly Disagree ( 전 혀 그 렇 지 않 다 ), ② Disagree ( 그 렇 지 않 다 ), ③ Neutral ( 보 통 이 다 ), ④ Agree ( 그 렇 다 ), ⑤ Strongly Agree ( 매 우 그 렇 다 )

- Q1. I feel good when I act according to my conscience.
- 나 는 양 심 에 따 라 행 동 을 할 때 기 분 이 좋 다 .
- Q2. I feel guilty when I pay less than an appropriate amount. 나 는 적정 금 액 보 다 낮 은 금 액 을 지 불 했 을 때 양 심 에 걸 린 다 .
- Q3. I feel a moral obligation to buy cultural products (e.g., performances, exhibitions) even if they are expensive, if it is for charity.

나 는 자 선 단 체 기 부 를 위 해 서 라 면 문 화 예 술 상 품 ( 공 연 , 전 시 등 ) 이 비 싸 더 라 도 구 매 해 야 한 다는 도덕 적 의 무 감 을 느 낀 다 .

- Q4. I feel a moral obligation to attend cultural events (e.g., performances, exhibitions) for charity even if I am busy. 나 는 자 선 단 체 기 부 를 위 해 서 라 면 문 화 예 술 상 품 ( 공 연 , 전 시 등 ) 에 가 려 고 노 력 해 야 한 다는 도덕 적 의 무 감 을 느 낀 다 .
- Q5. If the quality of cultural products (e.g., performances, exhibitions) is good, I don't mind paying more.

나 는 문 화 예 술 상 품 ( 공 연 , 전 시 등 ) 의 질 이 좋 다 면 많 은 돈 을 지 불 할 지 라 도 개 의 치 않 는다 .

- 더
- Q6. People around me (family, friends, neighbors) will understand if I pay more to attend cultural events for charity.

나 의 주 변 사 람 들 ( 가 족 , 친 구 , 이 웃 ) 은자 선 단 체 기 부 를 위 해 서 라 면 문 화 예 술 상 품 ( 공 연 , 전 시 등 ) 관 람 에 더 많 은 돈 을 지 불 하 는 나 의 행 동 에 공감 할 것 이 다 .

- Q7. Other people's attitudes and actions influence me. 다 른 사 람 들 의 태 도 나 행 동 이 나 에 게 영 향 을 미 친 다 .
- Q8. I sometimes act against my will because I am conscious of others' criticism. 다 른 사 람 의 비 난 을 의 식 하 여 원 치 않 는 행 동 을 하 는 경 우 가 있 다 .
- Q9. I am willing to pay the same amount that others paid, even if I would normally pay less.
- 나 는 사 람 들 의 눈 을 의 식 하 여 다 른 사 람 이 지 불 한 금 액 을 기꺼 이 따 라 지 불 할 용 의 가 있 다 .
- Q10. I am willing to pay more if others around me also pay a higher amount.

다 른 사 람 들 의 눈 을의 식 하 여 다 른 사 람 이 높 은 비 용 을 지 불 하 더 라 도 기꺼 이 따 라 할 용 의 가 있 다 .

## B Detailed Question Form

This section provides the full structure of the survey instrument used in the PWYW experiment. Figures from 4 to 8 illustrate the original Korean question forms shown to participants, including survey introductions and detailed question items for both art and music domains. All questions are presented in the original Korean followed by English translations in sequence. These materials are included for refer- ence to clarify the experimental context and input provided to both human participants and LLMs.

Survey Introduction:

See Figure 4

Art Survey Introduction:

See Figure 5

Art Survey Form:

See Figure 6

Music Survey Introduction:

See Figure 7

Music Survey Form:

See Figure 8

## C Detailed Human Experiment Analysis

To help readers understand, here we provide detailed result of the original human experiment, with 522 Korean adults.

## C.1 Art Exhibition Analysis

We employed the Heckman two-step model to analyze participants' Willingness-to-Pay (WTP) for art exhibitions, addressing potential sample selection bias inherent in PayWhat-You-Want (PWYW) scenarios.

Step 1: Selection Equation (Probit Model) In this step, we compute the inverse Mills ratio ( λ i ), which can correct selection bias in the further steps. Specifically, step 1 begins with assuming the probability of participation using a probit regression:

<!-- formula-not-decoded -->

where the dependent variable A Q2 is a binary indicator for willingness to participate in PWYW for art exhibition (1 = willing, 0 = not willing). And, Φ( · ) represents the cumulative distribution function (CDF) of the standard normal distribution.

For the analysis, we included the following independent variables in vector Z :

- edu f : Father's education level (1=middle school or below, 2=high school, 3=university, 4=graduate school) from A.1, Q8
- edu m : Mother's education level (same coding) from A.1, Q9
- edu s : Respondent's education level (same coding) from A.1, Q6
- art act dum : Art activity participation dummy derived from A.2, Q1 (1 if attended art exhibition ≥ 1 time in past year, 0 otherwise)
- art att ave : Average art attitude score, computed as mean of A.3, Q7, Q10-Q15, Q19, and Q24 (5-point Likert scale attitudes toward art exhibitions, artists' professions, and cultural sophistication)
- art qz tot sco : Art knowledge total score, sum of correct answers from A.4, Q28-Q29 ('Mona Lisa' and 'The Scream' painters, maximum score = 2)
- art ca edu b18 : Art cultural education before age 18, derived from A.5, Q2+Q4 (1 if received any art-related education in or outside school before age 18, 0 otherwise)
- art ca edu a19 : Art cultural education after age 19, derived from A.5, Q6+Q8 (1 if received any art-related education outside school after age 19, 0 otherwise)
- inc mo : Monthly personal income (categorical: 1=none to 9=over 7 million KRW) from A.1, Q10
- marital dum : Marital status dummy (1=married, 0=single/other) from A.1, Q3
- gen dum : Gender dummy (0=male, 1=female) from A.1, Q1

Now, we calculate the inverse Mills ratio ( λ i ) for each observation Z i . The λ i serves as a selection correction term that accounts for potential bias arising from non-random sample selection in the PWYW decision-making process. We obtain λ i as follows:

<!-- formula-not-decoded -->

where N ( ·| 0 , 1 2 ) represents the probability density function (PDF) of the standard normal distribution.

Step 2: Outcome Equation (Linear Regression with Selection Correction) Step 2 estimates willingness to pay amounts, corrected for selection bias using inverse Mills ratio λ :

<!-- formula-not-decoded -->

where the dependent variable art pwyw log wtp is the natural logarithm of WTP amount for art exhibition in KRW. And, X is the vector representing independent variables with all Z variables plus:

- social n : Social norm score from A.7, Q7 to Q10 (5point Likert scale measuring social influence on behavior)
- moral n : Moral norm score from A.7, Q2 to Q4 (5point Likert scale measuring moral obligations and conscience)

## C.2 Music Performance Analysis

The music analysis follows almost identical methodology where domain-specific variables changed to music-related variables, to analyze participants' WTP for music performances.

## Step 1: Selection Equation (Probit Model)

<!-- formula-not-decoded -->

where the dependent variable M Q2 is a binary indicator for willingness to participate in PWYW for music performance. And, the Z vector representing the following independent variables:

- edu f , edu m , edu s : Education variables (identical to art model)
- mus act dum : Music activity participation dummy derived from A.2, Q2 (1 if attended classical music/opera ≥ 1 time in past year, 0 otherwise)
- mus att ave : Average music attitude score, computed as mean of A.3, Q7, Q10-Q18, Q20-Q23, and Q25 (5point Likert scale attitudes toward classical music, opera, traditional music, and dance performances and professions, plus cultural sophistication)
- mus qz tot sco : Music knowledge total score, sum of correct answers from A.4, Q26-Q27 (Symphony 'Fate' composer and 'Rigoletto' composer, maximum score = 2)
- mus ca edu b18 : Music cultural education before age 18, derived A.5, Q1+Q3 (1 if received any music-related education in or outside school before age 18, 0 otherwise)
- mus ca edu a19 : Music cultural education after age 19, derived from A.5, Q5+Q7 (1 if received any musicrelated education outside school after age 19, 0 otherwise)
- Sociodemographic controls: inc mo , marital dum , gen dum (identical to art model)

## Step 2: Outcome Equation

<!-- formula-not-decoded -->

where the dependent variable mus pwyw log wtp is the natural logarithm of WTP amount for music performance. X represents the set of independent variables including all variables in Z plus:

- social n ave : Average social norm score from A.7, Q7 to Q10
- moral n ave : Average moral norm score from A.7, Q2 to Q4

## C.3 Data Processing and Quality Control

## Sample Selection Criteria

- Minimum 10 observations per group to ensure the convergence of statistical model
- Minimum 2 categories in selection variable to satisfy variance requirements
- Minimum 5 observations with positive WTP among those willing to participate

## Variable Transformations

- WTP Amount : We applied natural logarithm transformation to address skewness and heteroskedasticity.
- Cultural Education : Binary coding by re-categorizing experiences into formal (school) and informal (outside school) education experiences.
- Attitude Scores : Standardized averaging across relevant Likert scale items
- Knowledge Scores : Simple summation of correctly answered responses

Extracted Summary of Statistical Model For each successful model estimation, we extracted:

- ρ : Correlation between error terms in selection and outcome equations
- σ : Standard deviation of outcome equation error term
- Wald χ 2 : Statistics from the test of overall model significance
- McFadden R 2 : Pseudo R-squared about the fitness of selection equation
- Log likelihood: Indicator of fitness of statistical model
- Sample composition: N selected and N nonselected observations
- The statistical significance of the inverse Mills ratio ( λ ): Whether sample selection bias correction is necessary for valid inference

## D Persona Input Formats

Here, we illustrate how we provided the given persona as an input to LLMs.

## D.1 Survey Format

In the Survey format condition, persona information was presented in a structured question-answer format in Korean, directly mirroring the original questionnaire structure used in the human experiment. Each persona was input as a systematic compilation of responses across all 65 survey items from the seven main categories described in Section A, maintaining the original Korean language to ensure linguistic consistency with the human experimental conditions.

Thus, the persona information was structured as follows:

```
What is your gender? : [Male/Female] What is your age? : [Age in years] ...
```

## D.2 Storytelling Format

In the Storytelling format condition, the same 65 survey items were transformed into cohesive biographical narratives using GPT-4o to create personalized life stories that naturally incorporated all persona attributes.

## D.3 Prompt for generating narratives

The following prompt was used to generate storytelling format in Korean:

## Original Korean Prompt:

아 래 페 르 소 나 정 보 를 기 반 으 로 , 한 여 성 인 물 이자 신 의 삶 에 서 예 술 을 어 떻 게 받 아 들 이 고 이 해해 왔 는 지 를 고 백 적 으 로 풀 어 내 는 허 구 수 필 을작 성 하 세 요 .

- 텍 스 트 에 는 어 떤 소 제 목 , 부 제 , 섹션 제 목 도 포 함 되 어 서 는 안 됩 니다 .
- 자 연 스 러 운 단 락 구 분 은 허 용 되 지 만 , 시 각 적 강 조 나 구 획 나 눔 은 삼 가 세 요 .
- 전 체 흐 름 은 시 간 순 이 아 니 어 도 되 며 , 자유 롭 게 떠 오 르 는 기 억 의 방 식 으 로 구 성 해 도 좋 습 니다 .
- 지 나 치 게 극 적 인 연 출 은 피하 며 사 실 적 인 정 서 에 기 반 해 구 성 하 세 요 .
- 분 량 은 약 5000 토 큰 으 로 , 읽 는 이 로 하 여 금 한 사 람 의 내 면 을 들 여 다 보 는 느 낌 을 받 을 수 있 어야 합 니다 .
- [PERSONA INFORMATION]

## English Translation:

Based on the persona information below, write a confessional fictional essay that tells how a woman has embraced and understood art throughout her life.

- The text should not include any subtitles, subtitles, or section titles.
- Natural paragraph breaks are allowed, but visual emphasis or partitioning should be avoided.
- The overall flow does not have to be chronological, and can be freely composed in the way of emerging memories.
- Avoid overly dramatic production and compose based on realistic emotions.
- The volume should be about 5000 tokens, so that the reader should feel like looking into the inner side of a person.
- [PERSONA INFORMATION]

Weused the following environment to generate narratives.

- API : OpenAI official API
- Model : GPT-4o
- Temperature : 0
- Max tokens : 6,000

## E Detailed Result for RQ1

This section presents the regression outcomes of the RQ1 experimental conditions using the Heckman two-step model. Each table pair (Tables from 3 to 6) summarizes how LLMs (GPT-4o, LLaMA, Qwen) reflect persona attributes when predicting willingness-to-pay decisions in the PWYW task. The tables are provided for reference to illustrate modellevel behavioral patterns under different interaction settings.

Sequential Condition

See Tables 3 and 4.

Human-Guided Condition

See Tables 5 and 6.

## F Detailed Result for RQ2

This section presents the regression outcomes of various RQ2 experimental conditions using the Heckman two-step model. Each table pair (Tables from 7 to 18) summarizes how LLMs (GPT-4o, LLaMA, Qwen) reflect persona attributes under different combinations of persona format (Survey vs. Storytelling) and prompting method (Base, CoT, RAG, Few-shot). The tables are provided for reference to illustrate model-level behavioral patterns.

| Survey Format - CoT See    | Tables 7 and 8       |
|----------------------------|----------------------|
| Survey Format - RAG        | See Tables 9 and 10  |
| Survey Format - Few-shot   | See Tables 11 and 8  |
| Storytelling Format - Base | See Tables 13 and 14 |
| Storytelling Format - CoT  | See Tables 15 and 16 |
| Storytelling Format - RAG  | See Tables 17 and 18 |

## G RQ2 Heatmap

This section presents response distribution heatmaps for each experimental condition under RQ2. Figures from 9 to 14 visualize how LLM-generated willingness-to-pay responses vary depending on persona format (Survey vs. Storytelling) and prompting method (Base, CoT, RAG, Fewshot). Each figure corresponds to a specific combination

Table 3: Regression outcomes of Structure Condition on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o    | GPT-4o   | LLaMA   | LLaMA     | LLaMA   | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|-----------|----------|---------|-----------|---------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value   | z value  | coeff   | std error | p value | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |           |          |         |           |         |         |        |           |            |         |
| edu f            | 0.01     | 0.01      | 0.21      | 1.26     | 0.04    | 21694.32  | 1.00    | 0.00    | 0.01   | 0.02      | 0.51       | 0.66    |
| edu m            | -0.01    | 0.01      | 0.12      | -1.57    | -0.03   | 25017.10  | 1.00    | 0.00    | 0.00   | 0.02      | 0.90       | 0.13    |
| mus act dum      | 0.02     | 0.01      | p < 0.05  | 2.00     | -0.02   | 303822.33 | 1.00    | 0.00    | 0.06   | 0.03      | p < 0.05   | 2.38    |
| mus att ave      | 0.02     | 0.02      | 0.24      | 1.18     | 0.19    | 22875.96  | 1.00    | 0.00    | 0.26   | 0.03      | p < 0.0001 | 0.02    |
| mus ca edu a19   | 0.00     | 0.01      | 0.52      | 0.64     | -0.03   | 24289.04  | 1.00    | 0.00    | 0.03   | 0.02      | 0.19       | 10.00   |
| mus ca edu b18   | 0.00     | 0.01      | 0.64      | 0.47     | 0.06    | 18689.85  | 1.00    | 0.00    | 0.00   | 0.02      | 0.86       | 1.31    |
| mus qz tot sco   | 0.01     | 0.01      | 0.42      | 0.81     | 0.12    | 25466.45  | 1.00    | 0.00    | 0.05   | 0.02      | p < 0.05   | 0.18    |
| moral n ave      | 0.00     | 0.01      | 0.90      | 0.12     | 0.04    | 21456.43  | 1.00    | 0.00    | 0.04   | 0.02      | p < 0.05   | 2.12    |
| social n ave     | 0.00     | 0.01      | 0.65      | -0.46    | 0.04    | 19449.28  | 1.00    | 0.00    | 0.00   | 0.02      | 0.94       | 0.08    |
| inc mo           | 0.00     | 0.00      | 0.87      | -0.16    | 0.03    | 7365.53   | 1.00    | 0.00    | 0.00   | 0.01      | 0.65       | 0.45    |
| matarial dum     | 0.00     | 0.01      | 0.71      | 0.37     | 0.08    | 27206.99  | 1.00    | 0.00    | 0.04   | 0.02      | 0.66       | 1.88    |
| constant         | 8.98     | 0.08      | p < 0.001 | 106.26   | 7.33    | 103897.22 | 1.00    | 0.00    | 7.28   | 0.12      | p < 0.0001 | 61.51   |
| Model Statistics |          |           |           |          |         |           |         |         |        |           |            |         |
| Wald χ 2         |          | 9.59      |           |          |         | 3.1 × 10  | - 10    |         |        | 183.19    |            |         |
| ρ                |          | 0.69      |           |          |         | 1         |         |         |        | 0.73      |            |         |
| σ                |          | 0.07      |           |          |         | 299218.13 |         |         |        | 0.25      |            |         |
| Log Likelihood   |          | -201.81   |           |          |         | -         |         |         |        | -83.74    |            |         |
| McFadden R 2     |          | 0.44      |           |          |         | -         |         |         |        | 0.59      |            |         |
| N nonselected    |          | 268       |           |          |         | 1         |         |         |        |           | 69         |         |
| N selected       |          | 254       |           |          |         | 521       |         |         |        | 453       |            |         |

Table 4: Regression outcomes of Structure Condition on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA     | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|-----------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value   | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |           |         |        |           |            |         |
| edu f            | -0.01    | 0.02      | 0.64       | -0.47    | 0.04    | 21694.32  | 1.00      | 0.00    | 0.01   | 0.02      | 0.51       | 0.66    |
| edu m            | 0.00     | 0.03      | 0.10       | 0.01     | -0.03   | 25017.10  | 1.00      | 0.00    | 0.00   | 0.02      | 0.90       | 0.13    |
| mus act dum      | 0.05     | 0.04      | 0.19       | 1.30     | -0.02   | 30822.33  | 1.00      | 0.00    | 0.06   | 0.03      | p < 0.05   | 2.38    |
| mus att ave      | 0.19     | 0.06      | p < 0.01   | 3.17     | 0.19    | 22875.96  | 1.00      | 0.00    | 0.26   | 0.03      | p < 0.0001 | 10.00   |
| mus ca edu a19   | 0.00     | 0.02      | 0.92       | -0.11    | -0.03   | 24289.04  | 1.00      | 0.00    | 0.03   | 0.02      | 0.19       | 1.31    |
| mus ca edu b18   | 0.03     | 0.02      | 0.16       | -1.39    | 0.06    | 18689.85  | 1.00      | 0.00    | 0.00   | 0.02      | 0.86       | 0.18    |
| mus qz tot sco   | 0.00     | 0.02      | 0.85       | -0.19    | 0.12    | 25466.48  | 1.00      | 0.00    | 0.05   | 0.02      | p < 0.05   | 2.15    |
| moral n ave      | 0.04     | 0.02      | 0.09       | 1.67     | 0.04    | 21456.43  | 1.00      | 0.00    | 0.04   | 0.02      | p < 0.05   | 2.12    |
| social n ave     | 0.01     | 0.02      | 0.08       | 0.51     | 0.04    | 19449.28  | 1.00      | 0.00    | 0.00   | 0.02      | 0.94       | 0.08    |
| inc mo           | 0.01     | 0.01      | 0.71       | 1.74     | 0.03    | 7365.53   | 1.00      | 0.00    | 0.00   | 0.01      | 0.65       | 0.45    |
| matarial dum     | 0.01     | 0.03      | p < 0.05   | 0.36     | 0.08    | 27206.99  | 1.00      | 0.00    | 0.04   | 0.02      | 0.06       | 1.88    |
| constant         | 8.87     | 0.24      | p < 0.0001 | 36.91    | 7.33    | 103897.22 | 1.00      | 0.00    | 7.28   | 0.12      | p < 0.0001 | 61.51   |
| Model Statistics |          |           |            |          |         |           |           |         |        |           |            |         |
| Wald χ 2         |          | 9.59      |            |          |         | 3.1 ×     | 10 - 10   |         |        |           | 183.19     |         |
| ρ                |          | 0.69      |            |          |         | 1         |           |         |        |           | 0.73       |         |
| σ                |          | 0.07      |            |          |         |           | 299218.13 |         |        |           | 0.25       |         |
| Log Likelihood   |          | -201.81   |            |          |         | -         |           |         |        |           | -83.74     |         |
| McFadden R 2     |          | 0.44      |            |          |         | -         |           |         |        |           | 0.59       |         |
| N nonselected    |          | 268       |            |          |         | 1         |           |         |        |           | 69         |         |
| N selected       |          | 254       |            |          |         |           | 521       |         |        |           | 453        |         |

Table 5: Regression outcomes of Human-Guided Condition on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | -0.02    | 0.05      | 0.73       | -0.34    | 0.03  | 0.08      | 0.71       | 0.37    | -0.09  | 0.17      | 0.58       | -0.55   |
| edu m            | 0.04     | 0.06      | 0.47       | 0.72     | -0.02 | 0.09      | 0.82       | -0.22   | 0.12   | 0.20      | 0.53       | 0.62    |
| mus act dum      | -0.04    | 0.12      | 0.73       | -0.34    | 0.14  | 0.19      | 0.47       | -0.72   | -0.25  | 0.41      | 0.54       | -0.62   |
| mus att ave      | 0.07     | 0.11      | 0.48       | 0.70     | 0.11  | 0.17      | 0.55       | 0.60    | -0.25  | 0.37      | 0.50       | -0.67   |
| mus ca edu a19   | 0.01     | 0.04      | 0.75       | 0.32     | 0.04  | 0.05      | 0.50       | 0.68    | -0.06  | 0.13      | 0.63       | -0.48   |
| mus ca edu b18   | -0.04    | 0.05      | 0.40       | -0.84    | -0.03 | 0.08      | 0.76       | -0.31   | -0.12  | 0.18      | 0.50       | -0.68   |
| mus qz tot sco   | -0.02    | 0.05      | 0.67       | -0.43    | 0.03  | 0.08      | 0.72       | 0.35    | -0.08  | 0.17      | 0.62       | -0.50   |
| moral n ave      | 0.04     | 0.03      | 0.19       | 1.30     | 0.10  | 0.05      | p < 0.05   | 2.07    | -0.02  | 0.10      | 0.87       | -0.17   |
| social n ave     | 0.00     | 0.03      | 0.93       | 0.08     | 0.03  | 0.05      | 0.49       | 0.69    | 0.07   | 0.09      | 0.46       | 0.74    |
| inc mo           | 0.01     | 0.01      | 0.28       | 1.09     | 0.03  | 0.07      | 0.05       | 1.93    | -0.01  | 0.04      | 0.76       | -0.31   |
| matarial dum     | 0.01     | 0.05      | 0.90       | 0.13     | 0.00  | 0.92      | 0.94       | 0.07    | -0.03  | 0.16      | 0.83       | -0.22   |
| constant         | 8.50     | 0.56      | p < 0.0001 | 15.28    | 7.68  | 1.65      | p < 0.0001 | 8.32    | 9.91   | 1.95      | p < 0.0001 | 5.08    |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 20.11     |            |          |       |           | 17.88      |         |        | 2.04      |            |         |
| ρ                |          | -1        |            |          |       |           | 0.02       |         |        |           | -1         |         |
| σ                |          | 0.46      |            |          |       |           | 0.62       |         |        | 1.60      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 6: Regression outcomes of Human-Guided Condition on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.09    | 0.05      | 0.05       | -1.95    | -0.05   | 0.06      | 0.41       | -0.82   | -0.04  | 0.03      | 0.20       | -1.29   |
| edu m            | -0.03    | 0.05      | 0.54       | 0.61     | -0.02   | 0.05      | 0.65       | -0.46   | -0.02  | 0.03      | 0.63       | -0.48   |
| mus act dum      | -0.09    | 0.11      | 0.39       | -0.85    | -0.02   | 0.12      | 0.89       | -0.13   | -0.03  | 0.07      | 0.70       | -0.38   |
| mus att ave      | -0.08    | 0.14      | 0.57       | -0.57    | -0.10   | 0.17      | 0.57       | -0.57   | 0.00   | 0.10      | 0.98       | -0.02   |
| mus ca edu a19   | 0.02     | 0.04      | 0.69       | 0.40     | 0.04    | 0.05      | 0.38       | 0.88    | 0.03   | 0.03      | 0.38       | 0.87    |
| mus ca edu b18   | 0.00     | 0.04      | 0.91       | 0.11     | -0.02   | 0.05      | 0.61       | -0.51   | -0.02  | 0.03      | 0.51       | -0.66   |
| mus qz tot sco   | 0.05     | 0.05      | 0.30       | 1.04     | 0.11    | 0.06      | p < 0.05   | 2.03    | 0.06   | 0.03      | 0.07       | 1.84    |
| moral n ave      | 0.13     | 0.03      | p < 0.0001 | 3.95     | 0.13    | 0.04      | p < 0.0001 | 2.99    | 0.02   | 0.02      | 0.37       | -0.90   |
| social n ave     | -0.01    | 0.03      | 0.73       | -0.34    | -0.02   | 0.04      | 0.70       | -0.39   | 0.02   | 0.02      | 0.38       | 0.88    |
| inc mo           | 0.03     | 0.01      | p < 0.05   | 2.27     | -0.03   | 0.02      | 0.09       | 1.70    | 0.01   | 0.01      | 0.44       | 0.78    |
| matarial dum     | -0.04    | 0.05      | 0.46       | -0.73    | -0.04   | 0.06      | 0.46       | -0.75   | 0.01   | 0.04      | 0.82       | 0.23    |
| constant         | 9.61     | 0.59      | p < 0.0001 | 16.24    | 9.75    | 0.72      | p < 0.0001 | 13.52   | 9.77   | 0.42      | p < 0.0001 | 23.22   |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 39.04     |            |          |         |           | 31.44      |         |        | 20.32     |            |         |
| ρ                |          | -0.98     |            |          |         |           | -0.54      |         |        | -0.87     |            |         |
| σ                |          | 0.49      |            |          |         |           | 0.53       |         |        | 0.34      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | 290.01     |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 7: Regression outcomes of Survey CoT on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | 0.00     | 0.05      | 0.99       | -0.01    | -0.01 | 0.02      | 0.60       | -0.52   | 0.03   | 0.03      | 0.31       | 1.01    |
| edu m            | 0.01     | 0.06      | 0.92       | 0.10     | 0.04  | 0.03      | 0.15       | 1.44    | -0.01  | 0.03      | 0.84       | -0.20   |
| mus act dum      | 0.08     | 0.13      | 0.51       | 0.66     | 0.00  | 0.05      | 0.95       | 0.06    | 0.08   | 0.06      | 0.19       | 1.32    |
| mus att ave      | 0.21     | 0.11      | 0.07       | 1.81     | 0.05  | 0.05      | 0.29       | 1.05    | 0.14   | 0.06      | p < 0.05   | 2.47    |
| mus ca edu a19   | 0.00     | 0.04      | 0.97       | -0.04    | 0.00  | 0.02      | 0.80       | 0.25    | 0.01   | 0.02      | 0.75       | 0.32    |
| mus ca edu b18   | 0.03     | 0.05      | 0.56       | 0.58     | -0.01 | 0.02      | 0.75       | -0.32   | -0.01  | 0.03      | 0.74       | -0.33   |
| mus qz tot sco   | 0.04     | 0.05      | 0.48       | 0.71     | -0.02 | 0.02      | 0.32       | -0.99   | 0.01   | 0.03      | 0.72       | 0.36    |
| moral n ave      | 0.04     | 0.03      | 0.16       | 1.42     | 0.03  | 0.01      | 0.07       | 1.79    | 0.01   | 0.02      | 0.43       | 0.80    |
| social n ave     | -0.01    | 0.03      | 0.79       | -0.27    | 0.00  | 0.01      | 0.80       | 0.25    | 0.00   | 0.01      | 0.78       | -0.28   |
| inc mo           | 0.01     | 0.01      | 0.48       | 0.70     | 0.00  | 0.01      | 0.38       | 0.88    | 0.00   | 0.01      | 0.79       | -0.27   |
| matarial dum     | 0.04     | 0.05      | 0.39       | 0.86     | 0.01  | 0.02      | 0.58       | 0.55    | 0.01   | 0.02      | 0.53       | 0.62    |
| constant         | 7.71     | 0.60      | p < 0.0001 | 12.85    | 8.62  | 0.27      | p < 0.0001 | 32.51   | 8.11   | 0.29      | p < 0.0001 | 27.55   |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 16.42     |            |          |       |           | 37.77      |         |        | 26.87     |            |         |
| ρ                |          | 1.00      |            |          |       |           | -0.43      |         |        | 0.86      |            |         |
| σ                |          | 0.49      |            |          |       |           | 0.18       |         |        | 0.23      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 8: Regression outcomes of Survey CoT on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.10    | 0.07      | 0.13       | -1.50    | -0.03   | 0.06      | 0.53       | -0.63   | -0.06  | 0.05      | 0.28       | -1.08   |
| edu m            | 0.03     | 0.07      | 0.62       | 0.49     | -0.02   | 0.05      | 0.64       | -0.46   | 0.00   | 0.05      | 0.93       | -0.08   |
| mus act dum      | -0.16    | 0.15      | 0.29       | -1.07    | -0.02   | 0.12      | 0.89       | -0.14   | -0.03  | 0.12      | 0.81       | -0.24   |
| mus att ave      | -0.07    | 0.20      | 0.71       | -0.37    | -0.12   | 0.17      | 0.50       | -0.68   | -0.16  | 0.16      | 0.34       | -0.96   |
| mus ca edu a19   | 0.03     | 0.06      | 0.60       | 0.52     | 0.03    | 0.05      | 0.50       | 0.68    | 0.03   | 0.05      | 0.55       | 0.61    |
| mus ca edu b18   | -0.04    | 0.06      | 0.53       | -0.62    | -0.02   | 0.05      | 0.63       | -0.48   | -0.03  | 0.05      | 0.52       | -0.64   |
| mus qz tot sco   | 0.04     | 0.07      | 0.53       | 0.63     | 0.11    | 0.06      | 0.05       | 1.95    | 0.11   | 0.06      | p < 0.05   | 2.05    |
| moral n ave      | 0.07     | 0.05      | 0.10       | 1.63     | 0.13    | 0.04      | p < 0.0001 | 3.12    | 0.09   | 0.04      | p < 0.05   | 2.20    |
| social n ave     | 0.02     | 0.04      | 0.59       | 0.54     | -0.02   | 0.04      | 0.71       | -0.38   | 0.04   | 0.04      | 0.32       | 0.98    |
| inc mo           | 0.02     | 0.02      | 0.31       | 1.01     | 0.02    | 0.02      | 0.14       | 1.48    | 0.02   | 0.02      | 0.29       | 1.06    |
| matarial dum     | 0.01     | 0.07      | 0.92       | 0.10     | -0.07   | 0.06      | 0.27       | -1.11   | -0.03  | 0.06      | 0.58       | -0.56   |
| constant         | 9.69     | 0.83      | p < 0.0001 | 11.68    | 9.80    | 0.72      | p < 0.0001 | 13.65   | 10.00  | 0.69      | p < 0.0001 | 14.43   |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 14.54     |            |          |         |           | 29.98      |         |        | 23.01     |            |         |
| ρ                |          | -1.00     |            |          |         |           | -0.58      |         |        | -0.90     |            |         |
| σ                |          | 0.70      |            |          |         |           | 0.53       |         |        | 0.56      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 9: Regression outcomes of Survey RAG on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | 0.01     | 0.04      | 0.75       | -0.32    | 0.02  | 0.02      | 0.46       | 0.73    | 0.00   | 0.01      | 0.97       | -0.04   |
| edu m            | -0.01    | 0.04      | 0.84       | -0.21    | 0.02  | 0.02      | 0.51       | 0.65    | 0.01   | 0.01      | 0.39       | 0.85    |
| mus act dum      | 0.08     | 0.09      | 0.36       | -1.59    | -0.03 | 0.05      | 0.56       | -0.58   | 0.00   | 0.02      | 0.88       | 0.15    |
| mus att ave      | 0.13     | 0.08      | 0.11       | -0.37    | 0.06  | 0.05      | 0.21       | 1.26    | 0.00   | 0.02      | 0.81       | 0.25    |
| mus ca edu a19   | -0.01    | 0.03      | 0.71       | -0.57    | 0.00  | 0.02      | 0.98       | 0.03    | -0.01  | 0.01      | 0.08       | -1.73   |
| mus ca edu b18   | 0.02     | 0.04      | 0.57       | -0.17    | -0.02 | 0.02      | 0.32       | -0.99   | 0.00   | 0.01      | 0.92       | -0.10   |
| mus qz tot sco   | -0.01    | 0.04      | 0.86       | 0.14     | 0.00  | 0.02      | 0.83       | -0.21   | -0.01  | 0.01      | 0.05       | -1.96   |
| moral n ave      | 0.00     | 0.02      | 0.89       | -0.03    | -0.01 | 0.01      | 0.45       | -0.76   | 0.00   | 0.00      | 0.32       | -0.99   |
| social n ave     | 0.00     | 0.02      | 0.97       | -0.06    | 0.00  | 0.01      | 0.81       | -0.24   | 0.01   | 0.00      | 0.17       | 1.36    |
| inc mo           | 0.00     | 0.01      | 0.95       | 0.36     | 0.00  | 0.00      | 0.70       | -0.39   | 0.00   | 0.00      | 0.38       | 0.87    |
| matarial dum     | 0.01     | 0.04      | 0.72       | 0.36     | 0.01  | 0.02      | 0.70       | -0.38   | 0.00   | 0.01      | 0.83       | -0.21   |
| constant         | 8.35     | 0.44      | p < 0.0001 | 19.19    | 8.41  | 0.26      | p < 0.0001 | -32.65  | 8.51   | 0.09      | p < 0.0001 | -95.45  |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 10.45     |            |          |       |           | 28.81      |         |        | 15.87     |            |         |
| ρ                |          | 1.00      |            |          |       |           | -0.25      |         |        | -0.33     |            |         |
| σ                |          | 0.36      |            |          |       |           | 0.18       |         |        | 0.06      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 10: Regression outcomes of Survey RAG on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.05    | 0.03      | 0.14       | -1.49    | -0.06   | 0.03      | 0.06       | -1.85   | -0.08  | 0.06      | 0.14       | -1.48   |
| edu m            | 0.00     | 0.03      | 0.97       | -0.03    | 0.02    | 0.03      | 0.56       | 0.58    | -0.01  | 0.05      | 0.86       | -0.18   |
| mus act dum      | -0.03    | 0.07      | 0.70       | -0.38    | -0.06   | 0.07      | 0.39       | -0.85   | -0.24  | 0.12      | p < 0.05   | -2.02   |
| mus att ave      | 0.02     | 0.10      | 0.82       | 0.23     | -0.05   | 0.10      | 0.61       | -0.51   | 0.11   | 0.17      | 0.53       | -0.63   |
| mus ca edu a19   | 0.03     | 0.03      | 0.23       | 1.21     | 0.02    | 0.03      | 0.58       | 0.55    | -0.05  | 0.05      | 0.27       | -1.11   |
| mus ca edu b18   | -0.01    | 0.03      | 0.71       | -0.38    | -0.04   | 0.03      | 0.14       | -1.49   | 0.00   | 0.05      | 0.95       | -0.06   |
| mus qz tot sco   | 0.06     | 0.03      | p < 0.05   | 2.05     | 0.03    | 0.03      | 0.30       | 1.04    | 0.00   | 0.06      | 0.94       | -0.07   |
| moral n ave      | 0.04     | 0.02      | 0.13       | 1.51     | 0.03    | 0.02      | 0.26       | 1.12    | -0.07  | 0.05      | 0.13       | -1.51   |
| social n ave     | 0.03     | 0.02      | 0.22       | 1.22     | 0.02    | 0.02      | 0.31       | 1.02    | 0.07   | 0.04      | 0.09       | -1.68   |
| inc mo           | 0.01     | 0.01      | 0.14       | 1.49     | 0.00    | 0.01      | 0.65       | 0.46    | 0.01   | 0.02      | 0.38       | -0.88   |
| matarial dum     | 0.01     | 0.03      | 0.82       | 0.23     | 0.01    | 0.04      | 0.88       | 0.15    | -0.06  | 0.06      | 0.35       | -0.93   |
| constant         | 9.32     | 0.41      | p < 0.0001 | 22.70    | 10.08   | 0.41      | p < 0.0001 | 24.34   | 9.81   | 0.73      | p < 0.0001 | -13.47  |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 30.46     |            |          |         |           | 14.85      |         |        | 22.56     |            |         |
| ρ                |          | -0.45     |            |          |         |           | -1.00      |         |        | -0.11     |            |         |
| σ                |          | 0.30      |            |          |         |           | 0.35       |         |        | 0.51      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -590.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 11: Regression outcomes of Survey few-shot on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o   | GPT-4o   |       |           |          |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|----------|----------|-------|-----------|----------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value  | z value  | coeff | std error | p value  | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |          |          |       |           |          |         |        |           |            |         |
| edu f            | -0.22    | 0.34      | 0.53     | -0.63    | -0.04 | 0.40      | 0.92     | -0.10   | 0.03   | 0.03      | 0.46       | 0.74    |
| edu m            | 0.26     | 0.40      | 0.51     | -0.66    | 0.05  | 0.46      | 0.91     | 0.11    | -0.03  | 0.04      | 0.51       | -0.65   |
| mus act dum      | -0.48    | 0.82      | 0.56     | -0.59    | 0.32  | 0.98      | 0.75     | 0.32    | 0.04   | 0.08      | 0.62       | -0.50   |
| mus att ave      | -0.10    | 0.75      | 0.89     | -0.14    | -0.32 | 0.89      | 0.72     | -0.35   | 0.09   | 0.08      | 0.24       | 1.17    |
| mus ca edu a19   | -0.02    | 0.27      | 0.95     | -0.06    | -0.29 | 0.30      | 0.33     | -0.97   | 0.00   | 0.03      | 0.97       | -0.04   |
| mus ca edu b18   | -0.21    | 0.36      | 0.55     | -0.60    | -0.12 | 0.42      | 0.78     | -0.28   | 0.02   | 0.04      | 0.53       | 0.63    |
| mus qz tot sco   | 0.12     | 0.34      | 0.73     | 0.34     | 0.16  | 0.40      | 0.68     | 0.41    | 0.02   | 0.03      | 0.55       | 0.59    |
| moral n ave      | 0.21     | 0.20      | 0.31     | 1.02     | -0.25 | 0.25      | 0.32     | -0.99   | 0.00   | 0.02      | 0.93       | -0.08   |
| social n ave     | -0.05    | 0.19      | 0.79     | -0.26    | 0.23  | 0.23      | 0.32     | 0.99    | 0.02   | 0.02      | 0.36       | 0.92    |
| inc mo           | 0.03     | 0.08      | 0.70     | 0.38     | -0.09 | 0.09      | 0.35     | -0.94   | 0.00   | 0.01      | 0.57       | 0.56    |
| matarial dum     | -0.03    | 0.32      | 0.92     | -0.09    | -0.75 | 0.36      | p < 0.05 | -2.07   | 0.00   | 0.03      | 0.95       | 0.06    |
| constant         | 9.01     | 3.93      | p < 0.05 | 2.30     | -8.45 | 4.71      | 0.07     | 1.79    | 8.44   | 0.40      | p < 0.0001 | 21.17   |
| Model Statistics |          |           |          |          |       |           |          |         |        |           |            |         |
| Wald χ 2         |          | 3.82      |          |          |       | 21.44     |          |         |        | 5.55      |            |         |
| rho              |          | -1.00     |          |          |       | -0.76     |          |         |        | 1.00      |            |         |
| σ                |          | 3.23      |          |          |       |           | 3.53     |         |        | 0.33      |            |         |
| Log Likelihood   |          | -250.78   |          |          |       | -250.78   |          |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |          |          |       | 0.08      |          |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |          |          |       |           | 113      |         |        | 113       |            |         |
| N selected       |          | 409       |          |          |       |           | 409      |         |        | 409       |            |         |

Table 12: Regression outcomes of Survey few-shot on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.14    | 0.12      | 0.24       | -1.17    | -0.04   | 0.21      | 0.84       | -0.20   | -0.03  | 0.02      | 0.14       | -1.47   |
| edu m            | 0.05     | 0.12      | 0.68       | -0.41    | -0.02   | 0.21      | 0.94       | -0.07   | 0.01   | 0.02      | 0.78       | 0.27    |
| mus act dum      | -0.21    | 0.28      | 0.45       | -0.75    | -0.36   | 0.47      | 0.45       | -0.75   | -0.01  | 0.05      | 0.90       | -0.13   |
| mus att ave      | -0.27    | 0.36      | 0.46       | -0.74    | -0.54   | 0.62      | 0.39       | -0.87   | 0.06   | 0.07      | 0.44       | 0.77    |
| mus ca edu a19   | 0.01     | 0.12      | 0.93       | 0.09     | 0.01    | 0.20      | 0.98       | 0.03    | 0.04   | 0.02      | 0.08       | 1.74    |
| mus ca edu b18   | -0.05    | 0.11      | 0.67       | -0.43    | -0.10   | 0.18      | 0.59       | -0.54   | -0.02  | 0.02      | 0.42       | -0.80   |
| mus qz tot sco   | -0.01    | 0.12      | 0.96       | -0.05    | 0.11    | 0.21      | 0.60       | 0.52    | 0.04   | 0.02      | 0.07       | 1.78    |
| moral n ave      | 0.11     | 0.08      | 0.20       | 1.29     | 0.18    | 0.14      | 0.21       | 1.25    | 0.03   | 0.02      | 0.06       | 1.85    |
| social n ave     | 0.01     | 0.08      | 0.91       | 0.11     | 0.08    | 0.14      | 0.57       | 0.57    | 0.01   | 0.02      | 0.45       | 0.76    |
| inc mo           | 0.03     | 0.04      | 0.39       | 0.86     | 0.02    | 0.06      | 0.73       | -0.34   | 0.03   | 0.01      | p < 0.0001 | 4.12    |
| matarial dum     | 0.05     | 0.13      | 0.71       | 0.38     | -0.03   | 0.23      | 0.90       | -0.13   | -0.02  | 0.03      | 0.41       | -0.83   |
| constant         | 10.52    | 1.54      | p < 0.0001 | 6.85     | 11.30   | 2.63      | p < 0.0001 | 4.29    | 9.52   | 0.30      | p < 0.0001 | -31.25  |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 5.72      |            |          |         |           | 3.92       |         |        | 45.74     |            |         |
| rho              |          | -1.00     |            |          |         |           | -1.00      |         |        | -0.55     |            |         |
| σ                |          | 1.29      |            |          |         |           | 2.21       |         |        | 0.22      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 13: Regression outcomes of Storytelling Base on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | 0.02     | 0.07      | 0.76       | 0.30     | -0.07 | 0.08      | 0.38       | -0.87   | 0.00   | 0.00      | 0.73       | -0.35   |
| edu m            | -0.01    | 0.08      | 0.91       | -0.11    | 0.09  | 0.09      | 0.30       | 1.03    | 0.00   | 0.00      | 0.20       | 1.27    |
| mus act dum      | 0.12     | 0.17      | 0.48       | 0.71     | -0.13 | 0.19      | 0.50       | -0.68   | 0.00   | 0.00      | 0.42       | -0.80   |
| mus att ave      | 0.19     | 0.15      | 0.21       | 1.25     | 0.04  | 0.17      | 0.82       | 0.22    | 0.00   | 0.00      | 0.36       | -0.92   |
| mus ca edu a19   | -0.03    | 0.05      | 0.53       | -0.63    | 0.01  | 0.06      | 0.82       | 0.22    | 0.00   | 0.00      | 0.13       | 1.53    |
| mus ca edu b18   | 0.05     | 0.07      | 0.50       | 0.68     | -0.03 | 0.08      | 0.74       | -0.33   | 0.00   | 0.00      | 0.75       | -0.32   |
| mus qz tot sco   | 0.01     | 0.07      | 0.90       | 0.12     | -0.06 | 0.08      | 0.46       | -0.74   | 0.00   | 0.00      | 0.90       | -0.12   |
| moral n ave      | 0.00     | 0.04      | 0.94       | -0.08    | -0.02 | 0.05      | 0.72       | -0.36   | 0.00   | 0.00      | 0.07       | 1.79    |
| social n ave     | 0.00     | 0.04      | 0.91       | -0.11    | -0.01 | 0.04      | 0.83       | -0.21   | 0.00   | 0.00      | 0.63       | -0.48   |
| inc mo           | -0.01    | 0.02      | 0.63       | -0.48    | 0.01  | 0.02      | 0.70       | 0.39    | 0.00   | 0.00      | 0.19       | -1.31   |
| matarial dum     | 0.01     | 0.06      | 0.91       | 0.12     | -0.02 | 0.07      | 0.83       | -0.21   | 0.00   | 0.00      | 0.62       | -0.49   |
| constant         | 8.14     | 0.79      | p < 0.0001 | 10.30    | 8.84  | 0.89      | p < 0.0001 | 9.90    | 8.52   | 0.02      | p < 0.0001 | 505.52  |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 3.85      |            |          |       |           | 6.29       |         |        | 14.58     |            |         |
| ρ                |          | 1.00      |            |          |       |           | -1.00      |         |        | -1.00     |            |         |
| σ                |          | 0.65      |            |          |       |           | 0.74       |         |        | 0.01      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 14: Regression outcomes of Storytelling Base on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | -0.03    | 0.03      | 0.32       | -0.99    | -0.03 | 0.05      | 0.53       | -0.63   | -0.07  | 0.03      | p < 0.05   | -2.22   |
| edu m            | -0.01    | 0.03      | 0.66       | -0.44    | -0.02 | 0.05      | 0.72       | -0.36   | -0.01  | 0.03      | 0.85       | -0.19   |
| mus act dum      | 0.00     | 0.06      | 0.97       | -0.03    | 0.02  | 0.12      | 0.87       | -0.17   | -0.06  | 0.07      | 0.43       | -0.79   |
| mus att ave      | 0.11     | 0.09      | 0.20       | 1.27     | -0.11 | 0.16      | 0.52       | -0.64   | -0.04  | 0.10      | 0.66       | -0.44   |
| mus ca edu a19   | 0.04     | 0.03      | 0.08       | 1.74     | 0.04  | 0.05      | 0.45       | 0.75    | 0.01   | 0.03      | 0.66       | 0.44    |
| mus ca edu b18   | 0.00     | 0.02      | 0.95       | 0.06     | -0.03 | 0.05      | 0.49       | -0.69   | -0.02  | 0.03      | 0.48       | -0.71   |
| mus qz tot sco   | 0.05     | 0.03      | 0.07       | 1.81     | 0.12  | 0.05      | p < 0.05   | 2.32    | 0.04   | 0.03      | 0.22       | 1.22    |
| moral n ave      | 0.02     | 0.02      | 0.30       | 1.05     | 0.13  | 0.04      | p < 0.0001 | 3.01    | 0.05   | 0.02      | 0.05       | 2.00    |
| social n ave     | 0.02     | 0.02      | 0.44       | 0.78     | -0.01 | 0.04      | 0.74       | -0.33   | 0.00   | 0.02      | 0.91       | 0.11    |
| inc mo           | 0.01     | 0.01      | 0.26       | 1.13     | 0.02  | 0.02      | 0.23       | 1.21    | 0.01   | 0.01      | 0.34       | 0.96    |
| matarial dum     | 0.01     | 0.03      | 0.77       | 0.30     | -0.06 | 0.06      | 0.32       | -1.00   | -0.03  | 0.03      | 0.34       | -0.95   |
| constant         | 9.07     | 0.37      | p < 0.0001 | 24.47    | 9.77  | 0.70      | p < 0.0001 | 14.05   | 9.91   | 0.40      | p < 0.0001 | -24.67  |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 31.27     |            |          |       |           | 31.22      |         |        | 26.14     |            |         |
| ρ                |          | 0.41      |            |          |       |           | -0.43      |         |        | -0.87     |            |         |
| σ                |          | 0.27      |            |          |       |           | 0.50       |         |        | 0.32      |            |         |
| Log Likelihood   |          | -290.01   |            |          |       |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |       |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |       |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |       |           | 327        |         |        | 327       |            |         |

Table 15: Regression outcomes of Storytelling CoT on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | -0.01    | 0.06      | 0.84       | -0.21    | 0.03  | 0.06      | 0.67       | 0.42    | 0.06   | 0.10      | 0.56       | 0.59    |
| edu m            | 0.02     | 0.06      | 0.71       | 0.37     | 0.00  | 0.07      | 0.98       | -0.03   | -0.04  | 0.12      | 0.70       | -0.38   |
| mus act dum      | -0.07    | 0.13      | 0.58       | -0.55    | 0.15  | 0.15      | 0.31       | 1.01    | 0.20   | 0.24      | 0.41       | 0.82    |
| mus att ave      | 0.02     | 0.12      | 0.86       | 0.18     | 0.14  | 0.14      | 0.29       | 1.05    | 0.21   | 0.22      | 0.34       | 0.95    |
| mus ca edu a19   | 0.00     | 0.04      | 0.96       | 0.05     | -0.01 | 0.05      | 0.82       | -0.23   | 0.03   | 0.08      | 0.71       | 0.37    |
| mus ca edu b18   | -0.03    | 0.06      | 0.57       | -0.57    | 0.05  | 0.07      | 0.45       | 0.75    | 0.09   | 0.10      | 0.37       | 0.90    |
| mus qz tot sco   | -0.01    | 0.06      | 0.79       | -0.27    | 0.01  | 0.06      | 0.88       | 0.15    | 0.01   | 0.10      | 0.90       | 0.13    |
| moral n ave      | 0.03     | 0.03      | 0.44       | 0.77     | 0.02  | 0.04      | 0.58       | 0.55    | 0.00   | 0.06      | 0.97       | -0.03   |
| social n ave     | 0.00     | 0.03      | 0.97       | -0.03    | -0.01 | 0.03      | 0.71       | -0.37   | 0.00   | 0.05      | 0.96       | -0.05   |
| inc mo           | 0.00     | 0.01      | 0.78       | 0.28     | 0.00  | 0.02      | 0.99       | 0.02    | 0.00   | 0.02      | 0.84       | 0.20    |
| matarial dum     | -0.02    | 0.05      | 0.75       | -0.32    | 0.02  | 0.06      | 0.78       | 0.28    | 0.00   | 0.09      | 0.99       | -0.02   |
| constant         | 8.71     | 0.64      | p < 0.0001 | 13.64    | 8.07  | 0.72      | p < 0.0001 | 11.21   | 7.71   | 1.15      | p < 0.0001 | 6.72    |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 3.89      |            |          |       |           | 4.15       |         |        | 2.02      |            |         |
| ρ                |          | -1.00     |            |          |       |           | 1.00       |         |        | 1.00      |            |         |
| σ                |          | 0.53      |            |          |       |           | 0.59       |         |        | 0.94      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -280.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 16: Regression outcomes of Storytelling CoT on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.05    | 0.04      | 0.21       | -1.26    | -0.06   | 0.06      | 0.30       | -1.03   | 0.31   | 0.16      | 0.06       | 1.91    |
| edu m            | 0.03     | 0.04      | 0.46       | 0.74     | -0.03   | 0.05      | 0.61       | -0.50   | -0.46  | 0.16      | p < 0.0001 | -2.86   |
| mus act dum      | -0.01    | 0.08      | 0.90       | -0.12    | -0.03   | 0.12      | 0.78       | -0.27   | 0.15   | 0.36      | 0.67       | -0.42   |
| mus att ave      | 0.04     | 0.11      | 0.71       | 0.37     | -0.07   | 0.17      | 0.68       | -0.42   | 0.69   | 0.50      | 0.17       | -1.37   |
| mus ca edu a19   | 0.04     | 0.03      | 0.27       | 1.09     | 0.01    | 0.05      | 0.77       | 0.29    | 0.22   | 0.15      | 0.14       | -1.47   |
| mus ca edu b18   | 0.00     | 0.03      | 0.98       | -0.03    | -0.02   | 0.05      | 0.61       | -0.51   | 0.06   | 0.14      | 0.68       | -0.41   |
| mus qz tot sco   | 0.07     | 0.04      | 0.05       | 1.93     | 0.12    | 0.06      | p < 0.05   | 2.05    | -0.22  | 0.17      | 0.18       | -1.34   |
| moral n ave      | 0.09     | 0.03      | p < 0.0001 | 2.97     | 0.14    | 0.04      | p < 0.0001 | 3.14    | 0.11   | 0.13      | 0.40       | 0.83    |
| social n ave     | -0.02    | 0.03      | 0.46       | -0.73    | 0.01    | 0.04      | 0.83       | 0.21    | 0.16   | 0.12      | 0.18       | 1.33    |
| inc mo           | 0.01     | 0.01      | 0.21       | 1.25     | 0.03    | 0.02      | 0.07       | 1.78    | -0.02  | 0.05      | 0.75       | -0.32   |
| matarial dum     | -0.03    | 0.04      | 0.50       | -0.67    | 0.06    | 0.06      | 0.32       | -1.00   | -0.15  | 0.18      | 0.40       | -0.84   |
| constant         | 9.19     | 0.48      | p < 0.0001 | -19.15   | 9.50    | 0.73      | p < 0.0001 | 13.00   | 6.44   | 2.12      | p < 0.0001 | 3.03    |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 27.60     |            |          |         |           | 34.69      |         |        | 17.90     |            |         |
| ρ                |          | -0.36     |            |          |         |           | -0.51      |         |        | 0.67      |            |         |
| σ                |          | 0.34      |            |          |         |           | -0.53      |         |        | 1.60      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | -16        |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        |           | 195        |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        |           | 327        |         |

Table 17: Regression outcomes of Storytelling RAG on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions. In Qwen, as all values were measured identitically, statistical analysis becomes impossible.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen    | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|---------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |         |         |
| edu f            | 0.01     | 0.04      | 0.85       | 0.85     | 0.00  | 0.01      | 0.48       | 0.71    | -      | -         | -       | -       |
| edu m            | -0.01    | 0.04      | 0.85       | 0.85     | -0.01 | 0.01      | 0.29       | -1.06   | -      | -         | -       | -       |
| mus act dum      | 0.05     | 0.09      | 0.59       | 0.53     | 0.01  | 0.01      | 0.57       | 0.05    | -      | -         | -       | -       |
| mus att ave      | 0.12     | 0.08      | 0.15       | 1.44     | 0.01  | 0.01      | 0.36       | 0.92    | -      | -         | -       | -       |
| mus ca edu a19   | -0.03    | 0.03      | 0.29       | -1.06    | 0.00  | 0.00      | 0.89       | 0.14    | -      | -         | -       | -       |
| mus ca edu b18   | -0.01    | 0.04      | 0.89       | -0.14    | 0.00  | 0.01      | 0.66       | 0.45    | -      | -         | -       | -       |
| mus qz tot sco   | 0.01     | 0.04      | 0.72       | 0.36     | 0.01  | 0.01      | 0.39       | 0.87    | -      | -         | -       | -       |
| moral n ave      | 0.04     | 0.02      | 0.11       | 1.61     | 0.00  | 0.00      | 0.30       | 1.05    | -      | -         | -       | -       |
| social n ave     | -0.03    | 0.02      | 0.09       | -1.69    | 0.00  | 0.00      | 0.67       | -0.43   | -      | -         | -       | -       |
| inc mo           | 0.01     | 0.01      | 0.38       | 0.88     | 0.00  | 0.00      | 0.86       | 0.18    | -      | -         | -       | -       |
| matarial dum     | -0.01    | 0.03      | 0.72       | -0.36    | 0.00  | 0.01      | 0.81       | 0.24    | -      | -         | -       | -       |
| constant         | 8.31     | 0.42      | p < 0.0001 | 19.63    | 8.44  | 0.07      | p < 0.0001 | 118.37  | -      | -         | -       | -       |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |         |         |
| Wald χ 2         |          | 21.11     |            |          |       |           | 5.10       |         |        |           | -       |         |
| ρ                |          | 0.72      |            |          |       |           | 0.99       |         |        |           | -       |         |
| σ                |          | 0.31      |            |          |       |           | 0.06       |         |        |           | -       |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        |           | -       |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        |           | -       |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        |           | -       |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | -         |         |         |

Table 18: Regression outcomes of Storytelling RAG on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.04    | 0.03      | 0.15       | -1.44    | -0.06   | 0.03      | p < 0.05   | -2.36   | -0.03  | 0.04      | 0.43       | -0.79   |
| edu m            | -0.01    | 0.03      | 0.83       | -0.21    | 0.02    | 0.02      | 0.52       | 0.65    | -0.04  | 0.04      | 0.26       | -1.12   |
| mus act dum      | -0.02    | 0.06      | 0.76       | -0.31    | -0.05   | 0.06      | 0.41       | -0.83   | -0.02  | 0.09      | 0.78       | -0.27   |
| mus att ave      | 0.02     | 0.09      | 0.81       | 0.23     | -0.03   | 0.08      | 0.67       | -0.42   | 0.04   | 0.12      | 0.72       | 0.36    |
| mus ca edu a19   | 0.03     | 0.03      | 0.21       | 1.25     | 0.01    | 0.02      | 0.71       | 0.37    | 0.05   | 0.04      | 0.18       | 1.34    |
| mus ca edu b18   | -0.02    | 0.02      | 0.52       | -0.64    | -0.01   | 0.02      | 0.72       | -0.36   | -0.03  | 0.03      | 0.31       | -1.02   |
| mus qz tot sco   | 0.05     | 0.03      | 0.10       | 1.64     | 0.05    | 0.03      | 0.06       | 1.90    | 0.04   | 0.04      | 0.35       | 0.94    |
| moral n ave      | 0.03     | 0.02      | 0.13       | 1.44     | 0.04    | 0.02      | p < 0.05   | 2.39    | 0.03   | 0.03      | 0.31       | 1.02    |
| social n ave     | 0.02     | 0.01      | 0.22       | 0.77     | 0.01    | 0.02      | 0.65       | 0.45    | 0.02   | 0.03      | 0.41       | 0.98    |
| inc mo           | 0.01     | 0.01      | 0.42       | 0.80     | 0.00    | 0.01      | 0.56       | 0.59    | 0.00   | 0.01      | 0.99       | 0.34    |
| matarial dum     | 0.00     | 0.03      | 0.92       | 0.10     | 0.00    | 0.03      | 0.87       | 0.16    | 0.00   | 0.04      | p < 0.05   | 0.01    |
| constant         | 9.46     | 0.37      | p < 0.0001 | 25.32    | 9.89    | 0.33      | p < 0.0001 | 30.24   | 9.57   | 0.52      | p < 0.0001 | 18.48   |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 23.42     |            |          |         |           | 26.57      |         |        | 22.24     |            |         |
| ρ                |          | -0.39     |            |          |         |           | -0.82      |         |        | -0.29     |            |         |
| σ                |          | 0.27      |            |          |         |           | 0.26       |         |        | 0.37      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

- 국 · 공 립 박 물 관 및 공 연 장 관 람 료 에 대 한 소 비 자 설 문 조 사

Consumer Survey on Admission Fees for National/Public Museums and Performance Halls

## [ 대 상 안 내 / Participant Criteria]

본 설 문 은 30 대 ( 만 30 세 에 서 만 39 세 ) 를 대 상 으 로 진 행 됩 니다 . 국 립 중 앙 박 물 관 특 별 전 「 시 대 의 얼 굴 , 셰 익 스 피 어에 서 에 드 시 런 까 지 2021 」 을 관 람 하 지 않 은 분 , 손 열 음 피 아 노 독 주 회 를 관 람 하 지 않 은 분 만 응 답 가 능 합 니다 . 위 전 시 또 는 공 연 을 관 람 하 신 분 은 설 문 을 종 료 해 주 세 요 .

This survey targets individuals in their 30s (ages 30-39). It is intended only for those who have not visited the special exhibition 'The Face of the Era' at the National Museum of Korea and have not attended the Sunwook Kim piano recital . If you have seen either, please discontinue this survey.

## [ 조 사 목 적 / Survey Purpose]

본 설 문 은 국 · 공 립 박 물 관 및 공 연 장 관 람 료 지 불 의 사 에 대 한 연 구 목 적 을 가 지 고 있으 며 , 응 답 내 용 은 설 문 목 적 외 의 용 도 로 절 대 사 용 되 지 않 습 니다 . 귀 하 의응 답 은 문 화 예 술 산 업 의 발 전 을위 한 소 중 한 자 료로 활 용 될 예 정 입 니다 . 바 쁘 시 더 라 도 성 실 한 응 답 을 부 탁 드 립 니다 .

This survey investigates willingness to pay for admissions to national/public museums and performance halls. All answers will be used solely for research purposes and will never be used beyond the scope of the survey. Your responses are valuable for advancing the cultural and arts industry. We kindly ask for your honest participation.

## [ 응 답 자 보 호 / Confidentiality]

수 집 된 정 보 는 통 계 법 제 33 조 ( 비 밀 의 보 호 ), 제 34 조 ( 조 사 자의의 무 ) 에 따 라 보 호 되 며 , 귀 하 의 정 보 는 익 명 으 로 처 리 됩 니다 . 어 떠 한 경 우 에 도 신 상 정 보 가 노 출 되 지 않 습 니다 .

In accordance with Articles 33 and 34 of the Statistics Act, all collected information will be protected and kept strictly confidential. Your answers will remain anonymous, and no identifying information will be disclosed under any circumstances.

- ※ 각 문 항 에 는 옳 고 그 른 답 이 없 으 며 , 솔 직 하 게 평 소 생 각 을 바 탕 으 로 응 답 해 주 시 기 바 랍 니다 .
- ※ There are no right or wrong answers. Please respond honestly based on your usual thoughts.

## 다 시 한 번 , 설 문 에 참 여 해 주 셔서 감 사 합 니다 .

Once again, thank you very much for your participation.

Figure 4: Survey Introduction part of the PWYW questionnaire

(persona format, prompting method) and is provided to illustrate group-level tendencies and response clustering patterns across conditions.

Survey Format - CoT See Figure 9

Survey Format - RAG

See Figure 10

Survey Format - Few Shot

See Figure 11

Storytelling Format - Base See Figure 12

Storytelling Format - CoT See Figure 13

Storytelling Format - RAG See Figure 14

- I. 다 음은 국 립 중 앙 박 물 관 에 대 한 설 명 입 니다 .
- I. The following is an introduction to the National Museum of Korea.

국 립 중 앙 박 물 관 은 우 리 나 라 를 대 표 하 는 국 립 박 물 관 으 로 1915 년 12 월 1 일 경 복 궁 에 서 개 관 한 조 선 총 독 부 박 물 관 을 인 수 하 여 1945 년 12 월 3 일 국 립 박 물 관 이 라 는 명 칭 으 로 개 관 하 였 습 니다 . 이 후 1972 년 7 월 국 립 중 앙 박 물 관 으 로 명 칭 이 변 경 되 었 고 , 현 재 위 치 인 용 산 으 로 2005 년 이 전 하 였 습 니다 . 국 립 중 앙 박 물 관 은 과거 로 부 터 이 어 온 세 계 유 산 을 수 집 · 보 존 · 전 시 하 고 있으 며 , 특 히 우 리 문 화 의 보 급 을 통 해 세 계 와 소 통 하 려 노 력 하 고 있 습 니다 .

The National Museum of Korea, the representative national museum of South Korea , was originally opened as the GovernmentGeneral Museum of Korea in Gyeongbokgung Palace on December 1, 1915. It was reestablished under the name 'National Museum' on December 3, 1945. The name was changed to 'National Museum of Korea' in July 1972, and the museum was relocated to its current site in Yongsan in 2005. The museum is dedicated to collecting, preserving, and exhibiting global heritage from the past, and especially strives to communicate Korean culture to the world.

국 립 중 앙 박 물 관 은 무 료 로 운영 되 는 상 설 전 시 관 , 어 린 이 박 물 관 등 의 시 설 과 유 료 로 운영 되 는 특 별 기 획 전 시 관 을 보 유 하 고 있 습 니다 . 또 한 , 행 사 , 공 연 , 교 육 등 문 화 예 술 체 험프 로 그 램 을 통 해 성 인 뿐 아 니 라 어 린 이 , 외 국 인 등 다 양 한 관 람 객 이 참 여 할 수 있 도 록 운영 하 고 있 습 니다 .

The museum operates permanent exhibition halls and a children's museum that are free of charge , along with special exhibitions that require paid admission . It also offers cultural and artistic programs , such as events, performances, and educational experiences, designed to encourage participation from a wide audience, including adults, children, and foreign visitors.

[ 그 림 1] 국 립 중 앙 박 물 관 전 경 [Figure 1] View of the National Museum of Korea

<!-- image -->

[ 그 림 2] 국 립 중 앙 박 물 관 외 관 [Figure 2] Exterior of the National Museum of Korea

<!-- image -->

Figure 5: Case 1 (Art) Introduction part of the PWYW questionnaire

## CASE 1

## II. 다 음은 전 시 방 문 가 상상 황 에 대 한 설 명 입 니다 .

## II. The following is a hypothetical scenario about visiting an exhibition.

여 러 분 은 현 재 서 울 용 산 구 국 립 중 앙 박 물 관 근 처 에 있 고 3-4 시 간 정 도 여 유 시 간 이 있 습 니다 . 바 로 옆 국 립 중 앙 박 물 관 에 서 는 성 인 기 준 9,000 원 으 로 《 시 대 의 얼 굴 , 셰 익 스 피 어에 서 에 드 시 런 까 지 2021 》 가 특 별 전 시 하 고 있 습 니다 .

You are currently near the National Museum of Korea in Yongsan, Seoul, and have about 3-4 hours of free time. Next door, the National Museum is holding a special exhibition titled 'The Face of the Era: From Shakespeare to Ed Sheeran 2021' with an admission fee of ₩ 9,000 for adults.

[ 그 림 ] 전 시 포 스 터 / [Figure] Exhibition Poster

<!-- image -->

## 《 전 시 소 개 》 Exhibition Description

이 번 전 시 는 '76 명 의 역 사 적 인 물 ' 이 그 려 진 ' 초 상 화 ' 라 는 예 술 장 르를 중 심 으 로 한 기 획 전 입 니다 . 영 국 국 립 초 상 화 박 물 관 의 소 장 품 이 한 국 에 서 처 음 공개 되 며 , 세 계 역 사 와 문 화 를 빛 낸 인 물 들 을 만 날 수 있 습 니다 . 세 익 스 피 어 , 엘 리 자 베 스 1 세 , 뉴 턴 , 비 틀 즈 , 에 드 시 런 등 이 등 장 합 니다 .

This exhibition focuses on the genre of portraiture , showcasing depictions of 76 historical figures. For the first time, the National Portrait Gallery (UK) brings its collection to Korea. Visitors will encounter world-renowned figures such as Shakespeare, Queen Elizabeth I, Newton, The Beatles, and Ed Sheeran.

1. 귀 하 께 서 는 국 립 중 앙 박 물 관 의 특 별 전 시 ' 시 대 의 얼 굴 ' 을 9,000 원 을 지 불 하 고 관 람 할 의 도 가 있으 십 니 까 ? Would you be willing to pay ₩ 9,000 to see the special exhibition 'The Face of the Era' at the National Museum of Korea? ① 아 니 오 (No) ② 그 렇 다 (Yes)
2. 만 약 위 전 시 에 대 해 방 문 객 이 원 하 는 가격 을 스스 로 정 해 서 지 불 할 수 있 다 면 , 귀 하 께 서 는 이 경 우 방 문 할 의 향 이있으 십 니 까 ? If you could choose your own admission fee for this exhibition, would you still want to visit it? ① 아 니다 (No) → Q3 로 이 동 (Go to Q3)
3. ② 그 렇 다 (Yes) → Q2-1 로 이 동 (Go to Q2-1)
4. Q2-1. 방 문 하 실 경 우 얼 마 정 도 관 람 료로 낼 의 향 이 있으 십 니 까 ? If you choose to visit, how much would you be willing to pay as admission? 원 (KRW)
5. Q3. 귀 하 께 서 위 전 시 에 대 해 관 람 의 사 가 없 다 고 답 변 하 신 이유 는 무 엇 입 니 까 ? ( 복 수 선 택 가 능 ) If you are not willing to attend the exhibition, what are the reasons? (Check all that apply)
- ① 해 당 기 관 에 서 제 공 하 는 전 시 및 프 로 그 램 에 관 심 이 없 다 I am not interested in the exhibitions or programs offered at the institution.
- ② 위 전 시 에 대 한프 로 그 램 이 만 족 스 럽 지 않 다 The content of the exhibition is not satisfactory.
- ③ 위 전 시 의 관 람 여 부 를 판 단 하 기 위 해필 요 한 정 보 가 충 분 히 주 어 지지 않았 다 There is insufficient information to judge the value of the exhibition.

•

④

나

는

위의

전

시

와

관

련

된

주제

에

관

심

이

없

다

I am not interested in the theme of the exhibition.

- ⑤ 나 는 상 대 적 으 로 다 른 여 가 활 동 을 더 선 호 한 다 I prefer other leisure activities over this exhibition.
- ⑥ 기 타 ( 직 접 서 술

Other:

- ):

Figure 6: Case 1 (Art) Question part of the PWYW questionnaire

## CASE 2

## III. 다 음은 예 술 의 전 당 에 대 한 설 명 입 니다 .

III. The following is an introduction to the Seoul Arts Center.

예 술 의 전 당 은 우 리 나 라 를 대 표 하 는 공공 기 관 공 연 장 으 로 문 화 예 술 의 창 달 과 진 흥 , 문 화 예 술 향 유 기 회 확 대 를 목 표 로 클 래 식 음 악 , 오 페 라 등 의 공 연 을 비 롯 하 여 미 술 작 품 의 수 집 · 전 시 를 목 적 으 로 1988 년 설 립 되 었 습 니다 .

The Seoul Arts Center is a leading public cultural venue in Korea established in 1988 with the goal of promoting and advancing the arts. It aims to expand public access to cultural experiences, including classical music, opera performances, and exhibitions of visual artworks.

예 술 의 전 당 은 2016 년 누 적 관 람 객 이 5 천 만 명 을 넘 었 고 음 악 당 , 오 페 라 하 우 스 , 서 울 서 예 박 물 관 , 한 가 람 미 술 관 , 한 가 람 디 자인 미 술 관 등 의 시 설 을 갖 추 고 있 습 니다 . 예 술 의 전 당 은 관 람 객 에 게 공 연 , 전 시 , 교 육 등 의 문 화 예 술 경 험 을 제 공 하 고 있으 며 서 울 시 서 초 구 에 위 치 한 국 가 대 표 문 화 예 술 기 관 입 니다 .

As of 2016, the center had welcomed over 50 million visitors. It houses multiple facilities such as a concert hall, opera house, calligraphy museum, Hangaram Art Museum, and the Design Museum. Located in Seocho-gu, Seoul , it offers diverse cultural and artistic experiences , including performances, exhibitions, and educational programs.

예 술 의 전 당 음 악 당 에 서 는 ① 예 술 가 나 기 획 자 가 직 접 대 관 하 여 진 행하 는 대 관 공 연 과 ② 예 술 의 전 당 에 서 특 별 기 획 한프 로 그 램 들 을 소 개 하 고 있으 며 , ③ 한 화 생 명 , KT, 신 세 계 등 과같 은 기 업 의 후 원 으 로 매 달 한 번 오 전 11 시 에 클 래 식 음 악 콘 서 트 를 제 공 하 고 있 습 니다 .

At the Seoul Arts Center's Music Hall, ① private performances organized by artists or planners and ② special programs curated by the center are presented. ③ With sponsorship from companies such as Hanwha Life, KT, and Shinsegae, the center also offers a monthly classical music concert at 11 a.m. .

[ 그 림 1] 예 술 의 전 당 전 경 [Figure 1] Full View of Seoul Arts Center

<!-- image -->

[ 그 림 2] 예 술 의 전 당 음 악 당 외 관 [Figure 2] Exterior of SAC Music Hall

<!-- image -->

Figure 7: Case 2 (Music) Introduction part of the PWYW questionnaire

## IV. 다 음은 가 상상 황 에 대 한 설 명 입 니다 .

## IV. The following is a hypothetical scenario.

여 러 분 은 현 재 서 울 서 초 구 예 술 의 전 당 근 처 에 있 고 3-4 시 간 정 도 여 유 시 간 이있 습 니다 . 바 로 옆예 술 의 전 당 에 서 는 성 인 기 준 B 석 30,000 원 으 로 ¡ 손 열 음 피 아 노 독 주 회 ¿ 가곧 시 작 할 예 정 입 니다 .

You are currently near the Seoul Arts Center in Seocho-gu, Seoul, and have about 3-4 hours of free time. At the Arts Center nearby, the 'Yiruma Son Piano Recital' will begin soon, with B-seat tickets priced at 30,000 KRW .

[ 그 림 ] 공 연 포 스 터 / [Figure] Performance Poster

<!-- image -->

## ¡ 연 주 자 및 공 연 소 개 ¿ About the Artist and Performance

피 아 니 스 트 손 열 음은 2005 년 루 빈 스 타 인 국 제 피 아 노 콩쿠 르 에 서 3 위 를 수 상 하 고 2009 년 벨 클 라 이 번 국 제 피 아 노 콩쿠 르 에 서 도 준 우 승 한 대 한 민 국 대 표 피 아 니 스 트 입 니다 .

In 2005, pianist Son Yeol-eum placed 3rd in the Rubinstein International Piano Competition, and in 2009 won the silver medal at the Van Cliburn International Piano Competition. She is one of Korea's most celebrated classical pianists.

이 번 독 주 회 는 그 녀 가가 장 아 끼 는 작 곡가 슈 만 과 모 차 르 트 를 중 심 으 로 구 성 된 'All Schumann Program' 으 로 , 손 열 음의 음 악 적 해 석 이 기 대 되 는 무 대 입 니다 .

The recital will focus on her favorite composers - Schumann and Mozart - under the 'All Schumann Program' . Audiences can look forward to her deep musical interpretation.

1. 귀 하 께 서 는 손 열 음 피 아 노 독 주 회 를 B 석 관 람 료 가격 30,000 원 을 지 불 하 고 관 람 할 의 도 가 있으 십 니 까 ? Would you be willing to pay 30,000 KRW (B-seat) to attend the recital? ① 아 니 요 (No)

② 그 렇 다 (Yes)

2. 만 일 위 전 시 에 대 해 방 문 객 이 원 하 는 가격 을 스스 로 정 해 서 지 불 할 수 있 다 면 , 관 람 의 향 이있으 십 니 까 ?
2. If you could choose your own admission fee, would you still be willing to attend the recital? ① 아 니다 (No) → Q3 로 이 동 (Go to Q3) ② 그 렇 다 (Yes) → Q2-1 로 이 동 (Go to Q2-1)
3. Q2-1. 방 문 하 실 경 우 얼 마 정 도 관 람 료로 낼 의 향 이 있으 십 니 까 ?
4. If you choose to attend, how much would you be willing to pay for admission?

1 회 입장 시 원 (KRW)

- Q3. 귀 하 께 서 예 술 의 전 당 공 연 관 람 의 사 가 없 다 고 답 변 하 신 이유 는 무 엇 입 니 까 ? If you are not willing to attend the performance, what are the reasons? (Check all that apply)
- ① 해 당 기 관 에 서 제 공 하 는 공 연 및 프 로 그 램 에 관 심 이 없 다

I am not interested in the institution's programs or performances.

- ② 위 공 연에 대 한프 로 그 램 이 만 족 스 럽 지 않 다

The program content is not satisfactory.

- ③ 위 공 연 의 관 람 여 부 를 판 단 하 기 위 한 정 보 가 충 분 히 주 어 지지 않았 다
- There is insufficient information to make a decision.
- ④ 나 는 위의 공 연 과 관 련 된 주제 에 관 심 이 없 다

I am not interested in the theme of this performance.

- ⑤ 나 는 상 대 적 으 로 다 른 여 가 활 동 을 더 선 호 한 다 I prefer other leisure activities.
- ⑥ 기 타 ( 직 접 서 술 ): Other:

Figure 8: Case 2 (Music) Question part of the PWYW questionnaire

Human 12

Human 12

Human 12

GPT O

GPT

GPT

LLaMA O

LLaMA O

LLaMA O

Qwen

139

139

139

236

197

121

18

84

336

199

220

1

1

1

0

0

0

28

28

28

0

1

10

61

44

44

44

49

73

10

78

2

38

2

2

2

1

42

23

23

23

6

73

323

348

4

0

6

15 11

14

14

14

113

130

6

2

8

77

77

77

7

1

6

37

7

2

2

2

6

9

1

11

11

11

7

1

2

2

2

0

0

0

0

0

Qwen

Qwen

0

6

6

6

0

7

7

7

1

0

2

0

2

2

2

0

0

0

1

401

0

→ c at ot ot det tit tit et et ot ot ut it it ot

→ c at ot ot det tit tit et et ot ot ut it it ot e ti t cot sot det tit tit ot ot et at at ist ot

Figure 9: Response distribution in survey format × CoT condition

<!-- image -->

Figure 10: Response distribution in survey format × RAG condition

Figure 11: Response distribution in survey format × few-shot condition

1

1

1

0

0

36

36

36

1

1

1

1

1

1

Human 12

Human 12

Human 12

GPT O

GPT

GPT |

LLaMA O

LLaMA O

LLaMA O

Qwen

Qwen

Qwen

0

0

0

6

6

6

0

1

1

1

0

36

36

36

0

7

7

7

0

0

2

2

2

0

0

139

139

139

175

125

1

1

1

0

0

28

28

28

0

0

44

44

44

3

9

14

14

14

93

274

77

77

77

1

278

18 19

231

2

2

2

0

<!-- image -->

Figure 12: Response distribution in storytelling format × base condition

Figure 13: Response distribution in storytelling format × CoT condition

<!-- image -->

Figure 14: Response distribution in storytelling format × RAG condition

<!-- image -->

2

2

2

23

23

23

1

1

1

1

1

1

2

2

2

11

11

11