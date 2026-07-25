from .filters import ExerciseFilters


class QueryEngine:

    def search(self, exercises, **criteria):

        result = exercises

        if criteria.get("zone"):
            result = ExerciseFilters.by_zone(
                result,
                criteria["zone"],
            )

        if criteria.get("objective"):
            result = ExerciseFilters.by_objective(
                result,
                criteria["objective"],
            )

        if criteria.get("stroke"):
            result = ExerciseFilters.by_stroke(
                result,
                criteria["stroke"],
            )

        if criteria.get("equipment"):
            for equipment in criteria["equipment"]:
                result = ExerciseFilters.by_equipment(
                    result,
                    equipment,
                )

        if criteria.get("level"):
            result = ExerciseFilters.by_level(
                result,
                criteria["level"],
            )

        if criteria.get("distance"):
            result = ExerciseFilters.by_distance(
                result,
                criteria["distance"],
            )

        return result