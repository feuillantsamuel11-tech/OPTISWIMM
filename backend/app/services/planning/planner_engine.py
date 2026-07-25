from types import SimpleNamespace

from .planner_models import BlockPlan, SessionPlan
from .planner_rules import PLANNING_RULES


class PlannerEngine:

    def generate(self, volume, decision=None):

        if decision is None:
            decision = SimpleNamespace(
                specialist="",
                objectives=[],
            )

        profile = self._select_profile(decision)

        rules = PLANNING_RULES[profile]

        blocks = []

        for name, ratio, zone in rules:

            blocks.append(
                BlockPlan(
                    name=name,
                    volume=int(volume * ratio),
                    zone=zone,
                    objective=decision.objectives[0] if decision.objectives else "",
                )
            )

        return SessionPlan(
            total_volume=volume,
            blocks=blocks,
        )

    def _select_profile(self, decision):

        specialist = getattr(decision, "specialist", "")

        if specialist == "sprinter":
            return "sprint"

        return "default"