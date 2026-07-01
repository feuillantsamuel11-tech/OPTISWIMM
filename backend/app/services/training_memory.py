from sqlalchemy import text

from app.database import SessionLocal


class TrainingMemory:

    def __init__(self):

        self.db = SessionLocal()
    
    # ==========================================
    # RECENT PRIMARY OBJECTIVES
    # ==========================================

    def get_recent_primary_objectives(

        self,

        athlete_id,

        limit=5
    ):

        query = text(
            """
            SELECT
                primary_objective
            FROM training_history
            WHERE athlete_id = :athlete_id
            AND primary_objective IS NOT NULL
            ORDER BY id DESC
            LIMIT :limit
            """
        )

        rows = self.db.execute(

            query,

            {
                "athlete_id":
                athlete_id,

                "limit":
                limit
            }
        ).fetchall()

        return [

            row[0]
            for row in rows
            if row[0]
        ]

    # ==========================================
    # RECENT OBJECTIVES
    # ==========================================

    def get_recent_objectives(

        self,

        athlete_id,

        limit=10
    ):

        query = text(
            """
            SELECT
                primary_objective
            FROM training_history
            WHERE athlete_id = :athlete_id
            AND primary_objective IS NOT NULL
            ORDER BY id DESC
            LIMIT :limit
            """
        )

        rows = self.db.execute(

            query,

            {
                "athlete_id":
                athlete_id,

                "limit":
                limit
            }
        ).fetchall()

        return [

            row[0]
            for row in rows
            if row[0]
        ]

    # ==========================================
    # RECENT CNS
    # ==========================================

    def get_recent_cns(

        self,

        athlete_id,

        limit=7
    ):

        query = text(
            """
            SELECT
                total_cns
            FROM training_history
            WHERE athlete_id = :athlete_id
            AND total_cns IS NOT NULL
            ORDER BY id DESC
            LIMIT :limit
            """
        )

        rows = self.db.execute(

            query,

            {
                "athlete_id":
                athlete_id,

                "limit":
                limit
            }
        ).fetchall()

        return [

            row[0]
            for row in rows
            if row[0] is not None
        ]
    
    def get_recent_training_loads(

        self,

        athlete_id,

        limit=28
    ):

        query = text(
            """
            SELECT
                training_load
            FROM training_history
            WHERE athlete_id = :athlete_id

            AND training_load IS NOT NULL
            AND duration_minutes IS NOT NULL
            AND rpe IS NOT NULL

            ORDER BY id DESC

            LIMIT :limit
            """
        )

        rows = self.db.execute(

            query,

            {
                "athlete_id":
                athlete_id,

                "limit":
                limit
            }
        ).fetchall()

        return [

            float(row[0])

            for row in rows

            if row[0] is not None
        ]
    # ==========================================
    # SAVE SESSION
    # ==========================================

    def save_generated_session(

        self,

        athlete_id,

        session_identity,

        primary_objective,

        secondary_objective,

        total_cns,

        training_load=None,

        duration_minutes=None,

        rpe=None,

        session_score=None
):


        query = text(
            """
            INSERT INTO training_history (

                athlete_id,
                session_identity,
                primary_objective,
                secondary_objective,
                total_cns,
                training_load,
                duration_minutes,
                rpe,
                session_score
            )
            VALUES (

                :athlete_id,
                :session_identity,
                :primary_objective,
                :secondary_objective,
                :total_cns,
                :training_load,
                :duration_minutes,
                :rpe,
                :session_score
            )
            """
        )

        self.db.execute(

            query,

            {
                "athlete_id":
                athlete_id,

                "session_identity":
                session_identity,

                "primary_objective":
                primary_objective,

                "secondary_objective":
                secondary_objective,

                "total_cns":
                total_cns,

                "training_load":
                training_load,

                "duration_minutes":
                duration_minutes,

                "rpe":
                rpe,

                "session_score":
                session_score
            }
        )

        self.db.commit()

    # ==========================================
    # SESSION COUNT
    # ==========================================

    def get_session_count(

        self,

        athlete_id
    ):

        query = text(
            """
            SELECT COUNT(*)
            FROM training_history
            WHERE athlete_id = :athlete_id
            """
        )

        result = self.db.execute(

            query,

            {
                "athlete_id":
                athlete_id
            }

        ).scalar()

        return result or 0