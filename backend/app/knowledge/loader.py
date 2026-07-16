from pathlib import Path
import yaml

from app.knowledge.base import BaseKnowledgeObject
from app.knowledge.registry import KnowledgeRegistry
from app.knowledge.validator import KnowledgeValidator


class KnowledgeLoader:

    def __init__(self, knowledge_path: Path):
        self.knowledge_path = Path(knowledge_path)

    def load(self) -> KnowledgeRegistry:

        registry = KnowledgeRegistry()

        for yaml_file in self.knowledge_path.rglob("*.yaml"):

            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            obj = BaseKnowledgeObject(**data)

            KnowledgeValidator.validate(obj)

            registry.add(obj)

        return registry