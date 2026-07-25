from .models import Exercise


class ExerciseRepository:

    def __init__(self):
        self._exercises: list[Exercise] = []

    def add(self, exercise: Exercise):
        self._exercises.append(exercise)

    def all(self):
        return self._exercises

    def count(self):
        return len(self._exercises)

    def clear(self):
        self._exercises.clear()

    def find_by_zone(self, zone: str):
        return [
            e
            for e in self._exercises
            if e.zone == zone
        ]

    def find_by_objective(self, objective: str):
        return [
            e
            for e in self._exercises
            if e.objective == objective
        ]

    def find_by_stroke(self, stroke: str):
        return [
            e
            for e in self._exercises
            if e.stroke == stroke
        ]