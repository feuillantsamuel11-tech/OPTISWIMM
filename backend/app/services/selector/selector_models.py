from dataclasses import dataclass


@dataclass
class ExerciseCandidate:

    exercise_id: int

    score: float

    reason: str