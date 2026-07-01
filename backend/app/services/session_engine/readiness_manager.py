
class ReadinessManager:

    def __init__(self):

        pass

    # =================================================
    # READINESS SCORE
    # =================================================

    def calculate_readiness_score(

        self,

        readiness
    ):

        sleep_quality = readiness.get(
            "sleep_quality",
            5
        )

        stress_level = readiness.get(
            "stress_level",
            5
        )

        muscle_soreness = readiness.get(
            "muscle_soreness",
            5
        )

        motivation = readiness.get(
            "motivation",
            5
        )

        hrv_score = readiness.get(
            "hrv_score",
            5
        )

        fatigue_subjective = readiness.get(
            "fatigue_subjective",
            5
        )

        score = (

            sleep_quality * 1.2
            +
            motivation * 1.2
            +
            hrv_score * 1.1
            -
            stress_level * 0.8
            -
            muscle_soreness * 0.7
            -
            fatigue_subjective * 0.8
        )

        normalized = max(

            1,

            min(
                10,
                round(score / 2, 2)
            )
        )

        return normalized

    # =================================================
    # READINESS LEVEL
    # =================================================

    def get_readiness_level(

        self,

        score
    ):

        if score >= 8:

            return "elite"

        if score >= 6:

            return "high"

        if score >= 4:

            return "moderate"

        return "low"

    # =================================================
    # CNS STATE
    # =================================================

    def get_cns_state(

        self,

        readiness_score
    ):

        if readiness_score >= 8:

            return "primed"

        if readiness_score >= 6:

            return "ready"

        if readiness_score >= 4:

            return "neutral"

        return "fatigued"

    # =================================================
    # RECOVERY STATE
    # =================================================

    def get_recovery_state(

        self,

        soreness,

        fatigue
    ):

        combined = (
            soreness + fatigue
        ) / 2

        if combined <= 2:

            return "excellent"

        if combined <= 4:

            return "good"

        if combined <= 6:

            return "acceptable"

        return "poor"

    # =================================================
    # BUILD PROFILE
    # =================================================

    def build_profile(

        self,

        readiness
    ):

        readiness_score = (
            self.calculate_readiness_score(
                readiness
            )
        )

        readiness_level = (
            self.get_readiness_level(
                readiness_score
            )
        )

        cns_state = (
            self.get_cns_state(
                readiness_score
            )
        )

        recovery_state = (
            self.get_recovery_state(

                readiness.get(
                    "muscle_soreness",
                    5
                ),

                readiness.get(
                    "fatigue_subjective",
                    5
                )
            )
        )

        return {

            "readiness_score":
            readiness_score,

            "readiness_level":
            readiness_level,

            "cns_state":
            cns_state,

            "recovery_state":
            recovery_state
        }

