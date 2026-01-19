"""
OpenRouter Client Factory for Agent-Trust Integration

This module provides OpenRouter configuration and client creation for both
legacy (v0.x module-level) and modern (v1.x instance-based) OpenAI SDK patterns.

Usage:
    # For legacy openai.* module-level API calls:
    from src.openrouter_client import initialize_openrouter
    initialize_openrouter()
    import openai
    response = openai.ChatCompletion.create(...)

    # For modern OpenAI() client instances:
    from src.openrouter_client import get_openrouter_client
    client = get_openrouter_client()
    response = client.chat.completions.create(...)

Environment Variables:
    OPENROUTER_API_KEY: OpenRouter API key (required)
    OPENROUTER_BASE_URL: OpenRouter base URL (default: https://openrouter.ai/api/v1)
    OPENROUTER_APP_URL: Application URL for attribution (optional)
    OPENROUTER_APP_NAME: Application name for attribution (optional)
    OPENAI_API_KEY: Fallback if OPENROUTER_API_KEY not set

Author: TrustBench Project (Iteration C2)
Date: 2026-01-19
"""

import logging
import os
import time
from typing import Optional, Dict, Any

# Try to load dotenv if available (graceful fallback if not installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Default OpenRouter configuration
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"


def _get_env(key: str, default: Optional[str] = None, fallback_key: Optional[str] = None) -> Optional[str]:
    """
    Get environment variable with optional fallback.

    Args:
        key: Primary environment variable name
        default: Default value if not found
        fallback_key: Alternative environment variable to check

    Returns:
        Environment variable value or default
    """
    value = os.getenv(key)
    if value:
        return value
    if fallback_key:
        value = os.getenv(fallback_key)
        if value:
            logger.debug(f"Using fallback {fallback_key} for {key}")
            return value
    return default


def _build_headers(app_url: Optional[str] = None, app_name: Optional[str] = None) -> Dict[str, str]:
    """
    Build OpenRouter attribution headers.

    Args:
        app_url: Application URL for HTTP-Referer header
        app_name: Application name for X-Title header

    Returns:
        Dictionary of headers (empty dict if no attribution provided)
    """
    headers = {}
    if app_url:
        headers["HTTP-Referer"] = app_url
    if app_name:
        headers["X-Title"] = app_name
    return headers


def initialize_openrouter(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    app_name: Optional[str] = None,
) -> None:
    """
    Initialize OpenRouter for legacy openai.* module-level API calls.

    This function patches the global openai module configuration to route
    all API calls through OpenRouter. It supports both OpenAI SDK v0.x and
    v1.x legacy patterns.

    Args:
        api_key: OpenRouter API key (default: from env OPENROUTER_API_KEY or OPENAI_API_KEY)
        base_url: OpenRouter base URL (default: from env or https://openrouter.ai/api/v1)
        app_url: Application URL for attribution (default: from env OPENROUTER_APP_URL)
        app_name: Application name for attribution (default: from env OPENROUTER_APP_NAME)

    Raises:
        ImportError: If openai module is not installed
        ValueError: If API key is not provided and not found in environment

    Example:
        >>> from src.openrouter_client import initialize_openrouter
        >>> initialize_openrouter()
        >>> import openai
        >>> response = openai.ChatCompletion.create(
        ...     model="gpt-3.5-turbo",
        ...     messages=[{"role": "user", "content": "Hello"}]
        ... )
    """
    try:
        import openai
    except ImportError:
        raise ImportError(
            "openai package not installed. "
            "Install with: pip install openai"
        )

    # Get configuration from arguments or environment
    api_key = api_key or _get_env("OPENROUTER_API_KEY", fallback_key="OPENAI_API_KEY")
    base_url = base_url or _get_env("OPENROUTER_BASE_URL", default=DEFAULT_BASE_URL)
    app_url = app_url or _get_env("OPENROUTER_APP_URL")
    app_name = app_name or _get_env("OPENROUTER_APP_NAME")

    if not api_key:
        raise ValueError(
            "OpenRouter API key not found. "
            "Set OPENROUTER_API_KEY or OPENAI_API_KEY environment variable, "
            "or pass api_key argument."
        )

    # Build attribution headers
    headers = _build_headers(app_url, app_name)

    # CRITICAL: Set environment variable for libraries that create their own OpenAI clients
    # (e.g., CAMEL framework). This ensures all clients use OpenRouter.
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_BASE_URL"] = base_url

    # Patch module-level configuration
    # Note: OpenAI SDK v1.x still supports module-level attributes for backward compatibility
    openai.api_key = api_key

    # Try v1.x attribute first, fallback to v0.x
    try:
        openai.base_url = base_url
        logger.debug(f"Set openai.base_url = {base_url} (v1.x style)")
    except AttributeError:
        openai.api_base = base_url
        logger.debug(f"Set openai.api_base = {base_url} (v0.x style)")

    # Set default headers if SDK supports it
    if headers:
        try:
            if not hasattr(openai, 'default_headers'):
                openai.default_headers = {}
            openai.default_headers.update(headers)
            logger.debug(f"Set attribution headers: {headers}")
        except AttributeError:
            logger.warning("Unable to set attribution headers (SDK version may not support it)")

    logger.info(f"✓ OpenRouter initialized for legacy API (base_url: {base_url})")
    if app_name or app_url:
        logger.info(f"  Attribution: {app_name or 'N/A'} | {app_url or 'N/A'}")


