#!/usr/bin/env python3
"""TrustBench experiment runner CLI."""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trustbench.config import Config
from trustbench.runs.runner import TrustGameRunner
from trustbench.runs.aggregate import Aggregator


def main():
    parser = argparse.ArgumentParser(
        description="Run TrustBench experiments",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run mode (no API calls)
  python scripts/run_trustbench.py --config configs/xie_mvp.yaml --dry-run

  # Limit to 5 episodes for testing
  python scripts/run_trustbench.py --config configs/xie_mvp.yaml --dry-run --limit 5

  # Run with real API (requires OPENROUTER_API_KEY)
  python scripts/run_trustbench.py --config configs/xie_mvp.yaml
        """
    )

    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to YAML config file"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run in dry-run mode (no API calls, fake outputs)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of episodes (for testing)"
    )

    args = parser.parse_args()

    # Load config
    print(f"Loading config: {args.config}")
    try:
        config = Config(args.config)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

    print(f"Experiment ID: {config.experiment_id}")

    # Initialize runner
    runner = TrustGameRunner(config=config, dry_run=args.dry_run)

    # Run experiment
    try:
        runner.run(limit=args.limit)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError during run: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # Compute aggregates
    print("\nComputing aggregate statistics...")
    aggregator = Aggregator(episodes=runner.get_episodes(), config=config)
    aggregates = aggregator.write_aggregates(
        output_dir=runner.output_dir,
        run_id=runner.run_id
    )

    # Print summary
    print("\n" + "="*60)
    print("EXPERIMENT SUMMARY")
    print("="*60)
    print(f"Total episodes: {len(runner.get_episodes())}")
    print(f"Output directory: {runner.output_dir}")
    print(f"\nResults by condition:")
    print("-"*60)

    for condition_key, agg in aggregates.items():
        stats = agg["trustor_stats"]
        print(f"\n{agg['condition']}")
        print(f"  Episodes: {agg['n_episodes']}")
        print(f"  Valid: {agg['n_valid']} (VRR: {stats['vrr']:.1%})")
        if stats['mean_sent'] is not None:
            print(f"  Mean sent: ${stats['mean_sent']:.2f} (SD: ${stats['sd_sent']:.2f})")
            print(f"  Median: ${stats['median_sent']:.1f}, Range: [${stats['min_sent']:.1f}, ${stats['max_sent']:.1f}]")

    print("\n" + "="*60)
    print("Run completed successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
