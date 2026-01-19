# Agent-Trust Integration Plan (Iteration C2)

**Date**: 2026-01-19
**Branch**: `iteration-c1-checkpoint`
**Upstream**: https://github.com/camel-ai/agent-trust
**Pinned Commit**: `9ce6bee29daf1f58c091077d89560ccd6d076f8b` (2025-04-05)

## Objective

Integrate the upstream `agent-trust` repository into our workspace and route all OpenAI API calls through OpenRouter, enabling multi-provider LLM experiments for trust game research while maintaining reproducibility with the original NeurIPS 2024 paper.

## Integration Method: Git Submodule

**Decision**: Use `git submodule` to vendor the agent-trust repository.

**Rationale**:
- Version pinning to specific commit for reproducibility
- Easy upstream synchronization for bug fixes
- Clean separation between our code and vendored code
- Standard practice for research code dependencies

**Commands**:
```bash
mkdir -p vendor
git submodule add https://github.com/camel-ai/agent-trust.git vendor/agent-trust
cd vendor/agent-trust
git checkout 9ce6bee29daf1f58c091077d89560ccd6d076f8b
cd ../..
git add .gitmodules vendor/agent-trust
```

**Upstream Tracking**:
```bash
# Future: Update to newer upstream version
cd vendor/agent-trust
git fetch origin
git checkout <new-commit-hash>
cd ../..
git add vendor/agent-trust
git commit -m "Update agent-trust to <new-version>"
```

## Repository Structure Overview

### Agent-Trust Key Components

```
vendor/agent-trust/
├── agent_trust/                    # Main package
│   ├── all_game_person.py         # Core experiment runner (415 lines)
│   ├── no_repeated_demo.py        # Single-round Gradio demo (238 lines)
│   ├── repeated_demo.py           # Multi-round Gradio demo (369 lines)
│   ├── exp_model_class.py         # Model enum (OpenAI + open-source)
│   ├── structure_output.py        # Structured extraction with instructor
│   ├── multi_round_person.py      # Multi-round game logic
│   ├── function_calls.py          # Utility functions
│   ├── prompt/                    # JSON prompt templates
│   │   ├── person_all_game_prompt.json
│   │   ├── character_2.json
│   │   ├── LLM_player_prompt.json
│   │   └── ...
│   ├── No repeated res/           # Non-repeated game results
│   └── repeated res/              # Repeated game results
├── requirements.txt               # Dependencies (openai==1.12.0)
├── pyproject.toml                 # Poetry config
└── README.md                      # Upstream docs
```

### Our Integration Layer

```
src/
└── openrouter_client.py           # NEW: OpenRouter client factory

tools/
└── test_openrouter_agent_trust.py # NEW: Smoke test

specs/
└── 03_openrouter_env.md           # NEW: Environment variable spec

plans/
└── 04_agent_trust_integration.md  # THIS FILE

vendor/agent-trust/
└── README_OPENROUTER.md           # NEW: OpenRouter usage guide
```

## OpenAI API Usage Analysis

### SDK Version: Hybrid v0.x + v1.x

The agent-trust codebase uses `openai==1.12.0` but with **mixed patterns**:

#### Pattern 1: Legacy v0.x Module-Level API (Dominant)
**Files**:
- `agent_trust/all_game_person.py:93`
- `agent_trust/no_repeated_demo.py:31`
- `agent_trust/structure_output.py:48-50`

**Code**:
```python
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.completions.create(...)  # or openai.ChatCompletion.create(...)
```

#### Pattern 2: Modern v1.x Client Instance (Rare)
**Files**:
- `agent_trust/structure_output.py:13`

**Code**:
```python
from openai import OpenAI
client = instructor.patch(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))
```

### Critical Call Sites

| File | Line | Call | Model | Notes |
|------|------|------|-------|-------|
| `all_game_person.py` | 93 | `openai.completions.create()` | text-davinci-003 | Legacy completions endpoint |
| `no_repeated_demo.py` | 31 | `openai.completions.create()` | text-davinci-003 | Same as above |
| `repeated_demo.py` | - | Via CAMEL ChatAgent | Various | Indirect via camel-ai framework |
| `structure_output.py` | 13 | `OpenAI(api_key=...)` | gpt-3.5-turbo | Modern SDK + instructor patch |
| `structure_output.py` | 50 | `openai.ChatCompletion.create()` | gpt-3.5-turbo | Legacy style despite modern client! |

