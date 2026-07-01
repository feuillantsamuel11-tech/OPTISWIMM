
class RecoveryManager:

    def __init__(self):

        pass

    # ============================================
    # RECOVERY VOLUME
    # ============================================

    def get_recovery_volume(

        self,

        fatigue_state,

        age
    ):

        if age >= 50:

            return 800

        if fatigue_state == "very_high":

            return 800

        if fatigue_state == "high":

            return 600

        if fatigue_state == "moderate":

            return 400

        return 200

    # ============================================
    # RECOVERY OBJECTIVES
    # ============================================

    def get_recovery_objectives(

        self,

        fatigue_state,

        age
    ):

        objectives = [

            "parasympathetic"
        ]

        if age >= 40:

            objectives.append(
                "mobility"
            )

        if fatigue_state in [

            "high",
            "very_high"
        ]:

            objectives.append(
                "cooldown"
            )

        return objectives

    # ============================================
    # NEED EXTRA RECOVERY
    # ============================================

    def needs_extra_recovery(

        self,

        readiness_level,

        fatigue_state
    ):

        if readiness_level == "low":

            return True

        if fatigue_state in [

            "high",
            "very_high"
        ]:

            return True

        return False

    # ============================================
    # RECOVERY INTENSITY
    # ============================================

    def get_recovery_intensity(

        self,

        age
    ):

        if age >= 40:

            return 1

        return 2

    # ============================================
    # BUILD RECOVERY PROFILE
    # ============================================

    def build_profile(

        self,

        readiness_level,

        fatigue_state,

        age
    ):

        return {

            "recovery_volume":
            self.get_recovery_volume(

                fatigue_state,

                age
            ),

            "recovery_objectives":
            self.get_recovery_objectives(

                fatigue_state,

                age
            ),

            "extra_recovery":
            self.needs_extra_recovery(

                readiness_level,

                fatigue_state
            ),

            "recovery_intensity":
            self.get_recovery_intensity(
                age
            )
        }

