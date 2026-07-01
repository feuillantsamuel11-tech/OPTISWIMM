from app.models.exercise import (
    Exercise
)

from app.database import (
    SessionLocal
)


class BlockBuilder:

    def __init__(self):

        self.db = SessionLocal()

    # =================================================
    # QUERY EXERCISES
    # =================================================

    def query_exercises(

        self,

        objective
    ):

        return (

            self.db
            .query(Exercise)
            .filter(
                Exercise.objective == objective
            )
            .all()
        )

    # =================================================
    # FILTER DUPLICATES
    # =================================================

    def filter_duplicates(

        self,

        exercises,

        used_titles
    ):

        filtered = []

        for ex in exercises:

            if ex.title not in used_titles:

                filtered.append(ex)

        return filtered

    # =================================================
    # FILTER INTENSITY
    # =================================================

    def filter_intensity(

        self,

        exercises,

        max_intensity
    ):

        filtered = []

        for ex in exercises:

            if ex.intensity_score <= max_intensity:

                filtered.append(ex)

        return filtered

    # =================================================
    # FILTER VOLUME
    # =================================================

    def filter_volume(

        self,

        exercises,

        max_volume=None
    ):

        if max_volume is None:

            return exercises

        filtered = []

        for ex in exercises:

            if ex.volume <= max_volume:

                filtered.append(ex)

        return filtered

    # =================================================
    # SERIALIZE
    # =================================================

    def serialize(

        self,

        exercise
    ):

        return {
            "id":
            exercise.id,

            "title":
            exercise.title,

            "objective":
            exercise.objective,

            "category":
            exercise.category,

            "stroke":
            exercise.stroke,

            "zone":
            exercise.zone_code,

            "energy_system":
            exercise.energy_system,

            "pedagogical_focus":
            exercise.pedagogical_focus,

            "race_specificity":
            exercise.race_specificity,

            "difficulty_level":
            exercise.difficulty_level,

            "volume":
            exercise.volume,

            "rest":
            exercise.rest,

            "intensity":
            exercise.intensity_score,

            "cns":
            exercise.cns_load,

            "fatigue_cost":
            exercise.fatigue_cost,

            "equipment":
            exercise.equipment,

            "tags":
            exercise.tags
        }

    # =================================================
    # BUILD BLOCK
    # =================================================

    def build(

        self,

        objective,

        age,

        used_titles,

        max_intensity=10,

        max_volume=None,

        limit=1
    ):

        exercises = (
            self.query_exercises(
                objective
            )
        )

        exercises = (
            self.filter_duplicates(

                exercises,

                used_titles
            )
        )

        exercises = (
            self.filter_intensity(

                exercises,

                max_intensity
            )
        )

        exercises = (
            self.filter_volume(

                exercises,

                max_volume
            )
        )

        selected = []

        for ex in exercises[:limit]:

            used_titles.add(
                ex.title
            )

            selected.append(
                self.serialize(ex)
            )

        return selected