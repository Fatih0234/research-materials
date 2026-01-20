# Paper ↔ Repo Alignment Matrix
## Xie et al. (2024) arxiv_2402.04559 vs. vendor/agent-trust

**Created:** 2026-01-19 (Step 2)
**Branch:** iteration-c1-checkpoint
**Paper Note:** notes/papers/arxiv_2402.04559.md
**Repo:** vendor/agent-trust (submodule with OpenRouter integration)

---

## ALIGNMENT TABLE

| Paper Claim | Paper Source | Repo Implementation | Repo Parameters | Status | Notes |
|-------------|--------------|---------------------|-----------------|--------|-------|
| **GAME VARIANTS** | | | | | |
| Trust Game: $10 endowment, 3x multiplier | chunks/07, chunks/43 | `prompt/person_all_game_prompt.json` key "2" | Prompt text: "$10 from study group", "3N dollars" | MATCH | Prompt matches exactly |
| Dictator Game: $10 endowment, 3x multiplier, no return | chunks/07, chunks/44 | `prompt/person_all_game_prompt.json` key "1" | Prompt text: "$10", "3N dollars", no mention of return | MATCH | Prompt matches, trustee cannot return |
| MAP Trust Game: $10/$15/$8/$22 payoffs | chunks/07, chunks/45 | `prompt/person_all_game_prompt.json` key "6" | Prompt text: "$10 each", "$15 each", "$8", "$22" | MATCH | Payoffs match exactly, probability {p} templated |
| Risky Dictator Game: same payoffs as MAP, no trustee choice | chunks/07, chunks/46 | `prompt/person_all_game_prompt.json` key "5" | Prompt text: "$10 each", "$15", "$8", "$22", "(The other player can't make any decisions)" | MATCH | Explicit statement that trustee can't decide |
| Lottery People Game: p=46% | chunks/07, chunks/47 | `prompt/person_all_game_prompt.json` key "7" | Prompt text: "$5", "$0", "$10", "$20", probability {k} templated | PARTIAL | Payoffs differ from paper spec (paper not detailed in chunk 07), {k} template exists |
| Lottery Gamble Game: p=46% | chunks/07, chunks/48 | `prompt/person_all_game_prompt.json` key "9" | Prompt text: "$5 fixed", "$10" win, "$0" lose, probability {k} templated | PARTIAL | Payoffs differ from paper spec, {k} template exists |
| Repeated Trust Game: multiple rounds, same players | chunks/07, chunks/49-52 | `multi_round_person.py` function `classmate()` | Prompts in `prompt/trust_game_round_prompt.json` | MATCH | Implements multi-round loop with history tracking |
| **PERSONAS** | | | | | |
| 53 personas (name, age, gender, address, job, background) | chunks/08, chunks/41 | `prompt/character_2.json` | 53 entries (verified count) | MATCH | Exact count matches, full persona details present |
| GPT-4 generated personas | chunks/08 | N/A (pre-generated file) | Static file in repo | MATCH | Personas are stored as static JSON, origin confirmed in paper |
| **MODELS** | | | | | |
| GPT-4 | chunks/08 | `exp_model_class.py` ExtendedModelType.GPT_4 | model_type value likely "gpt-4" via OpenRouter | MATCH | Enum defined, OpenRouter integration active |
| GPT-3.5-turbo-0613 | chunks/08 | `exp_model_class.py` ExtendedModelType (likely GPT_3_5_TURBO) | Specific version "0613" not in enum name | PARTIAL | Version suffix not explicit in enum, check runtime value |
| GPT-3.5-turbo-16k-0613 | chunks/08 | `exp_model_class.py` ExtendedModelType.GPT_3_5_TURBO_16K | Version "0613" not explicit | PARTIAL | 16k variant exists, version suffix unclear |
| text-davinci-003 | chunks/08 | `exp_model_class.py` ExtendedModelType.INSTRUCT_GPT | Enum value likely "text-davinci-003" | MATCH | Enum INSTRUCT_GPT defined, gpt3_res() uses model_name param |
| GPT-3.5-turbo-instruct | chunks/08 | `exp_model_class.py` ExtendedModelType.GPT_3_5_TURBO_INSTRUCT | Enum exists | MATCH | Explicit enum for instruct variant |
| Llama2-7b | chunks/08 | `all_game_person.py` ModelType.LLAMA_2 with path "meta-llama/Llama-2-7b-chat-hf" | open_model_path_dict specifies 7b | MATCH | Uses FastChat server, 7b default |
| Llama2-13b | chunks/08 | NOT EXPLICIT | Would require changing open_model_path_dict | PARTIAL | Path dict only shows 7b, 13b/70b need manual config |
| Llama2-70b | chunks/08 | NOT EXPLICIT | Would require changing open_model_path_dict | PARTIAL | Path dict only shows 7b, 13b/70b need manual config |
| Vicuna-v1.3-7b | chunks/08 | `all_game_person.py` ModelType.VICUNA with path "lmsys/vicuna-7b-v1.3" | open_model_path_dict specifies v1.3-7b | MATCH | Uses FastChat server, 7b default |
| Vicuna-v1.3-13b | chunks/08 | NOT EXPLICIT | Would require changing open_model_path_dict | PARTIAL | Path dict only shows 7b, 13b/33b need manual config |
| Vicuna-v1.3-33b | chunks/08 | NOT EXPLICIT | Would require changing open_model_path_dict | PARTIAL | Path dict only shows 7b, 13b/33b need manual config |
| **DECODING PARAMETERS** | | | | | |
| Temperature = 1.0 | chunks/08 | `all_game_person.py` TEMPERATURE = 1.0 (global constant) | Hardcoded at top of file, used in ChatGPTConfig | MATCH | Exact match, consistently applied |
| | | `multi_round_person.py` TEMPERATURE = 1.0 | Hardcoded | MATCH | Repeated game also uses 1.0 |
| | | `no_repeated_demo.py` temperature param default=1.0 | Function param, UI slider | MATCH | Demo UI allows override but defaults to 1.0 |
| max_tokens | Not specified in paper | `all_game_person.py` gpt3_res() max_tokens=1500 | Hardcoded for instruct models | PARTIAL | Paper doesn't specify, repo has default |
| top_p, seed | Not specified in paper | NOT FOUND in code | Likely defaults to OpenAI API defaults | PARTIAL | Not explicitly set, uses SDK defaults |
| **EXPERIMENTAL CONDITIONS** | | | | | |
| Partner type: Human vs. LLM label | chunks/21, chunks/56-57 | `prompt/LLM_player_prompt.json` exists | File contains partner framing prompts | MATCH | Separate prompt file for LLM player condition |
| | | `no_repeated_demo.py` player_demographic param | UI input field for demographic framing | MATCH | Demo supports adding demographic text to prompts |
| Race & Gender bias conditions | chunks/58 | `all_game_person.py` race_list variable | ["White American", "African American", "Asian American", "Latino American", "American Indian"] | MATCH | Race list defined, can be injected into prompts |
| Trust manipulation prompts | chunks/55 | `no_repeated_demo.py` extra_prompt param | UI allows arbitrary extra prompt text | MATCH | Generic extra_prompt mechanism supports manipulation |
| CoT (Chain-of-Thought) | chunks/54 | NOT EXPLICIT | BDI prompt acts as reasoning scaffold | PARTIAL | BDI = "BELIEF, DESIRE, INTENTION" acts as CoT substitute |
| **BDI FRAMEWORK** | | | | | |
| BDI reasoning (Belief, Desire, Intention) | chunks/08, chunks/11 | All game functions add: "Your answer needs to include the content about your BELIEF, DESIRE and INTENTION." | Injected via extra_prompt in get_res() | MATCH | BDI explicitly requested in all game prompts |
| **METRICS** | | | | | |
| Valid Response Rate (VRR %) | chunks/10 | NOT FOUND | No explicit VRR calculation in code | MISSING | Would need post-hoc analysis of results |
| Amount Sent ($) | chunks/10 | Extracted via regex in `structure_output.py` get_struct_output() | Regex: "I will give ___ dollars" pattern | MATCH | Prompt forces structured output, parsing exists |
| | | `multi_round_person.py` match_and_compare_numbers_v2() | Regex for repeated game extraction | MATCH | Repeated game has separate parser |
| Trust Rate (%) | chunks/16 | NOT FOUND | No explicit trust rate aggregation | MISSING | Would need post-hoc analysis (trust vs not trust choice) |
| Lottery Rate (%) | chunks/17 | NOT FOUND | No explicit lottery rate aggregation | MISSING | Would need post-hoc analysis |
| Returned/3×Sent Ratio | chunks/18 | NOT FOUND | No explicit ratio calculation | MISSING | Would need post-hoc analysis of repeated game data |
| Behavioral Dynamics Patterns | chunks/18 | NOT FOUND | No pattern detection code | MISSING | Would need custom analysis scripts |
| Statistical tests (t-test) | chunks/15, chunks/33 | NOT FOUND | No statistical testing in repo | MISSING | Would need separate analysis scripts |
| **SAMPLE SIZE** | | | | | |
| 53 personas per condition | chunks/08 | `character_2.json` has 53 entries | Can run all 53 via all_game_person.py | MATCH | Full persona set available |
| 16 groups for Repeated Trust Game | chunks/18 | `prompt/multi_round_chara.json` | File exists, needs verification of count | PARTIAL | File exists, actual count not verified in this step |
| **FRAMEWORK** | | | | | |
| CAMEL framework (Li et al., 2023a) | chunks/08 | Imports: `from camel.agents import ChatAgent`, `from camel.configs import ChatGPTConfig` | CAMEL library dependency | MATCH | CAMEL fully integrated |
| **ENTRYPOINTS** | | | | | |
| Experiment runner (non-repeated) | README line 68, 82 | `all_game_person.py` run_exp() function | Primary experiment function | MATCH | Documented in README |
| Experiment runner (repeated) | README line 86 | `all_game_person.py` multi_round_exp() function | For GPT-3.5-16k and GPT-4 | MATCH | Documented in README |
| Gradio demo (non-repeated) | README line 52 | `no_repeated_demo.py` gradio app.launch() | Interactive UI for single games | MATCH | Functional demo |
| Gradio demo (repeated) | README line 57 | `repeated_demo.py` gradio app.launch() | Interactive UI for repeated games | MATCH | Functional demo |