### Dependencies
- `openai==1.12.0` - Modern SDK
- `camel-ai==0.1.1` - Agent framework (makes own OpenAI calls)
- `instructor==0.5.2` - Structured output extraction
- `gradio==4.18.0` - Web UI demos

## Integration Architecture: Minimal Monkey-Patching

### Strategy Rationale
1. **Preserve research code integrity**: NeurIPS 2024 paper results must be reproducible
2. **Minimize invasiveness**: OpenRouter is OpenAI-compatible at API level
3. **Support both patterns**: Handle legacy module-level and modern client-based calls
4. **Centralize config**: Single source of truth for OpenRouter settings

### Component: OpenRouter Client Factory

**File**: `src/openrouter_client.py`

**Purpose**: Centralize OpenRouter configuration and provide both legacy and modern API support.

**Key Functions**:

```python
def initialize_openrouter(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    app_name: Optional[str] = None,
) -> None:
    """
    Initialize OpenRouter for legacy openai.* module-level API calls.

    Patches global openai configuration:
    - openai.api_key
    - openai.api_base (or openai.base_url depending on SDK version)
    - openai.default_headers (for attribution)

    Args:
        api_key: OpenRouter API key (default: OPENROUTER_API_KEY or OPENAI_API_KEY env var)
        base_url: OpenRouter base URL (default: OPENROUTER_BASE_URL or https://openrouter.ai/api/v1)
        app_url: Application URL for attribution (default: OPENROUTER_APP_URL env var)
        app_name: Application name for attribution (default: OPENROUTER_APP_NAME env var)
    """
    pass


def get_openrouter_client(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    app_name: Optional[str] = None,
) -> OpenAI:
    """
    Create and return a modern OpenAI client configured for OpenRouter.

    Use for new code or patching instructor.patch(OpenAI(...)).

    Args:
        Same as initialize_openrouter()

    Returns:
        OpenAI client instance configured for OpenRouter
    """
    pass


def map_model_name(model: str) -> str:
    """
    [FUTURE] Map OpenAI model names to OpenRouter provider-prefixed format.

    Not implemented in Iteration C2 (preserves OpenAI names for compatibility).

    Args:
        model: OpenAI model name (e.g., "gpt-3.5-turbo")

    Returns:
        OpenRouter model name (e.g., "openai/gpt-3.5-turbo")
    """
    pass
```

**Features**:
- Reads env vars: `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL`, `OPENROUTER_APP_URL`, `OPENROUTER_APP_NAME`
- Falls back to `OPENAI_API_KEY` for compatibility
- Adds HTTP-Referer and X-Title headers (OpenRouter attribution)
- Handles SDK version differences (v0.x `api_base` vs v1.x `base_url`)

## Patch Strategy: Direct Edits

**Decision**: Add 2-line imports directly to agent-trust demo files.

**Rationale**:
- Simplest approach for stable research code
- Agent-trust is not actively developed (paper already published)
- Upstream updates unlikely to cause conflicts
- Clear and explicit (no hidden wrapper magic)

### Files to Modify

#### 1. `vendor/agent-trust/agent_trust/no_repeated_demo.py`
**Location**: Top of file (after existing imports)
**Changes**:
```python
# Existing imports...
import openai
# ... more imports ...

# ADD THESE 2 LINES:
import sys; sys.path.insert(0, '../../..') # Add repo root to path
from src.openrouter_client import initialize_openrouter; initialize_openrouter()

# Rest of file unchanged...
```

#### 2. `vendor/agent-trust/agent_trust/repeated_demo.py`
**Location**: Same as above
**Changes**: Same 2-line patch

#### 3. `vendor/agent-trust/agent_trust/all_game_person.py`
**Location**: Same as above
**Changes**: Same 2-line patch

#### 4. `vendor/agent-trust/agent_trust/structure_output.py`
**Location**: Line 13 (client instantiation)
**Changes**:
```python
# BEFORE:
client = instructor.patch(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))

# AFTER:
import sys; sys.path.insert(0, '../../..')
from src.openrouter_client import get_openrouter_client
client = instructor.patch(get_openrouter_client())
```

