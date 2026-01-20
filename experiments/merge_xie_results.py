#!/usr/bin/env python3
"""
Merge Xie replication outputs from multiple runs into a single results folder.
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import yaml

REPO_ROOT = Path(__file__).parent.parent
VENDOR_PATH = REPO_ROOT / "vendor" / "agent-trust"


def load_config(config_path: str) -> Dict[str, Any]:
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    config["_config_path"] = config_path
    return config


def load_episodes(episodes_path: Path) -> List[Dict[str, Any]]:
    episodes = []
    with open(episodes_path, "r") as f:
        for line in f:
            if line.strip():
                episodes.append(json.loads(line))
    return episodes


def write_episodes(output_path: Path, episodes: List[Dict[str, Any]]):
    with open(output_path, "w") as f:
        for episode in episodes:
            f.write(json.dumps(episode) + "\n")


def calculate_aggregates(episodes: List[Dict[str, Any]]) -> pd.DataFrame:
    if not episodes:
        return pd.DataFrame()

    df = pd.DataFrame(episodes)
    valid_df = df[df["success"] == True].copy()
    if valid_df.empty:
        return pd.DataFrame()

    aggregates = []
    for (model_id, model_name, game_id), group in valid_df.groupby(
        ["model_id", "model_paper_name", "game_id"]
    ):
        amounts = group["sent_amount"].dropna()
        aggregates.append(
            {
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
        )

    return pd.DataFrame(aggregates)


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


def get_git_commit() -> str:
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
    except Exception:
        return "unknown"


def get_vendor_git_commit() -> str:
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
    except Exception:
        return "unknown"


def copy_raw_outputs(source_dir: Path, output_dir: Path):
    raw_dir = source_dir / "raw"
    if not raw_dir.exists():
        return

    dest_raw = output_dir / "raw"
    dest_raw.mkdir(exist_ok=True)

    for item in raw_dir.iterdir():
        if not item.is_file():
            continue
        dest_path = dest_raw / item.name
        if dest_path.exists():
            dest_path = dest_raw / f"{source_dir.name}__{item.name}"
        shutil.copy2(item, dest_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge Xie replication results")
    parser.add_argument(
        "--config",
        required=True,
        help="Path to YAML configuration file",
    )
    parser.add_argument(
        "--source-dir",
        action="append",
        required=True,
        help="Source results directory (repeatable)",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory for merged results",
    )

    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "raw").mkdir(exist_ok=True)

    episodes: List[Dict[str, Any]] = []
    source_runs = []

    for source in args.source_dir:
        source_dir = Path(source)
        episodes_path = source_dir / "episodes.jsonl"
        if not episodes_path.exists():
            print(f"✗ Missing episodes.jsonl in {source_dir}")
            return 1
        source_runs.append(source_dir.name)
        source_episodes = load_episodes(episodes_path)
        episodes.extend(source_episodes)
        copy_raw_outputs(source_dir, output_dir)
        print(f"✓ Loaded {len(source_episodes)} episodes from {source_dir}")

    if not episodes:
        print("✗ No episodes to merge")
        return 1

    write_episodes(output_dir / "episodes.jsonl", episodes)
    aggregates = calculate_aggregates(episodes)
    aggregates.to_csv(output_dir / "aggregates.csv", index=False)
    write_analysis_outputs(output_dir, episodes)

    metadata = {
        "run_id": output_dir.name,
        "experiment_id": config.get("experiment_name", "unknown"),
        "paper_id": config.get("paper_id", "unknown"),
        "config_path": str(config.get("_config_path", "unknown")),
        "config_resolved": config,
        "git_commit": get_git_commit(),
        "python_version": sys.version.split()[0],
        "merged_at": datetime.now().isoformat(),
        "total_episodes": len(episodes),
        "total_models": len(set(ep.get("model_id") for ep in episodes)),
        "source_runs": source_runs,
        "environment": {
            "openrouter_base_url": "https://openrouter.ai/api/v1",
            "vendor_agent_trust_commit": get_vendor_git_commit(),
        },
    }

    with open(output_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"✓ Merged results saved to {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
