
class AthleteMonitoring:

    def __init__(self):

        pass

    # =================================================
    # ACUTE FATIGUE
    # =================================================

    def calculate_acute_fatigue(

        self,

        session_cns,

        session_intensity
    ):

        fatigue = (

            session_cns * 0.6
            +
            session_intensity * 0.4
        )

        return round(
            fatigue,
            2
        )

    # =================================================
    # CHRONIC FATIGUE
    # =================================================

    def calculate_chronic_fatigue(

        self,

        weekly_cns_history
    ):

        if len(weekly_cns_history) == 0:

            return 0

        average = (

            sum(weekly_cns_history)
            /
            len(weekly_cns_history)
        )

        return round(
            average,
            2
        )

    # =================================================
    # CNS RECOVERY
    # =================================================

    def calculate_cns_recovery(

        self,

        sleep_quality,

        hrv_score,

        stress_level
    ):

        recovery = (

            sleep_quality
            +
            hrv_score
            -
            stress_level
        )

        return max(
            1,
            round(recovery / 2, 2)
        )

    # =================================================
    # OVERTRAINING RISK
    # =================================================

    def get_overtraining_risk(

        self,

        acute_fatigue,

        chronic_fatigue,

        recovery_score
    ):

        risk_score = (

            acute_fatigue
            +
            chronic_fatigue
            -
            recovery_score
        )

        if risk_score >= 60:

            return "very_high"

        if risk_score >= 45:

            return "high"

        if risk_score >= 30:

            return "moderate"

        return "low"

    # =================================================
    # FRESHNESS
    # =================================================

    def calculate_freshness(

        self,

        fatigue,

        soreness,

        hrv
    ):

        freshness = (

            hrv
            +
            (10 - fatigue)
            +
            (10 - soreness)
        )

        return round(
            freshness / 3,
            2
        )

    # =================================================
    # ADAPTATION STATE
    # =================================================

    def get_adaptation_state(

        self,

        chronic_fatigue
    ):

        if chronic_fatigue >= 70:

            return "overreached"

        if chronic_fatigue >= 55:

            return "high_adaptation"

        if chronic_fatigue >= 40:

            return "productive"

        return "building"

    # =================================================
    # PERFORMANCE STATE
    # =================================================

    def get_performance_state(

        self,

        freshness,

        adaptation_state
    ):

        if (

            freshness >= 8
            and
            adaptation_state in [

                "productive",
                "high_adaptation"
            ]
        ):

            return "peak_ready"

        if freshness <= 4:

            return "fatigued"

        return "normal"

    # =================================================
    # BUILD MONITORING PROFILE
    # =================================================

    def build_profile(

        self,

        readiness,

        weekly_cns_history,

        latest_session
    ):

        acute_fatigue = (

            self.calculate_acute_fatigue(

                latest_session.get(
                    "total_cns",
                    0
                ),

                latest_session.get(
                    "average_intensity",
                    0
                )
            )
        )

        chronic_fatigue = (

            self.calculate_chronic_fatigue(
                weekly_cns_history
            )
        )

        recovery_score = (

            self.calculate_cns_recovery(

                readiness.get(
                    "sleep_quality",
                    5
                ),

                readiness.get(
                    "hrv_score",
                    5
                ),

                readiness.get(
                    "stress_level",
                    5
                )
            )
        )

        overtraining_risk = (

            self.get_overtraining_risk(

                acute_fatigue,

                chronic_fatigue,

                recovery_score
            )
        )

        freshness = (

            self.calculate_freshness(

                readiness.get(
                    "fatigue_subjective",
                    5
                ),

                readiness.get(
                    "muscle_soreness",
                    5
                ),

                readiness.get(
                    "hrv_score",
                    5
                )
            )
        )

        adaptation_state = (

            self.get_adaptation_state(
                chronic_fatigue
            )
        )

        performance_state = (

            self.get_performance_state(

                freshness,

                adaptation_state
            )
        )

        return {

            "acute_fatigue":
            acute_fatigue,

            "chronic_fatigue":
            chronic_fatigue,

            "recovery_score":
            recovery_score,

            "freshness":
            freshness,

            "adaptation_state":
            adaptation_state,

            "overtraining_risk":
            overtraining_risk,

            "performance_state":
            performance_state
        }

