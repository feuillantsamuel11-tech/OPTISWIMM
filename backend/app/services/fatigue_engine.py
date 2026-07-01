class FatigueEngine:

    def __init__(self):

        pass

    # =================================================
    # CALCULATE SESSION FATIGUE
    # =================================================

    def calculate_session_fatigue(

        self,

        exercises
    ):

        total_fatigue = 0

        total_cns = 0

        total_volume = 0

        for ex in exercises:

            total_fatigue += (
                ex.fatigue_cost or 0
            )

            total_cns += (
                ex.cns_load or 0
            )

            total_volume += (
                ex.volume or 0
            )

        fatigue_state = (
            self.classify_fatigue(

                total_fatigue,

                total_cns,

                total_volume
            )
        )

        return {

            "fatigue_score":
            total_fatigue,

            "cns_load":
            total_cns,

            "volume":
            total_volume,

            "fatigue_state":
            fatigue_state
        }

    # =================================================
    # CLASSIFY FATIGUE
    # =================================================

    def classify_fatigue(

        self,

        fatigue_score,

        cns_load,

        volume
    ):

        if (

            fatigue_score >= 35

            or cns_load >= 12

            or volume >= 7000
        ):

            return "high"

        elif (

            fatigue_score >= 20

            or cns_load >= 7

            or volume >= 4500
        ):

            return "moderate"

        return "low"

    # =================================================
    # ESTIMATE FATIGUE STATE
    # =================================================

    def estimate_fatigue_state(

        self,

        athlete_state
    ):

        readiness = athlete_state.get(
            "readiness_state",
            "good"
        )

        soreness = athlete_state.get(
            "muscle_soreness",
            0
        )

        cns_load = athlete_state.get(
            "cns_load_above",
            0
        )

        fatigue_level = "low"

        if (

            readiness == "critical"

            or soreness >= 8

            or cns_load >= 9
        ):

            fatigue_level = "high"

        elif (

            readiness in [

                "low",

                "moderate"
            ]

            or soreness >= 5

            or cns_load >= 6
        ):

            fatigue_level = "moderate"

        return {

            "fatigue_state":
            fatigue_level,

            "estimated_cns":
            cns_load,

            "estimated_soreness":
            soreness
        }

    # =================================================
    # RECOVERY NEEDED
    # =================================================

    def recovery_needed(

        self,

        fatigue_state
    ):

        if isinstance(
            fatigue_state,
            dict
        ):

            fatigue_level = fatigue_state.get(
                "fatigue_state",
                "low"
            )

        else:

            fatigue_level = fatigue_state

        return fatigue_level == "high"

    # =================================================
    # CALCULATE MICROCYCLE LOAD
    # =================================================

    def calculate_microcycle_load(

        self,

        sessions
    ):

        total_volume = 0

        total_cns = 0

        total_fatigue = 0

        session_count = len(sessions)

        for session in sessions:

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

            total_fatigue += metrics.get(
                "average_intensity",
                0
            )

        average_fatigue = 0

        if session_count > 0:

            average_fatigue = round(

                total_fatigue
                / session_count,

                2
            )

        load_state = self.classify_microcycle_load(

            total_volume,

            total_cns,

            average_fatigue
        )

        return {

            "total_volume":
            total_volume,

            "total_cns":
            total_cns,

            "average_intensity":
            average_fatigue,

            "load_state":
            load_state
        }

    # =================================================
    # CLASSIFY MICROCYCLE LOAD
    # =================================================

    def classify_microcycle_load(

        self,

        volume,

        cns,

        intensity
    ):

        if (

            volume >= 35000

            or cns >= 45

            or intensity >= 8
        ):

            return "very_high"

        elif (

            volume >= 25000

            or cns >= 30

            or intensity >= 6.5
        ):

            return "high"

        elif (

            volume >= 15000

            or cns >= 18

            or intensity >= 5
        ):

            return "moderate"

        return "low"