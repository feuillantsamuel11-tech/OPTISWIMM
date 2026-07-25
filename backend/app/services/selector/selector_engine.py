from app.repositories.exercise_repository import ExerciseRepository
from .selector_models import ExerciseCandidate


class SelectorEngine:

    def __init__(self):
        self.repo = ExerciseRepository()

    def select(self, block):

        exercises = self.repo.find(
            zone=block.zone,
            objective=block.objective,
        )

        candidates = []

        for exercise in exercises:

            candidates.append(
                ExerciseCandidate(
                    exercise_id=exercise.id,
                    score=1.0,
                    reason="repository match",
                )
            )

        return candidates