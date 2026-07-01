
from app.services.intelligent_session_builder import (
    IntelligentSessionBuilder
)

SPRINTER_MICROCYCLE = {

    1: "speed",
    2: "race_pace",
    3: "aerobic",
    4: "speed",
    5: "race_pace",
    6: "mixed",
    7: "recovery"
}

MIDDLE_DISTANCE_MICROCYCLE = {

    1: "threshold",
    2: "speed",
    3: "aerobic",
    4: "race_pace",
    5: "threshold",
    6: "mixed",
    7: "recovery"
}

DISTANCE_MICROCYCLE = {

    1: "aerobic",
    2: "threshold",
    3: "aerobic",
    4: "threshold",
    5: "race_pace",
    6: "mixed",
    7: "recovery"
}

class MicrocycleEngine:

    def __init__(self):

        self.session_builder = (
            IntelligentSessionBuilder()
        )

    # =================================================
    # DAILY DISTRIBUTION
    # =================================================

    def build_day_plan(

        self,

        day_index
    ):

        mapping = {

            1: "high",

            2: "moderate",

            3: "high",

            4: "recovery",

            5: "high",

            6: "moderate",

            7: "recovery"
        }

        return mapping.get(
            day_index,
            "moderate"
        )

    # =================================================
    # ADJUST READINESS
    # =================================================

    def adjust_readiness(

        self,

        readiness,

        load_type
    ):

        adjusted = readiness.copy()

        if load_type == "high":

            adjusted[
                "motivation"
            ] = min(
                10,
                adjusted.get(
                    "motivation",
                    5
                ) + 1
            )

        elif load_type == "recovery":

            adjusted[
                "fatigue_subjective"
            ] = max(
                1,
                adjusted.get(
                    "fatigue_subjective",
                    5
                ) - 2
            )

            adjusted[
                "muscle_soreness"
            ] = max(
                1,
                adjusted.get(
                    "muscle_soreness",
                    5
                ) - 2
            )

        return adjusted

    # =================================================
    # GENERATE MICROCYCLE
    # =================================================

    def generate_microcycle(

        self,

        athlete,

        readiness
    ):

        days = []

        total_volume = 0

        total_cns = 0

        for day in range(1, 8):

            load_type = (
                self.build_day_plan(
                    day
                )
            )

            adjusted_readiness = (
                self.adjust_readiness(

                    readiness,

                    load_type
                )
            )

            session = (
                self.session_builder
                .build_session(

                    athlete,

                    adjusted_readiness
                )
            )

            metrics = session.get(
                "metrics",
                {}
            )

            total_volume += metrics.get(
                "total_volume",
                0
            )

            total_cns += metrics.get(
                "total_cns",
                0
            )

            days.append({

                "day":
                day,

                "load_type":
                load_type,

                "session":
                session
            })

        return {

            "days":
            days,

            "weekly_metrics": {

                "weekly_volume":
                total_volume,

                "weekly_cns":
                total_cns
            }
        }

