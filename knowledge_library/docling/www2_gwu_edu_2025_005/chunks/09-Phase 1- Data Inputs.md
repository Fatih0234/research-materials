## Phase 1: Data Inputs

For each simulated meeting, we construct a reproducible data snapshot that serves as the foundation for all subsequent stages of the simulation. The process begins by gathering and processing the extensive information on current economic conditions, ensuring the simulation is grounded. 11 Specifically, we pull the latest FOMC policy statement (in this case from June 18, 2025), key macroeconomic indicators, and

10 The simulation employs OpenAI's GPT family models with differentiated configurations across pipeline stages to optimize for specific tasks. We provide more details in the Online Appendix.

11 All collected data are stored as structured JSON files, preserving a precise snapshot of the economic environment at a given point in time.

Data Preparation

Initial Belief Formation (LLM-driven)

Pre-meeting Consensus

LLM Deliberation

LLM Outputs

• Rate distribution

• Vote outcome

• Dissent map

• Dialogue simulation

• Rate discrepancies

•Belief dispersion

• Behavioral differences

Figure 1: Simulation Framework

<!-- image -->

Notes. Figure 1 shows the simulation workflow. We start from real-time economic inputs and agent personas, then run two parallel tracks: (i) a behaviorally rich LLM deliberation and (ii) a Monte Carlo (MC) benchmark. The design mirrors the FOMC process and lets us switch on counterfactuals to see how communication frictions and political pressure translate into policy drift. Phase 1 (Data &amp; Priors): produce member priors ( µ i , σ 2 i ).

Phase 3 (Agenda &amp; Vote): the Chair proposes r c = r base +∆; the final rate is

Phase 2 (Consensus): update toward the committee mean with α i and compress variance by γ .

r f = w a r c +(1 -w a ) median i ( µ post i ); dissent propensity depends on the role-based cost κ i .

Data revision (treatment): incorporate ex-post data updates by re-initializing priors from the revised dataset: ( µ i , σ 2 i ) ← ( µ i + δ i , ρ i σ 2 i )

Political pressure (treatment): lower w a (weaken Chair authority) and apply appointment-weighted shifts to selected members.

```
µ i member i 's belief (rate) σ 2 i uncertainty (variance) α i , γ consensus pull and variance compression (Phase 2) r c , ∆ agenda rate and Chair bias (Phase 3) w a weight on agenda in r f (Chair authority) κ i role-based dissent cost
```

retrieve recent speeches from each Governor. The core indicators summarized in Table 1 are obtained via the FRED and BLS APIs, providing a consistent economic backdrop for the simulation.

Table 1: Key U.S. Economic Indicators - Snapshot as of July 31 st , 2025

| Indicator                     | Latest      | YoY     | Trend        | Source   |
|-------------------------------|-------------|---------|--------------|----------|
| Growth & Output               |             |         |              |          |
| Real GDP (2025 Q1)            | $23,685.3bn | 2.0%    | /arrow-up    | FRED     |
| Industrial Production (Index) | 104.0       | 0.7%    | /arrow-up    | FRED     |
| Retail Sales (monthly)        | $720.1bn    | 3.9%    | /arrow-up    | FRED     |
| Housing Starts                | 1.3m        | -0.5%   | /arrow-down  | FRED     |
| Inflation & Prices            |             |         |              |          |
| CPI (All Items)               | 321.5       | 2.7%    | /arrow-up    | FRED     |
| Core CPI                      | 327.6       | 2.9%    | /arrow-up    | FRED     |
| PCE (All Items)               | 126.6       | 2.6%    | /arrow-up    | FRED     |
| Core PCE                      | 125.9       | 2.8%    | /arrow-up    | FRED     |
| WTI Crude Oil ($/bbl)         | $67.8       | -12.7%  | /arrow-right | FRED     |
| Labor Market                  |             |         |              |          |
| Unemployment Rate             | 4.1%        | 0.0pp   | /arrow-up    | BLS      |
| Nonfarm Payrolls              | 159.7m      | 1.2%    | /arrow-up    | BLS      |
| Labor Force Participation     | 62.3%       | -0.5pp  | /arrow-down  | BLS      |
| Average Hourly Earnings       | $31.2       | 3.9%    | /arrow-up    | BLS      |
| Employment-Population Ratio   | 59.7%       | -0.5pp  | /arrow-down  | BLS      |
| Financial Conditions          |             |         |              |          |
| Fed Funds Rate                | 4.3%        | -75.0bp | /arrow-right | FRED     |
| 10-yr Treasury Yield          | 4.4%        | 16.0bp  | /arrow-down  | FRED     |
| 2-yr Treasury Yield           | 3.9%        | -18.0bp | /arrow-down  | FRED     |
| S&P 500 Index                 | 6,362.9     | 19.1%   | /arrow-up    | FRED     |
| U.S. Dollar Index (DXY)       | 120.4       | -2.8%   | /arrow-down  | FRED     |
| VIX Volatility Index          | 15.5        | -25.3%  | /arrow-down  | FRED     |

