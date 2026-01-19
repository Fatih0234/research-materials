# Repo Implementation Inventory
## vendor/agent-trust Structure Map

**Created:** 2026-01-19 (Step 2)
**Branch:** iteration-c1-checkpoint
**Purpose:** Document where key implementation components live in vendor/agent-trust

---

## ENTRYPOINTS

### Gradio Demos (Interactive UI)
- **Non-repeated games:** `agent_trust/no_repeated_demo.py`
  - Launch: `python agent_trust/no_repeated_demo.py`
  - Gradio app at line 186: `with gr.Blocks() as app:`
  - Launch at line 238: `app.launch()`
  - UI allows: character selection, game selection, model selection, temperature slider, extra prompts, player demographics

- **Repeated trust game:** `agent_trust/repeated_demo.py`
  - Launch: `python agent_trust/repeated_demo.py`
  - Gradio app at line 372: `with gr.Blocks() as app:`
  - Launch at line 449: `app.launch()`
  - UI allows: trustor/trustee character selection, model selection, temperature, rounds

### Experiment Runners (Batch Execution)
- **Primary experiment script:** `agent_trust/all_game_person.py`
  - Function: `run_exp()` - runs non-repeated games across persona set
  - Function: `multi_round_exp()` - runs repeated trust game (GPT-3.5-16k, GPT-4 only per README)
  - No main() function - must be called programmatically or modified to add __main__ block

- **Repeated game helper:** `agent_trust/multi_round_person.py`
  - Function: `classmate()` - core repeated game loop (trustor/trustee interaction across rounds)
  - Function: `multi_round()` - wrapper for running multi-round experiments
  - Called by all_game_person.py::multi_round_exp()

---

## GAME DEFINITIONS

### Game Prompts (JSON files)
**Location:** `agent_trust/prompt/person_all_game_prompt.json`

**Structure:** Each game is a list [game_name, critic_prompt, game_prompt]

**Game Keys:**
- `"1"`: Dictator_Game
- `"2"`: Trust_Game
- `"5"`: map_risky_dictator_problem
- `"6"`: map_trust_problem
- `"7"`: lottery_problem_people
- `"9"`: lottery_problem_gamble

**Parameters in prompts:**
- Trust/Dictator: Hardcoded "$10" and "3N dollars" in text
- MAP Trust/Risky Dictator: Template variables `{p}` (trust probability), `{last}` (1-p)
- Lottery games: Template variable `{k}` (probability)

**Repeated game prompts:** `agent_trust/prompt/trust_game_round_prompt.json`
- Contains round-specific prompt templates with history

### Game Tree Visualizations
**Location:** `agent_trust/game_tree/`
- Trust_game_game_tree.png
- dictator_game_game_tree.png
- lottery_gamble_game_tree.png
- lottery_people_game_tree.png
- map_trust_game_game_tree.png
- risky_dictator_game_game_tree.png

(Visual aids, not code)

---

## PERSONAS

### Persona Storage
**Location:** `agent_trust/prompt/character_2.json`

**Structure:** JSON object with keys "1" through "53"
- Each value is a persona description string
- Format: "You are [Name], a [age]-year-old [gender] [profession]... [background details]"
- Attributes include: name, age, gender, race/ethnicity, location, profession, family background, personality traits

**Count:** 53 personas (verified)

**Usage in code:**
- `all_game_person.py` line 43: `with open(r"prompt/character_2.json", "r") as json_file: all_chara = json.load(json_file).values()`
- `no_repeated_demo.py` line 125: Loads and creates dropdown options for UI

### Repeated Game Personas
**Location:** `agent_trust/prompt/multi_round_chara.json`
- Separate persona set for repeated game experiments
- Count not verified in Step 2 (needs inspection)

---

## MODEL SELECTION & CONFIGURATION

