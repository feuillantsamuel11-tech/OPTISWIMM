from app.knowledge.registry import KnowledgeRegistry
from app.knowledge.base import BaseKnowledgeObject


def test_find_by_category():

    registry = KnowledgeRegistry()

    registry.add(
        BaseKnowledgeObject(
            id="A",
            name="Threshold",
            type="objective",
            category="training",
        )
    )

    registry.add(
        BaseKnowledgeObject(
            id="B",
            name="VO2",
            type="objective",
            category="training",
        )
    )

    result = registry.find_by_category("training")

    assert len(result) == 2