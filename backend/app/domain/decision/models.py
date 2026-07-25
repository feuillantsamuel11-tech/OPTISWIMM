from dataclasses import dataclass, field

@dataclass(slots=True)
class DecisionResult:
    objectives: list[str]
    constraints: dict = field(default_factory=dict)
    reasoning: list[str] = field(default_factory=list)
    confidence: float = 0.0
    specialist: str = "unknown"
    load_state: str = "unknown"