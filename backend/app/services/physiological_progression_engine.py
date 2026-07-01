class PhysiologicalProgressionEngine:

    def __init__(self):

        pass

    # =================================================
    # GET PROGRESSION
    # =================================================

    def get_progression(

        self,

        athlete_state
    ):

        readiness = athlete_state.get(
            "readiness_state",
            "moderate"
        )

        specialist = athlete_state.get(
            "specialist",
            "middle_distance"
        )

        # =============================================
        # HIGH READINESS
        # =============================================

        if readiness == "high":

            if specialist == (
                "sprint"
            ):

                return [

                    "easy_aerobic",

                    "technical_precision",

                    "neural_activation",

                    "speed_technical",

                    "race_pace"
                ]

            return [

                "easy_aerobic",

                "technical_precision",

                "race_activation",

                "race_pace",

                "speed_technical"
            ]

        # =============================================
        # MODERATE READINESS
        # =============================================

        if readiness == (
            "moderate"
        ):

            return [

                "easy_aerobic",

                "technical_precision",

                "race_activation",

                "race_pace"
            ]

        # =============================================
        # LOW READINESS
        # =============================================

        return [

            "easy_aerobic",

            "technical_precision",

            "recovery"
        ]

    # =================================================
    # LEGACY COMPATIBILITY
    # =================================================

    def build_progression(

        self,

        athlete_state
    ):

        return self.get_progression(
            athlete_state
        )