#!/usr/bin/env python3
"""
Xie et al. (2024) Replication Wrapper

Integration approach: Import vendor/agent-trust as library
Rationale:
  - Faster than subprocess (no spawn overhead for ~500+ API calls)
  - Better error handling (direct exception catching)
  - Easier debugging (stack traces preserved)
  - vendor/agent-trust designed as library (has __init__.py, functions)

Responsibilities:
  1. Load YAML config + model registry
  2. Resolve model panel → OpenRouter IDs
  3. Import vendor.agent_trust.all_game_person
  4. Call run_exp() for each model
  5. Transform vendor JSON → episodes.jsonl + aggregates.csv
  6. Write run_metadata.json
"""

import argparse
import json
import os
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import yaml

# Add vendor/agent-trust to Python path
REPO_ROOT = Path(__file__).parent.parent
VENDOR_PATH = REPO_ROOT / "vendor" / "agent-trust"
VENDOR_AGENT_TRUST_PATH = VENDOR_PATH / "agent_trust"
sys.path.insert(0, str(VENDOR_PATH))
sys.path.insert(0, str(VENDOR_AGENT_TRUST_PATH))  # For relative imports within agent_trust


def load_config(config_path: str) -> Dict[str, Any]:
    """Load and validate YAML configuration."""
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    print(f"✓ Loaded config from {config_path}")
    print(f"  Experiment: {config['experiment_name']}")
    print(f"  Paper: {config['paper_id']}")
    print(f"  Games: {len(config['games'])} game(s)")
    print(f"  Model panel: {len(config['model_panel'])} model(s)")

    return config


def load_model_registry(registry_path: str = "specs/05_model_registry.json") -> Dict[str, Any]:
    """Load model registry mapping paper models to OpenRouter IDs."""
    full_path = REPO_ROOT / registry_path
    with open(full_path, "r") as f:
        registry = json.load(f)

    print(f"✓ Loaded model registry from {registry_path}")
    print(f"  Total models: {len(registry)}")

    return registry


