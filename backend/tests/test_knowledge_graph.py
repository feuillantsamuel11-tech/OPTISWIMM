from app.knowledge.graph import KnowledgeGraph
from app.knowledge.registry import KnowledgeRegistry
from app.knowledge.base import BaseKnowledgeObject


def test_graph_get():

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

    obj = graph.get("DO-003")

    assert obj.id == "DO-003"

def test_graph_follow_empty():

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

    assert graph.methods(graph.get("DO-003")) == []