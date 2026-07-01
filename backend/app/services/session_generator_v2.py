import random

from app.database import SessionLocal

from app.models.exercise import Exercise

from app.services.constraint_engine import (
    ConstraintEngine
)

from app.services.fatigue_engine import (
    FatigueEngine
)


class SessionGeneratorV2:

    def __init__(self):

        self.db = SessionLocal()

        self.constraint_engine = (
            ConstraintEngine()
        )

        self.fatigue_engine = (
            FatigueEngine()
        )

    def get_exercises_by_objective(

        self,
        objective
    ):

        return self.db.query(
            Exercise
        ).filter(
            Exercise.objective == objective
        ).all()

    def build_athlete_state(

        self,
        previous_sessions
    ):

        microcycle = (

            self.fatigue_engine
            .calculate_microcycle_load(
                previous_sessions
            )
        )

        athlete_state = (

            self.fatigue_engine
            .estimate_fatigue_state(
                microcycle
            )
        )

        return athlete_state

    def generate_session(

        self,

        objectives,

        previous_sessions=None,

        manual_state=None,

        max_blocks=6
    ):

        if previous_sessions is None:
            previous_sessions = []

        athlete_state = {}

        # Automatic fatigue analysis
        if len(previous_sessions) > 0:

            athlete_state = (
                self.build_athlete_state(
                    previous_sessions
                )
            )

        # Manual override
        if manual_state:

            athlete_state.update(
                manual_state
            )

        candidate_exercises = []

        for objective in objectives:

            exercises = (
                self.get_exercises_by_objective(
                    objective
                )
            )

            candidate_exercises.extend(
                exercises
            )

        filtered = (

            self.constraint_engine
            .filter_exercises(

                candidate_exercises,

                athlete_state
            )
        )

        valid_exercises = filtered[
            "valid_exercises"
        ]

        blocked_exercises = filtered[
            "blocked_exercises"
        ]

        if len(valid_exercises) == 0:

            return {

                "session": [],

                "blocked":
                blocked_exercises,

                "athlete_state":
                athlete_state,

                "message":
                "No valid exercises found"
            }

        random.shuffle(valid_exercises)

        selected = valid_exercises[
            :max_blocks
        ]

        total_volume = sum(
            ex.volume or 0
            for ex in selected
        )

        average_intensity = round(

            sum(
                ex.intensity_score or 0
                for ex in selected
            )

            / len(selected),

            2
        )

        total_cns = sum(
            ex.cns_load or 0
            for ex in selected
        )

        total_fatigue = sum(
            ex.fatigue_cost or 0
            for ex in selected
        )

        return {

            "session": selected,

            "blocked":
            blocked_exercises,

            "athlete_state":
            athlete_state,

            "metrics": {

                "total_volume":
                total_volume,

                "average_intensity":
                average_intensity,

                "exercise_count":
                len(selected),

                "total_cns":
                total_cns,

                "total_fatigue":
                total_fatigue
            }
        }

    def close(self):

        self.db.close()