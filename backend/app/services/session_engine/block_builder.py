from app.models.exercise import (
    Exercise
)

from app.database import (
    SessionLocal
)

import random


class BlockBuilder:

    def __init__(self):

        self.db = SessionLocal()

    # =================================================
    # NORMALIZE TITLE
    # =================================================

    def normalize_title(

        self,

        title
    ):

        if not title:

            return ""

        return title.lower().strip()

    # =================================================
    # QUERY EXERCISES
    # =================================================

    def query_exercises(

        self,

        objective,

        category=None
    ):

        query = (

            self.db
            .query(Exercise)
            .filter(
                Exercise.objective == objective
            )
        )

        if category:

            query = query.filter(
                Exercise.category == category
            )

        return query.all()

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

            normalized = (

                self.normalize_title(
                    ex.title
                )
            )

            if normalized not in used_titles:

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

            intensity = (
                ex.intensity_score or 0
            )

            if intensity <= max_intensity:

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

        print(
            "MAX VOLUME:",
            max_volume
        )

        # Si plus de volume disponible,
        # aucun exercice ne doit être retenu

        if max_volume <= 0:

            print(
                "NO VOLUME REMAINING"
            )

            return []

        filtered = []

        for ex in exercises:

            volume = (
                ex.volume or 0
            )

            if volume <= max_volume:

                filtered.append(ex)

        print(
            "AFTER VOLUME:",
            len(filtered)
        )

        return filtered

    # =================================================
    # FILTER RACE SPECIFICITY
    # =================================================

    def filter_race_specificity(

        self,

        exercises,

        race_distance
    ):

        if not race_distance:

            return exercises

        distance_map = {

            50: {"50","all"},

            100: {"50", "100", "200","400", "all"},

            200: {"100", "200", "400", "all"},

            400: {"200", "400", "800"},

            800: {"400", "800", "1500"},

            1500: {"800", "1500"}
        }

        allowed = distance_map.get(

            race_distance,

            {"all"}
        )

        filtered = []

        for ex in exercises:

            if ex.category in {
                "cooldown",
                "recovery",
                "warmup",
                "preset"
            }:

                filtered.append(ex)

                continue   

            print(
                ex.title,
                ex.race_specificity,
                ex.category
            )
            
            spec = str(

                ex.race_specificity or ""

            ).lower().strip()

            print(
                "SPEC:",
                spec,
                "ALLOWED:",
                allowed
            )

            if spec not in {

                x.lower()

                for x in allowed
            }:

                continue

            # protection sprint

            if race_distance <= 100:

                if spec in {

                    "400",
                    "800",
                    "1500",
                    "open_water",
                    "5k",
                    "10k",
                    "25k"
                }:

                    continue

            # protection 200

            if race_distance == 200:

                if spec in {

                    "1500",
                    "open_water",
                    "5k",
                    "10k",
                    "25k"
                }:

                    continue

            # protection 400

            if race_distance == 400:

                if spec in {

                    "1500",
                    "open_water",
                    "5k",
                    "10k",
                    "25k"
                }:

                    continue

            filtered.append(ex)

        print(

            "RACE FILTER:",
            race_distance,
            "INPUT:",
            len(exercises)
        )

        print(

            "RACE FILTER OUTPUT:",
            len(filtered)
        )

        return filtered
    # =================================================
    # SCORE
    # =================================================

    def calculate_score(

        self,

        exercise
    ):

        score = 0

        score += (
            exercise.intensity_score or 0
        )

        score += max(
            0,
            10 - (
                exercise.cns_load or 0
            )
        )

        score += max(
            0,
            10 - (
                exercise.fatigue_cost or 0
            )
        )

        if (

            exercise.difficulty_level
            == "elite"

        ):

            score += 5
        
        return score

    # =================================================
    # RANK
    # =================================================

    def rank_exercises(

        self,

        exercises
    ):

        random.shuffle(
            exercises
        )

        return exercises

    # =================================================
    # REMOVE TITLE DUPLICATES
    # =================================================

    def remove_title_duplicates(

        self,

        exercises
    ):

        seen = set()

        unique = []

        for ex in exercises:

            title = (

                self.normalize_title(
                    ex.title
                )
            )

            if title in seen:

                continue

            seen.add(title)

            unique.append(ex)

        return unique

    # =================================================
    # DIVERSIFIED SELECTION
    # =================================================

    def diversified_selection(

        self,

        exercises,

        limit
    ):

        if not exercises:

            return []

        top_pool_size = min(
            20,
            len(exercises)
        )

        top_pool = (
            exercises[:top_pool_size]
        )

        random.shuffle(
            top_pool
        )

        top_pool = (

            self.remove_title_duplicates(
                top_pool
            )
        )

        return top_pool[:limit]

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
     # BUILD CANDIDATES
     # =================================================

    def build_candidates(

        self,

        objective,

        used_titles,

        race_distance=None,

        category=None,

        max_intensity=10,

        max_volume=None
    ):

        exercises = self.query_exercises(

            objective,

            category
        )

        print(
            "QUERY:",
            objective,
            category,
            "RESULTS:",
            len(exercises)
        )
        exercises = self.filter_duplicates(

            exercises,

            used_titles
        )
        print(
            "AFTER DUPLICATES:",
            len(exercises)
        )
        exercises = self.filter_intensity(

            exercises,

            max_intensity
        )

        exercises = self.filter_volume(

            exercises,

            max_volume
        )
        print(
            "AFTER VOLUME:",
            len(exercises)
        )
        exercises = self.filter_race_specificity(
            exercises,
            race_distance
        )

        print(
            "AFTER RACE FILTER:",
            len(exercises)
        )
        target_block = int(max_volume * 0.7)

        exercises = sorted(

            exercises,

            key=lambda ex:

            abs(
                (ex.volume or 0)
                - target_block
            )
        )



        exercises = self.rank_exercises(

            exercises
        )

        exercises = self.remove_title_duplicates(

            exercises
        )
        
        print(
            "FINAL CANDIDATES:",
            len(exercises)
        )

        for ex in exercises[:10]:

            print(
                ex.title,
                ex.race_specificity,
                ex.volume
            )
        return [

            self.serialize(ex)

            for ex in exercises
        ]   

    # =================================================
    #BUILD BLOCK
    # =================================================

    def build(

        self,

        objective,

        used_titles,

        race_distance=None,

        category=None,

        max_intensity=10,

        max_volume=None,

        limit=1,

        **kwargs
    ):

        exercises = self.query_exercises(

            objective,

            category
        )

        exercises = self.filter_duplicates(

            exercises,

            used_titles
        )

        exercises = self.filter_intensity(

            exercises,

            max_intensity
        )

        exercises = self.filter_volume(

            exercises,

            max_volume
        )

        exercises = self.filter_race_specificity(

            exercises,

            race_distance
        )

        exercises = self.rank_exercises(

            exercises
        )

        exercises = self.remove_title_duplicates(

            exercises
        )

        top_pool = exercises[:20]

         
        random.shuffle(
            top_pool
   )

        selected_exercises = top_pool[:limit]

        selected = []

        for ex in selected_exercises:

            used_titles.add(

                self.normalize_title(
                    ex.title
                )
            )

            selected.append(

                self.serialize(
                    ex
                )
            )

        return selected

    