**Total Changes**: 4 files, ~8 lines added

## Implementation Steps

### Phase 1: Setup Submodule
```bash
cd /Volumes/T7/llm-applied-economics
git checkout iteration-c1-checkpoint

# Add submodule
mkdir -p vendor
git submodule add https://github.com/camel-ai/agent-trust.git vendor/agent-trust

# Pin to commit
cd vendor/agent-trust
git checkout 9ce6bee29daf1f58c091077d89560ccd6d076f8b
cd ../..

# Stage changes
git add .gitmodules vendor/agent-trust
```

### Phase 2: Create Client Factory
```bash
# Create src/openrouter_client.py (see implementation below)
# ~150 lines: initialization, client factory, logging
```

### Phase 3: Patch Agent-Trust
```bash
# Edit 4 files in vendor/agent-trust/agent_trust/
# Add 2-line imports to: no_repeated_demo.py, repeated_demo.py, all_game_person.py
# Modify 1 line in: structure_output.py
```

### Phase 4: Create Documentation
```bash
# Write vendor/agent-trust/README_OPENROUTER.md
# Document setup, usage, model selection, troubleshooting
```

### Phase 5: Environment Config
```bash
# Update .env.example with OpenRouter variables
# Verify .gitignore includes .env
```

### Phase 6: Smoke Test
```bash
# Create tools/test_openrouter_agent_trust.py
# Run: python tools/test_openrouter_agent_trust.py
# Verify both legacy and modern API patterns work
```

### Phase 7: Commit
```bash
git add src/ tools/ specs/ plans/ vendor/agent-trust/ .env.example
git commit -m "Iteration C2: vendor agent-trust + OpenRouter integration"
git push origin iteration-c1-checkpoint
```

## Smoke Test Specification

**File**: `tools/test_openrouter_agent_trust.py`

**Test Cases**:

1. **Test Legacy API Pattern**
   - Initialize with `initialize_openrouter()`
   - Call `openai.ChatCompletion.create()`
   - Verify response structure
   - Log model, tokens, latency

2. **Test Modern API Pattern**
   - Get client with `get_openrouter_client()`
   - Call `client.chat.completions.create()`
   - Verify response structure
   - Log model, tokens, latency

3. **Test Environment Variable Loading**
   - Verify `OPENROUTER_API_KEY` is read
   - Verify fallback to `OPENAI_API_KEY` works
   - Verify defaults for base_url

4. **Test Attribution Headers**
   - Make request with `OPENROUTER_APP_URL` and `OPENROUTER_APP_NAME` set
   - Verify headers are included (check OpenRouter dashboard)

**Exit Criteria**:
- All 4 tests pass
- No API errors
- Response latency < 5 seconds
- Model name logged correctly