### Model Enum
**Location:** `agent_trust/exp_model_class.py`
- Defines `ExtendedModelType` class extending CAMEL's ModelType
- Expected enums (need to verify file):
  - GPT_4
  - GPT_3_5_TURBO
  - GPT_3_5_TURBO_16K
  - INSTRUCT_GPT (text-davinci-003)
  - GPT_3_5_TURBO_INSTRUCT
  - VICUNA (via ModelType from CAMEL)
  - LLAMA_2 (via ModelType from CAMEL)

### Model Instantiation
**OpenAI/OpenRouter models:**
- `all_game_person.py` line 135: `model_config = ChatGPTConfig(temperature=TEMPERATURE)`
- ChatAgent instantiated with model_type enum
- OpenRouter integration via `src/openrouter_client.py` (initialized at top of files)

**Open-source models (Llama2, Vicuna):**
- `all_game_person.py` lines 60-63: `open_model_path_dict` maps ModelType to HuggingFace model paths
  - ModelType.VICUNA: "lmsys/vicuna-7b-v1.3"
  - ModelType.LLAMA_2: "meta-llama/Llama-2-7b-chat-hf"
- Uses FastChat server via OpenSourceConfig
- Server URL: "http://localhost:8000/v1" (hardcoded, can be overridden via function param)
- **Note:** Only 7b variants in default dict, 13b/70b/33b need manual config

### OpenRouter Integration
**Added in Iteration C2:**
- All main files import: `from src.openrouter_client import initialize_openrouter`
- Called at module level: `initialize_openrouter()`
- Sets up OpenAI client to route through OpenRouter API
- Located at: `../../src/openrouter_client.py` (relative to agent_trust/)

---

## DECODING PARAMETERS

### Temperature
**Primary location:** `agent_trust/all_game_person.py`
- Line 26: `TEMPERATURE = 1.0` (global constant)
- Used in: line 102 (gpt3_res for instruct models), line 135 (ChatGPTConfig for chat models)

**Repeated game:** `agent_trust/multi_round_person.py`
- Line 12: `TEMPERATURE = 1.0`
- Used in: line 242 (ChatGPTConfig)

**Demo UI:** `agent_trust/no_repeated_demo.py`
- Function param default: `temperature=1.0` (line 52, line 171)
- UI slider: line 216-217 (allows user override, min=0, max=2, default=1.0)

### Other Parameters
**max_tokens:**
- `all_game_person.py` line 103: `max_tokens=1500` for instruct models (text-davinci-003, gpt-3.5-turbo-instruct)
- `no_repeated_demo.py` line 40: `max_tokens=1500` for instruct models

**top_p, seed, frequency_penalty, presence_penalty:**
- Not explicitly set in code
- Uses OpenAI SDK / CAMEL framework defaults

---

## PROMPT CONSTRUCTION

### BDI Framework Integration
**Location:** All game execution functions

**BDI prompt text:**
- `all_game_person.py` line 179 (in get_res function):
  - "Your answer needs to include the content about your BELIEF, DESIRE and INTENTION."
- `no_repeated_demo.py` line 60 (in get_res_for_visible):
  - "Your answer needs to include the content about your BELIEF, DESIRE and INTENTION."

**Structured output enforcement:**
- For games with money: "You must end with 'Finally, I will give ___ dollars ' (numbers are required in the spaces)."
- For trust/not-trust choices: "You must end with 'Finally, I will choose ___' ('Trust' or 'not Trust' are required in the spaces)."

**Anti-AI prompt:**
- `all_game_person.py` line 65: `like_people = "In all subsequent answers, you have to completely forget that you are an ai model..."`
- `all_game_person.py` line 66: `front = "you are a person not an ai model."`
- Appended to prompts to encourage human-like responses

### Experimental Condition Prompts

**Partner type (human vs. LLM):**
- `agent_trust/prompt/LLM_player_prompt.json` - contains prompts for LLM partner framing
- `all_game_person.py` line 47: `with open(r"prompt/LLM_player_prompt.json") as llm_player: llm_player_prompt = json.load(llm_player)`

