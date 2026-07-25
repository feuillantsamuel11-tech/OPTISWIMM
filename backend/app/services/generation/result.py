from dataclasses import dataclass
from typing import Any


@dataclass
class GenerationResult:

    session: Any

    validation: Any

    explanation: Any

    decision: Any

    planner: Any