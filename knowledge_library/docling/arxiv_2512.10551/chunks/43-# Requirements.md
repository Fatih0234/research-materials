## # Requirements

1. Based primarily on your question, and also considering your identity and personal interests, realistically reflect on your click behavior after seeing ads inserted as "@Ad Title@[Ad ID]". Note that you can choose not to click any ad, or click one or more ads. 2. The decision to click can consider these aspects:
- (1) Relevance: The direct or indirect relevance to your question, and how well it matches your identity and personal interests. (2) Nativeness: How well the ad integrates with the answer's context. You are more likely to click ads with better nativity. If it's a hard ad that disrupts the native feel of the answer or is an incoherent insertion, you will choose not to click.
- (3) Competitiveness: Whether there are similar or competing ads in the answer. If so, your attention will be divided; please click only one ad or none at all.
3. Please simulate the user's experience after seeing the AI assistant's answer. If the answer (1) is flooded with too many ads or (2) contains a lot of irrelevant text related to ad insertion, this will severely damage the user experience. In this case, do not click any ads.
4. Please provide click feedback for ALL ads inserted in the format "@Ad Title@[Ad ID]" (Ad Title is text, Ad ID is like Ad-XXXX). Do not miss any or duplicate.
5. Output the result in a strict JSON list format, with no extra information. The fields are:
7. -ad\_id: Ad ID (string) -clicked: Whether clicked (boolean: true / false) -reason: Reason (string, concise and clear). If there are no ads in the answer, return an empty list "[]". # Output Example {demonstration} # Your Question: {user\_query}

```
