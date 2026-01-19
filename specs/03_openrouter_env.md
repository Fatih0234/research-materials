# OpenRouter Environment Configuration Specification

**Version**: 1.0
**Status**: Draft
**Last Updated**: 2026-01-19
**Scope**: Iteration C2 - Agent-Trust Integration

## Overview

This document specifies all environment variables required for routing agent-trust experiments through OpenRouter. The configuration supports both OpenAI-compatible legacy patterns and modern SDK usage.

## Environment Variables

### Required Variables

#### `OPENROUTER_API_KEY`
- **Description**: API key for OpenRouter service
- **Format**: `sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (64 hex chars after prefix)
- **Required**: Yes
- **Fallback**: `OPENAI_API_KEY` (for backward compatibility)
- **Example**: `sk-or-v1-a1b2c3d4e5f6...`
- **Security**: Never commit to version control; store in `.env` file (gitignored)
- **Obtain from**: https://openrouter.ai/keys

**Usage**:
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
```

### Optional Variables

#### `OPENROUTER_BASE_URL`
- **Description**: Base URL for OpenRouter API endpoint
- **Format**: HTTPS URL ending without trailing slash
- **Required**: No
- **Default**: `https://openrouter.ai/api/v1`
- **Example**: `https://openrouter.ai/api/v1`
- **When to override**: Testing against staging/dev OpenRouter instances, or using self-hosted proxy

**Usage**:
```bash
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
```

#### `OPENROUTER_APP_URL`
- **Description**: Your application's URL for OpenRouter attribution (appears in OpenRouter dashboard analytics)
- **Format**: Valid HTTP/HTTPS URL
- **Required**: No (but recommended for analytics)
- **Default**: Empty string (no attribution)
- **Example**: `https://github.com/username/llm-applied-economics`
- **Maps to**: HTTP header `HTTP-Referer`

**Usage**:
```bash
export OPENROUTER_APP_URL="https://github.com/username/llm-applied-economics"
```

#### `OPENROUTER_APP_NAME`
- **Description**: Human-readable name of your application (appears in OpenRouter dashboard)
- **Format**: Plain text string
- **Required**: No (but recommended for analytics)
- **Default**: Empty string (no attribution)
- **Example**: `TrustBench Research`
- **Maps to**: HTTP header `X-Title`

**Usage**:
```bash
export OPENROUTER_APP_NAME="TrustBench Research"
```

