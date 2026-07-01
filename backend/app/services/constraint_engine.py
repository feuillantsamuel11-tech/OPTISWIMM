class ConstraintEngine:

    def __init__(self):

        pass

    # =================================================
    # FILTER CONSTRAINTS
    # =================================================

    def filter_constraints(

        self,

        exercises,

        athlete_state
    ):

        injury_history = athlete_state.get(
            "injury_history",
            []
        )

        fatigue_state = athlete_state.get(
            "fatigue_state",
            "low"
        )

        readiness = athlete_state.get(
            "readiness_state",
            "moderate"
        )

        filtered = []

        for ex in exercises:

            # =========================================
            # INJURY FILTER
            # =========================================

            tags = ex.tags or []

            blocked = False

            for injury in injury_history:

                if injury in tags:

                    blocked = True

            if blocked:

                continue

            # =========================================
            # FATIGUE FILTER
            # =========================================

            if fatigue_state == "high":

                if (

                    ex.intensity_score
                    and
                    ex.intensity_score >= 9
                ):

                    continue

            # =========================================
            # LOW READINESS FILTER
            # =========================================

            if readiness == "low":

                if (

                    ex.cns_load
                    and
                    ex.cns_load >= 3
                ):

                    continue

            filtered.append(ex)

        return filtered

    # =================================================
    # LEGACY COMPATIBILITY
    # =================================================

    def apply_constraints(

        self,

        exercises,

        athlete_state
    ):

        return self.filter_constraints(

            exercises,

            athlete_state
        )

    def validate_constraints(

        self,

        exercises,

        athlete_state
    ):

        return self.filter_constraints(

            exercises,

            athlete_state
        )