from app.domain.training_context import TrainingContext
from app.services.race_distance_engine import RaceDistanceEngine
from app.services.session_engine.specialist_manager import SpecialistManager


class AthleteContextBuilder:
    """
    Construit un TrainingContext à partir des informations
    du nageur et des paramètres de la séance.
    """

    def __init__(self):

        self.race_distance_engine = RaceDistanceEngine()
        self.specialist_manager = SpecialistManager()

    def build(

        self,

        athlete_profile=None,

        readiness_inputs=None,

        previous_sessions=None,

        current_block=None,

        target_competition=None,

        **kwargs

    ):

        athlete_profile = athlete_profile or {}
        readiness_inputs = readiness_inputs or {}

        athlete_state = dict(athlete_profile)

        athlete_state.update(readiness_inputs)
        athlete_state.update(kwargs)

        race_distance = athlete_state.get(
            "race_distance",
            400
        )

        distance_profile = (
            self.race_distance_engine.get_distance_profile(
                race_distance
            )
        )

        profile = self.specialist_manager.build_profile(
            athlete_state
        )

        context = TrainingContext(

            objective=athlete_state.get("objective"),

            race_distance=race_distance,

            specialist=profile["specialist"],

            level=athlete_state.get("level"),

            previous_block=current_block,
        )

        athlete_state["specialist"] = profile["specialist"]

        athlete_state["distance_focus"] = (
            athlete_state.get(
                "distance_focus",
                distance_profile["focus"]
            )
        )

        athlete_state["previous_sessions"] = (
            previous_sessions or []
        )

        athlete_state["current_block"] = current_block

        athlete_state["target_competition"] = (
            target_competition
        )

        return athlete_state, context