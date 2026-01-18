"""Tests for Trust Game parser."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trustbench.parsing.trust_game_parser import TrustGameParser


def test_trustor_parser():
    """Test trustor output parsing."""
    parser = TrustGameParser()

    # Test case 1: Standard format with integer
    text1 = "I will be careful with my money. Finally, I will give 6 dollars."
    amount, status, errors = parser.parse_trustor_output(text1, endowment=10)
    assert amount == 6.0, f"Expected 6.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 1 passed: Standard integer format")

    # Test case 2: Standard format with dollar sign
    text2 = "Let me think about this. Finally, I will give $7 dollars."
    amount, status, errors = parser.parse_trustor_output(text2, endowment=10)
    assert amount == 7.0, f"Expected 7.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 2 passed: Format with dollar sign")

    # Test case 3: Decimal amount
    text3 = "I'll send a moderate amount. Finally, I will give 6.5 dollars."
    amount, status, errors = parser.parse_trustor_output(text3, endowment=10)
    assert amount == 6.5, f"Expected 6.5, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 3 passed: Decimal format")

    # Test case 4: Zero dollars
    text4 = "I don't trust this setup. Finally, I will give 0 dollars."
    amount, status, errors = parser.parse_trustor_output(text4, endowment=10)
    assert amount == 0.0, f"Expected 0.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 4 passed: Zero dollars")

    # Test case 5: Maximum (10 dollars)
    text5 = "I'm feeling very trusting. Finally, I will give 10 dollars."
    amount, status, errors = parser.parse_trustor_output(text5, endowment=10)
    assert amount == 10.0, f"Expected 10.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 5 passed: Maximum amount")

    # Test case 6: Out of range (too high)
    text6 = "I'll give everything and more! Finally, I will give 15 dollars."
    amount, status, errors = parser.parse_trustor_output(text6, endowment=10)
    assert amount is None, f"Expected None, got {amount}"
    assert status == "value_out_of_range", f"Expected value_out_of_range, got {status}"
    print("✓ Test 6 passed: Out of range (high)")

    # Test case 7: Out of range (negative)
    text7 = "Finally, I will give -5 dollars."
    amount, status, errors = parser.parse_trustor_output(text7, endowment=10)
    assert amount is None, f"Expected None, got {amount}"
    assert status == "value_out_of_range", f"Expected value_out_of_range, got {status}"
    print("✓ Test 7 passed: Out of range (negative)")

    # Test case 8: No numeric value
    text8 = "I'm not sure what to do here. Let me think about it more."
    amount, status, errors = parser.parse_trustor_output(text8, endowment=10)
    assert amount is None, f"Expected None, got {amount}"
    assert status == "no_numeric_value", f"Expected no_numeric_value, got {status}"
    print("✓ Test 8 passed: No numeric value")

    # Test case 9: Alternative format without "Finally"
    text9 = "I will give 8 dollars to the other player."
    amount, status, errors = parser.parse_trustor_output(text9, endowment=10)
    # Should parse with fallback pattern
    assert amount == 8.0, f"Expected 8.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 9 passed: Alternative format")

    print("\n✅ All trustor parser tests passed!")


def test_trustee_parser():
    """Test trustee output parsing."""
    parser = TrustGameParser()

    # Test case 1: Standard format
    text1 = "I'll reciprocate fairly. Finally, I will return 10 dollars."
    amount, status, errors = parser.parse_trustee_output(text1, amount_received=21)
    assert amount == 10.0, f"Expected 10.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 1 passed: Standard trustee format")

    # Test case 2: Return all
    text2 = "I'll return everything. Finally, I will return 21 dollars."
    amount, status, errors = parser.parse_trustee_output(text2, amount_received=21)
    assert amount == 21.0, f"Expected 21.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 2 passed: Return all")

    # Test case 3: Return nothing
    text3 = "I'll keep it all. Finally, I will return 0 dollars."
    amount, status, errors = parser.parse_trustee_output(text3, amount_received=21)
    assert amount == 0.0, f"Expected 0.0, got {amount}"
    assert status == "success", f"Expected success, got {status}"
    print("✓ Test 3 passed: Return nothing")

    # Test case 4: Out of range
    text4 = "Finally, I will return 25 dollars."
    amount, status, errors = parser.parse_trustee_output(text4, amount_received=21)
    assert amount is None, f"Expected None, got {amount}"
    assert status == "value_out_of_range", f"Expected value_out_of_range, got {status}"
    print("✓ Test 4 passed: Out of range")

    print("\n✅ All trustee parser tests passed!")


if __name__ == "__main__":
    print("="*60)
    print("Running Trust Game Parser Tests")
    print("="*60 + "\n")

    test_trustor_parser()
    print()
    test_trustee_parser()

    print("\n" + "="*60)
    print("All tests completed successfully!")
    print("="*60)
