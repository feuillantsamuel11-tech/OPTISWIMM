class SessionSerializer:

    def __init__(self):

        pass

    # =================================================
    # SERIALIZE EXERCISE
    # =================================================

    def serialize_exercise(

        self,

        exercise
    ):

        if exercise is None:

            return None

        # =============================================
        # ALREADY SERIALIZED
        # =============================================

        if isinstance(
            exercise,
            dict
        ):

            return exercise

        # =============================================
        # SQLALCHEMY OBJECT
        # =============================================

        return {

            "id":
            exercise.id,

            "title":
            exercise.title,

            "category":
            exercise.category,

            "stroke":
            exercise.stroke,

            "zone":
            exercise.zone_code,

            "objective":
            exercise.objective,

            "equipment":
            exercise.equipment,

            "volume":
            exercise.volume,

            "intensity":
            exercise.intensity_score,

            "cns":
            exercise.cns_load,

            "rest":
            exercise.rest,

            "difficulty":
            exercise.difficulty_level,

            "focus":
            exercise.pedagogical_focus,

            "tags":
            exercise.tags or []
        }

    # =================================================
    # SERIALIZE BLOCK
    # =================================================

    def serialize_block(

        self,

        exercises
    ):

        serialized = []

        for ex in exercises:

            serialized.append(
                self.serialize_exercise(
                    ex
                )
            )

        return serialized

    # =================================================
    # SERIALIZE SESSION
    # =================================================

    def serialize_session(

        self,

        session_payload
    ):

        session = session_payload.get(
            "session",
            {}
        )

        return {

            "session_identity":

            session_payload.get(
                "session_identity"
            ),

            "progression":

            session_payload.get(
                "progression",
                []
            ),

            "metrics":

            session_payload.get(
                "metrics",
                {}
            ),

            "session": {

                "warmup":

                self.serialize_block(
                    session.get(
                        "warmup",
                        []
                    )
                ),

                "preset":

                self.serialize_block(
                    session.get(
                        "preset",
                        []
                    )
                ),

                "activation":

                self.serialize_block(
                    session.get(
                        "activation",
                        []
                    )
                ),

                "main_set":

                self.serialize_block(
                    session.get(
                        "main_set",
                        []
                    )
                ),

                "speed_set":

                self.serialize_block(
                    session.get(
                        "speed_set",
                        []
                    )
                ),

                "recovery":

                self.serialize_block(
                    session.get(
                        "recovery",
                        []
                    )
                ),

                "cooldown":

                self.serialize_block(
                    session.get(
                        "cooldown",
                        []
                    )
                )
            }
        }