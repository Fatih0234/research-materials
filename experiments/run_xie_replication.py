#!/usr/bin/env python3
"""
Xie et al. (2024) Replication Wrapper

Integration approach: Import vendor/agent-trust as library
Rationale:
  - Faster than subprocess (no spawn overhead for ~500+ API calls)
  - Better error handling (direct exception catching)
  - Easier debugging (stack traces preserved)
  - vendor/agent-trust designed as library (has __init__.py, functions)

Features:
  - INCREMENTAL SAVE: Results saved after each model completes
  - RESUME CAPABILITY: Can resume from checkpoint if interrupted
  - Checkpoint file tracks completed models
  - Per-model outputs stored under run_dir/per_model/<model>

Responsibilities:
  1. Load YAML config + model registry
  2. Resolve model panel → OpenRouter IDs
  3. Import vendor.agent_trust.all_game_person
  4. Call run_exp() for each model (with incremental save)
  5. Transform vendor JSON → episodes.jsonl + aggregates.csv
  6. Write run_metadata.json
"""

import argparse
import csv
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import pandas as pd
import yaml

# Add vendor/agent-trust to Python path
REPO_ROOT = Path(__file__).parent.parent
VENDOR_PATH = REPO_ROOT / "vendor" / "agent-trust"
VENDOR_AGENT_TRUST_PATH = VENDOR_PATH / "agent_trust"
sys.path.insert(0, str(VENDOR_PATH))
sys.path.insert(
    0, str(VENDOR_AGENT_TRUST_PATH)
)  # For relative imports within agent_trust


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


def load_model_registry(
    registry_path: str = "specs/05_model_registry.json",
) -> Dict[str, Any]:
    """Load model registry mapping paper models to OpenRouter IDs."""
    full_path = REPO_ROOT / registry_path
    with open(full_path, "r") as f:
        registry = json.load(f)

    print(f"✓ Loaded model registry from {registry_path}")
    print(f"  Total models: {len(registry)}")

    return registry


def resolve_models(
    model_panel: List[str], registry: Dict[str, Any]
) -> List[Dict[str, Any]]:
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


def create_output_directory(
    template: str,
    resume_dir: Optional[str] = None,
    output_dir_override: Optional[str] = None,
) -> Path:
    """Create timestamped output directory or resume from existing."""
    if resume_dir:
        output_dir = Path(resume_dir)
        if not output_dir.exists():
            raise ValueError(f"Resume directory does not exist: {resume_dir}")
        print(f"✓ Resuming from existing directory: {output_dir}")
    elif output_dir_override:
        output_dir = Path(output_dir_override)
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Using output directory: {output_dir}")
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(template.replace("{timestamp}", timestamp))
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created output directory: {output_dir}")

    return output_dir


def safe_model_dir_name(model_id: str) -> str:
    return model_id.replace("/", "_").replace(":", "_")


def get_model_output_dir(run_dir: Path, model_id: str) -> Path:
    return run_dir / "per_model" / safe_model_dir_name(model_id)


def load_checkpoint(output_dir: Path) -> Dict[str, Any]:
    """Load checkpoint file to see which models have completed."""
    checkpoint_path = output_dir / "checkpoint.json"
    if checkpoint_path.exists():
        with open(checkpoint_path, "r") as f:
            checkpoint = json.load(f)
        print(
            f"✓ Loaded checkpoint: {len(checkpoint.get('completed_models', []))} models completed"
        )
        return checkpoint
    return {"completed_models": [], "failed_models": []}


def save_checkpoint(output_dir: Path, checkpoint: Dict[str, Any]):
    """Save checkpoint file."""
    checkpoint_path = output_dir / "checkpoint.json"
    checkpoint["last_updated"] = datetime.now().isoformat()
    with open(checkpoint_path, "w") as f:
        json.dump(checkpoint, f, indent=2)


def get_model_game_key(model_id: str, game_id: str) -> str:
    """Create a unique key for model+game combination."""
    return f"{model_id}::{game_id}"


