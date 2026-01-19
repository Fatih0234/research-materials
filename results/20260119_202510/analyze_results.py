#!/usr/bin/env python3
"""
Analyze results from gpt-4o-mini validation study
"""

import json
import statistics
from pathlib import Path

# Load results
results_dir = Path(__file__).parent / 'raw_data'

with open(results_dir / 'Dictator_Game_gpt-3.5-turbo-0613.json', 'r') as f:
    dictator_data = json.load(f)

with open(results_dir / 'Trust_Game_gpt-3.5-turbo-0613.json', 'r') as f:
    trust_data = json.load(f)

print("=" * 80)
print("Trust Game Experiment Analysis")
print("Model: gpt-4o-mini (via OpenRouter)")
print("=" * 80)
print()

# Dictator Game Analysis
print("DICTATOR GAME ANALYSIS")
print("-" * 80)
dictator_amounts = dictator_data['res']
print(f"Total decisions: {len(dictator_amounts)}")
print(f"Mean: ${statistics.mean(dictator_amounts):.2f}")
print(f"Median: ${statistics.median(dictator_amounts):.2f}")
print(f"Std Dev: ${statistics.stdev(dictator_amounts):.2f}")
print(f"Min: ${min(dictator_amounts):.2f}")
print(f"Max: ${max(dictator_amounts):.2f}")
print()

# Distribution
print("Distribution of amounts given:")
from collections import Counter
dist = Counter(dictator_amounts)
for amount in sorted(dist.keys()):
    count = dist[amount]
    pct = (count / len(dictator_amounts)) * 100
    bar = "█" * int(pct / 2)
    print(f"  ${amount:4.1f}: {count:3d} ({pct:5.1f}%) {bar}")
print()

# Trust Game Analysis
print("TRUST GAME ANALYSIS")
print("-" * 80)
trust_amounts = trust_data['res']
print(f"Total decisions: {len(trust_amounts)}")
print(f"Mean: ${statistics.mean(trust_amounts):.2f}")
print(f"Median: ${statistics.median(trust_amounts):.2f}")
print(f"Std Dev: ${statistics.stdev(trust_amounts):.2f}")
print(f"Min: ${min(trust_amounts):.2f}")
print(f"Max: ${max(trust_amounts):.2f}")
print()

# Distribution
print("Distribution of amounts given:")
dist = Counter(trust_amounts)
for amount in sorted(dist.keys()):
    count = dist[amount]
    pct = (count / len(trust_amounts)) * 100
    bar = "█" * int(pct / 2)
    print(f"  ${amount:4.1f}: {count:3d} ({pct:5.1f}%) {bar}")
print()

# Comparison
print("COMPARISON")
print("-" * 80)
print(f"Dictator Game mean: ${statistics.mean(dictator_amounts):.2f}")
print(f"Trust Game mean: ${statistics.mean(trust_amounts):.2f}")
diff = statistics.mean(trust_amounts) - statistics.mean(dictator_amounts)
print(f"Difference: ${diff:.2f} ({'higher' if diff > 0 else 'lower'} in Trust Game)")
print()

# Behavioral insights
print("BEHAVIORAL INSIGHTS")
print("-" * 80)
print(f"Modal response (Dictator): ${statistics.mode(dictator_amounts):.2f}")
print(f"Modal response (Trust): ${statistics.mode(trust_amounts):.2f}")
print()

# Fairness analysis
fair_share = 5.0  # 50% of $10
dictator_fair = sum(1 for x in dictator_amounts if x == fair_share)
trust_fair = sum(1 for x in trust_amounts if x == fair_share)
print(f"Chose fair share ($5) in Dictator Game: {dictator_fair}/{len(dictator_amounts)} ({100*dictator_fair/len(dictator_amounts):.1f}%)")
print(f"Chose fair share ($5) in Trust Game: {trust_fair}/{len(trust_amounts)} ({100*trust_fair/len(trust_amounts):.1f}%)")
print()

# Generosity metrics
generous_threshold = 5.0  # >= $5 is generous
dictator_generous = sum(1 for x in dictator_amounts if x >= generous_threshold)
trust_generous = sum(1 for x in trust_amounts if x >= generous_threshold)
print(f"Generous (≥$5) in Dictator Game: {dictator_generous}/{len(dictator_amounts)} ({100*dictator_generous/len(dictator_amounts):.1f}%)")
print(f"Generous (≥$5) in Trust Game: {trust_generous}/{len(trust_amounts)} ({100*trust_generous/len(trust_amounts):.1f}%)")
print()

print("=" * 80)
print("Analysis complete")
print("=" * 80)
