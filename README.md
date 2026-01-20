# LLM Applied Economics: Trust Game Replication

A research project replicating behavioral economics experiments with Large Language Models (LLMs). This project specifically replicates the Trust Game experiments from [Xie et al. (2024)](https://arxiv.org/abs/2402.04559) using multiple LLM providers via OpenRouter.

## Overview

This project investigates whether LLMs exhibit human-like trust behaviors in economic games. We run the Trust Game experiment across 8 different models (Google Gemini, OpenAI GPT, Meta Llama) with 53 diverse personas to analyze:

- How much money LLM agents "send" in Trust Game scenarios
- Whether different models exhibit different trust patterns
- How persona characteristics affect trust decisions

## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- OpenRouter API key ([get one here](https://openrouter.ai/keys))

### Installation

```bash
# Clone the repository (with submodules)
git clone --recurse-submodules https://github.com/your-username/llm-applied-economics.git
cd llm-applied-economics

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENROUTER_API_KEY
```

### Running the Experiment

```bash
# Dry run (validate configuration without API calls)
uv run python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --dry-run

# Full run
uv run python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml
```

### Resuming an Interrupted Run

If the experiment is interrupted (Ctrl+C, crash, etc.), you can resume from where it left off:

```bash
uv run python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --resume results/arxiv_2402.04559/xie_trust_game_replication/run_<timestamp>
```

### Parallel Runs (One Model Per Terminal)

For faster wall-clock time, run one model per terminal and merge the results.

```bash
RUN_ID=20260120_025050
RUN_ROOT="results/arxiv_2402.04559/xie_trust_game_replication/run_${RUN_ID}"

uv run python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --models google/gemini-2.5-flash-lite \
  --output-dir "$RUN_ROOT"

uv run python experiments/run_xie_replication.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --models openai/gpt-5-nano \
  --output-dir "$RUN_ROOT"
```

Repeat for the remaining models, then merge:

```bash
uv run python experiments/merge_xie_results.py \
  --config experiments/configs/xie_2402_04559/replication_baseline.yaml \
  --run-dir "$RUN_ROOT"
```

The merge step creates `analysis/model_summary.csv` and `analysis/amount_sent_distribution.csv`
to support paper-style comparisons (VRR, medians, and Figure 2-style distributions).

## Project Structure

```
llm-applied-economics/
├── experiments/
│   ├── configs/
│   │   └── xie_2402_04559/
│   │       └── replication_baseline.yaml  # Experiment configuration
│   └── run_xie_replication.py             # Main experiment runner
├── specs/
│   └── 05_model_registry.json             # Model ID mappings
├── src/
│   └── openrouter_client.py               # OpenRouter API integration
├── vendor/
│   └── agent-trust/                       # NeurIPS 2024 codebase (git submodule)
├── knowledge_library/                     # Research paper library
│   ├── papers/                            # Downloaded PDFs
│   ├── docling/                           # Parsed PDF content
│   └── index.json                         # Citation index
├── results/                               # Experiment outputs (gitignored)
├── .env.example                           # Environment variable template
└── README.md                              # This file
```

## Models

The experiment uses 8 models across 3 providers:

| Provider | Model | OpenRouter ID |
|----------|-------|---------------|
| Google | Gemini 2.5 Flash Lite | `google/gemini-2.5-flash-lite` |
| Google | Gemini 2.0 Flash | `google/gemini-2.0-flash-001` |
| OpenAI | GPT-OSS-120B | `openai/gpt-oss-120b` |
| OpenAI | GPT-5-Mini | `openai/gpt-5-mini` |
| OpenAI | GPT-OSS-20B | `openai/gpt-oss-20b` |
| OpenAI | GPT-5-Nano | `openai/gpt-5-nano` |
| Meta | Llama 3.3 70B Instruct | `meta-llama/llama-3.3-70b-instruct` |
| Meta | Llama 3 8B Instruct | `meta-llama/llama-3-8b-instruct` |

## Configuration

### Environment Variables

Create a `.env` file with:

```bash
# Required: OpenRouter API Key
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Optional: Base URL (default: https://openrouter.ai/api/v1)
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Optional: Attribution headers
OPENROUTER_APP_NAME=TrustBench Research
OPENROUTER_APP_URL=https://github.com/your-username/llm-applied-economics
```

### Experiment Configuration

The YAML config file (`experiments/configs/xie_2402_04559/replication_baseline.yaml`) defines:

- **Games**: Which behavioral economics games to run (Trust Game = game_id "2")
- **Models**: List of OpenRouter model IDs to test
- **Personas**: 53 diverse character personas from the original paper
- **Decoding**: Temperature and other generation parameters

## Output Format

Each experiment run creates a timestamped directory:

```
results/arxiv_2402.04559/xie_trust_game_replication/run_20260120_143000/
├── episodes.jsonl      # Run-level episodes (after merge or full run)
├── aggregates.csv      # Summary statistics by model
├── metadata.json       # Run configuration and git commit info
├── analysis/           # Paper-aligned analysis outputs
│   ├── model_summary.csv
│   └── amount_sent_distribution.csv
├── raw/                # Consolidated vendor JSON outputs
└── per_model/
    ├── google_gemini-2.5-flash-lite/
    │   ├── episodes.jsonl
    │   └── raw/Trust_Game_google_gemini-2.5-flash-lite.json
    ├── openai_gpt-5-nano/
    │   ├── episodes.jsonl
    │   └── raw/Trust_Game_openai_gpt-5-nano.json
    └── ...
```

### Episode Schema (episodes.jsonl)

Each line contains:

```json
{
  "run_id": "20260120_143000",
  "model_id": "google/gemini-2.5-flash-lite",
  "model_paper_name": "Gemini-2.5-Flash-Lite",
  "game_name": "Trust_Game",
  "persona_id": "xie_001",
  "sent_amount": 5.0,
  "raw_output_text": "BELIEF: ... DESIRE: ... INTENTION: ... Finally, I will give 5 dollars",
  "success": true,
  "timestamp": "2026-01-20T14:30:15"
}
```

## Run Registry

Completed runs are logged in `notes/run_registry.csv` with run path, models,
games, and episode counts to make it easy to audit experiments over time.

## Key Features

### Incremental Save

Results are saved after **each model completes**, not at the end. This means:
- No lost data if the experiment is interrupted
- Progress is tracked in `checkpoint.json`
- Can resume from any point using `--resume`

### OpenRouter Integration

All models are accessed through [OpenRouter](https://openrouter.ai/), providing:
- Unified API for multiple providers (OpenAI, Google, Meta, etc.)
- Single API key for all models
- Cost tracking and rate limiting

### Vendor Code Integration

This project integrates the [agent-trust](https://github.com/camel-ai/agent-trust) codebase from NeurIPS 2024 as a git submodule. The vendor code has been patched to:
- Route API calls through OpenRouter
- Handle model IDs with special characters (/, :)
- Work with modern OpenAI SDK versions

## Knowledge Library

The `knowledge_library/` directory contains a structured collection of research papers for AI agent consumption:

- `papers/` - Downloaded PDFs
- `docling/` - Parsed PDF content with section-level chunks
- `web/` - Crawled web content as markdown
- `index.json` - Master index mapping citations to local files

Use `tools/build_knowledge_library.py` to rebuild the library from source documents.

## Troubleshooting

### "API error" or 404 responses

- Check that the model ID exists on OpenRouter
- Verify your API key is valid and has credits
- Some models may be temporarily unavailable

### FileNotFoundError during save

- This was fixed by sanitizing model IDs in paths
- Model IDs like `google/gemini-2.5-flash-lite` become `google_gemini-2.5-flash-lite` in filenames

### Resuming doesn't skip models

- Ensure you're pointing to the correct results directory
- Check that `checkpoint.json` exists in that directory

## References

- **Original Paper**: [Can Large Language Model Agents Simulate Human Trust Behaviors?](https://arxiv.org/abs/2402.04559) (Xie et al., 2024)
- **Agent-Trust Codebase**: [github.com/camel-ai/agent-trust](https://github.com/camel-ai/agent-trust)
- **OpenRouter**: [openrouter.ai](https://openrouter.ai/)

## License

This project is for research purposes. The vendor/agent-trust submodule is licensed under its original terms.
