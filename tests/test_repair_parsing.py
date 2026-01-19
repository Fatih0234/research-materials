"""Tests for repair-number parsing in runner."""

import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.modules.setdefault(
    "yaml",
    types.SimpleNamespace(safe_load=lambda *args, **kwargs: None, dump=lambda *args, **kwargs: None),
)
sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=object))

from trustbench.runs.runner import TrustGameRunner


def test_parse_repair_number_basic():
    amount, status, matched = TrustGameRunner._parse_repair_number("6", 10)
    assert amount == 6.0
    assert status == "success"

    amount, status, matched = TrustGameRunner._parse_repair_number(" 6 ", 10)
    assert amount == 6.0
    assert status == "success"

    amount, status, matched = TrustGameRunner._parse_repair_number("Answer: 6", 10)
    assert amount == 6.0
    assert status == "success"

    amount, status, matched = TrustGameRunner._parse_repair_number("$6", 10)
    assert amount == 6.0
    assert status == "success"


def test_parse_repair_number_invalid():
    amount, status, matched = TrustGameRunner._parse_repair_number("six", 10)
    assert amount is None
    assert status == "no_numeric_value"

    amount, status, matched = TrustGameRunner._parse_repair_number("11", 10)
    assert amount is None
    assert status == "value_out_of_range"

    amount, status, matched = TrustGameRunner._parse_repair_number("-1", 10)
    assert amount is None
    assert status == "value_out_of_range"
