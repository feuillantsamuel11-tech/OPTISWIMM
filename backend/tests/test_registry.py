from app.knowledge.base import BaseKnowledgeObject
from app.knowledge.registry import KnowledgeRegistry


def test_registry_add_and_get():
    registry = KnowledgeRegistry()

    obj = BaseKnowledgeObject(
        id="TEST-001",
        name="VO2 Development",
        type="objective",
        category="physiology",
    )

    registry.add(obj)

    assert registry.exists("TEST-001")
    assert registry.count() == 1
    assert registry.get("TEST-001").name == "VO2 Development"


def test_registry_duplicate():
    registry = KnowledgeRegistry()

    obj = BaseKnowledgeObject(
        id="TEST-001",
        name="VO2 Development",
        type="objective",
        category="physiology",
    )

    registry.add(obj)

    try:
        registry.add(obj)
        assert False
    except ValueError:
        assert True