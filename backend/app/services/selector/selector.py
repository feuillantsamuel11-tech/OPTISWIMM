from .selector_engine import SelectorEngine


class ExerciseSelector:

    def __init__(self):
        self.engine = SelectorEngine()

    def select(self, block):
        return self.engine.select(block)