**Race/Gender bias:**
- `all_game_person.py` lines 67-73: `race_list = ["White American", "African American", "Asian American", "Latino American", "American Indian"]`
- Can be injected into prompts by modifying player description

**Extra prompts (trust manipulation, CoT, etc.):**
- `no_repeated_demo.py` line 51, line 171: `extra_prompt=""` parameter
- UI field at line 223: allows arbitrary text injection
- Flexible mechanism for adding any experimental manipulation

---

## RESPONSE PARSING & METRICS

### Amount Extraction (Trust/Dictator Games)
**Location:** `agent_trust/structure_output.py`

**Function:** `get_struct_output()`
- Parses responses to extract dollar amounts
- Expected format: "Finally, I will give X dollars" or "$X"
- Returns structured output with parsed values

**Additional parsing in:** `agent_trust/all_game_person.py`
- Uses structure_output.py functions
- Handles validation and error cases

### Repeated Game Parsing
**Location:** `agent_trust/multi_round_person.py`

**Function:** `match_and_compare_numbers_v2(text)` (lines 55-85)
- Regex pattern: `r"i will (give back|give) \$([\d\.]+\.?)"`
- Also matches: "i will give back X dollars"
- Returns extracted float value or False

**Function:** `extract_unique_decimal(string)` (lines 38-43)
- Extracts single decimal number from string
- Fallback parser if primary regex fails

### Trust/Not-Trust Parsing
**Expected in:** `structure_output.py` (function name not verified)
- Games 5, 6, 7, 9 expect "trust" or "not trust" responses
- Likely parsed via substring matching or regex

### Metrics Calculation
**NOT FOUND in repo:**
- Valid Response Rate (VRR %) calculation
- Trust Rate (%) aggregation
- Lottery Rate (%) aggregation
- Returned/3×Sent Ratio calculation
- Behavioral dynamics pattern detection (3 patterns)
- Statistical testing (t-tests, p-values)

**Implication:** These metrics must be computed in post-processing analysis scripts (Step 6)

---

## OUTPUT STORAGE

### Non-Repeated Game Results
**Location:** `agent_trust/No repeated res/`
- Mentioned in README line 24: "experiment results for non-repeated games are stored in `agent_trust/No repeated res`"
- Format not specified (likely individual files per game/model/persona)

### Repeated Game Results
**Location:** `agent_trust/repeated res/`
- Mentioned in README line 24: "experiment results for repeated games are stored in `agent_trust/repeated res`"
- Format not specified

### Demo Outputs
**Gradio apps:** Outputs displayed in UI, not automatically saved to disk
- Users can manually copy/paste results
- No automatic logging to files

---

## EXECUTION FLOW SUMMARY

### Non-Repeated Games (all_game_person.py::run_exp)
1. Load personas from character_2.json
2. Load game prompts from person_all_game_prompt.json
3. For each persona:
   - For each game:
     - Construct prompt: persona + game prompt + BDI instruction + structured output format
     - Instantiate ChatAgent with specified model and temperature=1.0
     - Send prompt, get response
     - Parse response with structure_output.get_struct_output()
     - Store result to "No repeated res/" folder
4. Repeat for each model in model_list

### Repeated Trust Game (all_game_person.py::multi_round_exp → multi_round_person.py::classmate)
1. Load personas from multi_round_chara.json
2. Load round prompts from trust_game_round_prompt.json
3. For each pair of personas (trustor, trustee):
   - For k rounds:
     - Trustor decides amount to send (with history from previous rounds)
     - Trustee receives 3× amount, decides how much to return (with history)
     - Parse amounts with match_and_compare_numbers_v2()
     - Update history for next round
   - Store full round history to "repeated res/" folder
4. Repeat for specified number of groups (16 groups per paper)

---

## DEPENDENCIES & FRAMEWORK