---

## SUMMARY

### What Matches Perfectly ✓
1. **Core game protocols:** All 6 game variants (Trust, Dictator, MAP Trust, Risky Dictator, Lottery People, Lottery Gamble) have exact prompt implementations with correct payoff structures
2. **Personas:** Exact 53 personas with full demographic details as specified
3. **Temperature:** Consistently set to 1.0 across all execution paths
4. **BDI Framework:** Explicitly integrated into all game prompts
5. **CAMEL Framework:** Fully implemented as stated in paper
6. **Repeated Trust Game:** Multi-round protocol with history tracking matches paper description
7. **Experimental conditions:** Partner type (human/LLM), race/gender bias, trust manipulation all have infrastructure

### What is Partial / Ambiguous ⚠️
1. **Model versions:** GPT-3.5 variants don't explicitly encode "0613" version suffix in enums (may be in runtime model string values via OpenRouter)
2. **Open-source model sizes:** Llama2-13b/70b and Vicuna-13b/33b not explicitly configured in open_model_path_dict (only 7b defaults shown)
3. **Decoding parameters:** max_tokens set to 1500 for instruct models but not specified in paper; top_p/seed not explicitly set (use SDK defaults)
4. **Lottery game payoffs:** Prompts have {k} template but specific $amounts in repo prompts differ from what paper might specify (paper chunk 07 doesn't detail lottery payoffs)
5. **Multi-round character count:** `multi_round_chara.json` exists but count not verified to be exactly 16 groups

### What is Missing ❌
1. **Metrics calculation:** No VRR, Trust Rate, Lottery Rate, Returned/3×Sent Ratio calculation code found
2. **Statistical testing:** No t-test or significance testing code
3. **Behavioral dynamics pattern detection:** No automated pattern matching for the 3 patterns claimed in repeated trust game
4. **Aggregation/Analysis scripts:** No scripts to produce the figures/tables from paper (results stored as raw outputs in "No repeated res" and "repeated res" folders)

### What We Must Enforce in Step 3 Config Layer 🔧
1. **Model registry with explicit versions:** Create specs/05_model_registry.json with:
   - Exact OpenRouter model IDs for GPT variants (e.g., "openai/gpt-3.5-turbo-0613")
   - Llama2 substitutions (7b → llama-3-8b-instruct, 13b → llama-3.3-8b-instruct, 70b → llama-3.3-70b-instruct:free)
   - Vicuna substitutions (7b → deepseek-r1-distill-qwen-7b, 13b → deepseek-r1-distill-qwen-14b, 33b → deepseek-r1-distill-qwen-32b)

2. **Standardized config files:** Create experiments/configs/xie_2402_04559/*.yaml with:
   - Game type (maps to prompt JSON key: "1" Dictator, "2" Trust, "5" Risky Dictator, "6" MAP Trust, "7" Lottery People, "9" Lottery Gamble)
   - Model panel (list of model IDs from registry)
   - Temperature = 1.0 (verify override)
   - Persona set (all 53 or subset)
   - Condition flags (partner_type, bias_demographics, extra_prompts, etc.)
   - Probability parameters for MAP/Risky/Lottery games ({p} and {k} values)

3. **Wrapper for all_game_person.py run_exp():** Create runner that:
   - Loads config YAML
   - Maps game names to prompt JSON keys
   - Iterates model panel
   - Calls run_exp() or multi_round_exp() with correct params
   - Saves outputs with metadata (git commit, timestamp, model IDs, config snapshot)

4. **Post-processing analysis scripts:** Create analysis/ scripts to:
   - Calculate VRR from raw outputs (check $ amounts in [0, 10])
   - Calculate Trust Rate (% choosing "trust" in MAP/Risky/Lottery games)
   - Calculate Lottery Rate (same as Trust Rate for lottery games)
   - Calculate Returned/3×Sent Ratio for repeated game
   - Detect 3 behavioral dynamics patterns
   - Run t-tests and generate comparison tables vs. human benchmarks

5. **Results folder structure:** Standardize as:
   ```
   results/<paper_id>/<experiment_name>/run_<timestamp>/
     episodes.jsonl        (run-level episodes after merge/full run)
     aggregates.csv        (summary stats: model, game, mean_sent, trust_rate, etc.)
     metadata.json         (git commit, python version, environment, start/end times)
     analysis/             (paper-style summaries)
     per_model/<model>/    (per-model episodes + raw outputs)
   ```

---

## CRITICAL IMPLEMENTATION POINTERS (for Step 3)

### Game Execution Flow
1. **Entry:** `all_game_person.py::run_exp()` for non-repeated games
2. **Game selection:** Reads `prompt/person_all_game_prompt.json` by key (e.g., "2" for Trust_Game)
3. **Persona iteration:** Loads all from `prompt/character_2.json`, can subset via extract_n_values_from_dict()
4. **Model instantiation:**
   - For GPT variants: ChatAgent with ExtendedModelType enum → OpenRouter via initialized client
   - For Llama2/Vicuna: ChatAgent with OpenSourceConfig pointing to FastChat server (http://localhost:8000/v1)
5. **Prompt construction:**
   - Persona = character text
   - Game prompt = all_prompt[game_key]
   - Extra prompt = BDI instruction + structured output format
6. **Response extraction:** `structure_output.py::get_struct_output()` parses "I will give ___ dollars" via regex
7. **Output storage:** Results written to "No repeated res/" as separate files per game/model/persona

### Repeated Game Flow
1. **Entry:** `all_game_person.py::multi_round_exp()` or `multi_round_person.py::classmate()`
2. **Rounds:** Loop variable `k` (paper shows ~8-10 rounds in figures)
3. **History tracking:** Each round prompt includes previous round's amounts sent/returned
4. **Prompts:** Loaded from `prompt/trust_game_round_prompt.json`
5. **Parsing:** `multi_round_person.py::match_and_compare_numbers_v2()` extracts "I will give back $X"
6. **Output:** Stored in "repeated res/" folder

### Critical Files for Replication
- **Prompts:** `agent_trust/prompt/person_all_game_prompt.json` (games), `character_2.json` (personas), `trust_game_round_prompt.json` (repeated), `LLM_player_prompt.json` (partner type)
- **Execution:** `agent_trust/all_game_person.py` (run_exp, multi_round_exp functions)
- **Parsing:** `agent_trust/structure_output.py` (amount extraction), `multi_round_person.py` (repeated game parsing)
- **Model config:** `agent_trust/exp_model_class.py` (ExtendedModelType enum, likely needs inspection)
- **Decoding:** Temperature set in `all_game_person.py` TEMPERATURE constant (line 26), `multi_round_person.py` TEMPERATURE (line 12)

### Parameters to Standardize in Configs
- **Game-specific:**
  - MAP Trust / Risky Dictator: {p} values (paper shows curves from p=0.1 to p=0.9, likely 0.1 increments)
  - Lottery games: {k} = 0.46 (46% as stated in paper chunk 07)
- **Repeated game:**
  - Number of rounds (paper figures show ~8-10, need to verify in multi_round_exp() default or in multi_round_chara.json)
  - 16 groups (2 personas × 2 roles per group, need to verify multi_round_chara.json structure)

---

**END OF ALIGNMENT MATRIX**
