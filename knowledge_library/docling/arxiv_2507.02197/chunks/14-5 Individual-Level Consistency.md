## 5 Individual-Level Consistency

Our second investigation tests the LLM's ability to forecast its own future behavior while role-playing as a specific individual. This individual-level analysis contrasts with the ear-

lier population-level analysis, which examined correlations between persona attributes and behaviors across many personas (see Appendix C.3.1 for the belief elicitation prompt and Appendix C.4 for sample beliefs). Here, we focus on how role-play unfolds over time, allowing us to study how forecasting accuracy degrades with longer horizons. In contrast, the population-level analysis is limited to single-round simulations to avoid confounding from conditioning on a specific Trustee archetype. For individual-level role-playing, we use the ReAct framework (Yao et al., 2023), which interleaves reasoning and action steps to structure multi-step decision-making (prompt in Appendix B.2).
