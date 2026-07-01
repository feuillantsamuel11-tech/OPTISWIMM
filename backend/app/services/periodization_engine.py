from app.services.microcycle_builder import (
    MicrocycleBuilder
)
MICROCYCLE_MIDDLE_DISTANCE = {

    1: "threshold",

    2: "speed",

    3: "aerobic",

    4: "race_pace",

    5: "threshold",

    6: "mixed",

    7: "recovery"
}


MICROCYCLE_SPRINT = {

    1: "speed",

    2: "race_pace",

    3: "recovery",

    4: "speed",

    5: "race_pace",

    6: "mixed",

    7: "recovery"
}


MICROCYCLE_DISTANCE = {

    1: "aerobic",

    2: "threshold",

    3: "aerobic",

    4: "threshold",

    5: "race_pace",

    6: "mixed",

    7: "recovery"
}

class PeriodizationEngine:

    def __init__(self):

        self.microcycle_builder = (
            MicrocycleBuilder()
        )

    def build_macrocycle(

        self,

        weeks=12
    ):

        macrocycle = []

        for week in range(1, weeks + 1):

            phase = self.determine_phase(
                week,
                weeks
            )

            profile = self.determine_profile(
                phase
            )

            microcycle = (

                self.microcycle_builder
                .build_microcycle(
                    profile=profile
                )
            )

            macrocycle.append({

                "week": week,

                "phase": phase,

                "profile": profile,

                "microcycle": microcycle
            })

        return macrocycle

    def determine_phase(

        self,

        current_week,

        total_weeks
    ):

        if current_week <= 4:

            return "overload"

        if current_week <= 8:

            return "intensification"

        if current_week <= 10:

            return "race_pace"

        if current_week == 11:

            return "taper"

        return "competition"

    def determine_profile(

        self,

        phase
    ):

        if phase == "overload":

            return {

                "volume_multiplier": 1.3,

                "intensity_multiplier": 0.9,

                "recovery_priority": False
            }

        if phase == "intensification":

            return {

                "volume_multiplier": 1.0,

                "intensity_multiplier": 1.1,

                "recovery_priority": False
            }

        if phase == "race_pace":

            return {

                "volume_multiplier": 0.9,

                "intensity_multiplier": 1.2,

                "recovery_priority": False
            }

        if phase == "taper":

            return {

                "volume_multiplier": 0.6,

                "intensity_multiplier": 1.0,

                "recovery_priority": True
            }

        if phase == "competition":

            return {

                "volume_multiplier": 0.5,

                "intensity_multiplier": 1.1,

                "recovery_priority": True
            }

        return {

            "volume_multiplier": 1.0,

            "intensity_multiplier": 1.0,

            "recovery_priority": False
        }

         # ==========================================
    # DAILY FOCUS
    # ==========================================

    def get_daily_focus(

        self,

        specialist,

        day
    ):

        if specialist == "sprint":

            return (

                MICROCYCLE_SPRINT.get(

                    day,

                    "recovery"
                )
            )

        if specialist == "distance":

            return (

                MICROCYCLE_DISTANCE.get(

                    day,

                    "recovery"
                )
            )

        return (

            MICROCYCLE_MIDDLE_DISTANCE.get(

                day,

                "recovery"
            )
        )
