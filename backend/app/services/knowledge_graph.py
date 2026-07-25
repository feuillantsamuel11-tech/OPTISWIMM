class KnowledgeGraph:

    def __init__(self, registry):
        self.registry = registry

    def get_objective(self, objective_id):
        ...

    def get_methods(self, objective_id):
        ...

    def get_stimuli(self, method_id):
        ...

    def get_blocks(self, stimulus_id):
        ...

    def get_exercises(self, block_id):
        ...