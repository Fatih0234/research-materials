# Project Status

**Last Updated:** 2026-01-19
**Current Branch:** iteration-c1-checkpoint
**Phase:** TrustBench Paper Replication - Step 2 COMPLETE

---

## Current State

### Step 1: Paper Claims Inventory ✓ COMPLETE
- **Objective:** Extract exactly what Xie et al. (2024) arxiv_2402.04559 claims
- **Completed:** 2026-01-19
- **Output:** `notes/papers/arxiv_2402.04559.md`
- **Commit:** 5947aa6

**Extracted:**
- 6 game variants (Trust, Dictator, MAP Trust, Risky Dictator, Lottery People, Lottery Gamble)
- Repeated Trust Game protocol
- 53 personas design
- 9 model panel (GPT-4, GPT-3.5 variants, text-davinci-003, Llama2 3 sizes, Vicuna-v1.3 3 sizes)
- Temperature = 1.0
- Metrics: VRR, Amount Sent, Trust Rate, Lottery Rate, Returned/3×Sent Ratio, Behavioral Dynamics Patterns
- Key claims: Reciprocity anticipation, Risk perception, Prosocial preference, Behavioral dynamics
- Statistical tests: One-Tailed Independent Samples t-test
- Prompts locations documented

### Step 2: Repo Implementation Inventory ✓ COMPLETE
- **Objective:** Map vendor/agent-trust implementation to paper claims
- **Completed:** 2026-01-19
- **Outputs:**
  - `plans/05_paper_repo_alignment.md` (full alignment matrix)
  - `notes/step2_repo_inventory.md` (repo structure map)
- **Commit:** Pending (Step2: map repo implementation to paper claims)

**Key Findings:**
- ✓ All 6 game variants implemented with exact prompts/payoffs
- ✓ 53 personas match exactly (character_2.json)
- ✓ Temperature = 1.0 consistently set
- ✓ BDI framework integrated in all prompts
- ✓ CAMEL framework + OpenRouter routing confirmed
- ⚠️ Model versions (GPT-3.5-0613 suffix not explicit in enums)
- ⚠️ Llama2/Vicuna 13b/70b/33b not in default config (only 7b)
- ❌ Metrics calculation (VRR, Trust Rate, etc.) not implemented
- ❌ Statistical testing not implemented
- ❌ Analysis scripts missing

### Step 3: Model Registry + Replication Configs + Wrapper Runner ✓ COMPLETE
- **Objective:** Create minimal wrapper for running Xie replication without modifying vendor code
- **Completed:** 2026-01-19
- **Outputs:**
  - `specs/05_model_registry.json` - Paper models → OpenRouter IDs mapping
  - `experiments/configs/xie_2402_04559/replication_baseline.yaml` - Trust Game config
  - `experiments/run_xie_replication.py` - Wrapper runner (import-based integration)
- **Commit:** Pending (Step3: model registry + replication configs + wrapper runner)

**Created:**
1. **Model Registry** (`specs/05_model_registry.json`)
   - 11 model entries (9 paper models)
   - 4 exact matches: GPT-4, GPT-3.5-turbo-0613, GPT-3.5-turbo-16k, GPT-3.5-turbo-instruct
   - 5 substitutions:
     - text-davinci-003 → gpt-3.5-turbo-instruct
     - Llama2-{7,13,70}B → Llama-3/3.3-{8,8,70}B
     - Vicuna-v1.3-{7,13,33}B → DeepSeek-R1-Distill-Qwen-{7,14,32}B

2. **Replication Config** (`experiments/configs/xie_2402_04559/replication_baseline.yaml`)
   - Paper ID: arxiv_2402.04559
   - Game: Trust Game (game_id="2")
   - Personas: All 53 from character_2.json
   - Model panel: All 11 models from registry
   - Temperature: 1.0 (matches paper)
   - Output: episodes.jsonl + aggregates.csv + metadata.json

3. **Wrapper Runner** (`experiments/run_xie_replication.py`)
   - Integration: Import vendor/agent-trust as library (not subprocess)
   - Config loader + model resolver
   - Vendor experiment caller (run_exp wrapper)
   - Output transformer (vendor JSON → episodes.jsonl)
   - Aggregate calculator (VRR, mean/median/sd statistics)
   - Metadata tracker (git commit, timestamps, environment)

**How to Run:**
```bash
# Dry run (validate config without API calls)
python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --dry-run

# Full run (11 models × 53 personas = 583 API calls)
python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml
```

**Results Location:**
`results/xie_replication__<timestamp>__trust_game/`
- `episodes.jsonl` - Full episode records (1 per persona × model)
- `aggregates.csv` - Summary statistics by model
- `metadata.json` - Run metadata (git commit, timestamps, config snapshot)
- `raw/` - Original vendor/agent-trust JSON outputs

**Known Limitations:**
- Output transformation not fully implemented (vendor JSON location needs mapping)
- No retry logic for failed personas
- Single game only (Trust Game), other 5 games need configs
- No statistical testing (t-tests vs human baseline)
- No partner-type manipulation (Section 5 variations)

**Next Steps:**
- Step 4: Pilot run (single model, 53 personas, validate pipeline)
- Step 5: Full panel run (all 11 models, all games)
- Step 6: Comparison report (vs paper Table 1, statistical tests)
- Step 7: Evidence bundle (archive results + configs)

---

## Repository Structure

### Key Paths
- **Paper knowledge:** `knowledge_library/docling/arxiv_2402.04559/`
- **Paper notes:** `notes/papers/arxiv_2402.04559.md`
- **Vendor submodule:** `vendor/agent-trust/`
- **Future configs:** `experiments/configs/xie_2402_04559/` (not yet created)
- **Future results:** `results/xie_replication__<timestamp>__<panel>/` (not yet created)

---

## Recent Commits
- (Pending) Step2: map repo implementation to paper claims (alignment matrix)
- 5947aa6 Step1: extract paper claims (Xie 2402.04559)

---

## Notes
- Working in PLAN MODE: exploration + alignment + spec only
- No code execution yet (only safe edits to plan/notes)
- Following 7-step replication workflow from user instructions
