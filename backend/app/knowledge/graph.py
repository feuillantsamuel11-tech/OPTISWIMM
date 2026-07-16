from app.knowledge.registry import KnowledgeRegistry


class KnowledgeGraph:

    def __init__(self, registry: KnowledgeRegistry):
        self.registry = registry

    def get(self, object_id: str):
        return self.registry.get(object_id)

    def follow(self, source, relation: str):
        ids = getattr(source, relation, [])

        if not ids:
            return []

        return self.registry.get_many(ids)

    def methods(self, objective):
        return self.follow(
            objective,
            "recommended_methods"
        )

    def stimuli(self, method):
        return self.follow(
            method,
            "stimuli"
        )

    def blocks(self, stimulus):
        return self.follow(
            stimulus,
            "recommended_blocks"
        )

    def exercises(self, block):
        return self.follow(
            block,
            "recommended_exercises"
        )