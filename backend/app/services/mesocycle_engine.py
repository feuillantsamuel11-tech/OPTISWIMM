
from app.services.microcycle_engine import (
    MicrocycleEngine
)


class MesocycleEngine:

    def __init__(self):

        self.microcycle_engine = (
            MicrocycleEngine()
        )
    
    def get_current_week(
        self,
        session_count
    ):

        week = (

            (session_count // 7)

            % 4
        )

        return week


    def get_current_structure(
        self,
        session_count
    ):

        week = self.get_current_week(
            session_count
        )

        structure = (

            self.get_mesocycle_structure()
        )

        return structure[
            week
        ]
    # =================================================
    # WEEK STRUCTURE
    # =================================================
    
    

    def get_mesocycle_structure(

        self,

        weeks=4
    ):

        structure = []

        for week in range(weeks):

            if week == 0:

                structure.append({

                    "week_type":
                    "accumulation",

                    "volume_multiplier":
                    1.0,

                    "intensity_multiplier":
                    1.0
                })

            elif week == 1:

                structure.append({

                    "week_type":
                    "overload",

                    "volume_multiplier":
                    1.1,

                    "intensity_multiplier":
                    1.05
                })

            elif week == 2:

                structure.append({

                    "week_type":
                    "functional_overreach",

                    "volume_multiplier":
                    1.2,

                    "intensity_multiplier":
                    1.1
                })

            else:

                structure.append({

                    "week_type":
                    "deload",

                    "volume_multiplier":
                    0.7,

                    "intensity_multiplier":
                    0.8
                })

        return structure

    # =================================================
    # ADJUST READINESS
    # =================================================

    def adjust_readiness(

        self,

        readiness,

        week_type
    ):

        adjusted = readiness.copy()

        # =============================================
        # OVERLOAD
        # =============================================

        if week_type == "overload":

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
        # FUNCTIONAL OVERREACH
        # =============================================

        elif week_type == (

            "functional_overreach"
        ):

            adjusted[
                "fatigue_subjective"
            ] = min(

                10,

                adjusted.get(
                    "fatigue_subjective",
                    5
                ) + 2
            )

            adjusted[
                "muscle_soreness"
            ] = min(

                10,

                adjusted.get(
                    "muscle_soreness",
                    5
                ) + 2
            )

        # =============================================
        # DELOAD
        # =============================================

        elif week_type == "deload":

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
                "stress_level"
            ] = max(

                1,

                adjusted.get(
                    "stress_level",
                    5
                ) - 1
            )

        return adjusted

    # =================================================
    # APPLY LOAD MODIFIERS
    # =================================================

    def apply_load_modifiers(

        self,

        microcycle,

        structure
    ):

        volume_multiplier = structure[
            "volume_multiplier"
        ]

        intensity_multiplier = structure[
            "intensity_multiplier"
        ]

        metrics = microcycle[
            "weekly_metrics"
        ]

        metrics[
            "weekly_volume"
        ] = int(

            metrics[
                "weekly_volume"
            ]

            *
            volume_multiplier
        )

        metrics[
            "average_intensity"
        ] = round(

            metrics[
                "average_intensity"
            ]

            *
            intensity_multiplier,

            2
        )

        return microcycle

    # =================================================
    # ADAPTATION STATE
    # =================================================

    def get_adaptation_state(

        self,

        cumulative_cns
    ):

        if cumulative_cns >= 240:

            return "overreached"

        if cumulative_cns >= 180:

            return "high_adaptation"

        if cumulative_cns >= 120:

            return "productive"

        return "building"

    # =================================================
    # GENERATE MESOCYCLE
    # =================================================

    def generate_mesocycle(

        self,

        athlete,

        readiness,

        weeks=4
    ):

        structure = (

            self.get_mesocycle_structure(
                weeks
            )
        )

        mesocycle = []

        cumulative_cns = 0

        cumulative_volume = 0

        # =============================================
        # GENERATE WEEKS
        # =============================================

        for week_index, week_structure in enumerate(
            structure
        ):

            adjusted_readiness = (

                self.adjust_readiness(

                    readiness,

                    week_structure[
                        "week_type"
                    ]
                )
            )

            microcycle = (

                self.microcycle_engine
                .generate_microcycle(

                    athlete,

                    adjusted_readiness
                )
            )

            microcycle = (

                self.apply_load_modifiers(

                    microcycle,

                    week_structure
                )
            )

            microcycle[
                "week_number"
            ] = week_index + 1

            microcycle[
                "week_type"
            ] = week_structure[
                "week_type"
            ]

            mesocycle.append(
                microcycle
            )

            cumulative_cns += (

                microcycle[
                    "weekly_metrics"
                ][
                    "weekly_cns"
                ]
            )

            cumulative_volume += (

                microcycle[
                    "weekly_metrics"
                ][
                    "weekly_volume"
                ]
            )

        # =============================================
        # ADAPTATION
        # =============================================

        adaptation_state = (

            self.get_adaptation_state(
                cumulative_cns
            )
        )

        # =============================================
        # FINAL RESPONSE
        # =============================================

        return {

            "mesocycle_type":
            athlete.get(

                "specialist",

                "middle_distance"
            ),

            "weeks":
            weeks,

            "adaptation_state":
            adaptation_state,

            "total_volume":
            cumulative_volume,

            "total_cns":
            cumulative_cns,

            "microcycles":
            mesocycle
        }