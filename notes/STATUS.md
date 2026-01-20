# Project Status (2026-01-20)

## Overview

- Repo: /Volumes/T7/llm-applied-economics
- Branch: iteration-c1-checkpoint
- Focus: Xie et al. (2024) Trust Game replication with OpenRouter models
- Primary runner: experiments/run_xie_replication.py
- Config: experiments/configs/xie_2402_04559/replication_baseline.yaml
- Model registry: specs/05_model_registry.json

## Current Experiment Design

- Game: Trust Game (game_id "2", endowment 10, multiplier 3)
- Personas: 53 (vendor/agent-trust persona file)
- Temperature: 1.0
- Outputs per run:
  - episodes.jsonl (incremental append)
  - aggregates.csv (model-level summary)
  - metadata.json (run metadata)
  - raw/ (vendor JSONs)

## Model Panel (8 Models)

- google/gemini-2.5-flash-lite
- google/gemini-2.0-flash-001
- openai/gpt-oss-120b
- openai/gpt-5-mini
- openai/gpt-oss-20b
- openai/gpt-5-nano
- meta-llama/llama-3.3-70b-instruct
- meta-llama/llama-3-8b-instruct

## Recent Run (Local Only)

- Run ID: 20260120_025050
- Per-model outputs:
  - results/xie_replication__20260120_025050__trust_game__<model>
- Merged output:
  - results/xie_replication__20260120_025050__trust_game
- Total episodes: 424 (53 personas x 8 models)
- Results are not committed (results/ is gitignored).

## Parallel Run Support (New)

Added safe parallel execution to avoid file contention:

- --models: run a subset by model key or OpenRouter ID
- --output-dir: write to a unique directory per terminal

Example per model:

```bash
RUN_ID=20260120_025050
CONFIG=experiments/configs/xie_2402_04559/replication_baseline.yaml

uv run python experiments/run_xie_replication.py \
  --config "$CONFIG" \
  --models openai/gpt-5-nano \
  --output-dir "results/xie_replication__${RUN_ID}__trust_game__gpt-5-nano"
```

## Merge + Analysis Outputs (New)

New merge script: experiments/merge_xie_results.py

Merge example:

```bash
uv run python experiments/merge_xie_results.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --output-dir results/xie_replication__20260120_025050__trust_game \
  --source-dir results/xie_replication__20260120_025050__trust_game__gemini-2.5-flash-lite \
  --source-dir results/xie_replication__20260120_025050__trust_game__gpt-5-nano
```

Merge outputs:

- results/.../episodes.jsonl
- results/.../aggregates.csv
- results/.../metadata.json
- results/.../analysis/model_summary.csv
- results/.../analysis/amount_sent_distribution.csv

## Paper Alignment (Sections 3 and 4)

- Section 3 uses amount sent, VRR, and distributions (Figure 2). These are covered by aggregates.csv and amount_sent_distribution.csv.
- Section 4 compares against human baselines and behavioral factors. Current run supports baseline comparisons for the Trust Game; other factors require additional game variants.

## Files Changed Since Last Checkpoint

- experiments/run_xie_replication.py: added --models and --output-dir
- experiments/merge_xie_results.py: new merge + analysis helper
- README.md: documented parallel run and merge workflow

## Next Steps

- Decide whether to archive results externally or keep local only.
- Expand configs for additional Trust Game variants if needed for Section 4 analysis.
- Generate plots/tables from analysis outputs for the replication write-up.
