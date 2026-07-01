class SessionIdentityEngine:

    def __init__(self):

        pass

    # =================================================
    # DETERMINE SESSION IDENTITY
    # =================================================

    def determine_identity(

        self,

        athlete_state
    ):

        specialist = athlete_state.get(
            "specialist",
            "middle_distance"
        )

        readiness = athlete_state.get(
            "readiness_state",
            "moderate"
        )

        fatigue = athlete_state.get(
            "fatigue_state",
            "low"
        )

        prediction = athlete_state.get(
            "prediction",
            "normal"
        )

        level = athlete_state.get(
            "level",
            "intermediate"
        )

        # =============================================
        # HIGH READINESS ELITE
        # =============================================

        if (

            level == "elite"

            and

            readiness == "high"

            and

            fatigue == "low"
        ):

            if specialist == (
                "sprint"
            ):

                return (
                    "max_velocity_neural"
                )

            elif specialist == (
                "middle_distance"
            ):

                return (
                    "race_pace_precision"
                )

            else:

                return (
                    "aerobic_power"
                )

        # =============================================
        # MODERATE READINESS
        # =============================================

        if readiness == (
            "moderate"
        ):

            if specialist == (
                "middle_distance"
            ):

                return (
                    "race_pace_precision"
                )

            return (
                "threshold_control"
            )

        # =============================================
        # LOW READINESS
        # =============================================

        return (
            "recovery_technical"
        )

    # =================================================
    # LEGACY COMPATIBILITY
    # =================================================

    def select_identity(

        self,

        athlete_state
    ):

        return self.determine_identity(
            athlete_state
        )

    def build_identity(

        self,

        athlete_state
    ):

        return self.determine_identity(
            athlete_state
        )