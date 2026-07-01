class ObjectiveSelector:

    def __init__(self):

        pass

    # =================================================
    # PRIMARY OBJECTIVES
    # =================================================

    def get_primary_objectives(

        self,

        specialist
    ):

        mapping = {

            "sprint": [

                "speed",

                "race_pace"
            ],

            "middle_distance": [

                "race_pace",

                "threshold_control"
            ],

            "distance": [

                "aerobic_power",

                "threshold_control"
            ],

            "im": [

                "race_pace",

                "aerobic_technical"
            ]
        }

        return mapping.get(

            specialist,

            [
                "race_pace"
            ]
        )

    # =================================================
    # SECONDARY OBJECTIVES
    # =================================================

    def get_secondary_objectives(

        self,

        specialist
    ):

        mapping = {

            "sprint": [

                "start_power",

                "turn_speed"
            ],

            "middle_distance": [

                "vo2"
            ],

            "distance": [

                "vo2"
            ],

            "im": [

                "underwater_skill"
            ]
        }

        return mapping.get(

            specialist,

            []
        )

    # =================================================
    # SPEED OBJECTIVES V2
    # =================================================

    def get_speed_objectives(

        self,

        specialist
    ):

        mapping = {

            "sprint": [

                "start_power",

                "speed",

                "explosive_power"
            ],

            "middle_distance": [

                "speed",

                "race_pace",

                "microdose"
            ],

            "distance": [

                "microdose",

                "speed_awareness",

                "speed_technical"
            ],

            "im": [

                "speed",

                "turn_speed",

                "underwater_power"
            ]
        }

        return mapping.get(

            specialist,

            [
                "speed"
            ]
        )

    # =================================================
    # ACTIVATION OBJECTIVES
    # =================================================

    def get_activation_objectives(

        self,

        specialist
    ):

        mapping = {

            "sprint": [

                "neural_activation"
            ],

            "middle_distance": [

                "race_activation"
            ],

            "distance": [

                "aerobic_activation"
            ],

            "im": [

                "technical_activation"
            ]
        }

        return mapping.get(

            specialist,

            [
                "race_activation"
            ]
        )

    # =================================================
    # RECOVERY OBJECTIVES
    # =================================================

    def get_recovery_objectives(

        self
    ):

        return [

            "recovery",

            "adaptive_recovery"
        ]