## 3 Experimental Setup

With the goal of better understanding the ability of multi-agent LLM systems to model prosocial human behavior, we simulate three different types of experiments: (1) simulations which aim to directly capture effects observed in a previous lab experiment with human subjects; (2) simulations which combine effects from multiple previous lab experiments with human subjects; and (3) select "in-the-wild" real-world scenarios we use as case studies towards identifying mechanisms necessary for simulations to display human-like behavior. For all experiments, we use OpenAI's GPT4 (model gpt-4o-mini), which has been shown to have the ability to interpret inherently human concepts such as equity and also scores well on a variety of standardized tests, ranging from the Bar Exam to the GRE [24].

We specifically address the following three research questions:

- RQ1 Can multi-agent LLM system simulations replicate behaviors observed in PGG lab experiments with human subjects?
- a. Does priming LLM agents via game name replicate the effect of priming humans via game name?
- b. Does introducing transparency in contribution between LLMagentsreplicate the effect of introducing transparency in contribution between humans?
- c. Does varying the endowments of LLM agents replicate the effect of varying endowments of humans?
- RQ2 Can multi-agent LLM system simulations transfer effects observed in non-PGG lab experiments to simulations of the PGG?
- a. Does priming LLM agents with a methodology used in non-PGG cooperation game lab experiments have the expected result in LLM simulations of the PGG?
- b. Does the effect of priming over time, observed to fade in non-PGG competition game lab experiments, hold in LLM simulations of the PGG?
- RQ3 To what extent are multi-agent LLMs complex enough to simulate the rich set of unbounded options, actions, and interactions people do in the real world, outside of the lab?
- a. To see the complex interactions observed in the real world, what simulation mechanisms do we have to add to the set up of the system?

We expect generally positive results for the first two research questions, given that other work has shown the ability of LLMs to replicate lab experiments that are both published and unpublished [15], but still verify this in the context of the PGG towards understanding the abilities of multi-agent LLM systems to simulate prosocial behavior. The third research question is more open-ended - we use case studies of real-world scenarios towards identifying mechanisms required for simulations to show expected outcomes, a process which can be continued to be used by policy makers. As policy makers consider the specific scenarios which they need to simulate, they may realize and implement new mechanisms required to enable their simulation. However, we also expect that mechanisms will be generalizable to an extent across simulations of various situations.