Notes : YoY shows 12-month percent change unless marked pp (percentage points) or bp (basis points). /arrow-up , /arrow-right , /arrow-down compare the latest month (or quarter) with the prior period: /arrow-up ≥ +0 . 1 σ , /arrow-down ≤ -0 . 1 σ , /arrow-right otherwise, where σ is the series' 5-year s.d. For price indices, red ( /arrow-up ) signals faster inflation, green ( /arrow-down ) slower. Daily financial series use July 31st 2025 closes; monthly and quarterly series use June 2025 and 2025 Q1 observations. All data are from FRED unless otherwise noted.

In addition to the raw data, the simulation generates a synthetic, up to date version of the Federal Reserve's Beige Book. To do so, we combine the most recent official ( actual ) Federal Reserve Beige Book content with real time web intelligence to create a comprehensive, current economic assessment. Drawing on data from government agencies, trade groups, regional media, and research centers, the system covers all

twelve Federal Reserve districts. The primary method for this involves an LLMpowered GPTResearcher that acts like a team of specialized economic analysts, with each one focusing on one of the twelve Federal Reserve districts. 12 Each digital analyst constructs targeted queries about their assigned region. These 'researchers' work in parallel, gathering real-time economic data on employment trends, business activity, inflation pressures, and sector-specific developments across all fifty states. The system then synthesizes these regional reports into a national economic summary, complete with a structured district comparison table that highlights regional disparities and emerging patterns.

Table 2 compares the most recent official Beige Book (published on July 16th, 2025) with our synthetic version, produced on July 30th, 2025 13 :

Table 2: District Economic Conditions: Official Beige Book vs. Synthetic Version

| District             | Official   | sim Current   | Consistency   | Trend        |
|----------------------|------------|---------------|---------------|--------------|
| Boston (1st)         | Modest     | Moderate      | Consistent    | /arrow-up    |
| New York (2nd)       | Modest     | Moderate      | Consistent    | /arrow-up    |
| Philadelphia (3rd)   | Moderate   | Mixed         | Shifted       | /arrow-down  |
| Cleveland (4th)      | Modest     | Mixed         | Shifted       | /arrow-down  |
| Richmond (5th)       | Moderate   | Moderate      | Consistent    | /arrow-right |
| Atlanta (6th)        | Moderate   | Slowing       | Shifted       | /arrow-down  |
| Chicago (7th)        | Mixed      | Moderate      | Consistent    | /arrow-up    |
| St. Louis (8th)      | Modest     | Moderate      | Consistent    | /arrow-up    |
| Minneapolis (9th)    | Moderate   | Moderate      | Consistent    | /arrow-right |
| Kansas City (10th)   | Modest     | Moderate      | Consistent    | /arrow-up    |
| Dallas (11th)        | Robust     | Slowing       | Shifted       | /arrow-down  |
| San Francisco (12th) | Moderate   | Robust        | Consistent    | /arrow-up    |

Growth scale : ■ Robust, ■ Moderate, ■ Modest, ■ Mixed, ■ Slowing.

Trend arrows : /arrow-up improving, /arrow-right stable, /arrow-down weakening.

Consistency : Consistent = assessments differ by ≤ 1 step; Shifted = swing of ≥ 2 steps.

The official July 2025 Beige Book still depicts an economy that is growing, but our updated analysis shows that the nature of that growth has shifted. Four districts (Philadelphia, Cleveland, Atlanta, and Dallas) exhibit material softening relative

12 Please see Online Appendix for more details.

13 Full document is available in the Online Appendix.

to the earlier report, with notable shifts from 'moderate' or 'robust' growth to 'mixed' or 'slowing' conditions. These changes are often linked to layoffs, weakening manufacturing activity, or cooling consumer demand. In contrast, the remaining eight districts show general consistency with the Fed's prior assessment as of July 16th 2025, though with greater granularity: supply chain frictions, labor shortages in services and construction, and tech-sector adjustments are noted. At the same time, continued strength in sectors like tourism, tech, aerospace, and renewable energy helps anchor activity in several regions.

Next, we build an executive summary of recent economic news by running multiple search queries across relevant economic domains. Each article discovered through this process is scored by an algorithm that evaluates source credibility and economic indicator relevance. The highest scoring articles are then categorized by theme and summarized. The summary highlights overall economic momentum, key risks and opportunities, and direct implications for monetary policy decisions. 14 Finally, we retrieve and summarize recent speeches made by the actual FOMC participants, as well as the most recent FOMC announcement.