def append_episodes_to_jsonl(output_dir: Path, episodes: List[Dict[str, Any]]):
    """Append episodes to the JSONL file (incremental save)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    episodes_path = output_dir / "episodes.jsonl"
    with open(episodes_path, "a") as f:
        for episode in episodes:
            f.write(json.dumps(episode) + "\n")
    print(f"  ✓ Appended {len(episodes)} episodes to {episodes_path}")


def write_episodes_jsonl(output_dir: Path, episodes: List[Dict[str, Any]]):
    """Write episodes to JSONL file (overwrite)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    episodes_path = output_dir / "episodes.jsonl"
    with open(episodes_path, "w") as f:
        for episode in episodes:
            f.write(json.dumps(episode) + "\n")
    print(f"✓ Wrote {len(episodes)} episodes to {episodes_path}")


def load_episodes(episodes_path: Path) -> List[Dict[str, Any]]:
    episodes = []
    if episodes_path.exists():
        with open(episodes_path, "r") as f:
            for line in f:
                if line.strip():
                    episodes.append(json.loads(line))
    return episodes


def load_all_episodes(run_dir: Path) -> List[Dict[str, Any]]:
    """Load all episodes from run-level or per-model outputs."""
    run_level_path = run_dir / "episodes.jsonl"
    if run_level_path.exists():
        return load_episodes(run_level_path)

    episodes = []
    per_model_dir = run_dir / "per_model"
    if per_model_dir.exists():
        for model_dir in sorted(per_model_dir.iterdir()):
            episodes_path = model_dir / "episodes.jsonl"
            episodes.extend(load_episodes(episodes_path))
    return episodes


def run_vendor_experiment(
    model_spec: Dict[str, Any],
    game_config: Dict[str, Any],
    personas_path: str,
    temperature: float = 1.0,
    dry_run: bool = False,
) -> Optional[Dict[str, Any]]:
    """
    Run vendor/agent-trust experiment for a single model.

    Returns:
        Path to vendor output JSON, or None if dry_run=True
    """
    model_id = model_spec["openrouter_model_id"]
    game_id = game_config["game_id"]

    print(f"\n{'=' * 60}")
    print(f"Running: {model_spec['paper_name']} on {game_config['game_name']}")
    print(f"  Model ID: {model_id}")
    print(f"  Game ID: {game_id}")
    print(f"  Temperature: {temperature}")
    print(f"{'=' * 60}")

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

        # Create a model wrapper that mimics ExtendedModelType enum
        # Vendor code expects model.value for API calls AND folder paths
        class ModelWrapper:
            def __init__(self, model_id):
                # Keep original ID for API calls (OpenRouter needs "openai/gpt-4" format)
                self.value = model_id
                self._original_id = model_id
                # Clean version for folder names
                self._folder_safe_value = model_id.replace("/", "_").replace(":", "_")

            @property
            def is_openai(self) -> bool:
                """All models use OpenAI-compatible API through OpenRouter."""
                # Return True for ALL models since OpenRouter provides unified API
                # This ensures CAMEL uses ChatGPT config instead of OpenSourceConfig
                return True

            @property
            def is_open_source(self) -> bool:
                """All models routed through OpenRouter, not locally hosted."""
                # Always False - we're using OpenRouter API, not local model files
                return False

            @property
            def token_limit(self) -> int:
                """Return a reasonable default token limit."""
                if "gpt-4" in self._original_id:
                    return 8192
                elif "gpt-3.5" in self._original_id:
                    return 16385
                else:
                    return 4096  # Default for open-source models

            @property
            def value_for_tiktoken(self) -> str:
                """Return model ID for tiktoken, with fallbacks for unknown models."""
                # Map OpenRouter IDs to tiktoken-compatible model names
                model_id = self._original_id.lower()

                # Gemini models -> use gpt-4 encoding (similar performance tier)
                if "gemini" in model_id:
                    return "gpt-4"
                # GPT-5 models -> use gpt-4 encoding (most similar)
                elif "gpt-5" in model_id:
                    return "gpt-4"
                # GPT-4 models
                elif "gpt-4" in model_id:
                    return "gpt-4"
                # GPT-3.5 models
                elif "gpt-3.5" in model_id:
                    return "gpt-3.5-turbo"
                # GPT-OSS models -> use gpt-3.5-turbo as default
                elif "gpt-oss" in model_id:
                    return "gpt-3.5-turbo"
                # Llama models -> use gpt-3.5-turbo as default
                elif "llama" in model_id:
                    return "gpt-3.5-turbo"
                # All other models -> use gpt-3.5-turbo as safe default
                else:
                    return "gpt-3.5-turbo"

            def __str__(self):
                return self._original_id

        model_wrapper = ModelWrapper(model_id)

        # Call vendor run_exp function
        # Function signature: run_exp(model_list, whether_llm_player=False, gender=None,
        #                             special_prompt_key="", re_run=False, part_exp=True, need_run=None)
        result = run_exp(
            model_list=[model_wrapper],  # Pass model wrapper (has .value attribute)
            whether_llm_player=False,  # Not LLM vs LLM
            gender=None,  # Use gendered personas (None = use from character_2.json)
            special_prompt_key="",  # Use default prompts (no special prompt)
            re_run=False,  # Not a rerun
            part_exp=False,  # Run all games (or use need_run to filter)
            need_run=[game_id],  # List of game IDs to run
        )

        print(f"✓ Vendor experiment completed for {model_spec['paper_name']}")
        return {"success": True, "model_id": model_id}

    except Exception as e:
        print(f"✗ Error running experiment: {e}")
        import traceback

        traceback.print_exc()
        return {"success": False, "model_id": model_id, "error": str(e)}

    finally:
        # Always restore original working directory
        os.chdir(original_cwd)


