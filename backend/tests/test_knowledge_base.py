from app.knowledge.base import BaseKnowledgeObject


def test_create_knowledge_object():
    obj = BaseKnowledgeObject(
        id="TEST-001",
        name="Test Object",
        type="objective",
        category="physiology",
    )

    assert obj.id == "TEST-001"
    assert obj.status == "draft"
    assert obj.version == "1.0.0"