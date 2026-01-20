# Running Agent-Trust with OpenRouter

This guide explains how to run the agent-trust trust game experiments using OpenRouter instead of OpenAI directly, enabling multi-provider LLM access and cost optimization.

## Quick Start

### 1. Prerequisites

- Python 3.10+
- OpenRouter API key (get from [https://openrouter.ai/keys](https://openrouter.ai/keys))
- Agent-trust dependencies installed (see main README.md)

### 2. Environment Setup

Copy the example environment file and add your API key:

```bash
# From repository root
cp .env.example .env

# Edit .env and set your OpenRouter API key
# OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

Load environment variables:

```bash
# Method 1: Source in shell (bash/zsh)
set -a && source .env && set +a

# Method 2: Use direnv (if installed)
direnv allow

# Method 3: Python will auto-load if python-dotenv is installed
# (already handled by src/openrouter_client.py)
```

### 3. Run Demo

```bash
# Single-round trust game demo
cd vendor/agent-trust
python agent_trust/no_repeated_demo.py

# Multi-round trust game demo
python agent_trust/repeated_demo.py
```

The Gradio web interface will launch in your browser.

### 4. Verify Integration

Run the smoke test to verify OpenRouter is working:

```bash
# From repository root
python tools/test_openrouter_agent_trust.py
```

Expected output:
```
✓ All tests passed! OpenRouter integration is working.
```

## How It Works

### Integration Architecture

The OpenRouter integration uses a **minimal monkey-patching** approach:

1. **Client Factory** (`src/openrouter_client.py`):
   - Provides `initialize_openrouter()` for legacy API
   - Provides `get_openrouter_client()` for modern API
   - Centralizes OpenRouter configuration (base URL, API key, headers)

2. **Agent-Trust Patches** (4 files modified):
   - `agent_trust/no_repeated_demo.py` - Single-round demo
   - `agent_trust/repeated_demo.py` - Multi-round demo
   - `agent_trust/all_game_person.py` - Core experiment runner
   - `agent_trust/structure_output.py` - Structured extraction

Each file has **2 lines added** at the top:
```python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))
from src.openrouter_client import initialize_openrouter
initialize_openrouter()
```

This patches the global `openai` module to route all API calls through OpenRouter.

### What Gets Routed

All OpenAI API calls in agent-trust are automatically routed through OpenRouter:

| Code Pattern | Routed? | Notes |
|--------------|---------|-------|
| `openai.ChatCompletion.create()` | ✓ | Legacy chat API |
| `openai.completions.create()` | ✓ | Legacy completions API |
| `OpenAI()` client instances | ✓ | Modern SDK (via `get_openrouter_client()`) |
| CAMEL `ChatAgent` calls | ✓ | Respects module-level `openai.api_key` |
| Instructor structured output | ✓ | Patched client in `structure_output.py` |

## Model Selection

### Current Behavior (Iteration C2)

Agent-trust currently **hardcodes OpenAI model names** in `exp_model_class.py`:
- `gpt-3.5-turbo-0613`
- `gpt-3.5-turbo-16k-0613`
- `gpt-4`
- `text-davinci-003`

OpenRouter accepts these **without provider prefix**, so no code changes are needed.

### Supported Models

Any OpenAI-compatible model on OpenRouter works:

| Model Name | Provider | Notes |
|------------|----------|-------|
| `gpt-3.5-turbo` | OpenAI | Default, fastest |
| `gpt-3.5-turbo-0613` | OpenAI | Stable snapshot |
| `gpt-4` | OpenAI | Most capable |
| `text-davinci-003` | OpenAI | Legacy completions |

### Using Non-OpenAI Models (Future)

To use Anthropic Claude, Google Gemini, or other providers, you'll need to:

1. Add provider prefix to model names (e.g., `anthropic/claude-3.5-sonnet`)
2. Update `exp_model_class.py` to include new models
3. Use model name mapping in `src/openrouter_client.py` (not yet implemented)

This is planned for **Iteration C3+**.

## Environment Variables

### Required

- `OPENROUTER_API_KEY` - Your OpenRouter API key

### Optional (but Recommended)

- `OPENROUTER_APP_URL` - Your app URL (for OpenRouter analytics)
- `OPENROUTER_APP_NAME` - Your app name (for OpenRouter analytics)

Example:
```bash
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxx
OPENROUTER_APP_URL=https://github.com/username/llm-applied-economics
OPENROUTER_APP_NAME=TrustBench Research
```

### Optional (Advanced)

- `OPENROUTER_BASE_URL` - Override base URL (default: `https://openrouter.ai/api/v1`)
- `TRUSTBENCH_DEFAULT_MODEL` - Default model for experiments (future use)
- `TRUSTBENCH_FALLBACK_MODELS` - Fallback models (future routing feature)