**Run Command**:
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
python tools/test_openrouter_agent_trust.py
```

## Risk Assessment

### Risk 1: CAMEL Framework Bypasses Patches
**Likelihood**: Medium
**Impact**: High (core experiments would fail)
**Mitigation**: CAMEL's `ChatAgent` respects `openai.api_key` and `openai.api_base` module-level settings
**Verification**: Run `repeated_demo.py` (uses CAMEL) and check OpenRouter dashboard for requests

### Risk 2: Instructor Library Incompatibility
**Likelihood**: Low
**Impact**: Medium (structured extraction fails)
**Mitigation**: Instructor is OpenAI-compatible; test in smoke test
**Verification**: Test `structure_output.py` functionality with OpenRouter

### Risk 3: Model Name Conflicts
**Likelihood**: Low
**Impact**: Low (fallback to mapping layer)
**Mitigation**: OpenRouter accepts legacy OpenAI names without prefix
**Verification**: Test with `gpt-3.5-turbo-0613` (agent-trust's hardcoded model)

### Risk 4: Error Handling Changes
**Likelihood**: Medium
**Impact**: Low (graceful degradation)
**Mitigation**: OpenRouter uses same error classes as OpenAI SDK v1.x
**Verification**: Test with invalid API key to verify error handling

### Risk 5: API Key Leakage
**Likelihood**: Medium
**Impact**: Critical (security breach)
**Mitigation**:
- Never commit `.env`
- Add `.env` to `.gitignore`
- Document secure practices
- Review all commits before push
**Verification**: `git log -p` to check no secrets committed

## Model Naming Strategy (Phase 1)

**Decision**: Preserve OpenAI names without provider prefix.

**Rationale**:
- Zero code changes in agent-trust
- OpenRouter accepts `gpt-3.5-turbo-0613` without `openai/` prefix
- Maintains compatibility with `ExtendedModelType` enum

**Supported Models** (Iteration C2):
- `gpt-3.5-turbo` ✓
- `gpt-3.5-turbo-0613` ✓
- `gpt-3.5-turbo-16k-0613` ✓
- `gpt-4` ✓
- `text-davinci-003` ✓

**Unsupported** (requires mapping layer):
- `anthropic/claude-3.5-sonnet` ✗
- `google/gemini-pro` ✗
- `meta-llama/llama-3.1-70b` ✗

**Future Enhancement** (Iteration C3+):
- Implement `map_model_name()` in `src/openrouter_client.py`
- Add model mapping config file (YAML or JSON)
- Support cross-provider experiments

## Verification Checklist

### Before Commit:
- [ ] Submodule added and pinned to `9ce6bee`
- [ ] `src/openrouter_client.py` implements both API patterns
- [ ] All 4 agent-trust files patched correctly
- [ ] `specs/03_openrouter_env.md` complete
- [ ] `vendor/agent-trust/README_OPENROUTER.md` written
- [ ] `.env.example` includes OpenRouter vars
- [ ] `.gitignore` includes `.env`
- [ ] Smoke test passes with real API key
- [ ] `no_repeated_demo.py` runs successfully
- [ ] No secrets in git history (`git log -p | grep -i "sk-or-v1"`)

### After Commit:
- [ ] Changes pushed to `iteration-c1-checkpoint` branch
- [ ] Submodule commit hash recorded in this doc
- [ ] Integration plan (this file) committed to `plans/`

## Future Enhancements (Out of Scope)

1. **Model Fallback Routing** (Iteration C3)
   - Use OpenRouter's `models` array in `extra_body`
   - Automatic failover if primary model unavailable

2. **Multi-Provider Experiments** (Iteration C4)
   - Implement `map_model_name()` with provider prefixes
   - Add config for cross-provider model comparisons
   - Update `ExtendedModelType` enum or create wrapper

3. **Cost Tracking** (Iteration C5)
   - Log OpenRouter generation IDs
   - Query OpenRouter cost API after experiments
   - Generate cost reports

4. **Caching** (Future)
   - Add OpenRouter caching headers for repeated prompts
   - Reduce costs for multi-round experiments

5. **Async Support** (Future)
   - Create async client factory for concurrent experiments
   - Not needed for current agent-trust code (synchronous)

## Stop Condition

This iteration is **COMPLETE** when:
1. ✅ All files created/modified and committed
2. ✅ Smoke test passes with real OpenRouter API key
3. ✅ At least one demo (`no_repeated_demo.py`) runs successfully via OpenRouter
4. ✅ Changes pushed to `iteration-c1-checkpoint` branch
5. ❌ Paper extraction NOT started (deferred to Iteration C3+)

**Next Iteration**: Extract Horton 2023 methodology and replicate experiments using OpenRouter-enabled agent-trust.

## References

- **Agent-Trust Paper**: https://arxiv.org/abs/2402.04559
- **Agent-Trust Repo**: https://github.com/camel-ai/agent-trust
- **OpenRouter Docs**: https://openrouter.ai/docs
- **OpenAI SDK Migration Guide**: https://github.com/openai/openai-python/discussions/742
- **Instructor Library**: https://github.com/jxnl/instructor

## Appendix: Upstream Commit Details

```
Commit: 9ce6bee29daf1f58c091077d89560ccd6d076f8b
Author: Chengxing Xie (Contribution equality: *)
Date: 2025-04-05 19:05:34 -0500
Message: Update README.md

Repository: https://github.com/camel-ai/agent-trust
Branch: main
License: Apache 2.0 (assumed from CAMEL AI projects)
Paper: NeurIPS 2024 (accepted)
```
