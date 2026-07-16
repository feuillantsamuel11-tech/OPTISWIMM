from pathlib import Path

from app.knowledge.loader import KnowledgeLoader


def test_loader():

    loader = KnowledgeLoader(Path("../knowledge"))

    registry = loader.load()

    assert registry.count() >= 1