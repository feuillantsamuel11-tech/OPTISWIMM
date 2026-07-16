from app.services.context_builder import AthleteContextBuilder
from app.services.load_analyzer import LoadAnalyzer
from app.services.session_engine.objective_selector import (
    ObjectiveSelector,
)

from app.services.decision_engine.models import (
    DecisionResult,
)


class DecisionEngine:

    def __init__(self):

        self.context_builder = AthleteContextBuilder()

        self.load_analyzer = LoadAnalyzer()

        self.objective_selector = ObjectiveSelector()

    def analyze(self, athlete_profile):

        athlete_profile = athlete_profile or {}

        athlete_state, context = (
            self.context_builder.build(
                athlete_profile=athlete_profile
            )
        )

        load = self.load_analyzer.analyze(
            athlete_profile.get(
                "recent_loads",
                []
            )
        )

        primary = (
            self.objective_selector.get_primary_objectives(
                athlete_state["specialist"]
            )
        )

        secondary = (
            self.objective_selector.get_secondary_objectives(
                athlete_state["specialist"]
            )
        )

        reasoning = [

            f"Specialist: {athlete_state['specialist']}",

            f"Load: {load.load_state}",

            f"Race distance: {athlete_state['race_distance']}"
        ]

        confidence = 0.80

        return DecisionResult(

            objectives=primary + secondary,

            constraints={},

            reasoning=reasoning,

            confidence=confidence,

            specialist=athlete_state["specialist"],

            load_state=load.load_state,
        )