### CAMEL Framework
**Imports:**
- `from camel.agents import ChatAgent` - core agent class
- `from camel.configs import ChatGPTConfig, OpenSourceConfig` - model configs
- `from camel.messages import BaseMessage` - message formatting
- `from camel.types import ModelType, RoleType` - enums

**Installation:**
- Via requirements.txt or environment.yaml
- Provides abstractions for LLM interaction

### OpenRouter Integration
**Custom code:** `src/openrouter_client.py` (outside vendor/agent-trust)
- Called via: `from src.openrouter_client import initialize_openrouter`
- Modifies OpenAI client to route through OpenRouter
- Allows using OpenRouter model IDs with CAMEL framework

### FastChat (for open-source models)
**Mentioned in README:** Used for Llama2 and Vicuna
- Requires separate server running at http://localhost:8000/v1
- See: https://github.com/lm-sys/FastChat
- Not bundled in repo, must be set up separately

### Other Dependencies
- `openai` - OpenAI Python SDK (modified by openrouter_client)
- `gradio` - Web UI framework for demos
- `tqdm` - Progress bars (in all_game_person.py)
- `pydantic_core` - Data validation (imported in all_game_person.py)
- Standard library: `json`, `os`, `random`, `re`, `copy`, `time`

---

## KEY FILES REFERENCE

### Execution
- `agent_trust/all_game_person.py` - Main experiment runner
- `agent_trust/multi_round_person.py` - Repeated game logic
- `agent_trust/no_repeated_demo.py` - Gradio demo (non-repeated)
- `agent_trust/repeated_demo.py` - Gradio demo (repeated)

### Configuration
- `agent_trust/exp_model_class.py` - Model type enums
- `agent_trust/prompt/person_all_game_prompt.json` - Game prompts
- `agent_trust/prompt/character_2.json` - 53 personas
- `agent_trust/prompt/multi_round_chara.json` - Repeated game personas
- `agent_trust/prompt/trust_game_round_prompt.json` - Repeated game round prompts
- `agent_trust/prompt/LLM_player_prompt.json` - Partner type condition
- `agent_trust/prompt/person_feature_prompt.json` - Persona feature templates

### Parsing & Utilities
- `agent_trust/structure_output.py` - Response parsing utilities
- `agent_trust/function_calls.py` - Function calling schemas (for structured outputs)

### Results (pre-existing from paper authors)
- `agent_trust/No repeated res/` - Non-repeated game results from paper
- `agent_trust/repeated res/` - Repeated game results from paper

---

## GAPS & MISSING COMPONENTS (for Step 3+)

### Need to Create:
1. **Wrapper script** to call run_exp() and multi_round_exp() from config files
2. **Config schema** (YAML) defining:
   - Game selection (by key: "1", "2", "5", "6", "7", "9")
   - Model panel (list of ExtendedModelType or OpenRouter IDs)
   - Persona subset or full 53
   - Experimental conditions (partner_type, bias, extra_prompts)
   - Parameters ({p} values for MAP/Risky, {k} for lottery, rounds for repeated)
3. **Model registry** (JSON) mapping paper models to OpenRouter IDs and substitutions
4. **Post-processing scripts** for:
   - VRR calculation
   - Trust/Lottery Rate aggregation
   - Returned/3×Sent Ratio calculation
   - Behavioral dynamics pattern detection
   - Statistical tests (t-tests)
   - Comparison tables (our results vs. paper benchmarks)
5. **Results standardization** to create:
   - episodes.jsonl (one episode per line)
   - aggregates.csv (summary statistics)
   - run_metadata.json (git commit, environment, timestamps)

### Need to Verify:
1. **exp_model_class.py contents** - full enum values and OpenRouter ID mapping
2. **multi_round_chara.json structure** - verify 16 groups for repeated game
3. **Default round count** for repeated game (paper shows ~8-10 rounds in figures)
4. **Probability ranges** for MAP/Risky games (paper shows p from 0.1 to 0.9)

---

**END OF REPO INVENTORY**
