from app.services.decision_engine.decision_engine import DecisionEngine
from app.knowledge.registry import KnowledgeRegistry
from app.knowledge.graph import KnowledgeGraph
from app.knowledge.resolver import KnowledgeResolver

def test_generation_pipeline():

    decision_engine = DecisionEngine()

    registry = KnowledgeRegistry()

    graph = KnowledgeGraph(registry)

    resolver = KnowledgeResolver(graph)

    athlete = {
        "race_distance": 400,
        "recent_loads": [5000] * 28,
    }

    decision = decision_engine.analyze(athlete)

    objective = decision.objectives[0]

    path = resolver.resolve(objective)

    assert decision is not None
    assert decision.objectives is not None

    assert path is not None

    