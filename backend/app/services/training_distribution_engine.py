class TrainingDistributionEngine:

    def __init__(self):

        self.models = {

            "polarized": {

                "low_intensity":
                0.80,

                "moderate_intensity":
                0.10,

                "high_intensity":
                0.10
            },

            "pyramidal": {

                "low_intensity":
                0.70,

                "moderate_intensity":
                0.20,

                "high_intensity":
                0.10
            },

            "threshold_heavy": {

                "low_intensity":
                0.55,

                "moderate_intensity":
                0.30,

                "high_intensity":
                0.15
            },

            "sprint_based": {

                "low_intensity":
                0.60,

                "moderate_intensity":
                0.15,

                "high_intensity":
                0.25
            }
        }

    # =================================================
    # GET MODEL
    # =================================================

    def get_model(

        self,

        model_name
    ):

        return self.models.get(

            model_name,

            self.models["polarized"]
        )

    # =================================================
    # CLASSIFY SESSION
    # =================================================

    def classify_session(

        self,

        session_identity
    ):

        if session_identity in [

            "sprint_neural",

            "lactate_overload"
        ]:

            return "high_intensity"

        elif session_identity in [

            "threshold_build",

            "race_pace_precision"
        ]:

            return "moderate_intensity"

        return "low_intensity"

    # =================================================
    # ANALYZE MICROCYCLE
    # =================================================

    def analyze_microcycle(

        self,

        sessions
    ):

        distribution = {

            "low_intensity": 0,

            "moderate_intensity": 0,

            "high_intensity": 0,

            "high_cns": 0
        }

        for session in sessions:

            session_identity = session.get(
                "session_identity",
                "aerobic_recovery"
            )

            category = self.classify_session(
                session_identity
            )

            distribution[category] += 1

            # -----------------------------------------
            # CNS ANALYSIS
            # -----------------------------------------

            metrics = session.get(
                "metrics",
                {}
            )

            total_cns = metrics.get(
                "total_cns",
                0
            )

            if total_cns >= 8:

                distribution["high_cns"] += 1

        total = max(1, len(sessions))

        return {

            key: round(
                value / total,
                2
            )

            for key, value
            in distribution.items()
        }

    # =================================================
    # DISTRIBUTION WARNING
    # =================================================

    def distribution_warning(

        self,

        sessions,

        model_name="polarized"
    ):

        current = self.analyze_microcycle(
            sessions
        )

        target = self.get_model(
            model_name
        )

        warnings = []

        for key in [

            "low_intensity",

            "moderate_intensity",

            "high_intensity"
        ]:

            current_value = current.get(
                key,
                0
            )

            target_value = target.get(
                key,
                0
            )

            if current_value > (
                target_value + 0.15
            ):

                warnings.append({

                    "type":
                    key,

                    "current":
                    current_value,

                    "recommended":
                    target_value
                })

        # ---------------------------------------------
        # HIGH CNS WARNING
        # ---------------------------------------------

        if current["high_cns"] >= 0.50:

            warnings.append({

                "type":
                "high_cns_density",

                "current":
                current["high_cns"],

                "recommended":
                0.30
            })

        return warnings