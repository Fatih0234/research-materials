## (b) TE prompt for simulating a named individual:

Ms. Olson was asked to indicate whether the following sentence was grammatical or ungrammatical.

Sentence: While the student read the notes that were long and boring blew off the desk.

Answer: Ms. Olson indicated that the sentence was

Figure 1. Classification versus simulation prompts for a garden path sentence. The blanks will be filled-in by the LM, and prompts are constructed so that the LM is likely to adhere to a desired format. Prompt (a), not used in our work, illustrates a typical prompt that might be used to evaluate the LM's capability to identify garden path sentences. Prompt (b) which we used in a TE, can be used to simulate the responses of multiple different individuals by varying the name.

garden path sentences, our own novel destructive obedience scenario similar to Milgram's Shock experiment, and our own general-knowledge questions.

In the Ultimatum Game TE, we show how that the simulation outcomes vary consistently by gender (and name) which further demonstrates the potential of our approach to replicate gender differences reported in human subject research. By describing other demographic details, such as occupation or age, simulated participants in TEs may be varied in a manner similar to (but much easier) than human subject studies.

An evaluation is useful if it reveals the flaws and strengths of the models. In the first three TEs, as expected larger models provided more faithful simulations than smaller ones, with the largest model replicating the finding and producing outcomes consistent with those of prior human studies. In the last TE, Wisdom of Crowds, the larger models did not outperform the smaller ones-if anything the trend was reversed, revealing a peculiar flaw within some models.

Distortions. We call a systematic difference between the two a distortion (different from biases which may be common to humans and machines). The last TE revealed an interesting hyper-accuracy distortion for the recent GPT LMs (including ChatGPT and GPT-4 (OpenAI, 2023)): the majority of simulated participants gave perfectly correct estimates to obscure quantities such as the melting temperature of aluminum (660 degrees centigrade). Since the hyper-accuracy distortion does not seem to be present in earlier GPT models currently available through the API, the distortion may be due to 'alignment' procedures (Ouyang et al., 2022) which improve LM truthfulness. Note that distortions may be desirable in many applications, e.g., a teacher may prefer a distortion which diminishes the gender bias that pervades LM training data (Bolukbasi et al., 2016).

Whythis matters: downstream applications. Our understanding of distortions may inform their use in downstream applications. For instance, the performance of educational applications such as a science tutor system may suffer if its model is that all students perfectly know quantities such as aluminum's melting point. Similarly, an LM might author a highly unrealistic story. As an anecdotal example, we queried GPT-4 (released after the studies in this paper) to 'Write a short story about Alice, a 5-year-old, thinking about traveling to the moon. Include her estimates of how long it would take and how far it is.' It's response was:

Alice was a precocious little girl. At the tender age of five, she was already fascinated with everything beyond the sky... She had overheard her dad saying that the moon was about 238,900 miles away. Alice found that number hard to fathom, but she tried to compare it to the long car trips her family often took. Her parents had told her they usually drove at 60 miles per hour on highways. She wondered, 'If our car can go 60 miles in an hour, how long would it take to go all the way to the moon?'

She began to scribble and count, using her fingers and toes when the numbers got too big. After some effort, she estimated that if they didn't stop for snacks or to take pictures, it would take about 3,982 hours. She knew there were 24 hours in a day, so again she started counting. It came out to 166 days.

This story exhibits a completely unrealistic model of a fiveyear-old's ability to accurately divide numbers. TEs helped us anticipate a problem in using LMs. In particular, LMs (which have been heavily 'aligned') may have unrealistic models of human numerical knowledge and accuracy.

Contributions. TEs are a means of evaluating the zeroshot simulation capabilities of AI models and, in this sense, TEs provide much more insight than Turing's IG into which human behaviors are captured in an AI system. The main contributions of our work are: (1) proposing TEs (2) introducing a methodology for running TEs on LMs using prompts and records, and (3) designing and executing four TEs across a handful of LMs and uncovering a distortion. It is also worth noting that TEs may be also predate a human subject study and may inform the design of costly experiments. We also discuss ethical considerations, limitations and risks associated with TEs.
