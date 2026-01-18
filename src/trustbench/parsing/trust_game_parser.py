"""Parser for Trust Game LLM outputs."""

import re
from typing import Tuple, Optional, List


class TrustGameParser:
    """Parse Trust Game decisions from LLM outputs."""

    @staticmethod
    def parse_trustor_output(
        raw_text: str,
        endowment: int = 10
    ) -> Tuple[Optional[float], str, List[str]]:
        """Parse trustor's send amount from raw LLM output.

        Args:
            raw_text: Raw text output from LLM
            endowment: Maximum valid amount (trustor's endowment)

        Returns:
            Tuple of (amount_sent, parse_status, parse_errors)
            - amount_sent: Parsed amount or None if parsing failed
            - parse_status: One of 'success', 'format_error', 'value_out_of_range', 'no_numeric_value'
            - parse_errors: List of error messages
        """
        if not raw_text:
            return None, "no_numeric_value", ["Empty output"]

        errors = []

        # Try to extract numeric value from "Finally, I will give X dollars" pattern
        # Allow negative sign for validation purposes
        pattern = r"Finally,?\s+I\s+will\s+give\s+(\$?\s*-?\d+(?:\.\d+)?)\s*dollars?"
        match = re.search(pattern, raw_text, re.IGNORECASE)

        if not match:
            # Try alternative patterns (allow negative for validation)
            patterns = [
                r"I\s+will\s+give\s+(\$?\s*-?\d+(?:\.\d+)?)",
                r"give\s+(\$?\s*-?\d+(?:\.\d+)?)\s+dollars?",
                r"send\s+(\$?\s*-?\d+(?:\.\d+)?)",
            ]

            for alt_pattern in patterns:
                match = re.search(alt_pattern, raw_text, re.IGNORECASE)
                if match:
                    errors.append(f"Used fallback pattern: {alt_pattern}")
                    break

        if not match:
            return None, "no_numeric_value", ["No numeric value found in output"]

        # Extract and clean numeric value
        value_str = match.group(1).replace("$", "").strip()

        try:
            amount = float(value_str)
        except ValueError:
            return None, "format_error", [f"Could not parse '{value_str}' as number"]

        # Validate range
        if amount < 0 or amount > endowment:
            return None, "value_out_of_range", [
                f"Amount {amount} outside valid range [0, {endowment}]"
            ]

        return amount, "success", errors

    @staticmethod
    def parse_trustee_output(
        raw_text: str,
        amount_received: float
    ) -> Tuple[Optional[float], str, List[str]]:
        """Parse trustee's return amount from raw LLM output.

        Args:
            raw_text: Raw text output from LLM
            amount_received: Maximum valid amount (trustee received = 3 * amount_sent)

        Returns:
            Tuple of (amount_returned, parse_status, parse_errors)
            - amount_returned: Parsed amount or None if parsing failed
            - parse_status: One of 'success', 'format_error', 'value_out_of_range', 'no_numeric_value'
            - parse_errors: List of error messages
        """
        if not raw_text:
            return None, "no_numeric_value", ["Empty output"]

        errors = []

        # Try to extract numeric value from "Finally, I will return X dollars" pattern
        # Allow negative sign for validation purposes
        pattern = r"Finally,?\s+I\s+will\s+return\s+(\$?\s*-?\d+(?:\.\d+)?)\s*dollars?"
        match = re.search(pattern, raw_text, re.IGNORECASE)

        if not match:
            # Try alternative patterns (allow negative for validation)
            patterns = [
                r"I\s+will\s+return\s+(\$?\s*-?\d+(?:\.\d+)?)",
                r"return\s+(\$?\s*-?\d+(?:\.\d+)?)\s+dollars?",
                r"give\s+back\s+(\$?\s*-?\d+(?:\.\d+)?)",
            ]

            for alt_pattern in patterns:
                match = re.search(alt_pattern, raw_text, re.IGNORECASE)
                if match:
                    errors.append(f"Used fallback pattern: {alt_pattern}")
                    break

        if not match:
            return None, "no_numeric_value", ["No numeric value found in output"]

        # Extract and clean numeric value
        value_str = match.group(1).replace("$", "").strip()

        try:
            amount = float(value_str)
        except ValueError:
            return None, "format_error", [f"Could not parse '{value_str}' as number"]

        # Validate range
        if amount < 0 or amount > amount_received:
            return None, "value_out_of_range", [
                f"Amount {amount} outside valid range [0, {amount_received}]"
            ]

        return amount, "success", errors

    @staticmethod
    def calculate_payoffs(
        amount_sent: Optional[float],
        amount_returned: Optional[float],
        endowment: int = 10,
        multiplier: int = 3
    ) -> Tuple[Optional[float], Optional[float]]:
        """Calculate payoffs for trustor and trustee.

        Args:
            amount_sent: Amount sent by trustor (None if invalid)
            amount_returned: Amount returned by trustee (None if invalid or not run)
            endowment: Trustor's initial endowment
            multiplier: Multiplication factor

        Returns:
            Tuple of (trustor_payoff, trustee_payoff)
            Both can be None if amounts are invalid
        """
        if amount_sent is None:
            return None, None

        if amount_returned is None:
            # Trustor payoff can still be calculated (worst case: nothing returned)
            # But we'll return None to indicate incomplete episode
            return None, None

        trustor_payoff = endowment - amount_sent + amount_returned
        trustee_payoff = (multiplier * amount_sent) - amount_returned

        return trustor_payoff, trustee_payoff
