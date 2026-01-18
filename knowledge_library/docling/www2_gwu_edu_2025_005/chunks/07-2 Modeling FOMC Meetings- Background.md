## 2 Modeling FOMC Meetings: Background

' The debate on monetary policy is going on 365 days a year for 24 hours a day, all around the world. The meetings are definitely important, but they're a snapshot of the ongoing debate. '

- Former FOMC member James Bullard, in an interview 8

FOMC meetings are highly structured deliberations that anchor U.S. monetary policy. However, as James Bullard, former president of the Federal Reserve Bank of St. Louis, suggests, they represent only a moment in time within a broader, ongoing policy debate. While the meetings formalize key decisions, the underlying policy dialogue spans months, both within and beyond the Fed.

Each meeting typically follows a fixed agenda: staff economists present updated

8 See Hyatt (2024) for the full interview.

forecasts and alternative scenarios; FOMC members then offer prepared statements outlining their interpretations of the data and views on appropriate policy. 9 Following this stage, the Chair opens the floor for discussion, where members respond to others' arguments, and debate policy options. Finally, the committee votes on the policy decision. Dissenting votes are relatively rare and, when they occur, serve mainly to register an alternative viewpoint rather than to overturn the majority consensus (Thornton and Wheelock, 2014).

Our simulation mirrors the FOMC's workflow. The sequence of events, the information available to each participant, and the conversational norms governing discussion are modeled to reflect actual FOMC dynamics. Because monetary policy is an ongoing debate rather than a static decision, our framework can continuously ingest 'fresh' economic and market data, dynamically updating the simulation to reflect evolving conditions. Each FOMC participant in our framework is represented by an independent agent (implemented via an LLM) with a distinct profile. In the baseline setup, these agents correspond to the twelve voting members of that year's FOMC. However, the framework can easily extensible to include non-voting participants, other attendees, or hypothetical members. We describe the simulation pipeline next.
