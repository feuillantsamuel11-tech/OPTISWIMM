
from app.services.mesocycle_engine import (
    MesocycleEngine
)


class MacrocycleEngine:

    def __init__(self):

        self.mesocycle_engine = (
            MesocycleEngine()
        )

    # =================================================
    # SEASON STRUCTURE
    # =================================================

    def get_season_structure(

        self
    ):

        return [

            {
                "phase":
                "general_preparation",

                "weeks":
                4
            },

            {
                "phase":
                "aerobic_build",

                "weeks":
                4
            },

            {
                "phase":
                "threshold_build",

                "weeks":
                4
            },

            {
                "phase":
                "race_specific",

                "weeks":
                4
            },

            {
                "phase":
                "taper",

                "weeks":
                2
            },

            {
                "phase":
                "championship_peak",

                "weeks":
                1
            },

            {
                "phase":
                "transition",

                "weeks":
                2
            }
        ]

    # =================================================
    # PHASE ADJUSTMENT
    # =================================================

    def adjust_readiness_for_phase(

        self,

        readiness,

        phase
    ):

        adjusted = readiness.copy()

        # =============================================
        # BUILD PHASES
        # =============================================

        if phase in [

            "general_preparation",

            "aerobic_build",

            "threshold_build"
        ]:

            adjusted[
                "motivation"
            ] = min(

                10,

                adjusted.get(
                    "motivation",
                    5
                ) + 1
            )

        # =============================================
        # RACE SPECIFIC
        # =============================================

        elif phase == "race_specific":

            adjusted[
                "hrv_score"
            ] = min(

                10,

                adjusted.get(
                    "hrv_score",
                    5
                ) + 1
            )

        # =============================================
        # TAPER
        # =============================================

        elif phase == "taper":

            adjusted[
                "fatigue_subjective"
            ] = max(

                1,

                adjusted.get(
                    "fatigue_subjective",
                    5
                ) - 3
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

            adjusted[
                "hrv_score"
            ] = min(

                10,

                adjusted.get(
                    "hrv_score",
                    5
                ) + 2
            )

        # =============================================
        # CHAMPIONSHIP
        # =============================================

        elif phase == "championship_peak":

            adjusted[
                "motivation"
            ] = 10

            adjusted[
                "fatigue_subjective"
            ] = 1

            adjusted[
                "stress_level"
            ] = 2

        # =============================================
        # TRANSITION
        # =============================================

        elif phase == "transition":

            adjusted[
                "motivation"
            ] = max(

                3,

                adjusted.get(
                    "motivation",
                    5
                ) - 2
            )

        return adjusted

    # =================================================
    # PHASE OBJECTIVES
    # =================================================

    def get_phase_focus(

        self,

        phase
    ):

        mapping = {

            "general_preparation": [

                "aerobic_foundation",

                "technical_skill"
            ],

            "aerobic_build": [

                "aerobic_foundation",

                "threshold"
            ],

            "threshold_build": [

                "threshold",

                "vo2"
            ],

            "race_specific": [

                "race_pace",

                "neural_speed"
            ],

            "taper": [

                "race_activation",

                "parasympathetic"
            ],

            "championship_peak": [

                "max_velocity",

                "race_pace"
            ],

            "transition": [

                "parasympathetic",

                "mobility"
            ]
        }

        return mapping.get(

            phase,

            [
                "race_pace"
            ]
        )

    # =================================================
    # GENERATE MACROCYCLE
    # =================================================

    def generate_macrocycle(

        self,

        athlete,

        readiness
    ):

        structure = (
            self.get_season_structure()
        )

        macrocycle = []

        cumulative_volume = 0

        cumulative_cns = 0

        # =============================================
        # GENERATE PHASES
        # =============================================

        for phase_index, phase_data in enumerate(
            structure
        ):

            phase = phase_data[
                "phase"
            ]

            weeks = phase_data[
                "weeks"
            ]

            adjusted_readiness = (

                self.adjust_readiness_for_phase(

                    readiness,

                    phase
                )
            )

            mesocycle = (

                self.mesocycle_engine
                .generate_mesocycle(

                    athlete,

                    adjusted_readiness,

                    weeks=weeks
                )
            )

            mesocycle[
                "phase"
            ] = phase

            mesocycle[
                "phase_focus"
            ] = self.get_phase_focus(
                phase
            )

            mesocycle[
                "phase_number"
            ] = phase_index + 1

            macrocycle.append(
                mesocycle
            )

            cumulative_volume += (
                mesocycle[
                    "total_volume"
                ]
            )

            cumulative_cns += (
                mesocycle[
                    "total_cns"
                ]
            )

        # =============================================
        # FINAL RESPONSE
        # =============================================

        return {

            "season_type":
            athlete.get(

                "specialist",

                "middle_distance"
            ),

            "macrocycle_phases":
            len(macrocycle),

            "season_volume":
            cumulative_volume,

            "season_cns":
            cumulative_cns,

            "macrocycle":
            macrocycle
        }

