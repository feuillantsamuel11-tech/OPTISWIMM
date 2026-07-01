class ReadinessEngine:

    def __init__(self):

        pass

    # =================================================
    # EVALUATE READINESS
    # =================================================

    def evaluate_readiness(

        self,

        athlete_state
    ):

        sleep_hours = athlete_state.get(
            "sleep_hours",
            7
        )

        sleep_quality = athlete_state.get(
            "sleep_quality",
            5
        )

        hrv_score = athlete_state.get(
            "hrv_score",
            5
        )

        soreness = athlete_state.get(
            "muscle_soreness",
            5
        )

        stress = athlete_state.get(
            "stress_level",
            5
        )

        motivation = athlete_state.get(
            "motivation",
            5
        )

        fatigue = athlete_state.get(
            "fatigue_subjective",
            5
        )

        # =============================================
        # SCORING
        # =============================================

        score = 50

        score += (
            sleep_hours - 7
        ) * 3

        score += (
            sleep_quality - 5
        ) * 4

        score += (
            hrv_score - 5
        ) * 4

        score += (
            motivation - 5
        ) * 3

        score -= (
            soreness - 5
        ) * 3

        score -= (
            stress - 5
        ) * 3

        score -= (
            fatigue - 5
        ) * 4

        score = max(
            0,
            min(
                100,
                score
            )
        )

        # =============================================
        # STATE
        # =============================================

        if score >= 80:

            readiness_state = (
                "high"
            )

        elif score >= 60:

            readiness_state = (
                "moderate"
            )

        else:

            readiness_state = (
                "low"
            )

        return {

            "readiness_score":
            score,

            "readiness_state":
            readiness_state
        }

    # =================================================
    # LEGACY COMPATIBILITY
    # =================================================

    def calculate_readiness(

        self,

        athlete_state
    ):

        return self.evaluate_readiness(
            athlete_state
        )