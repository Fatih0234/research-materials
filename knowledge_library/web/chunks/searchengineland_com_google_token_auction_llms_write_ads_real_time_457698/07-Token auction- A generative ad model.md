## Token auction: A generative ad model
In traditional Google Ads, advertisers bid on keywords. 
  * The system then selects a matching pre-written ad, based on price and quality. 
  * The creative is fixed, and the auction is about placement.


In the Token Auction model proposed by the research paper, the paradigm flips. 
Advertisers don’t bid for slots; they bid to shape the very words the LLM will generate.
Here’s how it works according to research:
  * Each advertiser submits a single **bid**.
  * Alongside the bid, they provide a **language model** representing their brand’s voice, tone, and messaging preferences.
  * The system generates the response **token by token** , weighing the influence of each advertiser’s model according to their bid.


Rather than picking a winner, the system blends multiple advertisers’ influences into the output. The higher the bid, the more the generated language shifts toward that advertiser’s voice.
To aggregate the competing models, the researchers explore two strategies:
  * **Linear aggregation:** A weighted average that maintains incentive compatibility and bid responsiveness.
  * **Log-linear aggregation:** A more complex method that can break incentive alignment under certain conditions.


Understanding the difference is key: advertisers who don’t grasp which aggregation model is used might overspend with minimal impact, a costly mistake in a new kind of auction economy.
![The token auction model architecture. Source: Google Research](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201074%20900'%3E%3C/svg%3E)_The token auction model architecture, Source:[Google Research](https://storage.googleapis.com/gweb-research2023-media/images/MechanismDesign-2-Architecture.width-1250.png)_
