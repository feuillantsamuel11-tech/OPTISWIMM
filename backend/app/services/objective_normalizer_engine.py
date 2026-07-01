from sqlalchemy import text

from app.database import SessionLocal


class ObjectiveNormalizerEngine:

    def __init__(self):

        self.db = SessionLocal()

        # =============================================
        # OBJECTIVE MAPPING
        # =============================================

        self.mapping = {

            # -----------------------------------------
            # ACTIVATION
            # -----------------------------------------

            "speed_activation":
            "neural_activation",

            "sprint_activation":
            "neural_activation",

            "pull_activation":
            "neural_activation",

            "underwater_activation":
            "neural_activation",

            "general_activation":
            "neural_activation",

            # -----------------------------------------
            # TECHNICAL
            # -----------------------------------------

            "technical_activation":
            "technical_precision",

            "technical_stability":
            "technical_precision",

            "speed_awareness":
            "speed_technical",

            "technique":
            "technical_precision",

            "kick":
            "technical_precision",

            # -----------------------------------------
            # MOBILITY
            # -----------------------------------------

            "mobility_activation":
            "mobility",

            "mobility_recovery":
            "mobility",

            # -----------------------------------------
            # AEROBIC
            # -----------------------------------------

            "aerobic":
            "easy_aerobic",

            "aerobic_support":
            "easy_aerobic",

            "aerobic_technical":
            "easy_aerobic",

            "respiratory_activation":
            "aerobic_activation",

            # -----------------------------------------
            # LACTATE
            # -----------------------------------------

            "lactate":
            "lactate_tolerance",

            # -----------------------------------------
            # RECOVERY
            # -----------------------------------------

            "adaptive_recovery":
            "recovery",

            "shoulder_recovery":
            "recovery",

            "lower_back_recovery":
            "recovery",

            # -----------------------------------------
            # STRENGTH
            # -----------------------------------------

            "strength":
            "neural_activation",

            # -----------------------------------------
            # UNDERWATER
            # -----------------------------------------

            "underwater_power":
            "underwater_skill",

            # -----------------------------------------
            # RACE
            # -----------------------------------------

            "competition":
            "race_pace"
        }

        # =============================================
        # CATEGORY MAPPING
        # =============================================

        self.category_mapping = {

            "kick":
            "preset",

            "pull":
            "main_set",

            "cooldown":
            "recovery"
        }

    # =================================================
    # NORMALIZE OBJECTIVES
    # =================================================

    def normalize_objectives(self):

        updated = 0

        for old, new in self.mapping.items():

            query = text("""

                UPDATE exercises

                SET objective = :new

                WHERE objective = :old

            """)

            result = self.db.execute(

                query,

                {

                    "old": old,

                    "new": new
                }
            )

            updated += result.rowcount

        self.db.commit()

        return updated

    # =================================================
    # NORMALIZE CATEGORIES
    # =================================================

    def normalize_categories(self):

        updated = 0

        for old, new in (

            self.category_mapping.items()
        ):

            query = text("""

                UPDATE exercises

                SET category = :new

                WHERE category = :old

            """)

            result = self.db.execute(

                query,

                {

                    "old": old,

                    "new": new
                }
            )

            updated += result.rowcount

        self.db.commit()

        return updated

    # =================================================
    # SHOW OBJECTIVES
    # =================================================

    def show_objectives(self):

        query = text("""

            SELECT DISTINCT objective

            FROM exercises

            ORDER BY objective

        """)

        result = self.db.execute(query)

        return [

            row[0]

            for row in result.fetchall()
        ]

    # =================================================
    # SHOW CATEGORIES
    # =================================================

    def show_categories(self):

        query = text("""

            SELECT DISTINCT category

            FROM exercises

            ORDER BY category

        """)

        result = self.db.execute(query)

        return [

            row[0]

            for row in result.fetchall()
        ]

    # =================================================
    # RUN NORMALIZATION
    # =================================================

    def run(self):

        objective_updates = (
            self.normalize_objectives()
        )

        category_updates = (
            self.normalize_categories()
        )

        return {

            "status":
            "normalization_complete",

            "objective_updates":
            objective_updates,

            "category_updates":
            category_updates,

            "objectives":
            self.show_objectives(),

            "categories":
            self.show_categories()
        }

    # =================================================
    # CLOSE
    # =================================================

    def close(self):

        self.db.close()