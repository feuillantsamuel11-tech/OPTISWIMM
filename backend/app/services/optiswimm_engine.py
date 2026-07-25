from app.services.decision_engine.decision_engine import DecisionEngine

from app.services.intelligent_session_builder_v10 import (
    IntelligentSessionBuilder,
)

from app.knowledge.registry import KnowledgeRegistry
from app.knowledge.graph import KnowledgeGraph
from app.knowledge.resolver import KnowledgeResolver

from app.models.generation_result import GenerationResult
from app.services.explainability.explanation_engine import (
    ExplanationEngine,
)
class OptiSwimmEngine:

    def __init__(self):

        self.decision_engine = DecisionEngine()
        self.explanation_engine = ExplanationEngine()

        self.registry = KnowledgeRegistry()

        self.graph = KnowledgeGraph(self.registry)

        self.resolver = KnowledgeResolver(self.graph)

        self.session_builder = IntelligentSessionBuilder()

    def generate(self, profile: dict) -> GenerationResult:
        decision = self.decision_engine.analyze(profile)

        objective = decision.objectives[0]

        path = self.resolver.resolve(objective)

        session = self.session_builder.build_session(
            athlete=profile,
            readiness="normal",
        )
        
        explanation = self.explanation_engine.build(
            decision=decision,
            knowledge_path=path,
            session=session,
        )

        return GenerationResult(
            session=session,
            decision=decision,
            knowledge_path=path,
            explanation=explanation,
        ) 