def find_vendor_output(model_id: str, game_name: str) -> Optional[Path]:
    """Find the vendor output JSON file for a model+game."""
    # Sanitize model ID for folder name (matches the patch we applied)
    safe_model_name = safe_model_dir_name(model_id)

    # Vendor saves to: {safe_model_name}_res/res/{safe_model_name}_res/{game_name}_{model_id}.json
    # The path structure is a bit nested due to vendor code
    search_patterns = [
        VENDOR_AGENT_TRUST_PATH
        / f"{safe_model_name}_res"
        / "res"
        / f"{safe_model_name}_res"
        / f"{game_name}_{model_id}.json",
        VENDOR_AGENT_TRUST_PATH
        / f"{safe_model_name}_res"
        / f"{game_name}_{model_id}.json",
        VENDOR_AGENT_TRUST_PATH
        / "res"
        / f"{safe_model_name}_res"
        / f"{game_name}_{model_id}.json",
    ]

    # Also try with safe model name in the filename
    search_patterns.extend(
        [
            VENDOR_AGENT_TRUST_PATH
            / f"{safe_model_name}_res"
            / "res"
            / f"{safe_model_name}_res"
            / f"{game_name}_{safe_model_name}.json",
            VENDOR_AGENT_TRUST_PATH
            / "res"
            / f"{safe_model_name}_res"
            / f"{game_name}_{safe_model_name}.json",
        ]
    )

    for pattern in search_patterns:
        if pattern.exists():
            return pattern

    # Fallback: search recursively
    for json_file in VENDOR_AGENT_TRUST_PATH.glob(f"**/{game_name}*.json"):
        if safe_model_name in str(json_file) or model_id in str(json_file):
            return json_file

    return None


