from dataclasses import dataclass, field

@dataclass
class EngineContext:

    athlete_profile: dict

    decision = None

    knowledge_path = None

    session = None

    explanation = None

    warnings: list[str] = field(default_factory=list)

    metrics: dict = field(default_factory=dict)