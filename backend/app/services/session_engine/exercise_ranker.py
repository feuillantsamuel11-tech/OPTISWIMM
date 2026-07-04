from app.services.session_engine.scoring_engine import ScoringEngine

import random


class ExerciseRanker:
    """
    Responsable du classement et de la sélection des exercices.

    Le calcul du score est entièrement délégué à ScoringEngine.
    """

    def __init__(self):

        self.scoring = ScoringEngine()

    # =================================================
    # RANK
    # =================================================

    def rank(self, exercises):

        return sorted(
            exercises,
            key=self.scoring.calculate_score,
            reverse=True
        )

    # =================================================
    # DIVERSIFY
    # =================================================

    def diversify(

        self,

        exercises,

        top_pool_size=20
    ):

        if not exercises:
            return []

        top_pool = exercises[:min(
            top_pool_size,
            len(exercises)
        )]

        random.shuffle(top_pool)

        return top_pool

    # =================================================
    # SELECT
    # =================================================

    def select(

        self,

        exercises,

        limit=1,

        top_pool_size=20
    ):

        ranked = self.rank(exercises)

        diversified = self.diversify(

            ranked,

            top_pool_size
        )

        return diversified[:limit]