def cleanup_vendor_outputs(model_id: str):
    """Remove vendor-generated *_res folders after copying outputs."""
    safe_model_name = safe_model_dir_name(model_id)
    candidates = [
        VENDOR_AGENT_TRUST_PATH / f"{safe_model_name}_res",
        VENDOR_AGENT_TRUST_PATH / "res" / f"{safe_model_name}_res",
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.is_dir():
            shutil.rmtree(candidate, ignore_errors=True)


def consolidate_raw_outputs(run_dir: Path):
    """Collect per-model raw outputs into run-level raw folder."""
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(exist_ok=True)
    per_model_dir = run_dir / "per_model"
    if not per_model_dir.exists():
        return

    for model_dir in per_model_dir.iterdir():
        model_raw = model_dir / "raw"
        if not model_raw.exists():
            continue
        for item in model_raw.iterdir():
            if not item.is_file():
                continue
            dest = raw_dir / item.name
            if dest.exists():
                dest = raw_dir / f"{model_dir.name}__{item.name}"
            shutil.copy2(item, dest)


def write_analysis_outputs(output_dir: Path, episodes: List[Dict[str, Any]]):
    analysis_dir = output_dir / "analysis"
    analysis_dir.mkdir(exist_ok=True)

    aggregates = calculate_aggregates(episodes)
    if not aggregates.empty:
        aggregates.to_csv(analysis_dir / "model_summary.csv", index=False)

    df = pd.DataFrame(episodes)
    if df.empty:
        return

    valid_df = df[(df["success"] == True) & df["sent_amount"].notna()].copy()
    if valid_df.empty:
        return

    valid_df["sent_amount_bucket"] = valid_df["sent_amount"].round().astype(int)
    distribution = (
        valid_df.groupby(
            ["model_id", "model_paper_name", "game_id", "sent_amount_bucket"]
        )
        .size()
        .reset_index(name="count")
    )
    distribution.to_csv(analysis_dir / "amount_sent_distribution.csv", index=False)


def append_run_registry(entry: Dict[str, Any]):
    registry_path = REPO_ROOT / "notes" / "run_registry.csv"
    registry_path.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "run_id",
        "run_path",
        "paper_id",
        "experiment_name",
        "game_ids",
        "game_names",
        "model_ids",
        "total_models",
        "total_episodes",
        "mode",
        "created_at",
        "config_path",
        "git_commit",
        "notes",
    ]

    exists = registry_path.exists()
    with open(registry_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerow({key: entry.get(key, "") for key in fields})


def transform_vendor_output(
    vendor_output_path: Path,
    model_spec: Dict[str, Any],
    game_config: Dict[str, Any],
    run_id: str,
    paper_id: str,
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
        persona_idx = dialog_entry[0] if len(dialog_entry) > 0 else idx
        persona_text = dialog_entry[1] if len(dialog_entry) > 1 else ""
        raw_response = dialog_entry[2] if len(dialog_entry) > 2 else ""

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
            "error": error,
        }

        episodes.append(episode)

    return episodes


def calculate_aggregates(episodes: List[Dict[str, Any]]) -> pd.DataFrame:
    """Calculate aggregate statistics by model and game."""
    if not episodes:
        return pd.DataFrame()

    df = pd.DataFrame(episodes)

    # Filter to valid episodes only
    valid_df = df[df["success"] == True].copy()

    if valid_df.empty:
        return pd.DataFrame()

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
    output_dir: Path,
    config: Dict[str, Any],
    run_id: str,
    episodes: List[Dict[str, Any]],
    scope: str,
    model_ids: Optional[List[str]] = None,
    write_analysis: bool = False,
):
    """Save aggregates and metadata for a run or a single model."""
    if not episodes:
        print("\n⚠ No episodes found to aggregate")
        return

    aggregates = calculate_aggregates(episodes)
    aggregates_path = output_dir / "aggregates.csv"
    aggregates.to_csv(aggregates_path, index=False)
    print(f"✓ Saved aggregates to {aggregates_path}")

    resolved_model_ids = model_ids or sorted(
        {ep.get("model_id") for ep in episodes if ep.get("model_id")}
    )
    games = config.get("games", [])
    game_ids = [game.get("game_id") for game in games]
    game_names = [game.get("game_name") for game in games]

    metadata = {
        "run_id": run_id,
        "scope": scope,
        "experiment_id": config["experiment_name"],
        "paper_id": config["paper_id"],
        "config_path": str(config.get("_config_path", "unknown")),
        "config_resolved": config,
        "git_commit": get_git_commit(),
        "git_branch": get_git_branch(),
        "python_version": sys.version.split()[0],
        "start_time": config.get("_start_time", "unknown"),
        "end_time": datetime.now().isoformat(),
        "total_episodes": len(episodes),
        "total_models": len(resolved_model_ids),
        "model_ids": resolved_model_ids,
        "game_ids": game_ids,
        "game_names": game_names,
        "environment": {
            "openrouter_base_url": os.getenv(
                "OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"
            ),
            "vendor_agent_trust_commit": get_vendor_git_commit(),
        },
    }

    metadata_path = output_dir / "metadata.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"✓ Saved metadata to {metadata_path}")

    if write_analysis:
        write_analysis_outputs(output_dir, episodes)