**Full reference**: See `specs/03_openrouter_env.md`

## Running Experiments

### Single Trust Game (No Repetition)

```bash
cd vendor/agent-trust
python agent_trust/no_repeated_demo.py
```

This launches a Gradio interface where you can:
1. Select character profiles
2. Choose LLM model
3. Play trust games interactively
4. View results and BDI (Belief-Desire-Intention) reasoning

### Repeated Trust Game

```bash
cd vendor/agent-trust
python agent_trust/repeated_demo.py
```

This launches a multi-round trust game where:
1. Two LLM agents play repeated trust games
2. Trust evolves over multiple rounds
3. Results show trust dynamics over time

### Batch Experiments (Programmatic)

```python
import os
os.environ['OPENROUTER_API_KEY'] = 'sk-or-v1-...'

from agent_trust.all_game_person import run_exp

# Run experiments with specific models
run_exp(
    model_list=['gpt-3.5-turbo', 'gpt-4'],
    num_games=10,
    characters=['professor', 'trader', 'nurse']
)
```

Results are saved to:
- `agent_trust/No repeated res/` - Single-round results
- `agent_trust/repeated res/` - Multi-round results

## Cost Tracking

### View API Usage

Check your OpenRouter dashboard:
[https://openrouter.ai/activity](https://openrouter.ai/activity)

If you set `OPENROUTER_APP_URL` and `OPENROUTER_APP_NAME`, your requests will be tagged for easy filtering.

### Estimate Costs

Trust game experiments vary by:
- **Model**: GPT-3.5 (~$0.001/1K tokens) vs GPT-4 (~$0.03/1K tokens)
- **Game type**: Single-round (~500 tokens) vs multi-round (~2000 tokens)
- **Character complexity**: Longer character descriptions = more tokens

**Rough estimates** (as of 2026-01):
- Single trust game (GPT-3.5): $0.001 - $0.003
- Single trust game (GPT-4): $0.015 - $0.045
- 100 experiments (GPT-3.5): ~$0.10 - $0.30
- 100 experiments (GPT-4): ~$1.50 - $4.50

**Note**: OpenRouter pricing may change. Check [https://openrouter.ai/models](https://openrouter.ai/models) for current rates.

## Troubleshooting

### Issue: "API key not found"

**Symptom**: `ValueError: OpenRouter API key not found`

**Solution**:
```bash
# Check environment variable
echo $OPENROUTER_API_KEY

# If empty, load .env
set -a && source ../../.env && set +a

# Or set directly
export OPENROUTER_API_KEY="sk-or-v1-..."
```

### Issue: "Invalid API key"

**Symptom**: `401 Unauthorized` or `403 Forbidden`

**Solution**:
1. Verify key at [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. Check key hasn't expired
3. Ensure key starts with `sk-or-v1-`

### Issue: "Model not found"

**Symptom**: `404 Not Found` for model

**Solution**:
- Use legacy OpenAI names without provider prefix: `gpt-3.5-turbo`, NOT `openai/gpt-3.5-turbo`
- Check model availability at [https://openrouter.ai/models](https://openrouter.ai/models)
- Some models may be temporarily unavailable

### Issue: "Rate limit exceeded"

**Symptom**: `429 Too Many Requests`

**Solution**:
1. Check rate limits in OpenRouter dashboard
2. Add delays between requests (already implemented in agent-trust)
3. Upgrade OpenRouter plan for higher limits

### Issue: Gradio demo doesn't load

**Symptom**: Import errors or module not found

**Solution**:
```bash
# Install agent-trust dependencies
cd vendor/agent-trust
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yaml
conda activate agent-trust
```

### Issue: Attribution not showing in OpenRouter dashboard

**Symptom**: Requests appear but no app name/URL

**Solution**:
1. Verify `OPENROUTER_APP_URL` and `OPENROUTER_APP_NAME` are set
2. Check they're non-empty strings
3. Reload environment variables:
   ```bash
   set -a && source ../../.env && set +a
   ```

### Issue: Slow responses

**Symptom**: API calls take >10 seconds

**Solution**:
- OpenRouter adds ~100-500ms routing overhead (normal)
- Check model availability (some models are slower)
- Verify network connection
- Try different model (GPT-3.5 is faster than GPT-4)

## Logging and Debugging

### Enable Debug Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

from src.openrouter_client import initialize_openrouter
initialize_openrouter()
```

This will log:
- API key detection (masked)
- Base URL configuration
- Attribution headers
- Request/response metadata (tokens, latency)

### Check Configuration

```python
from src.openrouter_client import is_openrouter_initialized

if is_openrouter_initialized():
    print("✓ OpenRouter is configured")
else:
    print("✗ OpenRouter not initialized")
```

### Self-Test

Run the client factory self-test:

```bash
python -m src.openrouter_client
```

This checks:
1. Environment variables loaded
2. Legacy API initialization
3. Modern client creation

## Limitations (Iteration C2)

### Current Limitations

1. **OpenAI models only**: Can't use Anthropic, Google, or other providers yet
   - Workaround: Use model name mapping (Iteration C3+)

2. **No model fallbacks**: If a model is unavailable, requests fail
   - Workaround: Use OpenRouter's routing parameter (Iteration C3+)

3. **No cost tracking**: Must manually check OpenRouter dashboard
   - Workaround: Log generation IDs and query cost API (Iteration C5)

4. **Synchronous only**: No async/concurrent experiments
   - Workaround: Run multiple processes manually

### Known Issues

- **CAMEL framework**: May not respect OpenRouter headers (under investigation)
- **Instructor library**: Tested and working, but edge cases may exist
- **Error handling**: Old SDK error classes may not match (compatibility shims added)

## Additional Resources

- **OpenRouter Documentation**: [https://openrouter.ai/docs](https://openrouter.ai/docs)
- **Agent-Trust Paper**: [https://arxiv.org/abs/2402.04559](https://arxiv.org/abs/2402.04559)
- **Agent-Trust GitHub**: [https://github.com/camel-ai/agent-trust](https://github.com/camel-ai/agent-trust)
- **Environment Variables**: `../../specs/03_openrouter_env.md`
- **Integration Design**: `../../plans/04_agent_trust_integration.md`

## Getting Help

1. **Run smoke test**: `python tools/test_openrouter_agent_trust.py`
2. **Check logs**: Enable debug logging (see above)
3. **Review docs**: `specs/03_openrouter_env.md`
4. **Check OpenRouter status**: [https://status.openrouter.ai](https://status.openrouter.ai)

## Next Steps

After verifying the integration works:

1. **Run baseline experiments**: Replicate trust game results from Horton 2023 paper
2. **Compare costs**: OpenRouter vs direct OpenAI API
3. **Experiment with models**: Try different OpenAI models
4. **Scale up**: Run batch experiments (see Batch Experiments section)
5. **Analyze results**: Compare behavioral alignment across models

**Next Iteration (C3)**: Extract Horton 2023 methodology and replicate experiments.
