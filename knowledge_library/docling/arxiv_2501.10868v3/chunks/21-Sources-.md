## Sources:

- GitHub [Baazizi et al., 2021] : Extracted from open-source repositories containing schema definitions, representing practical, widely-used applications. Schemas from GitHub are of various complexities, totaling 6,000 schemas. We split the collection into trivial (fewer than 10 fields), easy (10-30 fields), medium (30-100 fields), hard (100-500 fields), and ultra (more than 500 fields), based on the total number of fields in each JSON schema to reflect increasing complexity and scale.
- Snowplow [Analytics, 2022] : Sourced from event-based analytics frameworks, showcasing schemas tailored for event-driven data structures.

- Kubernetes [Kubernetes, 2022] : Schemas defining configurations for container orchestration systems, highlighting schemas with intricate hierarchical structures.
- WashingtonPost [Post, 2022] : Schemas for The Washington Post's ANS specification.
- GlaiveAI2K GlaiveAI [2024] : 2,000 schemas extracted from a function-calling dataset. Each schema represents a function signature.
- JSON Schema Store [Schema Store Org, 2014] : The largest collection of independent JSON schemas in the world.

Table 9: Baisc statistics of the datasets used in the experiments.

| Dataset         |   Count | Size (KB) Med / Max   | Field Count Med / Max   | Max Fan-Out Med / Max   | Schema Depth Med / Max   |
|-----------------|---------|-----------------------|-------------------------|-------------------------|--------------------------|
| GlaiveAI-2K     |    1707 | 0.5 / 1.2             | 21 / 44                 | 4 / 7                   | 5 / 8                    |
| Github-Trivial  |     444 | 0.2 / 10.8            | 6 / 9                   | 4 / 9                   | 2 / 6                    |
| Github-Easy     |    1943 | 0.5 / 20.3            | 18 / 29                 | 5 / 19                  | 4 / 10                   |
| Snowplow        |     403 | 0.9 / 15.6            | 37 / 450                | 7 / 131                 | 3 / 13                   |
| Github-Medium   |    1976 | 1.5 / 58.3            | 51 / 99                 | 8 / 42                  | 6 / 15                   |
| Kubernetes      |    1064 | 2.7 / 818.6           | 41 / 11720              | 5 / 600                 | 5 / 7                    |
| Washington Post |     125 | 1.7 / 81.1            | 44 / 2093               | 7 / 84                  | 4 / 10                   |
| Github-Hard     |    1240 | 5.1 / 136.1           | 175 / 498               | 18 / 133                | 8 / 25                   |
| JSONSchemaStore |     492 | 5.9 / 2934.8          | 155 / 108292            | 14 / 6543               | 6 / 22                   |
| Github-Ultra    |     164 | 25.8 / 359.6          | 694 / 6919              | 37 / 412                | 8 / 23                   |
