
import random


class SessionVariation:

    def __init__(self):

        pass

    # ============================================
    # SESSION IDENTITIES
    # ============================================

    def get_session_identity(

        self,

        specialist,

        readiness_level
    ):

        if specialist == "sprint":

            identities = [

                "pure_speed",

                "neural_power",

                "speed_reactivity",

                "explosive_race"
            ]

        elif specialist == "middle_distance":

            identities = [

                "race_pace_precision",

                "threshold_pressure",

                "aerobic_power",

                "race_specific"
            ]

        elif specialist == "distance":

            identities = [

                "aerobic_capacity",

                "threshold_endurance",

                "oxygen_efficiency",

                "distance_control"
            ]

        else:

            identities = [

                "mixed_training"
            ]

        if readiness_level == "low":

            identities = [

                "recovery_technical",

                "low_stress_quality"
            ]

        return random.choice(
            identities
        )

    # ============================================
    # SESSION PROGRESSION
    # ============================================

    def get_progression(

        self,

        specialist
    ):

        mapping = {

            "sprint": [

                "aerobic_foundation",

                "technical_skill",

                "neural_activation",

                "neural_speed",

                "max_velocity"
            ],

            "middle_distance": [

                "aerobic_foundation",

                "technical_skill",

                "race_activation",

                "race_pace",

                "threshold"
            ],

            "distance": [

                "aerobic_foundation",

                "technical_skill",

                "threshold",

                "vo2",

                "parasympathetic"
            ],

            "im": [

                "aerobic_foundation",

                "technical_skill",

                "threshold",

                "race_pace",

                "neural_activation"
            ]
        }

        return mapping.get(

            specialist,

            [
                "race_pace"
            ]
        )

    # ============================================
    # SHOULD ADD SECONDARY STIMULUS
    # ============================================

    def should_add_secondary(

        self,

        readiness_level
    ):

        return readiness_level == "high"

    # ============================================
    # SESSION STYLE
    # ============================================

    def get_session_style(

        self,

        specialist
    ):

        mapping = {

            "sprint": "high_neural",

            "middle_distance": "mixed_intensity",

            "distance": "aerobic_density",

            "im": "hybrid"
        }

        return mapping.get(

            specialist,

            "balanced"
        )

    # ============================================
    # BUILD VARIATION PROFILE
    # ============================================

    def build_profile(

        self,

        specialist,

        readiness_level
    ):

        return {

            "identity":
            self.get_session_identity(

                specialist,

                readiness_level
            ),

            "progression":
            self.get_progression(
                specialist
            ),

            "secondary_stimulus":
            self.should_add_secondary(
                readiness_level
            ),

            "style":
            self.get_session_style(
                specialist
            )
        }

