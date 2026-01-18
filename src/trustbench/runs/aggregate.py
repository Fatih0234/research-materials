"""Aggregate statistics calculator for Trust Game results."""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
import statistics


class Aggregator:
    """Calculate aggregate statistics from episodes."""

    def __init__(self, episodes: List[Dict[str, Any]], config: Any):
        """Initialize aggregator.

        Args:
            episodes: List of episode records
            config: Experiment config
        """
        self.episodes = episodes
        self.config = config

    def aggregate(self) -> Dict[str, List[Dict[str, Any]]]:
        """Calculate aggregate statistics grouped by condition.

        Returns:
            Dict mapping condition labels to aggregate stat dicts
        """
        # Group episodes by condition (model + framing)
        conditions = {}

        for episode in self.episodes:
            model_id = episode["model_info"]["model_id"]
            framing = episode["partner_framing"]
            condition_key = f"{model_id}_{framing}"

            if condition_key not in conditions:
                conditions[condition_key] = {
                    "model_id": model_id,
                    "framing": framing,
                    "episodes": []
                }

            conditions[condition_key]["episodes"].append(episode)

        # Calculate stats for each condition
        aggregates = {}

        for condition_key, condition_data in conditions.items():
            stats = self._calculate_condition_stats(
                episodes=condition_data["episodes"],
                model_id=condition_data["model_id"],
                framing=condition_data["framing"]
            )
            aggregates[condition_key] = stats

        return aggregates

    def _calculate_condition_stats(
        self,
        episodes: List[Dict[str, Any]],
        model_id: str,
        framing: str
    ) -> Dict[str, Any]:
        """Calculate statistics for a single condition.

        Args:
            episodes: Episodes in this condition
            model_id: Model identifier
            framing: Partner framing treatment

        Returns:
            Aggregate statistics dict
        """
        n_episodes = len(episodes)

        # Extract valid amounts
        valid_amounts = []
        for ep in episodes:
            if ep["vrr_flags"]["valid_trustor"]:
                amount = ep["parsed_actions"]["amount_sent"]
                if amount is not None:
                    valid_amounts.append(amount)

        n_valid = len(valid_amounts)
        vrr = n_valid / n_episodes if n_episodes > 0 else 0

        # Calculate statistics
        if n_valid > 0:
            mean_sent = statistics.mean(valid_amounts)
            median_sent = statistics.median(valid_amounts)
            min_sent = min(valid_amounts)
            max_sent = max(valid_amounts)
            sd_sent = statistics.stdev(valid_amounts) if n_valid > 1 else 0

            # Distribution bins [0-1), [1-2), ..., [9-10], [10]
            bins = [0] * 11
            for amount in valid_amounts:
                if amount == 10:
                    bins[10] += 1
                else:
                    idx = int(amount)
                    bins[idx] += 1

        else:
            mean_sent = None
            median_sent = None
            min_sent = None
            max_sent = None
            sd_sent = None
            bins = [0] * 11

        # Build aggregate record
        aggregate = {
            "run_id": episodes[0]["run_id"],
            "experiment_id": episodes[0]["experiment_id"],
            "condition": f"{model_id.split('/')[-1]}_{framing}",
            "model_id": model_id,
            "partner_framing": framing,
            "n_episodes": n_episodes,
            "n_valid": n_valid,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "trustor_stats": {
                "vrr": vrr,
                "mean_sent": mean_sent,
                "sd_sent": sd_sent,
                "median_sent": median_sent,
                "min_sent": min_sent,
                "max_sent": max_sent,
                "distribution_bins": bins
            },
            "trustee_stats": None,  # Not implemented in MVP
            "human_baseline": self.config.human_baseline,
            "comparison_ready": {
                "sent_values": valid_amounts,
                "return_ratios": None
            }
        }

        return aggregate

    def write_aggregates(self, output_dir: Path, run_id: str):
        """Write aggregate statistics to JSON and CSV files.

        Args:
            output_dir: Output directory
            run_id: Run identifier
        """
        aggregates = self.aggregate()

        # Write JSON
        json_path = output_dir / f"aggregates_{run_id}.json"
        with open(json_path, 'w') as f:
            json.dump(list(aggregates.values()), f, indent=2)

        print(f"Aggregates JSON written to: {json_path}")

        # Write CSV
        csv_path = output_dir / f"aggregates_{run_id}.csv"
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)

            # Header
            writer.writerow([
                "condition",
                "model_id",
                "partner_framing",
                "n_episodes",
                "n_valid",
                "vrr",
                "mean_sent",
                "sd_sent",
                "median_sent",
                "min_sent",
                "max_sent"
            ])

            # Data rows
            for agg in aggregates.values():
                writer.writerow([
                    agg["condition"],
                    agg["model_id"],
                    agg["partner_framing"],
                    agg["n_episodes"],
                    agg["n_valid"],
                    f"{agg['trustor_stats']['vrr']:.3f}",
                    f"{agg['trustor_stats']['mean_sent']:.2f}" if agg['trustor_stats']['mean_sent'] is not None else "N/A",
                    f"{agg['trustor_stats']['sd_sent']:.2f}" if agg['trustor_stats']['sd_sent'] is not None else "N/A",
                    f"{agg['trustor_stats']['median_sent']:.1f}" if agg['trustor_stats']['median_sent'] is not None else "N/A",
                    f"{agg['trustor_stats']['min_sent']:.1f}" if agg['trustor_stats']['min_sent'] is not None else "N/A",
                    f"{agg['trustor_stats']['max_sent']:.1f}" if agg['trustor_stats']['max_sent'] is not None else "N/A"
                ])

        print(f"Aggregates CSV written to: {csv_path}")

        return aggregates
