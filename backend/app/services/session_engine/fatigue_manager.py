class FatigueManager:

    def __init__(self):

        pass

    # =================================================
    # TOTAL VOLUME
    # =================================================

    def calculate_volume(

        self,

        exercises
    ):

        total = 0

        for ex in exercises:

            total += ex.get(
                "volume",
                0
            )

        return total

    # =================================================
    # CNS LOAD
    # =================================================

    def calculate_cns_load(

        self,

        exercises
    ):

        total = 0

        for ex in exercises:

            total += ex.get(
                "cns",
                0
            )

        return total

    # =================================================
    # AVERAGE INTENSITY
    # =================================================

    def calculate_average_intensity(

        self,

        exercises
    ):

        if not exercises:

            return 0

        total = 0

        for ex in exercises:

            total += ex.get(
                "intensity",
                0
            )

        return round(

            total / len(exercises),

            2
        )

    # =================================================
    # FATIGUE STATE
    # =================================================

    def get_fatigue_state(

        self,

        cns_load
    ):

        if cns_load <= 5:

            return "fresh"

        if cns_load <= 10:

            return "functional"

        if cns_load <= 15:

            return "fatigued"

        return "overreached"