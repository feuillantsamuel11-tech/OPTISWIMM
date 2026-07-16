from dataclasses import dataclass, field

@dataclass
class Explanation:

    summary: str

    reasoning: list[str]

    confidence: float

    details: dict = field(default_factory=dict)