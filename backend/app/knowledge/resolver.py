from app.knowledge.path import KnowledgePath

class KnowledgeResolver:

    def __init__(self, graph):
        self.graph = graph

    def resolve(self, objective):

        path = KnowledgePath(
            objective=objective
        )

        path.methods = self.graph.methods(objective)

        for method in path.methods:
            path.stimuli.extend(
                self.graph.stimuli(method)
            )

        for stimulus in path.stimuli:
            path.blocks.extend(
                self.graph.blocks(stimulus)
            )

        for block in path.blocks:
            path.exercises.extend(
                self.graph.exercises(block)
            )

        return path