# TrustBench Quick Start Guide

**Project**: LLM Applied Economics - Trust Game Experiments
**Current Status**: Iteration C2 Complete ✅
**Last Updated**: 2026-01-19

---

## 🚀 Quick Start (3 Steps)

### 1. Set Up Environment
```bash
# Copy example and add your OpenRouter API key
cp .env.example .env
nano .env  # Add OPENROUTER_API_KEY=sk-or-v1-...
```

### 2. Run Tests
```bash
# Verify OpenRouter integration works
uv run python tools/test_openrouter_agent_trust.py
# Expected: 5/5 tests passed ✅
```

### 3. Launch Demo
```bash
# Run trust game demo with Gradio UI
cd vendor/agent-trust
./run_demo.sh
# Opens at http://127.0.0.1:7860
```

---

## 📁 Project Structure

```
llm-applied-economics/
├── src/
│   └── openrouter_client.py       # OpenRouter integration
├── tools/
│   └── test_openrouter_agent_trust.py  # Smoke tests
├── vendor/
│   └── agent-trust/                # Trust game experiments (submodule)
│       ├── run_demo.sh             # Demo launcher
│       ├── README_OPENROUTER.md    # Setup guide
│       └── agent_trust/            # Python package
├── specs/
│   └── 03_openrouter_env.md        # Environment variable docs
├── plans/
│   └── 04_agent_trust_integration.md  # Integration design
├── data/
│   └── papers/                      # Research papers
├── .env.example                     # Environment template
└── ITERATION_C2_COMPLETE.md        # Completion summary
```

---

## 🔧 Common Tasks

### Run Different Demos
```bash
cd vendor/agent-trust

# Single-round trust game (default)
./run_demo.sh no_repeated

# Multi-round trust game
./run_demo.sh repeated
```

### Check Costs
Visit OpenRouter dashboard: https://openrouter.ai/activity
- Requests are tagged with your `OPENROUTER_APP_NAME` if set

### Run Experiments Programmatically
```python
# From vendor/agent-trust/agent_trust/
from all_game_person import run_exp

# Run experiments with specific models
run_exp(
    model_list=['gpt-3.5-turbo', 'gpt-4'],
    num_games=10,
    characters=['professor', 'trader']
)
```

### Update Agent-Trust
```bash
# Pull latest from upstream
cd vendor/agent-trust
git fetch origin
git checkout <new-commit-hash>
cd ../..
git add vendor/agent-trust
git commit -m "Update agent-trust to <version>"
```

---

## 🔑 Environment Variables

### Required
- `OPENROUTER_API_KEY` - Your OpenRouter API key
  - Get from: https://openrouter.ai/keys

### Optional (Recommended)
- `OPENROUTER_APP_URL` - Your app URL for analytics
- `OPENROUTER_APP_NAME` - Your app name for analytics

### Optional (Advanced)
- `TRUSTBENCH_DEFAULT_MODEL` - Default model (e.g., `gpt-3.5-turbo`)
- `OPENROUTER_BASE_URL` - Override API base URL
- `TRUSTBENCH_FALLBACK_MODELS` - Comma-separated fallback models

See `specs/03_openrouter_env.md` for full documentation.

---

## 🐛 Troubleshooting

### Issue: "API key not found"
```bash
# Verify .env is loaded
cat .env | grep OPENROUTER_API_KEY

# Ensure python-dotenv is installed
uv add python-dotenv
```

### Issue: "No module named 'openai'"
```bash
# Install agent-trust dependencies
cd vendor/agent-trust
uv pip install --python .venv/bin/python3 -r requirements.txt
```

### Issue: Demo not loading
```bash
# Check if demo is running
ps aux | grep demo.py

# Check for port conflicts
lsof -i :7860

# Restart demo
pkill -f demo.py
cd vendor/agent-trust && ./run_demo.sh
```

### Issue: Slow responses
- **Latency**: OpenRouter adds ~100-500ms routing overhead (normal)
- **Check**: Model availability at https://openrouter.ai/models
- **Try**: Faster model (e.g., `gpt-3.5-turbo` instead of `gpt-4`)

---

## 📚 Documentation

- **Integration Design**: `plans/04_agent_trust_integration.md`
- **Environment Vars**: `specs/03_openrouter_env.md`
- **OpenRouter Setup**: `vendor/agent-trust/README_OPENROUTER.md`
- **Completion Summary**: `ITERATION_C2_COMPLETE.md`

---

## 🎯 Current Capabilities

### ✅ Working
- OpenRouter API integration (5/5 tests passed)
- Trust game demos (Gradio UI)
- Model selection (OpenAI models via OpenRouter)
- Environment-based configuration
- Cost tracking via OpenRouter dashboard

### 🚧 Planned (Future Iterations)
- Multi-provider models (Anthropic, Google, Meta)
- Automatic model fallbacks
- Built-in cost tracking
- Paper replication experiments

---

## 📖 Key Papers

1. **Horton (2023)** - "Large Language Models as Simulated Economic Agents"
   - Location: `data/papers/arxiv_2301.07543.pdf`
   - Extracted: `knowledge_library/papers/horton_2023_llm_economic_agents/`

2. **Agent-Trust (2024)** - "Can LLM Agents Simulate Human Trust Behavior?"
   - Paper: https://arxiv.org/abs/2402.04559
   - Code: `vendor/agent-trust/` (submodule)

---

## 🚦 Next Steps (Iteration C3)

1. Extract Horton 2023 experimental parameters
2. Replicate trust game experiments with agent-trust
3. Compare results with published paper
4. Document behavioral alignment metrics

---

## 🆘 Getting Help

1. **Check docs**: See `specs/` and `plans/` directories
2. **Run tests**: `uv run python tools/test_openrouter_agent_trust.py`
3. **Check logs**: Enable debug logging in `src/openrouter_client.py`
4. **OpenRouter status**: https://status.openrouter.ai

---

**Last Updated**: 2026-01-19 | **Branch**: `iteration-c1-checkpoint`
