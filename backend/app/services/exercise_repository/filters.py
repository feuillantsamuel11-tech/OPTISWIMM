from .models import Exercise


class ExerciseFilters:

    @staticmethod
    def by_zone(exercises, zone):
        return [
            e
            for e in exercises
            if e.zone == zone
        ]

    @staticmethod
    def by_objective(exercises, objective):
        return [
            e
            for e in exercises
            if e.objective == objective
        ]

    @staticmethod
    def by_stroke(exercises, stroke):
        return [
            e
            for e in exercises
            if e.stroke == stroke
        ]

    @staticmethod
    def by_equipment(exercises, equipment):

        return [
            e
            for e in exercises
            if equipment in e.equipment
        ]

    @staticmethod
    def by_level(exercises, level):

        return [
            e
            for e in exercises
            if e.level == level
        ]

    @staticmethod
    def by_distance(exercises, distance):

        return [
            e
            for e in exercises
            if e.distance == distance
        ]