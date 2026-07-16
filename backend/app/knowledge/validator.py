from app.knowledge.base import BaseKnowledgeObject


class KnowledgeValidator:

    @staticmethod
    def validate(obj: BaseKnowledgeObject) -> None:

        if not obj.id.strip():
            raise ValueError("Knowledge object ID cannot be empty.")

        if not obj.name.strip():
            raise ValueError("Knowledge object name cannot be empty.")

        if not obj.type.strip():
            raise ValueError("Knowledge object type cannot be empty.")

        if not obj.category.strip():
            raise ValueError("Knowledge object category cannot be empty.")