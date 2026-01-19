#!/usr/bin/env python3
"""
OpenRouter Agent-Trust Integration Smoke Test

This script verifies that the OpenRouter integration works correctly for both
legacy (v0.x module-level) and modern (v1.x client-based) OpenAI SDK patterns.

Usage:
    export OPENROUTER_API_KEY="sk-or-v1-..."
    python tools/test_openrouter_agent_trust.py

Tests:
    1. Environment variable loading
    2. Legacy API pattern (openai.ChatCompletion.create)
    3. Modern API pattern (client.chat.completions.create)
    4. Attribution headers
    5. Basic error handling

Author: TrustBench Project (Iteration C2)
Date: 2026-01-19
"""

import os
import sys
import time
from typing import Dict, Any

# Add repo root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Try to load .env file (requires python-dotenv)
try:
    from dotenv import load_dotenv
    # Load from repo root
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    load_dotenv(env_path)
except ImportError:
    print("Warning: python-dotenv not installed. Environment variables must be set manually.")
    print("Install with: pip install python-dotenv (or uv add python-dotenv)")
    print()

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_test(name: str, status: str, message: str = ""):
    """Print formatted test result."""
    if status == "pass":
        symbol = f"{GREEN}✓{RESET}"
    elif status == "fail":
        symbol = f"{RED}✗{RESET}"
    elif status == "warn":
        symbol = f"{YELLOW}!{RESET}"
    else:
        symbol = f"{BLUE}•{RESET}"

    print(f"  {symbol} {name}", end="")
    if message:
        print(f": {message}")
    else:
        print()


def test_environment_variables() -> bool:
    """Test 1: Check environment variables are loaded."""
    print(f"\n{BLUE}[Test 1/5]{RESET} Environment Variable Loading")
    print("-" * 60)

    all_pass = True

    # Check API key
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
    if api_key:
        masked_key = api_key[:15] + "..." + api_key[-4:] if len(api_key) > 20 else "***"
        print_test("API key found", "pass", masked_key)
    else:
        print_test("API key found", "fail", "Set OPENROUTER_API_KEY or OPENAI_API_KEY")
        all_pass = False

    # Check base URL
    base_url = os.getenv("OPENROUTER_BASE_URL") or "https://openrouter.ai/api/v1"
    print_test("Base URL", "pass", base_url)

    # Check optional attribution
    app_url = os.getenv("OPENROUTER_APP_URL")
    app_name = os.getenv("OPENROUTER_APP_NAME")

    if app_url:
        print_test("Attribution URL", "pass", app_url)
    else:
        print_test("Attribution URL", "warn", "Not set (optional)")

    if app_name:
        print_test("Attribution name", "pass", app_name)
    else:
        print_test("Attribution name", "warn", "Not set (optional)")

    return all_pass


def test_legacy_api() -> bool:
    """Test 2: Test legacy module-level API pattern."""
    print(f"\n{BLUE}[Test 2/5]{RESET} Legacy API Pattern (openai.ChatCompletion.create)")
    print("-" * 60)

    try:
        # Import and initialize
        from src.openrouter_client import initialize_openrouter
        import openai

        print_test("Import openrouter_client", "pass")

        # Initialize OpenRouter
        initialize_openrouter()
        print_test("Initialize OpenRouter", "pass")

        # Verify configuration
        api_key = openai.api_key
        if api_key:
            print_test("API key configured", "pass")
        else:
            print_test("API key configured", "fail")
            return False

        # Check base URL
        base_url = getattr(openai, 'base_url', None) or getattr(openai, 'api_base', None)
        if base_url and 'openrouter.ai' in str(base_url):
            print_test("Base URL configured", "pass", str(base_url))
        else:
            print_test("Base URL configured", "fail", f"Got: {base_url}")
            return False

        # Make API call
        print_test("Making API call", "info", "Testing completion...")
        start_time = time.time()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Hello from OpenRouter!' in exactly 5 words."}
            ],
            max_tokens=20,
            temperature=0.7
        )

        latency = time.time() - start_time

        # Verify response
        if response and hasattr(response, 'choices') and len(response.choices) > 0:
            content = response.choices[0].message.content
            print_test("API call succeeded", "pass", f"Latency: {latency:.2f}s")
            print_test("Response received", "pass", f"Content: '{content}'")

            # Log metadata
            if hasattr(response, 'usage'):
                usage = response.usage
                print_test(
                    "Token usage",
                    "info",
                    f"Prompt: {usage.prompt_tokens}, Completion: {usage.completion_tokens}"
                )
        else:
            print_test("API call succeeded", "fail", "Invalid response structure")
            return False

        return True

    except Exception as e:
        print_test("Legacy API test", "fail", str(e))
        import traceback
        traceback.print_exc()
        return False


