"""Trust Game experiment runner."""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

from ..config import Config
from ..llm.openrouter_client import OpenRouterClient, DryRunClient
from ..personas.loader import PersonaLoader
from ..prompts.loader import PromptLoader
from ..parsing.trust_game_parser import TrustGameParser


class TrustGameRunner:
    """Run Trust Game experiments with LLM agents."""

    def __init__(self, config: Config, dry_run: bool = False):
        """Initialize runner.

        Args:
            config: Experiment configuration
            dry_run: If True, use dry-run client instead of real API calls
        """
        self.config = config
        self.dry_run = dry_run

        # Initialize components
        if dry_run:
            print("Running in DRY-RUN mode (no API calls)")
            self.llm_client = DryRunClient()
        else:
            try:
                api_key = self.config.get_api_key()
                base_url = self.config.get_base_url()
                self.llm_client = OpenRouterClient(api_key=api_key, base_url=base_url)
            except ValueError as e:
                print(f"Warning: {e}")
                print("Falling back to DRY-RUN mode")
                self.llm_client = DryRunClient()
                self.dry_run = True

        # Load personas
        personas_config = self.config.personas_config
        # Fix path: config has wrong path, use actual path
        personas_path = "data/personas/xie_53.jsonl"
        self.persona_loader = PersonaLoader(personas_path)

        # Sample personas
        self.personas = self.persona_loader.sample(
            n_sample=personas_config["n_sample"],
            strategy=personas_config.get("sampling_strategy", "sequential"),
            seed=personas_config.get("seed")
        )

        print(f"Loaded {len(self.personas)} personas")

        # Initialize prompt loader
        self.prompt_loader = PromptLoader()

        # Initialize parser
        self.parser = TrustGameParser()

        # Setup output directory
        self.output_dir = self.config.get_output_dir()
        self.config.save_resolved_config(self.output_dir)

        # Generate run ID
        self.run_id = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

        # Create episodes file
        self.episodes_file = self.output_dir / f"episodes_{self.run_id}.jsonl"
        self.episodes = []

    def run(self, limit: int = None):
        """Run all experiment episodes.

        Args:
            limit: Optional limit on number of episodes (for testing)
        """
        game_config = self.config.game_config
        sampling_config = self.config.sampling_config
        treatments = self.config.treatments

        endowment = game_config["endowment"]
        multiplier = game_config["multiplier"]
        roles = game_config.get("roles", ["trustor"])

        # Generate all conditions
        conditions = []
        for model in self.config.models:
            for framing in treatments["partner_framing"]:
                for persona in self.personas:
                    conditions.append({
                        "model": model,
                        "framing": framing,
                        "persona": persona
                    })

        total = len(conditions)
        if limit:
            conditions = conditions[:limit]
            print(f"Limited to {limit} episodes (out of {total} total)")

        print(f"Running {len(conditions)} episodes...")

        # Run each episode
        for i, condition in enumerate(conditions, 1):
            print(f"[{i}/{len(conditions)}] {condition['model']['label']} | {condition['framing']} | {condition['persona']['persona_id']}")

            episode = self._run_episode(
                model=condition["model"],
                framing=condition["framing"],
                persona=condition["persona"],
                endowment=endowment,
                multiplier=multiplier,
                temperature=sampling_config["temperature"],
                top_p=sampling_config.get("top_p"),
                max_tokens=sampling_config.get("max_tokens"),
                seed=sampling_config.get("seed"),
                max_retries=sampling_config.get("n_retries", 3),
                retry_delay=sampling_config.get("retry_delay_seconds", 1.0)
            )

            # Write episode immediately (streaming)
            self._write_episode(episode)
            self.episodes.append(episode)

        print(f"\nCompleted {len(self.episodes)} episodes")
        print(f"Episodes written to: {self.episodes_file}")

    def _run_episode(
        self,
        model: Dict,
        framing: str,
        persona: Dict,
        endowment: int,
        multiplier: int,
        temperature: float,
        top_p: float,
        max_tokens: int,
        seed: int,
        max_retries: int,
        retry_delay: float
    ) -> Dict[str, Any]:
        """Run a single episode (trustor only for MVP).

        Args:
            model: Model config dict
            framing: Partner framing treatment
            persona: Persona dict
            endowment: Trustor endowment
            multiplier: Multiplication factor
            temperature: Sampling temperature
            top_p: Nucleus sampling
            max_tokens: Max tokens
            seed: Random seed
            max_retries: Max retries
            retry_delay: Retry delay

        Returns:
            Episode record dict
        """
        episode_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat() + "Z"

        # Render trustor prompt
        trustor_prompt = self.prompt_loader.render_trustor_prompt(
            persona_text=persona["persona_text"],
            partner_framing=framing,
            endowment=endowment,
            multiplier=multiplier
        )

        # Call LLM for trustor
        messages = [{"role": "user", "content": trustor_prompt}]

        llm_response = self.llm_client.call_llm(
            messages=messages,
            model=model["model_id"],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            seed=seed,
            max_retries=max_retries,
            retry_delay=retry_delay
        )

        # Parse trustor output
        raw_text = llm_response["raw_text"]
        api_error = llm_response["error"]

        if api_error:
            # API call failed
            amount_sent = None
            parse_status = "format_error"
            parse_errors = [api_error]
            valid_trustor = False
        else:
            amount_sent, parse_status, parse_errors = self.parser.parse_trustor_output(
                raw_text=raw_text,
                endowment=endowment
            )
            valid_trustor = (parse_status == "success")

        # Calculate payoffs (trustor-only, assume nothing returned for MVP)
        # In full implementation, we'd run trustee and calculate both
        if amount_sent is not None:
            # For MVP: assume trustee returns 0 (worst case)
            trustor_payoff = endowment - amount_sent
            trustee_payoff = multiplier * amount_sent
        else:
            trustor_payoff = None
            trustee_payoff = None

        # Build episode record
        episode = {
            "experiment_id": self.config.experiment_id,
            "run_id": self.run_id,
            "episode_id": episode_id,
            "timestamp": timestamp,
            "game_params": {
                "endowment": endowment,
                "multiplier": multiplier,
                "rounds": 1
            },
            "persona": {
                "persona_id": persona["persona_id"],
                "persona_text": persona["persona_text"]
            },
            "partner_framing": framing,
            "model_info": {
                "provider": "openrouter",
                "model_id": model["model_id"],
                "temperature": temperature,
                "top_p": top_p,
                "max_tokens": max_tokens,
                "seed": seed
            },
            "prompts": {
                "trustor_prompt": trustor_prompt,
                "trustee_prompt": None,
                "prompt_version_trustor": "v001",
                "prompt_version_trustee": None
            },
            "raw_outputs": {
                "trustor_raw": raw_text,
                "trustee_raw": None
            },
            "parsed_actions": {
                "amount_sent": amount_sent,
                "amount_returned": None,
                "parse_status_trustor": parse_status,
                "parse_status_trustee": None
            },
            "payoffs": {
                "trustor_payoff": trustor_payoff,
                "trustee_payoff": trustee_payoff
            },
            "vrr_flags": {
                "valid_trustor": valid_trustor,
                "valid_trustee": None
            },
            "errors": {
                "parse_errors": parse_errors,
                "api_errors": [api_error] if api_error else []
            },
            "llm_metadata": {
                "request_id": llm_response.get("request_id"),
                "latency": llm_response.get("latency"),
                "usage": llm_response.get("usage")
            }
        }

        return episode

    def _write_episode(self, episode: Dict[str, Any]):
        """Write episode to JSONL file.

        Args:
            episode: Episode record dict
        """
        with open(self.episodes_file, 'a') as f:
            f.write(json.dumps(episode) + "\n")

    def get_episodes(self) -> List[Dict[str, Any]]:
        """Get all episodes run so far."""
        return self.episodes
