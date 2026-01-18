## F AN ABLATION STUDY WITH AN 'OUT-OF-THE-BOX' LLM AGENT

Throughout Section 3.1, we endowed agents with the ability to plan and reflect as they played the FPSB and SPSB auctions. This 'plan-bid-reflect' loop reflects a modest instantiation of the chain-of-thought paradigm common in the machine learning literature and previous LLM auction experiments (Wei et al., 2022; Fish et al., 2024). However, one might reasonably ask how much of the sophisticated play we observe is actually due to this ability to plan and reflect.

Hence, we also report results of the experiments of Section 3.1 with 'Out-of-the-box' agents namely, we directly query LLM agents (after providing them with auction rules and their value, as per our simulation process) without eliciting their plans or allowing them to reflect on the results of the previous rounds. These IPV experiment results are reported in Figure 8.

1183 1184 1185 1186 1187 Overall, the bidding behaviors exhibited by the agents remain largely monotonic. However, interesting differences emerged between the plan-bid-reflect agents and the out-of-the-box agents. With the out-of-the-box LLM bidders there is now little difference in the bidding behavior between the FirstPrice and Second-Price auction, a stark difference from the plan-bid-reflect LLM bidders. Now, and unlike in human-subject experiments, no overbidding beyond the agent's value was observed in SPSB auctions. Specifically, in the left panel of Figure 8, no points lie above the bid=value line.

<!-- image -->

1239

1240

1241

Figure 6: Robustness check with Currency Variation under IPV setting.

1242

1243

1244

1245

1246

1247

1248

1249

1250

1251

1252

1253

1254

1255

1256

1257

1258

1259

1260

1261

1262

1263

1264

1265

1266

1267

1268

1269

1270

1271

1272

1273

1274

1275

1276

1277

1278

1279

1280

1281

1282

1283

1284

1285

1286

1287

1288

1289

1290

1291

1292

1293

1294

1295

Values
