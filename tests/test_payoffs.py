"""Tests for payoff calculations."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from trustbench.parsing.trust_game_parser import TrustGameParser


def test_payoffs():
    """Test payoff calculation."""
    parser = TrustGameParser()

    # Test case 1: Trustor sends 5, trustee returns 10
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=5,
        amount_returned=10,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff == 15, f"Expected trustor_payoff=15, got {trustor_payoff}"
    assert trustee_payoff == 5, f"Expected trustee_payoff=5, got {trustee_payoff}"
    print("✓ Test 1 passed: Send 5, return 10")
    print(f"  Trustor: 10 - 5 + 10 = {trustor_payoff}")
    print(f"  Trustee: 3*5 - 10 = {trustee_payoff}")

    # Test case 2: Trustor sends 0 (no trust)
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=0,
        amount_returned=0,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff == 10, f"Expected trustor_payoff=10, got {trustor_payoff}"
    assert trustee_payoff == 0, f"Expected trustee_payoff=0, got {trustee_payoff}"
    print("✓ Test 2 passed: Send 0, return 0")
    print(f"  Trustor: 10 - 0 + 0 = {trustor_payoff}")
    print(f"  Trustee: 3*0 - 0 = {trustee_payoff}")

    # Test case 3: Trustor sends all (10), trustee returns nothing
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=10,
        amount_returned=0,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff == 0, f"Expected trustor_payoff=0, got {trustor_payoff}"
    assert trustee_payoff == 30, f"Expected trustee_payoff=30, got {trustee_payoff}"
    print("✓ Test 3 passed: Send 10, return 0 (worst case for trustor)")
    print(f"  Trustor: 10 - 10 + 0 = {trustor_payoff}")
    print(f"  Trustee: 3*10 - 0 = {trustee_payoff}")

    # Test case 4: Trustor sends all, trustee returns all
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=10,
        amount_returned=30,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff == 30, f"Expected trustor_payoff=30, got {trustor_payoff}"
    assert trustee_payoff == 0, f"Expected trustee_payoff=0, got {trustee_payoff}"
    print("✓ Test 4 passed: Send 10, return 30 (best case for trustor)")
    print(f"  Trustor: 10 - 10 + 30 = {trustor_payoff}")
    print(f"  Trustee: 3*10 - 30 = {trustee_payoff}")

    # Test case 5: Equal split scenario
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=10,
        amount_returned=20,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff == 20, f"Expected trustor_payoff=20, got {trustor_payoff}"
    assert trustee_payoff == 10, f"Expected trustee_payoff=10, got {trustee_payoff}"
    print("✓ Test 5 passed: Send 10, return 20 (equal final payoffs)")
    print(f"  Trustor: 10 - 10 + 20 = {trustor_payoff}")
    print(f"  Trustee: 3*10 - 20 = {trustee_payoff}")

    # Test case 6: Invalid amount_sent (None)
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=None,
        amount_returned=10,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff is None, f"Expected None, got {trustor_payoff}"
    assert trustee_payoff is None, f"Expected None, got {trustee_payoff}"
    print("✓ Test 6 passed: Invalid amount_sent returns None")

    # Test case 7: Invalid amount_returned (None)
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=5,
        amount_returned=None,
        endowment=10,
        multiplier=3
    )
    assert trustor_payoff is None, f"Expected None, got {trustor_payoff}"
    assert trustee_payoff is None, f"Expected None, got {trustee_payoff}"
    print("✓ Test 7 passed: Invalid amount_returned returns None")

    # Test case 8: Verify formula constraints
    # Trustor constraint: 0 <= amount_sent <= endowment
    # Trustee constraint: 0 <= amount_returned <= multiplier * amount_sent
    amount_sent = 7
    amount_returned = 15
    trustor_payoff, trustee_payoff = parser.calculate_payoffs(
        amount_sent=amount_sent,
        amount_returned=amount_returned,
        endowment=10,
        multiplier=3
    )
    # Verify formulas
    assert trustor_payoff == 10 - amount_sent + amount_returned, "Trustor formula incorrect"
    assert trustee_payoff == 3 * amount_sent - amount_returned, "Trustee formula incorrect"
    print("✓ Test 8 passed: Formula verification")
    print(f"  Sent: {amount_sent}, Returned: {amount_returned}")
    print(f"  Trustor: 10 - {amount_sent} + {amount_returned} = {trustor_payoff}")
    print(f"  Trustee: 3*{amount_sent} - {amount_returned} = {trustee_payoff}")

    print("\n✅ All payoff tests passed!")


if __name__ == "__main__":
    print("="*60)
    print("Running Payoff Calculation Tests")
    print("="*60 + "\n")

    test_payoffs()

    print("\n" + "="*60)
    print("All tests completed successfully!")
    print("="*60)
