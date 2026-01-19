#!/usr/bin/env python3
"""
Trust Game Experiment Runner (Iteration C2 Validation)

Runs a controlled experiment with agent-trust using OpenRouter.
Tests the full pipeline with a subset of personas and games.

Usage:
    cd experiments
    ../vendor/agent-trust/.venv/bin/python3 run_trust_study.py
"""

import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Add paths
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / 'vendor' / 'agent-trust' / 'agent_trust'))

# Initialize OpenRouter BEFORE importing agent-trust modules
from src.openrouter_client import initialize_openrouter

# Set gpt-4o-mini as the model via environment (overrides .env if needed)
os.environ['TRUSTBENCH_DEFAULT_MODEL'] = 'gpt-4o-mini'

initialize_openrouter()

# Change to agent_trust directory for relative imports and file operations
agent_trust_dir = repo_root / 'vendor' / 'agent-trust' / 'agent_trust'
os.chdir(agent_trust_dir)

# Now import agent-trust modules
from exp_model_class import ExtendedModelType
from all_game_person import run_exp

# Configuration
EXPERIMENT_CONFIG = {
    'name': 'trust_study_gpt4o_mini_validation',
    'model': 'gpt-4o-mini',  # OpenRouter model
    'num_personas': 20,  # Use first 20 personas
    'games': ['1', '2'],  # Dictator Game and Trust Game
    'temperature': 1.0,
    'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S')
}

def main():
    print("=" * 80)
    print(f"Trust Game Experiment: {EXPERIMENT_CONFIG['name']}")
    print("=" * 80)
    print(f"Model: {EXPERIMENT_CONFIG['model']}")
    print(f"Personas: {EXPERIMENT_CONFIG['num_personas']}")
    print(f"Games: {EXPERIMENT_CONFIG['games']}")
    print(f"Temperature: {EXPERIMENT_CONFIG['temperature']}")
    print(f"Timestamp: {EXPERIMENT_CONFIG['timestamp']}")
    print("=" * 80)
    print()

    # Verify OpenRouter is configured
    if not os.getenv('OPENROUTER_API_KEY') and not os.getenv('OPENAI_API_KEY'):
        print("ERROR: No API key found!")
        print("Set OPENROUTER_API_KEY in .env file")
        return 1

    print("✓ OpenRouter API key found")
    print(f"✓ Base URL: {os.getenv('OPENAI_BASE_URL', 'not set')}")
    print()

    # Load persona and game data to show what we'll test
    with open('prompt/character_2.json', 'r') as f:
        personas = json.load(f)
    with open('prompt/person_all_game_prompt.json', 'r') as f:
        games = json.load(f)

    print(f"Loaded {len(personas)} total personas")
    print(f"Using first {EXPERIMENT_CONFIG['num_personas']} personas")
    print()

    for game_id in EXPERIMENT_CONFIG['games']:
        game_name = games[game_id][0]
        print(f"Game {game_id}: {game_name}")
    print()

    # Create results directory
    results_dir = Path(__file__).parent.parent / 'results' / EXPERIMENT_CONFIG['timestamp']
    results_dir.mkdir(parents=True, exist_ok=True)

    # Save experiment config
    config_file = results_dir / 'experiment_config.json'
    with open(config_file, 'w') as f:
        json.dump(EXPERIMENT_CONFIG, f, indent=2)
    print(f"✓ Saved config to: {config_file}")
    print()

    # Run experiment
    print("Starting experiment...")
    print("-" * 80)

    try:
        # Note: agent-trust's run_exp expects model names in its ExtendedModelType format
        # We need to add gpt-4o-mini to the model dict or use an existing one

        # For now, use gpt-3.5-turbo-0613 as a proxy (OpenRouter will get the right model from env)
        # The actual model routing happens via our OpenRouter integration

        print("Note: Using ExtendedModelType.GPT_3_5_TURBO_0613 as model type")
        print("      (OpenRouter will use gpt-4o-mini as configured in environment)")
        print()

        # Import after chdir
        from all_game_person import (
            run_exp, all_prompt, all_chara, ExtendedModelType
        )

        # Back up original data and modify for our subset
        print("Preparing persona subset...")

        # Load and select first N personas
        with open('prompt/character_2.json', 'r') as f:
            all_personas = json.load(f)

        # Get first N persona keys
        persona_keys = list(all_personas.keys())[:EXPERIMENT_CONFIG['num_personas']]
        selected_personas = {k: all_personas[k] for k in persona_keys}

        # Temporarily replace character file with subset
        shutil.copy('prompt/character_2.json', 'prompt/character_2.json.backup')
        with open('prompt/character_2.json', 'w') as f:
            json.dump(selected_personas, f, indent=2)

        print(f"Running with {len(selected_personas)} personas and {len(EXPERIMENT_CONFIG['games'])} games")
        print(f"Total experiments: {len(selected_personas) * len(EXPERIMENT_CONFIG['games'])}")
        print()

        # Run experiment with need_run parameter to specify games
        # part_exp=True means only run games in need_run list
        run_exp(
            model_list=[ExtendedModelType.GPT_3_5_TURBO_0613],  # Proxy for gpt-4o-mini
            part_exp=True,
            need_run=EXPERIMENT_CONFIG['games'],  # ['1', '2'] for Dictator and Trust games
            re_run=False
        )

        # Restore original character file
        shutil.move('prompt/character_2.json.backup', 'prompt/character_2.json')

        print()
        print("-" * 80)
        print("✓ Experiment completed successfully!")
        print()
        print(f"Results saved to: vendor/agent-trust/agent_trust/No repeated res/")
        print(f"Config saved to: {config_file}")

        return 0

    except Exception as e:
        print()
        print("-" * 80)
        print(f"✗ Experiment failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
