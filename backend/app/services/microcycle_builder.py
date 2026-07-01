from app.services.intelligent_session_builder import (
    IntelligentSessionBuilder
)

from app.services.fatigue_engine import (
    FatigueEngine
)


class MicrocycleBuilder:

    def __init__(self):

        self.session_builder = (
            IntelligentSessionBuilder()
        )

        self.fatigue_engine = (
            FatigueEngine()
        )

    def build_microcycle(

        self,

        profile="elite"
    ):

        microcycle = []

        previous_sessions = []

        training_days = [

            {
                "day": "Monday",

                "focus": "aerobic"
            },

            {
                "day": "Tuesday",

                "focus": "speed"
            },

            {
                "day": "Wednesday",

                "focus": "recovery"
            },

            {
                "day": "Thursday",

                "focus": "threshold"
            },

            {
                "day": "Friday",

                "focus": "race_pace"
            },

            {
                "day": "Saturday",

                "focus": "competition"
            },

            {
                "day": "Sunday",

                "focus": "recovery"
            }
        ]

        for training_day in training_days:

            athlete_state = {}

            # Calculate fatigue state
            if len(previous_sessions) > 0:

                microcycle_data = (

                    self.fatigue_engine
                    .calculate_microcycle_load(
                        previous_sessions
                    )
                )

                athlete_state = (

                    self.fatigue_engine
                    .estimate_fatigue_state(
                        microcycle_data
                    )
                )

            # Add focus-specific constraints

            focus = training_day["focus"]

            if focus == "recovery":

                athlete_state[
                    "fatigue_level"
                ] = "high"

            if focus == "speed":

                athlete_state[
                    "cns_priority"
                ] = True

            session = (

                self.session_builder
                .generate(
                    athlete_state
                )
            )

            microcycle.append({

                "day":
                training_day["day"],

                "focus":
                focus,

                "session":
                session
            })

            # Save exercises history

            all_exercises = []

            for block in (
                session["session"]
                .values()
            ):

                all_exercises.extend(block)

            previous_sessions.append(
                all_exercises
            )

        return microcycle