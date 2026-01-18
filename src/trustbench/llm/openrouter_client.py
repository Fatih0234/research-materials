"""OpenRouter API client for LLM calls."""

import os
import time
from typing import Dict, Any, Optional, Tuple

from openai import OpenAI


class OpenRouterClient:
    """Client for calling LLMs via OpenRouter API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://openrouter.ai/api/v1"
    ):
        """Initialize OpenRouter client.

        Args:
            api_key: OpenRouter API key (if None, read from OPENROUTER_API_KEY env var)
            base_url: OpenRouter API base URL
        """
        if api_key is None:
            api_key = os.getenv("OPENROUTER_API_KEY")
            if not api_key:
                raise ValueError("OPENROUTER_API_KEY environment variable not set")

        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )

    def call_llm(
        self,
        messages: list,
        model: str,
        temperature: float = 1.0,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        seed: Optional[int] = None,
        max_retries: int = 3,
        retry_delay: float = 1.0
    ) -> Dict[str, Any]:
        """Call LLM via OpenRouter with retry logic.

        Args:
            messages: List of message dicts with 'role' and 'content'
            model: OpenRouter model ID (e.g., 'openrouter/openai/gpt-4-turbo')
            temperature: Sampling temperature
            top_p: Nucleus sampling parameter
            max_tokens: Max completion tokens
            seed: Random seed (if supported by model)
            max_retries: Max number of retries on failure
            retry_delay: Base delay between retries (exponential backoff)

        Returns:
            Dict with:
                - raw_text: Full LLM output text
                - request_id: Request ID if available
                - latency: Response latency in seconds
                - usage: Token usage metadata
                - error: Error message if failed (None on success)
        """
        # Build request params
        params = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        if top_p is not None:
            params["top_p"] = top_p
        if max_tokens is not None:
            params["max_tokens"] = max_tokens
        if seed is not None:
            params["seed"] = seed

        # Retry loop
        last_error = None
        for attempt in range(max_retries):
            try:
                start_time = time.time()
                response = self.client.chat.completions.create(**params)
                latency = time.time() - start_time

                # Extract response data
                raw_text = response.choices[0].message.content
                request_id = getattr(response, 'id', None)

                usage = {
                    "prompt_tokens": response.usage.prompt_tokens if response.usage else None,
                    "completion_tokens": response.usage.completion_tokens if response.usage else None,
                    "total_tokens": response.usage.total_tokens if response.usage else None,
                }

                return {
                    "raw_text": raw_text,
                    "request_id": request_id,
                    "latency": latency,
                    "usage": usage,
                    "error": None
                }

            except Exception as e:
                last_error = str(e)
                if attempt < max_retries - 1:
                    # Exponential backoff
                    wait_time = retry_delay * (2 ** attempt)
                    time.sleep(wait_time)
                else:
                    # Max retries reached
                    return {
                        "raw_text": None,
                        "request_id": None,
                        "latency": None,
                        "usage": None,
                        "error": f"Failed after {max_retries} retries: {last_error}"
                    }

        # Should not reach here, but just in case
        return {
            "raw_text": None,
            "request_id": None,
            "latency": None,
            "usage": None,
            "error": f"Unexpected error: {last_error}"
        }


class DryRunClient:
    """Dry-run client that generates fake outputs without calling LLM API."""

    def __init__(self, seed: int = 42):
        """Initialize dry-run client.

        Args:
            seed: Random seed for deterministic fake outputs
        """
        import random
        self.rng = random.Random(seed)

    def call_llm(
        self,
        messages: list,
        model: str,
        temperature: float = 1.0,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        seed: Optional[int] = None,
        max_retries: int = 3,
        retry_delay: float = 1.0
    ) -> Dict[str, Any]:
        """Generate fake LLM output for dry-run mode.

        Args:
            messages: List of message dicts (analyzed to determine role)
            model: Model ID (not used in dry-run)
            Other args: Ignored in dry-run

        Returns:
            Dict with fake response data
        """
        # Determine if this is trustor or trustee based on message content
        prompt_text = messages[-1]["content"] if messages else ""

        if "how much money would you give" in prompt_text.lower():
            # Trustor role
            amount = self.rng.randint(0, 10)
            raw_text = (
                f"I'll approach this decision carefully. Given the setup of this experiment, "
                f"I need to balance trust with prudence. The multiplication factor means my contribution "
                f"can benefit both of us if reciprocated.\n\n"
                f"Finally, I will give {amount} dollars."
            )
        elif "how much will you return" in prompt_text.lower():
            # Trustee role - extract amount received from prompt
            import re
            match = re.search(r"you received \$(\d+)", prompt_text)
            if match:
                received = int(match.group(1))
                amount = self.rng.randint(0, received)
            else:
                amount = 5  # fallback
            raw_text = (
                f"Considering the trust shown by the other player, I want to reciprocate fairly. "
                f"I'll return a portion that reflects good faith.\n\n"
                f"Finally, I will return {amount} dollars."
            )
        else:
            # Unknown - default to trustor
            amount = 5
            raw_text = f"Finally, I will give {amount} dollars."

        return {
            "raw_text": raw_text,
            "request_id": f"dry_run_{self.rng.randint(1000, 9999)}",
            "latency": 0.1,
            "usage": {
                "prompt_tokens": 100,
                "completion_tokens": 50,
                "total_tokens": 150
            },
            "error": None
        }
