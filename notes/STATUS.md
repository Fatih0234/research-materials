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
  - run_<timestamp>/per_model/<model>/episodes.jsonl (per-model episodes)
  - run_<timestamp>/aggregates.csv (run-level summary after merge/full run)
  - run_<timestamp>/metadata.json (run metadata)
  - run_<timestamp>/analysis/ (model summaries + amount distributions)
  - run_<timestamp>/raw/ (consolidated vendor outputs)

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
- Run root:
  - results/arxiv_2402.04559/xie_trust_game_replication/run_20260120_025050
- Per-model outputs:
  - results/arxiv_2402.04559/xie_trust_game_replication/run_20260120_025050/per_model/<model>
- Total episodes: 424 (53 personas x 8 models)
- Results are not committed (results/ is gitignored).

## Parallel Run Support (New)

Added safe parallel execution to avoid file contention:

- --models: run a subset by model key or OpenRouter ID
- --output-dir: set the shared run directory (per-model output is isolated)

Example per model:

```bash
RUN_ID=20260120_025050
RUN_ROOT="results/arxiv_2402.04559/xie_trust_game_replication/run_${RUN_ID}"
CONFIG=experiments/configs/xie_2402_04559/replication_baseline.yaml

uv run python experiments/run_xie_replication.py \
  --config "$CONFIG" \
  --models openai/gpt-5-nano \
  --output-dir "$RUN_ROOT"
```

## Merge + Analysis Outputs (New)

New merge script: experiments/merge_xie_results.py

Merge example:

```bash
uv run python experiments/merge_xie_results.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --run-dir "$RUN_ROOT"
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
- .gitignore: ignore vendor *_res artifacts
- experiments/configs/xie_2402_04559/replication_baseline.yaml: new run root path

## Run Registry (New)

- notes/run_registry.csv records completed run summaries for quick overview.

## Next Steps

- Decide whether to archive results externally or keep local only.
- Expand configs for additional Trust Game variants if needed for Section 4 analysis.
- Generate plots/tables from analysis outputs for the replication write-up.
