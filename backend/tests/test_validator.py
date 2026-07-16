import pytest

from app.knowledge.base import BaseKnowledgeObject
from app.knowledge.validator import KnowledgeValidator


def test_validator_accepts_valid_object():

    obj = BaseKnowledgeObject(
        id="DO-001",
        name="Develop VO2max",
        type="objective",
        category="physiology",
    )

    KnowledgeValidator.validate(obj)


def test_validator_rejects_empty_id():

    obj = BaseKnowledgeObject(
        id="",
        name="Develop VO2max",
        type="objective",
        category="physiology",
    )

    with pytest.raises(ValueError):

        KnowledgeValidator.validate(obj)