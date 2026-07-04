from app.models.exercise import Exercise


class ScoringEngine:
    """
    Centralise le calcul du score d'un exercice.

    V1 :
    - reprend exactement la logique historique de BlockBuilder
    - aucun changement fonctionnel
    """

    def calculate_score(self, exercise: Exercise) -> int:

        score = 0

        score += exercise.intensity_score or 0

        score += max(
            0,
            10 - (exercise.cns_load or 0)
        )

        score += max(
            0,
            10 - (exercise.fatigue_cost or 0)
        )

        if exercise.difficulty_level == "elite":
            score += 5

        return score