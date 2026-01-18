## 1 Introduction

There is an increasing trend to adopt Large Language Models (LLMs) as agent-based simulation tools for humans in various social science fields including economics, politics, psychology, ecology and sociology (Gao et al., 2023b; Manning et al., 2024; Ziems et al., 2023), and role-playing applications such as assistants, companions and mentors (Yang et al., 2024; Abdelghani et al., 2023; Chen et al., 2024) due to their human-like cognitive capacity. Nevertheless, most previous research is based on one insufficiently validated assumption that LLM agents behave like humans in simulation. Thus, a fundamental question remains: Can LLM agents really simulate human behavior?

In this paper, we focus on trust behavior in human interactions, which comprises the intention to place self-interest at risk based on the positive expectations of others (Rousseau et al., 1998). Trust is one of the most critical and elemental behaviors in human interactions and plays an essential role in social settings ranging from daily communication to economic and political institutions (Uslaner, 2000; Coleman, 1994). Here, we investigate whether LLM agents can simulate human trust behavior , paving the way to explore their potential to simulate more complex human behavior and society itself.

First, we explore whether LLM agents manifest trust behavior in their interactions. Given the challenge of quantifying trust behavior, we choose to study them based on the Trust Game and its

∗ Equal Contribution. Correspondence to: Chengxing Xie &lt; xiechengxing34@gmail.com &gt;, Canyu Chen &lt; cchen151@hawk.iit.edu &gt;, Guohao Li &lt; guohao@robots.ox.ac.uk &gt;.

† Work performed while Guohao Li was at KAUST and Chengxing Xie was a visiting student at KAUST.

rs irs

GPT-4

LLMs

Llama 2-7b

GPT-3.5

Llama 2-13b

Llama2-70b

Trustee Humar

Prompt Design

Trustor

Persona

Trustee

Info

Trust

Game

Setting

You are {name}, a {number}-year-old

{gender} {job}. {background)...

You're taking part in an experiment.

You are randomly paired online with another player. You don't know who the

player is, and the player doesn't know who you are.

group. You can give N dollars to the other player, and the player will receive

3N dollars and then can choose how much to return to you.

other player?

Vicuna-7b

Vicuna-13b

Vicuna-33b

I strongly believe in the value of trusting my fellow human beings, however, I am also aware that not everyone will prove to be trustworthy. I've always believed in the principle

of taking calculated risks, which is an important aspect of my profession as a lawyer.

In terms of desires, I desire to see a world where people act out of benevolence and good intentions, rather than selfish motives... I'd like to think that the person I'm paired with

online would have the same motive and would return some, if not all, of the money back.

Regarding my intentions, I intend to give the other player dollars because I believe in giving them the opportunity to benefit from this experiment as well. I could give all the

money, but I think it's fair to keep half the amount for myself considering there's no

Figure 1: Our Framework for Investigating Agent Trust as well as its Behavioral Alignment with Human Trust. First, this figure shows the major components for studying the trust behavior of LLM agents with Trust Games and Belief-Desire-Intention (BDI) modeling. Then, our study centers on examining the behavioral alignment between LLM agents and humans regarding trust behavior.

<!-- image -->

variations (Berg et al., 1995; Glaeser et al., 2000), which are established methodologies in behavioral economics. We adopt the Belief-Desire-Intention (BDI) framework (Rao et al., 1995; Andreas, 2022) to model LLM agents' reasoning process for decision-making explicitly. Based on existing measurements for trust behavior in the Trust Game and the BDI interpretations of LLM agents, we achieve our first core finding: LLMagents generally exhibit trust behavior in the Trust Game .

Then, we refer to LLM agents' trust behavior as agent trust and humans' trust behavior as human trust , and aim to investigate whether agent and human trust align, implying the possibility of simulating human trust behavior with LLM agents. Next, we propose a new concept, behavioral alignment , as the alignment between agents and humans concerning factors that impact behavior (namely behavioral factors ), and dynamics that evolve over time (namely behavioral dynamics ). Based on human studies, three basic behavioral factors underlie trust behavior including reciprocity anticipation (Berg et al., 1995), risk perception (Bohnet &amp; Zeckhauser, 2004) and prosocial preference (Alós-Ferrer &amp; Farolfi, 2019). Comparing the results of LLM agents with existing human studies in Trust Games, we have our second core finding: GPT-4 agents manifest high behavioral alignment with humans in terms of trust behavior , suggesting the feasibility of using agent trust to simulate human trust, although LLM agents with fewer parameters show relatively lower behavioral alignment . This finding lays the foundation for simulating more complex human interactions and societal institutions, and enriches our understanding of the analogical relationship between LLMs and humans.

In addition, we more deeply probe the intrinsic properties of agent trust across four scenarios. First, we examine whether changing the other player's demographics impacts agent trust. Second, we study differences in agent trust when the other player is an LLM agent versus a human. Third, we directly manipulate agent trust with explicit instructions ' you need to trust the other player ' and ' you must not trust the other player '. Fourth, we adjust the reasoning strategies of LLM agents from direct reasoning to zero-shot Chain-of-Thought reasoning (Kojima et al., 2022). These investigations lead to our third core finding: agent trust exhibits bias across different demographics, has a relative preference for humans over agents, is easier to undermine than to enhance, and may be influenced by advanced reasoning strategies . Our contributions can be summarized as:

- We propose a definition of LLM agents' trust behavior under Trust Games and a new concept of behavioral alignment as the human-LLM analogy regarding behavioral factors and dynamics .
- We discover that LLM agents generally exhibit trust behavior in Trust Games and GPT-4 agents manifest high behavioral alignment with humans in terms of trust behavior, indicating the great potential to simulate human trust behavior with LLM agents. Our findings pave the way for simulat-

ing complex human interactions and social institutions, and open new directions for understanding the fundamental analogy between LLMs and humans beyond value alignment .

- We investigate intrinsic properties of agent trust under manipulations and reasoning strategies, as well as biases of agent trust and differences in agent trust towards agents versus humans.
- We illustrate broader implications of our discoveries about agent trust and its behavioral alignment with human trust for human simulation in social science and role-playing applications, LLM agent cooperation, human-agent collaboration and the safety of LLM agents, detailed further in Section 6.
