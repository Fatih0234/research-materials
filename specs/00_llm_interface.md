# LLM Interface Specification: OpenRouter Calling Contract

**Created:** 2026-01-18 (Iteration C0)
**Purpose:** Define the OpenRouter API calling contract for TrustBench experiment runner
**Status:** Draft - will be refined during Iteration D (runner design)

---

## 1. Provider Selection

**Provider:** OpenRouter (https://openrouter.ai)

**Rationale:**
- Single API key, unified interface to multiple LLM providers
- Supports GPT-4, Claude, Gemini, Llama, and other models
- Cost efficiency via provider arbitrage
- Consistent request/response schema across providers
- Built-in rate limiting and error handling

**Alternative Considered:** Direct provider APIs (OpenAI SDK, Anthropic SDK, Google AI SDK)
- **Rejected:** Requires managing multiple API clients, separate billing, inconsistent schemas

---

## 2. Model Identifier Format

**Format:** `openrouter/{provider}/{model-id}`

**Examples:**
- `openrouter/openai/gpt-4-turbo`
- `openrouter/openai/gpt-4o`
- `openrouter/anthropic/claude-3.5-sonnet`
- `openrouter/google/gemini-pro-1.5`
- `openrouter/meta-llama/llama-3.1-70b-instruct`

**Configuration:**
- Runner accepts model ID as parameter
- Config file maps short names to full OpenRouter IDs:
  ```json
  {
    "models": {
      "gpt4": "openrouter/openai/gpt-4-turbo",
      "claude": "openrouter/anthropic/claude-3.5-sonnet"
    }
  }
  ```

---

## 3. Required Per-Call Logged Fields

For reproducibility and debugging, **every LLM API call** must log the following fields:

### Request Metadata
- `request_id`: Unique identifier for this call (UUID)
- `timestamp`: ISO 8601 timestamp (UTC)
- `model`: Full OpenRouter model ID (e.g., `openrouter/openai/gpt-4-turbo`)
- `provider`: Provider name extracted from model ID (e.g., `openai`)
- `model_version`: Version string if available from API response
- `api_endpoint`: OpenRouter endpoint used (e.g., `https://openrouter.ai/api/v1/chat/completions`)

### Sampling Parameters
- `temperature`: Float (0.0 - 2.0)
- `top_p`: Float (0.0 - 1.0)
- `max_tokens`: Integer (max completion length)
- `seed`: Integer (if supported by model, else `null`)
- `n`: Number of completions requested (for self-consistency)
- `stop_sequences`: Array of stop tokens (if used)

### Prompt Content
- `prompt_hash`: SHA-256 hash of full prompt text (for deduplication)
- `prompt_version`: Version identifier for prompt template used (e.g., `v1.0-trust-investor`)
- `prompt_text`: Full prompt text sent to model (system + user messages concatenated)
- `messages`: Array of message objects (for chat-based models):
  ```json
  [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ]
  ```

### Response Content
- `raw_output_text`: Full text returned by model (before any parsing)
- `parsed_action`: Extracted action value (numeric or structured) after parsing
- `parse_success`: Boolean (did parsing succeed?)
- `parse_errors`: Array of error messages if parsing failed (empty array if success)
- `retry_count`: Number of retries attempted (0 if first attempt succeeded)

### Token Usage & Cost
- `prompt_tokens`: Integer (from API response)
- `completion_tokens`: Integer (from API response)
- `total_tokens`: Integer (prompt + completion)
- `cost_usd`: Estimated cost in USD (calculated from OpenRouter pricing)

### Episode Context (if applicable)
- `episode_id`: Which game episode this call belongs to
- `role`: Which role this LLM is playing (`investor` | `trustee` | etc.)
- `condition`: Experimental condition/treatment label

---

## 4. Structured Output Strategy

**Goal:** Extract numeric actions (e.g., "send 7 tokens") or structured data from LLM free text.

### Approach: Multi-Stage Parsing with Repair

**Stage 1: Attempt JSON Parse (if using JSON prompts)**
- If prompt requests JSON format, try `json.loads(raw_output_text)`
- If successful, extract action field and validate schema
- If fails, proceed to Stage 2

**Stage 2: Regex Extraction (for numeric actions)**
- Patterns:
  - `send (\d+)` → extract integer
  - `return (\d+)` → extract integer
  - `contribute (\d+)` → extract integer
- If successful, return parsed value
- If fails, proceed to Stage 3

**Stage 3: LLM Repair Prompt (up to K retries)**
- Send repair prompt: "The previous response was not valid. Please respond with ONLY a number between 0 and 10."
- Retry with `temperature=0` for determinism
- Max retries: K=3 (configurable)
- If still fails, mark as `parse_error` and log

**Stage 4: Manual Review Flag**
- If parsing fails after K retries, flag episode for manual review
- Log full conversation history
- Option: Skip episode in analysis OR impute conservative value (e.g., 0)

**Logging:** Record ALL parsing attempts in `parse_errors` array, even successful ones:
```json
{
  "parse_errors": [
    {"attempt": 1, "method": "json", "error": "Invalid JSON syntax"},
    {"attempt": 2, "method": "regex", "success": true, "value": 7}
  ]
}
```

---

## 5. Reproducibility Guarantees

### Prompt Versioning
- **All prompts must be versioned** (e.g., `v1.0`, `v1.1`)
- Changes to prompt wording = new version
- Store prompt templates in `prompts/` directory with version suffix
- Log prompt version in every call

### Config Snapshots
- Before each experiment run, snapshot full config to `results/<run_id>/config.json`
- Includes: model IDs, sampling params, prompt versions, random seeds
- Enables exact replication of any run

### Seed Handling
- **If model supports seeding** (e.g., OpenAI `seed` parameter):
  - Use fixed seed per episode for determinism
  - Log seed in request metadata
- **If model does NOT support seeding** (e.g., some Claude versions):
  - Set `seed=null` in logs
  - Acknowledge non-determinism in documentation
  - Run larger sample sizes to average out variance

### Model Version Tracking
- OpenRouter returns model version in some responses
- Log exact version string (e.g., `gpt-4-turbo-2024-04-09`)
- If version not returned, log as `null` and note in README

---

## 6. Rate Limiting & Error Handling

### Rate Limits
- OpenRouter enforces provider-specific rate limits
- Runner must implement **exponential backoff** on 429 errors
- Backoff strategy:
  ```python
  wait_time = min(2 ** retry_count, 60)  # cap at 60 seconds
  ```
- Max retries for rate limit: 10 (configurable)

### Error Handling
- **Transient Errors (429, 503):** Retry with backoff
- **Invalid Request (400):** Log error, do NOT retry
- **Authentication (401, 403):** Fail immediately with clear error
- **Timeout (504):** Retry up to 3 times, then skip episode
- **All Errors:** Log to `errors.jsonl` with full context

---

## 7. Self-Consistency Implementation

For papers using self-consistency (Wang et al. 2023):

**Request:** Set `n > 1` in API call (e.g., `n=5`)
**Response:** Receive multiple completions
**Aggregation:**
- **For numeric actions:** Calculate mean and standard deviation
- **For categorical actions:** Majority vote (mode)
- **Logging:** Store all N outputs, plus aggregated result

**Example:**
```json
{
  "n": 5,
  "raw_outputs": ["send 8", "send 7", "send 8", "send 9", "send 8"],
  "parsed_actions": [8, 7, 8, 9, 8],
  "aggregated_action": 8.0,
  "std_dev": 0.632,
  "majority_vote": 8
}
```

---

## 8. OpenRouter-Specific Features

### Model Fallback
- OpenRouter supports fallback models if primary fails
- Example config:
  ```json
  {
    "model": "openrouter/openai/gpt-4-turbo",
    "fallback": ["openrouter/openai/gpt-4o"]
  }
  ```
- Log which model actually responded

### Cost Tracking
- OpenRouter provides token counts and pricing info
- Runner calculates cost per episode
- Aggregate total cost per experiment run
- Display in results summary

---

## 9. Example API Call (Pseudocode)

```python
import openai
import hashlib
import uuid
import json
from datetime import datetime

def call_llm(prompt_text, model, temperature, top_p, max_tokens, seed=None):
    """
    Call OpenRouter API and log all required fields.
    """
    # Generate request ID
    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat() + "Z"

    # Hash prompt for deduplication
    prompt_hash = hashlib.sha256(prompt_text.encode()).hexdigest()

    # Prepare API request
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    request_params = {
        "model": model,
        "messages": [{"role": "user", "content": prompt_text}],
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "seed": seed  # null if not supported
    }

    # Make API call
    response = client.chat.completions.create(**request_params)

    # Extract response
    raw_output_text = response.choices[0].message.content
    model_version = response.model  # OpenRouter returns actual model version

    # Parse action
    parsed_action, parse_errors = parse_action(raw_output_text)

    # Log everything
    log_entry = {
        "request_id": request_id,
        "timestamp": timestamp,
        "model": model,
        "model_version": model_version,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "seed": seed,
        "prompt_hash": prompt_hash,
        "prompt_text": prompt_text,
        "raw_output_text": raw_output_text,
        "parsed_action": parsed_action,
        "parse_errors": parse_errors,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "cost_usd": calculate_cost(response.usage, model)
    }

    save_log(log_entry)
    return parsed_action
```

---

## 10. Future Extensions

**Batch API Support:**
- OpenRouter may add batch endpoints for cost savings
- Runner should support batch mode for non-interactive experiments

**Streaming:**
- For debugging/monitoring, support streaming responses
- Display partial outputs in real-time during development

**Model Comparison:**
- Run same prompt across multiple models in parallel
- Log model ID in results for easy comparison

---

## 11. Validation Checklist

Before using OpenRouter integration in production:

- [ ] API key tested and authenticated
- [ ] All required fields logged in test calls
- [ ] Prompt hashing works correctly
- [ ] Parsing logic handles edge cases (empty output, malformed JSON)
- [ ] Error handling tested (429, 503, timeout)
- [ ] Cost calculation verified against OpenRouter pricing
- [ ] Self-consistency aggregation tested with n>1
- [ ] Config snapshot includes all reproducibility info
- [ ] Logs are human-readable and machine-parseable (JSONL)

---

**Status:** Draft specification - refine during Iteration D
**Next:** Use this spec to implement runner in Iteration D
