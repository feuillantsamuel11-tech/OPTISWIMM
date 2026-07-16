from dataclasses import dataclass, field
from typing import Any

from app.knowledge.path import KnowledgePath
from app.services.decision_engine.models import DecisionResult


@dataclass
class GenerationResult:
    session: Any
    decision: DecisionResult
    knowledge_path: KnowledgePath

    explanation: Any | None = None

    warnings: list[str] = field(default_factory=list)

    metrics: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)