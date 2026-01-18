"""Persona loader and sampler."""

import json
from pathlib import Path
from typing import List, Dict, Any


class PersonaLoader:
    """Load and sample personas from JSONL file."""

    def __init__(self, personas_path: str):
        """Initialize persona loader.

        Args:
            personas_path: Path to JSONL file containing personas
        """
        self.personas_path = Path(personas_path)
        if not self.personas_path.exists():
            raise FileNotFoundError(f"Personas file not found: {personas_path}")

        self.personas = self._load_personas()

    def _load_personas(self) -> List[Dict[str, Any]]:
        """Load all personas from JSONL file."""
        personas = []
        with open(self.personas_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    personas.append(json.loads(line))

        if not personas:
            raise ValueError(f"No personas found in {self.personas_path}")

        # Validate required fields
        for i, persona in enumerate(personas):
            if "persona_id" not in persona:
                raise ValueError(f"Persona {i} missing persona_id")
            if "persona_text" not in persona:
                raise ValueError(f"Persona {i} missing persona_text")

        return personas

    def sample(
        self,
        n_sample: int,
        strategy: str = "sequential",
        seed: int = None
    ) -> List[Dict[str, Any]]:
        """Sample personas according to strategy.

        Args:
            n_sample: Number of personas to sample
            strategy: Sampling strategy ('sequential', 'random', 'stratified')
            seed: Random seed (only used for random/stratified)

        Returns:
            List of sampled personas
        """
        if n_sample > len(self.personas):
            print(f"Warning: Requested {n_sample} personas but only {len(self.personas)} available. Using all.")
            n_sample = len(self.personas)

        if strategy == "sequential":
            # Take first n_sample personas
            return self.personas[:n_sample]

        elif strategy == "random":
            # Random sampling with optional seed
            import random
            if seed is not None:
                random.seed(seed)
            return random.sample(self.personas, n_sample)

        elif strategy == "stratified":
            # For MVP, stratified is same as sequential
            # In future, could stratify by demographics if available
            print("Warning: stratified sampling not implemented, using sequential")
            return self.personas[:n_sample]

        else:
            raise ValueError(f"Unknown sampling strategy: {strategy}")

    def __len__(self) -> int:
        """Number of personas available."""
        return len(self.personas)
