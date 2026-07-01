
class SpecialistManager:

    def __init__(self):

        pass

    # ============================================
    # VOLUME TARGETS
    # ============================================

    def get_volume_target(

        self,

        specialist,

        age
    ):

        if age >= 40:

            return 3000

        mapping = {

            "sprint": 4000,

            "middle_distance": 6000,

            "distance": 7500,

            "im": 6500
        }

        return mapping.get(

            specialist,

            4500
        )

    # ============================================
    # CNS LIMITS
    # ============================================

    def get_cns_limit(

        self,

        specialist,

        age
    ):

        if age >= 40:

            return 10

        mapping = {

            "sprint": 20,

            "middle_distance": 16,

            "distance": 12,

            "im": 18
        }

        return mapping.get(

            specialist,

            14
        )

    # ============================================
    # MAX INTENSITY
    # ============================================

    def get_max_intensity(

        self,

        specialist
    ):

        mapping = {

            "sprint": 10,

            "middle_distance": 9,

            "distance": 8,

            "im": 9
        }

        return mapping.get(

            specialist,

            8
        )

    # ============================================
    # RECOVERY MULTIPLIER
    # ============================================

    def get_recovery_multiplier(

        self,

        age
    ):

        if age >= 50:

            return 2.0

        if age >= 40:

            return 1.5

        return 1.0

    # ============================================
    # SPECIALIST PROFILE
    # ============================================

    def build_profile(

        self,

        athlete
    ):

        race_distance = athlete.get(
            "race_distance",
            400
        )

        if race_distance in [50, 100]:
            specialist = "sprint"
        elif race_distance in [200, 400]:
            specialist = "middle_distance"
        elif race_distance in [800, 1500]:
            specialist = "distance"
        else:
            specialist = athlete.get(
                "specialist",
                "middle_distance"
            )

        age = athlete.get(
            "age",
            18
        )

        return {
            "specialist": specialist,
            "age": age,
            "volume_target": self.get_volume_target(
                specialist,
                age
            ),
            "cns_limit": self.get_cns_limit(
                specialist,
                age
            ),
            "max_intensity": self.get_max_intensity(
                specialist
            ),
            "recovery_multiplier": self.get_recovery_multiplier(
                age
            )
        }

