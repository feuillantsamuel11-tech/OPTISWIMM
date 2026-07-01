from sqlalchemy import text

from app.database import SessionLocal


class DatabaseCleanupEngine:

    def __init__(self):

        self.db = SessionLocal()

    # =================================================
    # NORMALIZE OBJECTIVES
    # =================================================

    def normalize_objectives(self):

        replacements = {

            "race activation":
            "race_activation",

            "race-activation":
            "race_activation",

            "neural activation":
            "neural_activation",

            "speed technical":
            "speed_technical",

            "easy aerobic":
            "easy_aerobic",

            "threshold-control":
            "threshold_control",

            "active recovery":
            "active_recovery",

            "parasympathetic recovery":
            "parasympathetic"
        }

        for old, new in replacements.items():

            query = text("""

                UPDATE exercises

                SET objective = :new

                WHERE objective = :old

            """)

            self.db.execute(

                query,

                {

                    "old": old,

                    "new": new
                }
            )

        self.db.commit()

    # =================================================
    # NORMALIZE CATEGORIES
    # =================================================

    def normalize_categories(self):

        replacements = {

            "Speed":
            "speed",

            "Recovery":
            "recovery",

            "Warm Up":
            "warmup",

            "Main Set":
            "main_set"
        }

        for old, new in replacements.items():

            query = text("""

                UPDATE exercises

                SET category = :new

                WHERE category = :old

            """)

            self.db.execute(

                query,

                {

                    "old": old,

                    "new": new
                }
            )

        self.db.commit()

    # =================================================
    # FIX INTENSITY
    # =================================================

    def normalize_intensity(self):

        query = text("""

            UPDATE exercises

            SET intensity_score = 5

            WHERE intensity_score > 10

        """)

        self.db.execute(query)

        query = text("""

            UPDATE exercises

            SET intensity_score = 1

            WHERE intensity_score < 1

        """)

        self.db.execute(query)

        self.db.commit()

    # =================================================
    # RECOVERY OBJECTIVES
    # =================================================

    def create_recovery_objectives(self):

        recovery_objectives = [

            "recovery",

            "active_recovery",

            "parasympathetic",

            "relaxation"
        ]

        for objective in recovery_objectives:

            query = text("""

                UPDATE exercises

                SET category = 'recovery'

                WHERE objective = :objective

            """)

            self.db.execute(

                query,

                {

                    "objective":
                    objective
                }
            )

        self.db.commit()

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
    # RUN CLEANUP
    # =================================================

    def run_full_cleanup(self):

        self.normalize_objectives()

        self.normalize_categories()

        self.normalize_intensity()

        self.create_recovery_objectives()

        return {

            "status":
            "cleanup_complete",

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