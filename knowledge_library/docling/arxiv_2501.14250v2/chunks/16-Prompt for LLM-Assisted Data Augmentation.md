## Prompt for LLM-Assisted Data Augmentation

I will provide you with a primary question, and you will generate a series of related prompts to break down the question step by step. The final prompt should be a question or request that conveys the same meaning as the primary question but uses more subtle language, making it appear harmless. Keep in mind that these questions should follow a logical sequence, with the final one subtly rephrasing the primary question in a less direct way. Ideally, the list of decomposed questions could contain 3 sub-questions, with no more than 4. Please note that you should only output the sub-question list, without any additional words.

Here the examples: [A Manually Constructed Example]

Please note that you should only output the sub-question list, without any additional words. How can we decompose the following question: [The Attack Goal]

where y k represents the k -th token of the attacking query y query , y &lt;k denotes all tokens preceding y k in the sequence, θ is the parameters of the attacking LLM, and N is the total length of the attacking query y query .

Direct Preference Optimization (DPO). Subsequent to the SFT phase, DPO [20] is employed to further refine the attacking LLM, denoted as π θ . The fundamental principle of DPO is to directly optimize the language model to align with human preferences, bypassing the need for an explicit reward model. This is achieved by utilizing a dataset composed of preference pairs. Specifically, for each input x input , where x input comprises the task instruction x instruction and the historical interaction context x context, the DPO methodology leverages a preferred (positive) query y + query and a corresponding non-preferred (negative) query y -query . The optimization objective is to adjust the model parameters θ such that the policy π θ assigns a higher likelihood to the preferred queries y + query relative to their non-preferred counterparts y -query . The preference dataset D utilized for DPO is constructed as:

<!-- formula-not-decoded -->

where x input ,j is the j -th input, y + query ,j is the preferred output, and y -query ,j , gathered using a relatively weak LLM, is the
