from dataclasses import dataclass


@dataclass
class Exercise:

    id: int
    name: str
    zone: str
    objective: str


class ExerciseRepository:

    def find(
        self,
        zone=None,
        objective=None,
    ):

        exercises = [
            Exercise(1, "8x100 seuil", "Z4", "threshold_control"),
            Exercise(2, "16x50 sprint", "Z7", "speed"),
            Exercise(3, "12x200 aérobie", "Z2", "aerobic_capacity"),
        ]

        result = []

        for exercise in exercises:

            if zone and exercise.zone != zone:
                continue

            if objective and exercise.objective != objective:
                continue

            result.append(exercise)

        return result