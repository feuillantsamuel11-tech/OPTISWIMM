from typing import Dict, List

from app.knowledge.base import BaseKnowledgeObject


class KnowledgeRegistry:
    """
    Central registry for every knowledge object.
    """

    def __init__(self):
        self._objects: Dict[str, BaseKnowledgeObject] = {}

    def add(self, obj: BaseKnowledgeObject) -> None:
        """Add a knowledge object to the registry."""
        if obj.id in self._objects:
            raise ValueError(f"Object '{obj.id}' already exists.")

        self._objects[obj.id] = obj

    def get(self, object_id: str) -> BaseKnowledgeObject:
        """Return a knowledge object."""
        return self._objects[object_id]

    def exists(self, object_id: str) -> bool:
        """Check if an object exists."""
        return object_id in self._objects

    def all(self) -> List[BaseKnowledgeObject]:
        """Return all registered objects."""
        return list(self._objects.values())

    def count(self) -> int:
        """Return the number of registered objects."""
        return len(self._objects)

    def get_many(
        self,
        object_ids: list[str]
    ) -> list[BaseKnowledgeObject]:

        return [
            self.get(object_id)
            for object_id in object_ids
            if self.exists(object_id)
        ]     
    def find_by_category(
        self,
        category: str
    ) -> list[BaseKnowledgeObject]:

        return [
        obj
        for obj in self._objects.values()
        if obj.category == category
    ]

    def find_by_type(
        self,
        knowledge_type: str
    ) -> list[BaseKnowledgeObject]:

        return [
            obj
            for obj in self._objects.values()
            if obj.type == knowledge_type
        ]

    def search(
        self,
        tag: str
    ) -> list[BaseKnowledgeObject]:

        return [
            obj
            for obj in self._objects.values()
            if tag in obj.tags
        ]    
            