#### `TRUSTBENCH_DEFAULT_MODEL`
- **Description**: Default model to use for experiments when not explicitly specified
- **Format**: OpenRouter model identifier (see Model Naming Conventions below)
- **Required**: No
- **Default**: `gpt-3.5-turbo` (OpenAI's GPT-3.5 Turbo via OpenRouter)
- **Example**: `openai/gpt-4o`, `anthropic/claude-3.5-sonnet`, `gpt-3.5-turbo`

**Usage**:
```bash
export TRUSTBENCH_DEFAULT_MODEL="openai/gpt-4o"
```

**Note**: Agent-trust code currently hardcodes models in `exp_model_class.py`. This variable is for future use or wrapper scripts.

#### `TRUSTBENCH_FALLBACK_MODELS`
- **Description**: Comma-separated list of fallback models if default fails (for future OpenRouter routing feature)
- **Format**: Comma-separated OpenRouter model identifiers
- **Required**: No
- **Default**: Empty (no fallbacks)
- **Example**: `openai/gpt-3.5-turbo,anthropic/claude-3.5-sonnet,google/gemini-pro`

**Usage**:
```bash
export TRUSTBENCH_FALLBACK_MODELS="openai/gpt-3.5-turbo,anthropic/claude-3.5-sonnet"
```

**Note**: Requires implementation in `src/openrouter_client.py` to use OpenRouter's `extra_body.models` routing parameter. Out of scope for Iteration C2.

## Model Naming Conventions

OpenRouter supports two naming formats:

### Format 1: Legacy OpenAI Names (Recommended for C2)
**Pattern**: `{model-name}` (e.g., `gpt-3.5-turbo`, `gpt-4`, `text-davinci-003`)

**Examples**:
- `gpt-3.5-turbo`
- `gpt-3.5-turbo-0613`
- `gpt-3.5-turbo-16k-0613`
- `gpt-4`
- `text-davinci-003`

**Pros**:
- No code changes required in agent-trust
- Direct compatibility with existing `ExtendedModelType` enum

**Cons**:
- Only routes to OpenAI models
- Cannot use Anthropic, Google, or other providers

### Format 2: Provider-Prefixed Names (Future Enhancement)
**Pattern**: `{provider}/{model-name}` (e.g., `openai/gpt-4`, `anthropic/claude-3.5-sonnet`)

**Examples**:
- `openai/gpt-4o`
- `anthropic/claude-3-5-sonnet-20241022`
- `google/gemini-pro-1.5`
- `meta-llama/llama-3.1-70b-instruct`

**Pros**:
- Multi-provider routing
- Access to non-OpenAI models
- Explicit provider selection

**Cons**:
- Requires model name mapping layer (not implemented in C2)
- Breaks compatibility with agent-trust's hardcoded OpenAI model names

## Configuration File: .env

**Location**: `/Volumes/T7/llm-applied-economics/.env`

**Template** (also in `.env.example`):
```bash
# =============================================================================
# OpenRouter Configuration (Iteration C2)
# =============================================================================

# Required: OpenRouter API Key
# Obtain from: https://openrouter.ai/keys
OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE

# Optional: OpenRouter API Base URL
# Default: https://openrouter.ai/api/v1
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Optional: Attribution (recommended for analytics)
# Your app's URL (shows in OpenRouter dashboard)
OPENROUTER_APP_URL=https://github.com/username/llm-applied-economics

# Your app's name (shows in OpenRouter dashboard)
OPENROUTER_APP_NAME=TrustBench Research

# Optional: Model Selection (for future use)
# Default model for experiments (OpenRouter format)
TRUSTBENCH_DEFAULT_MODEL=gpt-3.5-turbo

# Fallback models (comma-separated, for future routing feature)
TRUSTBENCH_FALLBACK_MODELS=

# =============================================================================
# Backward Compatibility (Optional)
# =============================================================================

# Legacy OpenAI API key (fallback if OPENROUTER_API_KEY not set)
# OPENAI_API_KEY=sk-...
```

## Loading Environment Variables

### Method 1: Direct Export (Development)
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
export OPENROUTER_APP_NAME="TrustBench Research"
python vendor/agent-trust/agent_trust/no_repeated_demo.py
```

### Method 2: .env File with python-dotenv (Recommended)
```python
# At top of script or in src/openrouter_client.py
from dotenv import load_dotenv
load_dotenv()  # Loads .env from current directory or parent directories

import os
api_key = os.getenv("OPENROUTER_API_KEY")
```

### Method 3: .env File with Shell (Quick Testing)
```bash
# Load all vars from .env
set -a
source .env
set +a

# Run script
python vendor/agent-trust/agent_trust/no_repeated_demo.py
```

## Security Best Practices

### DO:
- ✅ Store API keys in `.env` file (gitignored)
- ✅ Use environment variables for secrets
- ✅ Rotate API keys regularly
- ✅ Use separate keys for dev/staging/prod
- ✅ Review `.gitignore` to ensure `.env` is excluded

### DON'T:
- ❌ Commit `.env` file to version control
- ❌ Hardcode API keys in source code
- ❌ Share API keys via chat, email, or screenshots
- ❌ Use production keys in public demos (Gradio apps)
- ❌ Log API keys (even in debug mode)

## Validation

### Check Configuration
```python
import os
from dotenv import load_dotenv

load_dotenv()

required = ["OPENROUTER_API_KEY"]
optional = ["OPENROUTER_BASE_URL", "OPENROUTER_APP_URL", "OPENROUTER_APP_NAME"]

print("Required Variables:")
for var in required:
    value = os.getenv(var)
    status = "✓ SET" if value else "✗ MISSING"
    print(f"  {var}: {status}")

print("\nOptional Variables:")
for var in optional:
    value = os.getenv(var)
    status = f"✓ {value}" if value else "✗ Not set (using default)"
    print(f"  {var}: {status}")
```

### Test Connection
```bash
# Smoke test (requires tools/test_openrouter_agent_trust.py)
python tools/test_openrouter_agent_trust.py
```

## Troubleshooting

### Issue: "API key not found"
**Solution**: Check that `OPENROUTER_API_KEY` is set and `.env` file is loaded

```bash
# Verify environment variable
echo $OPENROUTER_API_KEY

# If empty, load .env
set -a && source .env && set +a
```

### Issue: "Invalid API key"
**Solution**: Verify key format and expiration at https://openrouter.ai/keys

### Issue: "Model not found"
**Solution**: Check model name format (use legacy OpenAI names for C2)

```bash
# Valid (C2):
gpt-3.5-turbo
gpt-4

# Invalid (C2 - requires mapping layer):
openai/gpt-3.5-turbo
anthropic/claude-3.5-sonnet
```

### Issue: "Rate limit exceeded"
**Solution**: Check OpenRouter dashboard for rate limits and credits

### Issue: Attribution headers not appearing in OpenRouter dashboard
**Solution**: Verify `OPENROUTER_APP_URL` and `OPENROUTER_APP_NAME` are set and non-empty

```python
# Debug headers in src/openrouter_client.py
import os
print("HTTP-Referer:", os.getenv("OPENROUTER_APP_URL"))
print("X-Title:", os.getenv("OPENROUTER_APP_NAME"))
```

## Reference Links

- **OpenRouter Documentation**: https://openrouter.ai/docs
- **OpenRouter API Keys**: https://openrouter.ai/keys
- **OpenRouter Models**: https://openrouter.ai/models
- **OpenRouter Pricing**: https://openrouter.ai/models (per-model pricing)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-19 | Initial specification for Iteration C2 |
