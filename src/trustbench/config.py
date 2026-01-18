"""Configuration loader and validator for TrustBench experiments."""

import hashlib
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


class Config:
    """Experiment configuration with validation."""

    def __init__(self, config_path: str):
        """Load and validate experiment config from YAML file.

        Args:
            config_path: Path to YAML config file
        """
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(self.config_path) as f:
            self.data = yaml.safe_load(f)

        self._validate()

    def _validate(self):
        """Validate required config fields."""
        required = [
            "experiment_id",
            "openrouter",
            "models",
            "personas",
            "game",
            "treatments",
            "sampling",
            "output"
        ]

        for field in required:
            if field not in self.data:
                raise ValueError(f"Missing required config field: {field}")

        # Validate openrouter
        if "api_key_env_var" not in self.data["openrouter"]:
            raise ValueError("Missing openrouter.api_key_env_var")

        # Validate models
        if not isinstance(self.data["models"], list) or len(self.data["models"]) == 0:
            raise ValueError("models must be a non-empty list")

        for model in self.data["models"]:
            if "model_id" not in model:
                raise ValueError("Each model must have model_id")

        # Validate personas
        personas = self.data["personas"]
        if "source_path" not in personas or "n_sample" not in personas:
            raise ValueError("personas must have source_path and n_sample")

        # Validate game
        game = self.data["game"]
        required_game = ["variant", "endowment", "multiplier", "rounds"]
        for field in required_game:
            if field not in game:
                raise ValueError(f"game.{field} is required")

        # Validate treatments
        if "partner_framing" not in self.data["treatments"]:
            raise ValueError("treatments.partner_framing is required")

        # Validate sampling
        if "temperature" not in self.data["sampling"]:
            raise ValueError("sampling.temperature is required")

        # Validate output
        output = self.data["output"]
        if "episodes_dir" not in output or "aggregates_dir" not in output:
            raise ValueError("output must have episodes_dir and aggregates_dir")

    def get_experiment_hash(self) -> str:
        """Generate unique hash for this experiment configuration.

        Includes: experiment_id, models, treatments, game params, and prompt versions.
        Used to create experiment_id subdirectory in results.
        """
        hash_components = [
            self.data["experiment_id"],
            str(self.data["models"]),
            str(self.data["treatments"]),
            str(self.data["game"]),
        ]

        # Add prompt versions if specified
        if "prompts" in self.data:
            hash_components.append(str(self.data["prompts"]))

        hash_string = "|".join(hash_components)
        return hashlib.sha256(hash_string.encode()).hexdigest()[:12]

    def get_output_dir(self) -> Path:
        """Get output directory for this experiment run."""
        exp_hash = self.get_experiment_hash()
        base_dir = Path("results") / exp_hash
        base_dir.mkdir(parents=True, exist_ok=True)
        return base_dir

    def save_resolved_config(self, output_dir: Path):
        """Save resolved config with computed values to output directory."""
        resolved = self.data.copy()
        resolved["_meta"] = {
            "config_path": str(self.config_path.absolute()),
            "experiment_hash": self.get_experiment_hash(),
            "output_dir": str(output_dir.absolute()),
        }

        config_out = output_dir / "config.resolved.yaml"
        with open(config_out, 'w') as f:
            yaml.dump(resolved, f, default_flow_style=False, sort_keys=False)

    def get_api_key(self) -> str:
        """Get OpenRouter API key from environment."""
        env_var = self.data["openrouter"]["api_key_env_var"]
        api_key = os.getenv(env_var)
        if not api_key:
            raise ValueError(f"Environment variable {env_var} not set")
        return api_key

    def get_base_url(self) -> str:
        """Get OpenRouter base URL."""
        return self.data["openrouter"].get("base_url", "https://openrouter.ai/api/v1")

    @property
    def experiment_id(self) -> str:
        return self.data["experiment_id"]

    @property
    def models(self) -> List[Dict[str, Any]]:
        return self.data["models"]

    @property
    def personas_config(self) -> Dict[str, Any]:
        return self.data["personas"]

    @property
    def game_config(self) -> Dict[str, Any]:
        return self.data["game"]

    @property
    def treatments(self) -> Dict[str, Any]:
        return self.data["treatments"]

    @property
    def sampling_config(self) -> Dict[str, Any]:
        return self.data["sampling"]

    @property
    def output_config(self) -> Dict[str, Any]:
        return self.data["output"]

    @property
    def human_baseline(self) -> Optional[Dict[str, Any]]:
        return self.data.get("human_baseline")
