## 1 Introduction

The rapid advancements in LMs in recent years have significantly broadened their applications, extending beyond natural language tasks to more complex challenges such

∗ Work done during internship at Microsoft.

Token/s

150-

100

50-

20

40

60

Kubernetes

Guidance |

(A) Efficiency

Kubernetes

Washington

Post

(B) Coverage

Github Easy

Snowplow

Github

Medium

LLM only

Github

Hard

Accuracy(%)

90-

Washington

Post

Github

80

Hard

• XGrammar L

Figure 1: Comparison across various constrained-decoding frameworks by efficiency (speed of output generation), coverage (support for JSON Schema features), and quality (effects on underlying task accuracy). Guidance outperforms other frameworks on these dimensions.

<!-- image -->

as web navigation [Yao et al., 2023b], data extraction [Polak &amp; Morgan, 2024], and tool use [Schick et al., 2023]. Unlike traditional natural language processing (NLP) tasks where the output is aimed at review by humans, output in these applications is often consumed by machines such as controller and service APIs. The machine-oriented nature of these applications requires LMs to generate structured outputs that strictly adhere to predefined formats and constraints. However, the LM generation process is probabilistic and does not provide guarantees on the output's structure, making it challenging to deploy LMs in applications requiring structured inputs and high reliability.

The methodology of constrained decoding, a technique that integrates constraints into the decoding process of LMs, has been developed to address the need to adapt LM generations to the challenge of providing structured output. Constrained decoding intervenes in the decoding process of LMs by masking out invalid tokens based on given constraints and prefix tokens. This intervention guides the LM to sample only from valid tokens, ensuring that the final output perfectly conforms to a predefined structure.

The strong demand for structured generation [Liu et al., 2024] has led to the development of various constrained-decoding frameworks 2 , such as Guidance [Guidance AI, 2023], Outlines [Willard &amp; Louf, 2023], XGrammar [Dong et al., 2024] and the grammar module of Llamacpp [Gerganov &amp; al., 2023] These frameworks provide broad support for different types of constraints, minimal overhead, and compatibility with various LM ecosystems, facilitating the adoption of constrained decoding in real-world applications.

JSON Schema offers a high level, domain-specific way to define constraints for JSON data, a widely adopted data interchange format. As a result, JSON Schema has emerged as a key specification language for constrained decoding. Commercial LM providers, such as OpenAI, have embraced constrained decoding by incorporating support for JSON Schema directly into their APIs. These integrations highlight the emergence of JSON

2 We use the terms constrained decoding framework and grammar engine interchangeably.

80-

70-

60-

50-

40

Schema as an industry-wide standard for specifying constraints on structured outputs, ensuring compatibility across diverse applications.

Despite the growing adoption of constrained decoding for structured generation, several issues and questions persist:

Q1: Efficiency : Does constrained decoding slow down or speed up the generation process? Which framework is the most efficient?

Q2: Coverage : The JSON Schema specification has an evolving and expansive feature set. How well do existing constrained decoding frameworks support these features?

Q3: Quality : While constrained decoding guarantees that LM outputs conform to a desired structure, does it negatively affect the semantic quality of outputs?

To answer these questions, we need to study constrained-decoding methods with a large-scale, diverse, and real-world collection of user-defined structures. To evaluate the performance of constrained decoding frameworks, we introduce JSONSchemaBench , a collection of 10K real-world JSON schemas from various sources, Organized into 10 datasets of varying complexity and diversity, the benchmark spans domains such as function signatures, service APIs, and system configurations. We evaluate six state-of-the-art constrained decoding frameworks, including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini, on JSONSchemaBench. We pair this real-world schema dataset with the official JSON Schema Test Suite [JSON Schema Org, 2024] in order to extract detailed insights into coverage of JSON Schema functionality across these frameworks, and to further evaluate them with considerations of end-to-end task accuracy in the context of multiple real-world tasks. Altogether, our evaluation takes three aspects into consideration: efficiency, coverage, and quality. We define specific metrics to measure these three functional aspects and evaluate constrained decoding frameworks against them. Through extensive experiments, we converge on the following findings as illustrated in Figure 1. (1) Constrained decoding can speed up the generation process by 50% compared to unconstrained decoding. (2) Frameworks demonstrate significant differences in their actual support for real-world JSON schemas, with the best framework supporting twice as many schemas as the worst. (3) Constrained decoding consistently improves the performance of downstream tasks up to 4%, even for tasks with minimal structure like GSM8k.

Contributions Our contributions are three-fold:

- We assemble JSON schemas from various sources and organize them into a benchmark, JSONSchemaBench, to facilitate the evaluation of constrained decoding frameworks on JSON schema.
- We propose a fine-grained evaluation framework to assess the versatility of constrained decoding frameworks in handling diverse JSON schema features, including declared coverage, empirical coverage, and compliance rate.
- We evaluate six state-of-the-art constrained decoding frameworks on JSONSchemaBench, uncovering their strengths and limitations in generating schemacompliant JSON outputs and analyzing their impact on downstream tasks.
