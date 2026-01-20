#!/bin/bash
# Helper script to run agent-trust demos with OpenRouter
# Usage: ./run_demo.sh [demo_name]
#   demo_name: no_repeated (default) | repeated

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load environment from repo root
if [ -f "../../.env" ]; then
    export $(cat ../../.env | grep -v '^#' | xargs)
    echo "✓ Loaded environment variables from .env"
else
    echo "⚠ Warning: ../../.env not found. Make sure OPENROUTER_API_KEY is set."
fi

# Determine which demo to run
DEMO="${1:-no_repeated}"

case "$DEMO" in
    no_repeated|single)
        echo "Running single-round trust game demo..."
        cd agent_trust
        ../.venv/bin/python no_repeated_demo.py
        ;;
    repeated|multi)
        echo "Running multi-round trust game demo..."
        cd agent_trust
        ../.venv/bin/python repeated_demo.py
        ;;
    *)
        echo "Unknown demo: $DEMO"
        echo "Usage: $0 [no_repeated|repeated]"
        exit 1
        ;;
esac
