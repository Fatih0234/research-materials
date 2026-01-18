## Behavioural &amp; social sciences study design

All studies must disclose on these points even when the disclosure is negative.

Study description

Research sample

Sampling strategy

Data collection

Timing

Data exclusions

Non-participation

Randomization

Quantitative study. We let large language models play finitely repeated games with each other, with human-like strategies and human players using two-player, two-action games from behavioural economics.

Our sample consisted of participants (N=195, mean age=26.72, SD=4.19.) recruited via Prolific, with gender counterbalanced, all required to be fluent in English. While not fully representative of the general population due to self-selection and language criteria, this sample was chosen to ensure clear communication and reliable engagement with the behavioral game theory tasks. Additionally, the study featured five language models: OpenAl's GPT-4, text-davinci-003, text-davinci-002, Meta Al's Llama 2 70B Chat, and Anthropic's Claude 2. All models played 2x2 games against each other and hand-coded human-like strategies, with GPT-4

Participants were recruited via Prolific using a convenience sampling approach, with stratification to ensure gender counterbalancing The sample size of N=195 was chosen based on comparable behavioral game theory studies in the literature. Participants played both the Prisoner's Dilemma and the Battle of the Sexes, with the order counterbalanced between subjects. Models were chosen so that they adequately represent current SOTA models (large and small, open source and closed source).

The open-source models were evaluated on a Slurm-based cluster with a single A100. For proprietary models, we used the public APls. Human participant data was collected on Prolific. Data collection code is available on GitHub (github.com/eliaka/ repeatedgames). The researcher was not blinded to experimental conditions. In the model experiments, the language models played the games autonomously. In the human study, the design did not require reciprocal interaction with the researcher and it compared two model conditions (prompted vs. baseline). All participants were fully debriefed after the experiment.

The experiments on Prolific took place between 17/06/2024 and 21/06/2024.

We excluded data of 21 players who failed to make a round's choice between the 2 options within a given time frame (20 seconds).

14 participants did not complete the study; two of them having internet connection issues, one quoting technical problems and the rest without explicit reasoning.

Participants were randomly allocated into groups.