def get_git_commit() -> str:
    """Get current git commit hash."""
    try:
        import subprocess

        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
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
            check=True,
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
            check=True,
        )
        return result.stdout.strip()
    except:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Run Xie et al. (2024) replication")
    parser.add_argument(
        "--config", required=True, help="Path to YAML configuration file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config without running experiments",
    )
    parser.add_argument(
        "--resume",
        type=str,
        default=None,
        help="Resume from existing output directory (path to directory)",
    )
    parser.add_argument(
        "--models",
        type=str,
        default=None,
        help="Comma-separated list of model keys or OpenRouter IDs to run",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Override run directory path (useful for parallel runs)",
    )

    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("Xie et al. (2024) Replication Wrapper")
    print("  [INCREMENTAL SAVE ENABLED]")
    print("=" * 60 + "\n")

    if args.resume and args.output_dir:
        print("✗ Error: --resume and --output-dir cannot be used together")
        return 1

    # Load configuration
    config = load_config(args.config)
    config["_config_path"] = args.config
    config["_start_time"] = datetime.now().isoformat()

    # Load model registry
    registry = load_model_registry()

    # Resolve model panel
    model_specs = resolve_models(config["model_panel"], registry)

    if args.models:
        model_filter = {item.strip() for item in args.models.split(",") if item.strip()}
        filtered_specs = []
        matched = set()
        for spec in model_specs:
            if spec["key"] in model_filter or spec["openrouter_model_id"] in model_filter:
                filtered_specs.append(spec)
                if spec["key"] in model_filter:
                    matched.add(spec["key"])
                if spec["openrouter_model_id"] in model_filter:
                    matched.add(spec["openrouter_model_id"])

        missing = sorted(model_filter - matched)
        if missing:
            print(f"  ⚠ Warning: Requested model(s) not found: {', '.join(missing)}")

        if not filtered_specs:
            print("✗ Error: No matching models found for --models")
            return 1

        model_specs = filtered_specs
        print(f"✓ Filtered model panel to {len(model_specs)} model(s)")

    if args.dry_run:
        print("\n✓ DRY RUN: Configuration validated successfully")
        print(f"  Would run {len(model_specs)} models × {len(config['games'])} games")
        print(
            f"  = {len(model_specs) * len(config['games']) * config['personas_count']} total API calls"
        )
        return 0

    # Create or resume output directory
    run_dir = create_output_directory(
        config["output_dir_template"],
        args.resume,
        args.output_dir,
    )
    per_model_root = run_dir / "per_model"
    per_model_root.mkdir(exist_ok=True)

    run_id = run_dir.name
    if run_id.startswith("run_"):
        run_id = run_id.replace("run_", "", 1)

    use_run_checkpoint = args.models is None
    run_checkpoint = load_checkpoint(run_dir) if use_run_checkpoint else {}
    completed_models: Set[str] = set(run_checkpoint.get("completed_models", []))
    failed_models: List[str] = run_checkpoint.get("failed_models", [])

    # Calculate progress
    total_combinations = len(model_specs) * len(config["games"])
    already_completed = len(completed_models)

    if use_run_checkpoint and already_completed > 0:
        print(
            f"\n📊 Progress: {already_completed}/{total_combinations} model-game combinations already completed"
        )
        print(f"   Resuming from where we left off...\n")

    # Run experiments with INCREMENTAL SAVE
    models_completed_this_run = 0
    models_failed_this_run = 0

    for model_spec in model_specs:
        model_id = model_spec["openrouter_model_id"]
        model_output_dir = get_model_output_dir(run_dir, model_id)
        model_output_dir.mkdir(parents=True, exist_ok=True)
        (model_output_dir / "raw").mkdir(exist_ok=True)

        if use_run_checkpoint:
            checkpoint_dir = run_dir
            checkpoint = run_checkpoint
            model_completed = completed_models
            model_failed = failed_models
        else:
            checkpoint_dir = model_output_dir
            checkpoint = load_checkpoint(checkpoint_dir)
            model_completed = set(checkpoint.get("completed_models", []))
            model_failed = checkpoint.get("failed_models", [])

        for game_config in config["games"]:
            game_id = game_config["game_id"]
            model_game_key = get_model_game_key(model_id, game_id)

            # Skip if already completed
            if model_game_key in model_completed:
                print(
                    f"\n⏭ Skipping {model_spec['paper_name']} - {game_config['game_name']} (already completed)"
                )
                continue

            # Run vendor experiment
            vendor_result = run_vendor_experiment(
                model_spec=model_spec,
                game_config=game_config,
                personas_path=config["personas_path"],
                temperature=config["decoding"]["temperature"],
                dry_run=False,
            )

            if vendor_result is None or not vendor_result.get("success", False):
                print(
                    f"  ✗ Failed: {model_spec['paper_name']} - {game_config['game_name']}"
                )
                model_failed.append(model_game_key)
                models_failed_this_run += 1

                # Save checkpoint even on failure
                checkpoint["failed_models"] = model_failed
                save_checkpoint(checkpoint_dir, checkpoint)
                continue

            # Find and transform vendor output
            vendor_output_path = find_vendor_output(model_id, game_config["game_name"])

            if vendor_output_path and vendor_output_path.exists():
                print(f"  Found vendor output: {vendor_output_path}")

                # Transform to episodes
                episodes = transform_vendor_output(
                    vendor_output_path=vendor_output_path,
                    model_spec=model_spec,
                    game_config=game_config,
                    run_id=run_id,
                    paper_id=config["paper_id"],
                )

                # INCREMENTAL SAVE: Append episodes immediately
                append_episodes_to_jsonl(model_output_dir, episodes)

                # Copy raw vendor output to results/raw/
                raw_dir = model_output_dir / "raw"
                safe_model_name = safe_model_dir_name(model_id)
                raw_copy_path = raw_dir / f"{game_config['game_name']}_{safe_model_name}.json"
                shutil.copy2(vendor_output_path, raw_copy_path)
                print(f"  ✓ Copied raw output to {raw_copy_path}")
                cleanup_vendor_outputs(model_id)

            else:
                print(f"  ⚠ Could not find vendor output file for {model_id}")
                # Still mark as completed since the API calls were made

            # Mark as completed and save checkpoint
            model_completed.add(model_game_key)
            checkpoint["completed_models"] = list(model_completed)
            save_checkpoint(checkpoint_dir, checkpoint)

            if use_run_checkpoint:
                completed_models = model_completed

            models_completed_this_run += 1

            if use_run_checkpoint:
                print(
                    f"\n  💾 CHECKPOINT SAVED: {len(completed_models)}/{total_combinations} complete"
                )
                print(
                    f"     Progress this run: {models_completed_this_run} completed, {models_failed_this_run} failed\n"
                )
        if not use_run_checkpoint:
            model_episodes = load_episodes(model_output_dir / "episodes.jsonl")
            save_results(
                output_dir=model_output_dir,
                config=config,
                run_id=run_id,
                episodes=model_episodes,
                scope="model",
                model_ids=[model_spec["openrouter_model_id"]],
            )

    # Save final aggregates and metadata
    print("\n" + "=" * 60)
    print("Saving final results...")
    print("=" * 60)

    if use_run_checkpoint:
        episodes = load_all_episodes(run_dir)
        if episodes:
            write_episodes_jsonl(run_dir, episodes)
            consolidate_raw_outputs(run_dir)
        save_results(
            output_dir=run_dir,
            config=config,
            run_id=run_id,
            episodes=episodes,
            scope="run",
            write_analysis=True,
        )

        append_run_registry(
            {
                "run_id": run_id,
                "run_path": str(run_dir),
                "paper_id": config.get("paper_id", ""),
                "experiment_name": config.get("experiment_name", ""),
                "game_ids": ";".join(
                    [g.get("game_id") for g in config.get("games", []) if g.get("game_id")]
                ),
                "game_names": ";".join(
                    [
                        g.get("game_name")
                        for g in config.get("games", [])
                        if g.get("game_name")
                    ]
                ),
                "model_ids": ";".join(
                    [
                        spec["openrouter_model_id"]
                        for spec in model_specs
                        if spec.get("openrouter_model_id")
                    ]
                ),
                "total_models": len(model_specs),
                "total_episodes": len(episodes),
                "mode": "full",
                "created_at": datetime.now().isoformat(),
                "config_path": str(config.get("_config_path", "")),
                "git_commit": get_git_commit(),
                "notes": "",
            }
        )

    # Print summary
    print("\n" + "=" * 60)
    print("✓ Replication complete!")
    print("=" * 60)
    print(f"  Results directory: {run_dir}")
    if use_run_checkpoint:
        print(f"  Total completed: {len(completed_models)}/{total_combinations}")
    print(
        f"  This run: {models_completed_this_run} completed, {models_failed_this_run} failed"
    )
    if failed_models:
        print(f"  Failed models: {len(failed_models)}")
    if not use_run_checkpoint:
        print("  Note: Run-level aggregates require merge_xie_results.py")
    print("=" * 60 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
