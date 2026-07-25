from .planner_engine import PlannerEngine


class Planner:

    def __init__(self):
        self.engine = PlannerEngine()

    def generate(
        self,
        volume,
        decision=None,
    ):
        return self.engine.generate(
            volume,
            decision,
        )