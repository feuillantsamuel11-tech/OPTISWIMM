from app.models.exercise import Exercise
from app.domain.training_context import TrainingContext


class ScoringEngine:
    """
    Moteur central de calcul du score.

    Toutes les règles de sélection doivent être
    implémentées ici.
    """

    def calculate_score(
        self,
        exercise: Exercise,
        context: TrainingContext | None = None,
    ) -> int:

        score = 0

        # -----------------------------
        # Score de base
        # -----------------------------

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

        # -----------------------------
        # Règles contextuelles
        # -----------------------------

        if context is not None:

            if (
                context.max_intensity is not None
                and exercise.intensity_score is not None
            ):

                if exercise.intensity_score > context.max_intensity:

                    score -= 20

        return score