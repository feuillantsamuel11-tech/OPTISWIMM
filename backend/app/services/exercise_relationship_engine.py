class ExerciseRelationshipEngine:

    def __init__(self):

        self.relationships = {

            "mobility": {

                "prepares": [

                    "neural_activation",

                    "speed_technical",

                    "race_activation"
                ]
            },

            "easy_aerobic": {

                "prepares": [

                    "threshold",

                    "race_pace",

                    "aerobic_power"
                ]
            },

            "neural_activation": {

                "potentiates": [

                    "max_velocity",

                    "speed"
                ]
            },

            "resisted_speed": {

                "potentiates": [

                    "max_velocity"
                ]
            },

            "lactate_tolerance": {

                "conflicts": [

                    "max_velocity",

                    "speed"
                ]
            },

            "threshold": {

                "duplicates": [

                    "threshold_control"
                ]
            },

            "race_pace": {

                "conflicts": [

                    "recovery",

                    "parasympathetic"
                ]
            }
        }

    # =================================================
    # GET RELATIONSHIPS
    # =================================================

    def get_relationships(

        self,

        objective
    ):

        return self.relationships.get(
            objective,
            {}
        )

    # =================================================
    # CHECK CONFLICT
    # =================================================

    def has_conflict(

        self,

        current_objective,

        next_objective
    ):

        relations = self.get_relationships(
            current_objective
        )

        conflicts = relations.get(
            "conflicts",
            []
        )

        return (
            next_objective in conflicts
        )

    # =================================================
    # CHECK DUPLICATION
    # =================================================

    def has_duplication(

        self,

        current_objective,

        next_objective
    ):

        relations = self.get_relationships(
            current_objective
        )

        duplicates = relations.get(
            "duplicates",
            []
        )

        return (
            next_objective in duplicates
        )

    # =================================================
    # CHECK POTENTIATION
    # =================================================

    def has_potentiation(

        self,

        current_objective,

        next_objective
    ):

        relations = self.get_relationships(
            current_objective
        )

        potentiates = relations.get(
            "potentiates",
            []
        )

        return (
            next_objective in potentiates
        )

    # =================================================
    # CHECK PREPARATION
    # =================================================

    def prepares(

        self,

        current_objective,

        next_objective
    ):

        relations = self.get_relationships(
            current_objective
        )

        prepares = relations.get(
            "prepares",
            []
        )

        return (
            next_objective in prepares
        )