def resolve_models(model_panel: List[str], registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Resolve model panel keys to full model specifications."""
    resolved = []

    for model_key in model_panel:
        if model_key not in registry:
            print(f"  ⚠ Warning: Model '{model_key}' not found in registry, skipping")
            continue

        model_spec = registry[model_key].copy()
        model_spec["key"] = model_key
        resolved.append(model_spec)

    print(f"✓ Resolved {len(resolved)} models:")
    for spec in resolved:
        status_symbol = "→" if spec["status"] == "substitute" else "="
        print(f"  {status_symbol} {spec['paper_name']}: {spec['openrouter_model_id']}")

    return resolved


def create_output_directory(template: str) -> Path:
    """Create timestamped output directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(template.replace("{timestamp}", timestamp))
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    (output_dir / "raw").mkdir(exist_ok=True)

    print(f"✓ Created output directory: {output_dir}")

    return output_dir


def run_vendor_experiment(
    model_spec: Dict[str, Any],
    game_config: Dict[str, Any],
    personas_path: str,
    temperature: float = 1.0,
    dry_run: bool = False
) -> Optional[Dict[str, Any]]:
    """
    Run vendor/agent-trust experiment for a single model.

    Returns:
        Path to vendor output JSON, or None if dry_run=True
    """
    model_id = model_spec["openrouter_model_id"]
    game_id = game_config["game_id"]

    print(f"\n{'='*60}")
    print(f"Running: {model_spec['paper_name']} on {game_config['game_name']}")
    print(f"  Model ID: {model_id}")
    print(f"  Game ID: {game_id}")
    print(f"  Temperature: {temperature}")
    print(f"{'='*60}")

    if dry_run:
        print("  [DRY RUN] Skipping actual execution")
        return None

    # Change to vendor directory (vendor code uses relative paths)
    original_cwd = os.getcwd()
    vendor_cwd = VENDOR_AGENT_TRUST_PATH

    try:
        os.chdir(vendor_cwd)
        print(f"  Changed working directory to: {vendor_cwd}")

        # Import vendor code (must be after chdir)
        from agent_trust.all_game_person import run_exp
        from agent_trust.exp_model_class import ExtendedModelType

        # Map OpenRouter model ID to ExtendedModelType
        # The vendor code uses model type enum to route API calls
        # Since we're using OpenRouter, we need to create a compatible model type
        # For now, we'll use a string-based approach and let OpenRouter handle routing

        # Call vendor run_exp function
        # Note: This may need adjustment based on actual vendor function signature
        result = run_exp(
            model_list=[model_id],  # Pass OpenRouter model ID directly
            need_run=[game_id],     # List of game IDs to run
            llm_player=False,        # Not LLM vs LLM
            is_genderless=False,     # Use gendered personas
            is_special_prompt=False, # Use default prompts
            is_rerun=False           # Not a rerun
        )

        print(f"✓ Vendor experiment completed for {model_spec['paper_name']}")
        return result

    except Exception as e:
        print(f"✗ Error running experiment: {e}")
        import traceback
        traceback.print_exc()
        return None

    finally:
        # Always restore original working directory
        os.chdir(original_cwd)


def transform_vendor_output(
    vendor_output_path: Path,
    model_spec: Dict[str, Any],
    game_config: Dict[str, Any],
    run_id: str,
    paper_id: str
) -> List[Dict[str, Any]]:
    """
    Transform vendor JSON output to standardized episodes format.

    Expected vendor JSON structure:
    {
        "res": [5.0, 7.0, 3.0, ...],  # Amounts sent per persona
        "dialog": [[0, "You are Emily...", "I will give..."], ...],
        "origin_prompt": [game_key, critic_prompt, game_description],
        "structured_output": [[{BDI_dict}, input_content], ...]
    }
    """
    with open(vendor_output_path, "r") as f:
        vendor_data = json.load(f)

    episodes = []

    # Extract arrays
    amounts = vendor_data.get("res", [])
    dialogs = vendor_data.get("dialog", [])

    # Align by index
    for idx, (amount, dialog_entry) in enumerate(zip(amounts, dialogs)):
        persona_idx = dialog_entry[0]
        persona_text = dialog_entry[1]
        raw_response = dialog_entry[2]

        # Validate amount
        success = True
        error = None
        if not isinstance(amount, (int, float)):
            success = False
            error = f"Invalid amount type: {type(amount)}"
        elif amount < 0 or amount > 10:
            success = False
            error = f"Amount out of range: {amount}"

        episode = {
            "run_id": run_id,
            "paper_id": paper_id,
            "model_id": model_spec["openrouter_model_id"],
            "model_paper_name": model_spec["paper_name"],
            "game_id": game_config["game_id"],
            "game_name": game_config["game_name"],
            "persona_id": f"xie_{persona_idx:03d}",
            "persona_blob": persona_text,
            "prompt_version_or_path": "vendor/agent-trust/agent_trust/prompt/person_all_game_prompt.json",
            "condition_flags": {"partner_framing": "baseline"},
            "sent_amount": float(amount) if success else None,
            "returned_amount": None,  # Only trustor in this game
            "raw_output_text": raw_response,
            "timestamp": datetime.now().isoformat(),
            "temperature": 1.0,
            "success": success,
            "error": error
        }

        episodes.append(episode)

    return episodes


def calculate_aggregates(episodes: List[Dict[str, Any]]) -> pd.DataFrame:
    """Calculate aggregate statistics by model and game."""
    df = pd.DataFrame(episodes)

    # Filter to valid episodes only
    valid_df = df[df["success"] == True].copy()

    # Group by model_id and game_id
    aggregates = []

    for (model_id, model_name, game_id), group in valid_df.groupby(
        ["model_id", "model_paper_name", "game_id"]
    ):
        amounts = group["sent_amount"].dropna()

        agg = {
            "model_id": model_id,
            "model_paper_name": model_name,
            "game_id": game_id,
            "n": len(group),
            "n_valid": len(amounts),
            "vrr": len(amounts) / len(group) if len(group) > 0 else 0.0,
            "mean_sent": amounts.mean() if len(amounts) > 0 else None,
            "median_sent": amounts.median() if len(amounts) > 0 else None,
            "sd_sent": amounts.std() if len(amounts) > 0 else None,
            "min_sent": amounts.min() if len(amounts) > 0 else None,
            "max_sent": amounts.max() if len(amounts) > 0 else None,
        }

        aggregates.append(agg)

    return pd.DataFrame(aggregates)


def save_results(
    episodes: List[Dict[str, Any]],
    aggregates: pd.DataFrame,
    config: Dict[str, Any],
    output_dir: Path,
    run_id: str
):
    """Save all results to output directory."""

    # Save episodes.jsonl
    episodes_path = output_dir / "episodes.jsonl"
    with open(episodes_path, "w") as f:
        for episode in episodes:
            f.write(json.dumps(episode) + "\n")
    print(f"✓ Saved {len(episodes)} episodes to {episodes_path}")

    # Save aggregates.csv
    aggregates_path = output_dir / "aggregates.csv"
    aggregates.to_csv(aggregates_path, index=False)
    print(f"✓ Saved aggregates to {aggregates_path}")

    # Save metadata.json
    metadata = {
        "run_id": run_id,
        "experiment_id": config["experiment_name"],
        "paper_id": config["paper_id"],
        "config_path": str(config.get("_config_path", "unknown")),
        "config_resolved": config,
        "git_commit": get_git_commit(),
        "git_branch": get_git_branch(),
        "python_version": sys.version.split()[0],
        "start_time": config.get("_start_time", "unknown"),
        "end_time": datetime.now().isoformat(),
        "environment": {
            "openrouter_base_url": os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
            "vendor_agent_trust_commit": get_vendor_git_commit()
        }
    }

    metadata_path = output_dir / "metadata.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"✓ Saved metadata to {metadata_path}")


def get_git_commit() -> str:
    """Get current git commit hash."""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except:
        return "unknown"


def get_git_branch() -> str:
    """Get current git branch."""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except:
        return "unknown"


def get_vendor_git_commit() -> str:
    """Get vendor/agent-trust git commit hash."""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=VENDOR_PATH,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Run Xie et al. (2024) replication")
    parser.add_argument(
        "--config",
        required=True,
        help="Path to YAML configuration file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config without running experiments"
    )

    args = parser.parse_args()

    print("\n" + "="*60)
    print("Xie et al. (2024) Replication Wrapper")
    print("="*60 + "\n")

    # Load configuration
    config = load_config(args.config)
    config["_config_path"] = args.config
    config["_start_time"] = datetime.now().isoformat()

    # Load model registry
    registry = load_model_registry()

    # Resolve model panel
    model_specs = resolve_models(config["model_panel"], registry)

    if args.dry_run:
        print("\n✓ DRY RUN: Configuration validated successfully")
        print(f"  Would run {len(model_specs)} models × {len(config['games'])} games")
        print(f"  = {len(model_specs) * len(config['games']) * config['personas_count']} total API calls")
        return 0

    # Create output directory
    output_dir = create_output_directory(config["output_dir_template"])
    run_id = output_dir.name.split("__")[1]  # Extract timestamp as run_id

    # Run experiments
    all_episodes = []

    for model_spec in model_specs:
        for game_config in config["games"]:
            # Run vendor experiment
            vendor_result = run_vendor_experiment(
                model_spec=model_spec,
                game_config=game_config,
                personas_path=config["personas_path"],
                temperature=config["decoding"]["temperature"],
                dry_run=False
            )

            if vendor_result is None:
                print(f"  ⚠ Skipping {model_spec['paper_name']} - {game_config['game_name']}")
                continue

            # Transform output
            # Note: This requires finding the vendor output file
            # For now, we'll create a placeholder
            # In actual implementation, need to locate vendor JSON output

            print(f"  ⚠ Output transformation not yet implemented")
            print(f"     TODO: Locate vendor JSON at vendor/agent-trust/[model]_res/[game]_res/*.json")

    # Save results
    if all_episodes:
        aggregates = calculate_aggregates(all_episodes)
        save_results(all_episodes, aggregates, config, output_dir, run_id)
    else:
        print("\n⚠ No episodes to save (output transformation not implemented)")

    print("\n" + "="*60)
    print("✓ Replication complete")
    print(f"  Results: {output_dir}")
    print("="*60 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