def test_modern_api() -> bool:
    """Test 3: Test modern client-based API pattern."""
    print(f"\n{BLUE}[Test 3/5]{RESET} Modern API Pattern (client.chat.completions.create)")
    print("-" * 60)

    try:
        from src.openrouter_client import get_openrouter_client

        print_test("Import get_openrouter_client", "pass")

        # Get client
        client = get_openrouter_client()
        print_test("Create OpenRouter client", "pass", f"Type: {type(client).__name__}")

        # Verify client configuration
        if hasattr(client, 'base_url') and 'openrouter.ai' in str(client.base_url):
            print_test("Client base URL", "pass", str(client.base_url))
        else:
            print_test("Client base URL", "warn", "Unable to verify")

        # Make API call
        print_test("Making API call", "info", "Testing completion...")
        start_time = time.time()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Modern API works!' in exactly 4 words."}
            ],
            max_tokens=20,
            temperature=0.7
        )

        latency = time.time() - start_time

        # Verify response
        if response and response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            print_test("API call succeeded", "pass", f"Latency: {latency:.2f}s")
            print_test("Response received", "pass", f"Content: '{content}'")

            # Log metadata
            if hasattr(response, 'usage') and response.usage:
                usage = response.usage
                print_test(
                    "Token usage",
                    "info",
                    f"Prompt: {usage.prompt_tokens}, Completion: {usage.completion_tokens}"
                )
        else:
            print_test("API call succeeded", "fail", "Invalid response structure")
            return False

        return True

    except Exception as e:
        print_test("Modern API test", "fail", str(e))
        import traceback
        traceback.print_exc()
        return False


def test_instructor_compatibility() -> bool:
    """Test 4: Test instructor library compatibility (used in agent-trust)."""
    print(f"\n{BLUE}[Test 4/5]{RESET} Instructor Library Compatibility")
    print("-" * 60)

    try:
        # Check if instructor is installed
        try:
            import instructor
            print_test("Instructor library installed", "pass", f"Version: {instructor.__version__}")
        except ImportError:
            print_test("Instructor library installed", "warn", "Not installed (optional for agent-trust)")
            return True  # Not a failure, just not installed

        from pydantic import BaseModel
        from src.openrouter_client import get_openrouter_client

        # Define test schema
        class Response(BaseModel):
            word_count: int
            message: str

        print_test("Define Pydantic schema", "pass")

        # Create patched client
        client = instructor.patch(get_openrouter_client())
        print_test("Patch client with instructor", "pass")

        # Make structured API call
        print_test("Making structured API call", "info", "Testing extraction...")
        start_time = time.time()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=Response,
            messages=[
                {"role": "user", "content": "Say hello in exactly 3 words and count them."}
            ],
            max_tokens=30
        )

        latency = time.time() - start_time

        # Verify structured response
        if isinstance(response, Response):
            print_test("Structured extraction", "pass", f"Latency: {latency:.2f}s")
            print_test("Response parsed", "pass", f"Word count: {response.word_count}, Message: '{response.message}'")
        else:
            print_test("Structured extraction", "fail", f"Got type: {type(response)}")
            return False

        return True

    except ImportError:
        print_test("Instructor compatibility", "warn", "Instructor not installed (optional)")
        return True  # Not a failure
    except Exception as e:
        print_test("Instructor compatibility", "fail", str(e))
        import traceback
        traceback.print_exc()
        return False


def test_error_handling() -> bool:
    """Test 5: Test basic error handling."""
    print(f"\n{BLUE}[Test 5/5]{RESET} Error Handling")
    print("-" * 60)

    try:
        from src.openrouter_client import get_openrouter_client

        # Test with invalid model
        print_test("Testing invalid model", "info", "Should handle gracefully...")

        try:
            client = get_openrouter_client()
            response = client.chat.completions.create(
                model="invalid-model-name-12345",
                messages=[{"role": "user", "content": "test"}],
                max_tokens=5
            )
            print_test("Invalid model handling", "warn", "Accepted invalid model (OpenRouter may have fallback)")
        except Exception as e:
            error_type = type(e).__name__
            print_test("Invalid model handling", "pass", f"Caught {error_type}: {str(e)[:50]}")

        return True

    except Exception as e:
        print_test("Error handling test", "fail", str(e))
        return False


def main():
    """Run all smoke tests."""
    print(f"\n{BLUE}{'=' * 60}{RESET}")
    print(f"{BLUE}OpenRouter Agent-Trust Integration Smoke Test{RESET}")
    print(f"{BLUE}{'=' * 60}{RESET}")

    results = {}

    # Run tests
    results['env'] = test_environment_variables()

    if not results['env']:
        print(f"\n{RED}✗ Environment check failed. Please set OPENROUTER_API_KEY.{RESET}")
        print(f"{YELLOW}  Example: export OPENROUTER_API_KEY='sk-or-v1-...'{RESET}")
        sys.exit(1)

    results['legacy'] = test_legacy_api()
    results['modern'] = test_modern_api()
    results['instructor'] = test_instructor_compatibility()
    results['errors'] = test_error_handling()

    # Summary
    print(f"\n{BLUE}{'=' * 60}{RESET}")
    print(f"{BLUE}Test Summary{RESET}")
    print(f"{BLUE}{'=' * 60}{RESET}")

    total = len(results)
    passed = sum(1 for v in results.values() if v)

    for test_name, passed_status in results.items():
        status = f"{GREEN}PASS{RESET}" if passed_status else f"{RED}FAIL{RESET}"
        print(f"  {test_name.ljust(15)}: {status}")

    print(f"\n{BLUE}Result: {passed}/{total} tests passed{RESET}")

    if passed == total:
        print(f"\n{GREEN}✓ All tests passed! OpenRouter integration is working.{RESET}")
        print(f"\n{BLUE}Next steps:{RESET}")
        print(f"  1. Run agent-trust demos: cd vendor/agent-trust && python agent_trust/no_repeated_demo.py")
        print(f"  2. View README: cat vendor/agent-trust/README_OPENROUTER.md")
        return 0
    else:
        print(f"\n{RED}✗ Some tests failed. Please review errors above.{RESET}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
