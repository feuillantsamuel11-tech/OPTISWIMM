from app.services.exercise_relationship_engine import (
    ExerciseRelationshipEngine
)


class ExerciseScoringEngine:

    def __init__(self):

        self.relationship_engine = (
            ExerciseRelationshipEngine()
        )

    # =================================================
    # SCORE EXERCISE
    # =================================================

    def score_exercise(

        self,

        exercise,

        athlete_state,

        previous_objectives=None
    ):

        if previous_objectives is None:
            previous_objectives = []

        score = 50

        # =================================================
        # PREFERRED OBJECTIVES
        # =================================================

        preferred = athlete_state.get(
            "preferred_objectives",
            []
        )

        if (
            exercise.objective
            in preferred
        ):

            score += 25

        # =================================================
        # BLOCK INTELLIGENCE
        # =================================================

        current_block = athlete_state.get(
            "current_block"
        )

        # ---------------------------------------------
        # WARMUP PROTECTION
        # ---------------------------------------------

        if current_block == "warmup":

            if exercise.intensity_score >= 7:
                score -= 50

            if exercise.cns_load >= 4:
                score -= 40

        # ---------------------------------------------
        # PRESET
        # ---------------------------------------------

        if current_block == "preset":

            if exercise.intensity_score >= 8:
                score -= 40

        # ---------------------------------------------
        # COOLDOWN PROTECTION
        # ---------------------------------------------

        if current_block == "cooldown":

            if exercise.intensity_score >= 5:
                score -= 60

            if exercise.cns_load >= 3:
                score -= 50

        # =================================================
        # READINESS
        # =================================================

        readiness = athlete_state.get(
            "readiness_state",
            "good"
        )

        if readiness == "critical":

            if exercise.intensity_score >= 7:
                score -= 40

        elif readiness == "low":

            if exercise.intensity_score >= 7:
                score -= 25

        elif readiness == "optimal":

            if exercise.intensity_score >= 7:
                score += 15

        # =================================================
        # CNS MANAGEMENT
        # =================================================

        cns_load = athlete_state.get(
            "cns_load_above",
            0
        )

        if cns_load >= 6:

            if exercise.cns_load >= 3:
                score -= 30

        # =================================================
        # SHOULDER PROTECTION
        # =================================================

        if athlete_state.get(
            "shoulder_pain",
            False
        ):

            if (
                exercise.equipment
                == "pull"
            ):

                score -= 50

        # =================================================
        # RECOVERY PRIORITY
        # =================================================

        recovery_priority = (
            athlete_state.get(
                "recovery_priority",
                False
            )
        )

        if recovery_priority:

            if (
                exercise.category
                == "recovery"
            ):

                score += 20

        # =================================================
        # SPECIALIST
        # =================================================

        specialist = athlete_state.get(
            "specialist",
            "middle_distance"
        )

        if specialist == "sprint":

            if (
                exercise.race_specificity
                in ["50", "100"]
            ):

                score += 15

        elif specialist == "distance":

            if (
                exercise.race_specificity
                in ["800", "1500"]
            ):

                score += 15

        # =================================================
        # FATIGUE
        # =================================================

        fatigue = athlete_state.get(
            "fatigue_level",
            "low"
        )

        if fatigue == "high":

            score -= (
                exercise.fatigue_cost * 4
            )

        elif fatigue == "moderate":

            score -= (
                exercise.fatigue_cost * 2
            )

        # =================================================
        # RELATIONSHIP ENGINE
        # =================================================

        for previous in previous_objectives:

            # -----------------------------------------
            # POTENTIATION
            # -----------------------------------------

            potentiates = (

                self.relationship_engine
                .has_potentiation(

                    previous,

                    exercise.objective
                )
            )

            if potentiates:

                score += 20

            # -----------------------------------------
            # PREPARATION
            # -----------------------------------------

            prepares = (

                self.relationship_engine
                .prepares(

                    previous,

                    exercise.objective
                )
            )

            if prepares:

                score += 15

            # -----------------------------------------
            # CONFLICT
            # -----------------------------------------

            conflict = (

                self.relationship_engine
                .has_conflict(

                    previous,

                    exercise.objective
                )
            )

            if conflict:

                score -= 40

            # -----------------------------------------
            # DUPLICATION
            # -----------------------------------------

            duplication = (

                self.relationship_engine
                .has_duplication(

                    previous,

                    exercise.objective
                )
            )

            if duplication:

                score -= 20

        # =================================================
        # CLAMP SCORE
        # =================================================

        score = max(
            0,
            min(100, score)
        )

        return score

    # =================================================
    # RANK EXERCISES
    # =================================================

    def rank_exercises(

        self,

        exercises,

        athlete_state,

        previous_objectives=None
    ):

        if previous_objectives is None:
            previous_objectives = []

        scored = []

        for exercise in exercises:

            score = self.score_exercise(

                exercise,

                athlete_state,

                previous_objectives
            )

            scored.append({

                "exercise":
                exercise,

                "score":
                score
            })

        scored.sort(

            key=lambda x: x["score"],

            reverse=True
        )

        return scored
    