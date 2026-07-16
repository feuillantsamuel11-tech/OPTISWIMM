from app.knowledge.resolver import KnowledgeResolver
from app.knowledge.graph import KnowledgeGraph
from app.knowledge.registry import KnowledgeRegistry
from app.knowledge.base import BaseKnowledgeObject

def test_resolver():
    registry = KnowledgeRegistry()

    registry.add(
        BaseKnowledgeObject(
            id="DO-003",
            name="Threshold",
            type="objective",
            category="training",
        )
    )

    graph = KnowledgeGraph(registry)
    resolver = KnowledgeResolver(graph)

    objective = graph.get("DO-003")
    path = resolver.resolve(objective)

    assert path.objective.id == "DO-003"