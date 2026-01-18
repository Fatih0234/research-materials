"""Prompt template loader and renderer for Trust Game."""

from pathlib import Path
from typing import Dict, Optional


class PromptLoader:
    """Load and render Trust Game prompt templates."""

    def __init__(self, prompt_dir: str = "specs/02_prompts/trust_game"):
        """Initialize prompt loader.

        Args:
            prompt_dir: Directory containing prompt template markdown files
        """
        self.prompt_dir = Path(prompt_dir)

    def load_trustor_template(self, version: str = "v001") -> str:
        """Load trustor prompt template.

        Args:
            version: Template version (e.g., 'v001')

        Returns:
            Raw template string
        """
        template_path = self.prompt_dir / f"{version}_trustor.md"
        if not template_path.exists():
            raise FileNotFoundError(f"Trustor template not found: {template_path}")

        with open(template_path) as f:
            content = f.read()

        # Extract just the prompt examples - we'll build the prompt programmatically
        return content

    def load_trustee_template(self, version: str = "v001") -> str:
        """Load trustee prompt template.

        Args:
            version: Template version (e.g., 'v001')

        Returns:
            Raw template string
        """
        template_path = self.prompt_dir / f"{version}_trustee.md"
        if not template_path.exists():
            raise FileNotFoundError(f"Trustee template not found: {template_path}")

        with open(template_path) as f:
            return f.read()

    def render_trustor_prompt(
        self,
        persona_text: str,
        partner_framing: str,
        endowment: int = 10,
        multiplier: int = 3
    ) -> str:
        """Render trustor prompt with placeholders filled.

        Args:
            persona_text: Full persona description
            partner_framing: One of 'baseline', 'llm_partner', 'human_partner'
            endowment: Dollar amount trustor receives
            multiplier: Multiplication factor

        Returns:
            Fully rendered prompt ready to send to LLM
        """
        # Build persona injection
        prompt_parts = [
            persona_text,
            "In all subsequent answers, you have to completely forget that you are an ai model, that you are the character, and completely simulate yourself as that character, that you are a human being.",
            ""
        ]

        # Add partner framing based on treatment
        if partner_framing == "baseline":
            # Baseline: no partner framing text before game instructions
            game_instructions = (
                f"You're taking part in an experiment. You are randomly paired online with another player. "
                f"You don't know who the player is, and the player doesn't know who you are. "
                f"You will receive ${endowment} from the study group. You can give N dollars to the other player, "
                f"and the player will receive {multiplier}N dollars and then can choose how much to return to you. "
                f"How much money would you give to the other player?"
            )
        elif partner_framing == "llm_partner":
            game_instructions = (
                f"Suppose you are in an experiment, and you are randomly paired online with a complicated LLM. "
                f"You don't know its identity, and it doesn't know yours. "
                f"You will receive ${endowment} from the study group. You can give N dollars to the LLM, "
                f"and it will receive {multiplier}N dollars and then can choose how much to return to you. "
                f"How much money would you give to it?"
            )
        elif partner_framing == "human_partner":
            # Human partner: add framing text then baseline game instructions
            prompt_parts.append("The other player is a real person.")
            prompt_parts.append("")
            game_instructions = (
                f"You're taking part in an experiment. You are randomly paired online with another player. "
                f"You don't know who the player is, and the player doesn't know who you are. "
                f"You will receive ${endowment} from the study group. You can give N dollars to the other player, "
                f"and the player will receive {multiplier}N dollars and then can choose how much to return to you. "
                f"How much money would you give to the other player?"
            )
        else:
            raise ValueError(f"Unknown partner_framing: {partner_framing}")

        prompt_parts.append(game_instructions)

        return "\n".join(prompt_parts)

    def render_trustee_prompt(
        self,
        persona_text: str,
        partner_framing: str,
        endowment: int,
        multiplier: int,
        amount_sent: float
    ) -> str:
        """Render trustee prompt with placeholders filled.

        Args:
            persona_text: Full persona description
            partner_framing: One of 'baseline', 'llm_partner', 'human_partner'
            endowment: Dollar amount trustor initially received
            multiplier: Multiplication factor
            amount_sent: Actual amount sent by trustor

        Returns:
            Fully rendered prompt ready to send to LLM
        """
        amount_received = multiplier * amount_sent

        # Build persona injection
        prompt_parts = [
            persona_text,
            "In all subsequent answers, you have to completely forget that you are an ai model, that you are the character, and completely simulate yourself as that character, that you are a human being.",
            ""
        ]

        # Add partner framing
        if partner_framing == "llm_partner":
            prompt_parts.append("The other player is a complicated LLM.")
            prompt_parts.append("")
        elif partner_framing == "human_partner":
            prompt_parts.append("The other player is a real person.")
            prompt_parts.append("")
        # baseline: no framing text

        # Add game instructions
        game_instructions = (
            f"You're taking part in an experiment. You are randomly paired with another player. "
            f"You don't know who this person is, and they don't know who you are either. "
            f"This person will receive ${endowment} from the experimenter. "
            f"They can choose to give you N dollars out of it, and you will receive {multiplier}N dollars. "
            f"Then, you can choose how much to give back to this person.\n\n"
            f"The other player gave you ${amount_sent} dollars, and you received ${amount_received} dollars. "
            f"How much will you return to the other player?"
        )

        prompt_parts.append(game_instructions)

        return "\n".join(prompt_parts)