def get_openrouter_client(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    app_name: Optional[str] = None,
) -> Any:
    """
    Create and return a modern OpenAI client configured for OpenRouter.

    Use this for new code or when patching libraries like instructor that
    expect an OpenAI client instance.

    Args:
        api_key: OpenRouter API key (default: from env OPENROUTER_API_KEY or OPENAI_API_KEY)
        base_url: OpenRouter base URL (default: from env or https://openrouter.ai/api/v1)
        app_url: Application URL for attribution (default: from env OPENROUTER_APP_URL)
        app_name: Application name for attribution (default: from env OPENROUTER_APP_NAME)

    Returns:
        OpenAI client instance configured for OpenRouter

    Raises:
        ImportError: If openai package is not installed
        ValueError: If API key is not provided and not found in environment

    Example:
        >>> from src.openrouter_client import get_openrouter_client
        >>> client = get_openrouter_client()
        >>> response = client.chat.completions.create(
        ...     model="gpt-3.5-turbo",
        ...     messages=[{"role": "user", "content": "Hello"}]
        ... )
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError(
            "openai package not installed or version too old. "
            "Install with: pip install openai>=1.0.0"
        )

    # Get configuration from arguments or environment
    api_key = api_key or _get_env("OPENROUTER_API_KEY", fallback_key="OPENAI_API_KEY")
    base_url = base_url or _get_env("OPENROUTER_BASE_URL", default=DEFAULT_BASE_URL)
    app_url = app_url or _get_env("OPENROUTER_APP_URL")
    app_name = app_name or _get_env("OPENROUTER_APP_NAME")

    if not api_key:
        raise ValueError(
            "OpenRouter API key not found. "
            "Set OPENROUTER_API_KEY or OPENAI_API_KEY environment variable, "
            "or pass api_key argument."
        )

    # Build attribution headers
    headers = _build_headers(app_url, app_name)

    # Create client instance
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
        default_headers=headers if headers else None,
    )

    logger.info(f"✓ OpenRouter client created (base_url: {base_url})")
    if app_name or app_url:
        logger.info(f"  Attribution: {app_name or 'N/A'} | {app_url or 'N/A'}")

    return client


def map_model_name(model: str) -> str:
    """
    [FUTURE] Map OpenAI model names to OpenRouter provider-prefixed format.

    This function is a placeholder for future enhancement (Iteration C3+).
    Currently returns the model name unchanged to preserve compatibility
    with agent-trust's hardcoded OpenAI model names.

    Args:
        model: OpenAI model name (e.g., "gpt-3.5-turbo")

    Returns:
        OpenRouter model name (currently unchanged from input)

    Example (future):
        >>> map_model_name("gpt-3.5-turbo")
        "openai/gpt-3.5-turbo"
        >>> map_model_name("claude-3.5-sonnet")
        "anthropic/claude-3-5-sonnet-20241022"
    """
    # Phase 1: No mapping, preserve OpenAI names
    # OpenRouter accepts legacy names without provider prefix
    return model


# Convenience function for logging API calls (optional utility)
def log_api_call(
    model: str,
    prompt_tokens: Optional[int] = None,
    completion_tokens: Optional[int] = None,
    latency: Optional[float] = None,
    **kwargs
) -> None:
    """
    Log API call metadata for observability.

    Args:
        model: Model name used
        prompt_tokens: Number of prompt tokens
        completion_tokens: Number of completion tokens
        latency: API call latency in seconds
        **kwargs: Additional metadata to log
    """
    log_data = {
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "latency_sec": latency,
    }
    log_data.update(kwargs)

    logger.info(f"API Call: {log_data}")


# Module-level initialization check
def is_openrouter_initialized() -> bool:
    """
    Check if OpenRouter has been initialized for legacy API.

    Returns:
        True if openai module is configured with OpenRouter base URL
    """
    try:
        import openai
        # Check if base URL contains openrouter.ai
        base_url = getattr(openai, 'base_url', None) or getattr(openai, 'api_base', None)
        if base_url and 'openrouter.ai' in str(base_url):
            return True
    except (ImportError, AttributeError):
        pass
    return False


# Self-test when run as script
if __name__ == "__main__":
    print("OpenRouter Client Factory Self-Test")
    print("=" * 50)

    # Test 1: Check environment variables
    print("\n[1/3] Checking environment variables...")
    api_key = _get_env("OPENROUTER_API_KEY", fallback_key="OPENAI_API_KEY")
    if api_key:
        print(f"  ✓ API key found ({api_key[:20]}...)")
    else:
        print("  ✗ API key not found (set OPENROUTER_API_KEY)")

    base_url = _get_env("OPENROUTER_BASE_URL", default=DEFAULT_BASE_URL)
    print(f"  ✓ Base URL: {base_url}")

    app_url = _get_env("OPENROUTER_APP_URL")
    app_name = _get_env("OPENROUTER_APP_NAME")
    if app_url or app_name:
        print(f"  ✓ Attribution: {app_name or 'N/A'} | {app_url or 'N/A'}")
    else:
        print("  ! No attribution headers (optional)")

    # Test 2: Initialize legacy API
    print("\n[2/3] Testing legacy API initialization...")
    try:
        initialize_openrouter()
        print("  ✓ Legacy API initialized")
        print(f"  ✓ OpenRouter check: {is_openrouter_initialized()}")
    except Exception as e:
        print(f"  ✗ Error: {e}")

    # Test 3: Create modern client
    print("\n[3/3] Testing modern client creation...")
    try:
        client = get_openrouter_client()
        print(f"  ✓ Modern client created: {type(client).__name__}")
    except Exception as e:
        print(f"  ✗ Error: {e}")

    print("\n" + "=" * 50)
    print("Self-test complete!")
    print("\nTo test with actual API calls, run:")
    print("  python tools/test_openrouter_agent_trust.py")
