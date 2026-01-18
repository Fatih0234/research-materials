## Governors

With the informational foundation in place, the simulation proceeds to the formation of private opinions. Each agent is assigned a unique persona based on the realworld characteristics of its corresponding FOMC voting member. Personas are built from biographical details, recent public statements, inferred policy leanings, and district-specific economic context. Each agent receives:

a) a role description and career biography 15 ;

b) a macro dashboard (Table 1) showing current levels and two lags of first differences;

14 Analyses draw on nearly 190 unique articles over a two-week collection window ending July 31, 2025. The highest relevance pieces are clustered around labor market trends (10 articles).

15 Details provided in the Online Appendix.

- c) current macro context, including the latest policy statement, a synthetic Beige Book summary, recent news, and the member's own speeches and interviews.

Agents integrate these qualitative and quantitative inputs with their personas to form an initial private policy view. Each is prompted to issue a rate recommendation and a one-sentence justification, representing the agent's initial belief mean, µ initial i . This output serves as input to the numeric vote engine, detailed in Section 3.1.

We also include a stance evolution module in persona building, which uses an LLM to classify recent public speeches into hawkish, dovish, or data-dependent stances. These signals are aggregated with a strong recency bias, i.e., recent speeches count most, earlier ones less, producing a posterior stance with calibrated confidence. The system flags any discrete shifts from past views and feeds this evolved stance into persona construction, so rate recommendations and uncertainty can adjust dynamically to members' latest communications.
