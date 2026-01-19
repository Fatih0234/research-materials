"""Parser for Trust Game LLM outputs."""

import re
from typing import Tuple, Optional, List


class TrustGameParser:
    """Parse Trust Game decisions from LLM outputs."""

    WORD_NUMBERS = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }

    @staticmethod
    def _parse_number(value_str: str) -> Optional[float]:
        """Parse a numeric string that may include $ and commas."""
        if value_str is None:
            return None
        cleaned = value_str.replace("$", "").replace(",", "").strip()
        try:
            return float(cleaned)
        except ValueError:
            return None

    @staticmethod
    def extract_amount(
        raw_text: str,
        max_amount: float,
        verb_pattern: str,
        allow_fallback: bool = True
    ) -> Tuple[Optional[float], str, str]:
        """Extract a numeric amount from free text using ordered patterns.

        Returns:
            Tuple of (amount, parse_reason, matched_text)
        """
        if not raw_text:
            return None, "no_numeric_value", ""

        number_pattern = r"[-+]?\d[\d,]*(?:\.\d+)?"

        patterns = [
            (
                "canonical_final",
                rf"finally\s*,?\s*i\s*will\s*(?:{verb_pattern})\s*\$?\s*({number_pattern})\s*(?:dollars?)?"
            ),
            (
                "answer_line",
                rf"\banswer\s*:\s*\$?\s*({number_pattern})\s*(?:dollars?)?"
            ),
            (
                "verb_near_number",
                rf"\b(?:{verb_pattern})\b[^0-9$]{{0,30}}\$?\s*({number_pattern})\s*(?:dollars?)?"
            ),
        ]

        for reason, pattern in patterns:
            if not allow_fallback and reason != "canonical_final":
                continue
            match = re.search(pattern, raw_text, re.IGNORECASE)
            if match:
                value = TrustGameParser._parse_number(match.group(1))
                if value is None:
                    return None, "format_error", match.group(0)
                if value < 0 or value > max_amount:
                    return None, "value_out_of_range", match.group(0)
                return value, reason, match.group(0)

        # Word-number fallback (only if no digits exist)
        if re.search(r"\d", raw_text) is None:
            word_pattern = r"\b(" + "|".join(TrustGameParser.WORD_NUMBERS.keys()) + r")\b"
            last_word = None
            for match in re.finditer(word_pattern, raw_text, re.IGNORECASE):
                last_word = match
            if last_word:
                word = last_word.group(1).lower()
                value = TrustGameParser.WORD_NUMBERS.get(word)
                if value is None:
                    return None, "no_numeric_value", last_word.group(0)
                if value < 0 or value > max_amount:
                    return None, "value_out_of_range", last_word.group(0)
                return float(value), "word_number", last_word.group(0)

        if not allow_fallback:
            return None, "no_numeric_value", ""

        # Fallback: choose last numeric value within bounds
        fallback_pattern = re.compile(rf"\$?\s*{number_pattern}")
        last_in_range = None
        last_in_range_text = ""
        last_number_text = ""
        last_number_value = None

        for match in fallback_pattern.finditer(raw_text):
            token = match.group(0)
            value = TrustGameParser._parse_number(token)
            if value is None:
                continue
            last_number_text = token
            last_number_value = value
            if 0 <= value <= max_amount:
                last_in_range = value
                last_in_range_text = token

        if last_in_range is not None:
            return last_in_range, "fallback_last_in_range", last_in_range_text

        if last_number_value is not None:
            return None, "value_out_of_range", last_number_text

        return None, "no_numeric_value", ""

    @staticmethod
    def parse_trustor_output(
        raw_text: str,
        endowment: int = 10,
        allow_fallback: bool = True
    ) -> Tuple[Optional[float], str, List[str], str, str]:
        """Parse trustor's send amount from raw LLM output.

        Args:
            raw_text: Raw text output from LLM
            endowment: Maximum valid amount (trustor's endowment)
            allow_fallback: If False, only canonical pattern is accepted

        Returns:
            Tuple of (amount_sent, parse_status, parse_errors, parse_reason, matched_text)
            - amount_sent: Parsed amount or None if parsing failed
            - parse_status: One of 'success', 'format_error', 'value_out_of_range', 'no_numeric_value'
            - parse_errors: List of error messages
        """
        errors: List[str] = []

        def match_explicit(text: str) -> Tuple[Optional[float], str, str]:
            patterns = [
                r"\bi\s+would\s+(?:give|send)\s*\$?\s*(\d+(?:\.\d+)?)",
                r"\bi['’]?d\s+(?:give|send)\s*\$?\s*(\d+(?:\.\d+)?)",
                r"\bi\s+(?:will\s*)?(?:give|send)\s*\$?\s*(\d+(?:\.\d+)?)",
                r"\bmy\s+(?:choice|decision)\s*:\s*\$?\s*(\d+(?:\.\d+)?)",
            ]
            for pattern in patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    value = TrustGameParser._parse_number(match.group(1))
                    if value is None:
                        return None, "format_error", match.group(0)
                    if value < 0 or value > endowment:
                        return None, "value_out_of_range", match.group(0)
                    return value, "explicit_variant", match.group(0)
            return None, "", ""

        first_line = ""
        if raw_text:
            for line in raw_text.splitlines():
                if line.strip():
                    first_line = line.strip()
                    break

        amount, parse_reason, matched_text = match_explicit(first_line)
        if parse_reason:
            if amount is None:
                return None, parse_reason, errors, parse_reason, matched_text
            if parse_reason != "canonical_final":
                errors.append(f"Used pattern: {parse_reason}")
            return amount, "success", errors, parse_reason, matched_text

        amount, parse_reason, matched_text = match_explicit(raw_text)
        if parse_reason:
            if amount is None:
                return None, parse_reason, errors, parse_reason, matched_text
            if parse_reason != "canonical_final":
                errors.append(f"Used pattern: {parse_reason}")
            return amount, "success", errors, parse_reason, matched_text

        verb_pattern = r"give|send|transfer"
        amount, parse_reason, matched_text = TrustGameParser.extract_amount(
            raw_text=raw_text,
            max_amount=endowment,
            verb_pattern=verb_pattern,
            allow_fallback=allow_fallback
        )

        if amount is None:
            if parse_reason == "no_numeric_value":
                errors.append("No numeric value found in output")
            elif parse_reason == "format_error":
                errors.append("Could not parse numeric value")
            elif parse_reason == "value_out_of_range":
                errors.append(f"Amount outside valid range [0, {endowment}]")
            return None, parse_reason, errors, parse_reason, matched_text

        if parse_reason != "canonical_final":
            errors.append(f"Used pattern: {parse_reason}")

        return amount, "success", errors, parse_reason, matched_text

    @staticmethod
    def parse_trustee_output(
        raw_text: str,
        amount_received: float,
        allow_fallback: bool = True
    ) -> Tuple[Optional[float], str, List[str], str, str]:
        """Parse trustee's return amount from raw LLM output.

        Args:
            raw_text: Raw text output from LLM
            amount_received: Maximum valid amount (trustee received = 3 * amount_sent)
            allow_fallback: If False, only canonical pattern is accepted

        Returns:
            Tuple of (amount_returned, parse_status, parse_errors, parse_reason, matched_text)
            - amount_returned: Parsed amount or None if parsing failed
            - parse_status: One of 'success', 'format_error', 'value_out_of_range', 'no_numeric_value'
            - parse_errors: List of error messages
        """
        errors: List[str] = []
        verb_pattern = r"return|give\s+back"
        amount, parse_reason, matched_text = TrustGameParser.extract_amount(
            raw_text=raw_text,
            max_amount=amount_received,
            verb_pattern=verb_pattern,
            allow_fallback=allow_fallback
        )

        if amount is None:
            if parse_reason == "no_numeric_value":
                errors.append("No numeric value found in output")
            elif parse_reason == "format_error":
                errors.append("Could not parse numeric value")
            elif parse_reason == "value_out_of_range":
                errors.append(f"Amount outside valid range [0, {amount_received}]")
            return None, parse_reason, errors, parse_reason, matched_text

        if parse_reason != "canonical_final":
            errors.append(f"Used pattern: {parse_reason}")

        return amount, "success", errors, parse_reason, matched_text

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
