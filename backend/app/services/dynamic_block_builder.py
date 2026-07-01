class DynamicBlockBuilder:

    def __init__(self):

        self.identity_templates = {

            "sprint_neural": {

                "warmup_focus":
                "neural_activation",

                "preset_focus":
                "speed_technical",

                "main_focus":
                "max_velocity",

                "recovery_focus":
                "active_recovery",

                "cooldown_focus":
                "parasympathetic"
            },

            "aerobic_recovery": {

                "warmup_focus":
                "easy_aerobic",

                "preset_focus":
                "technical_precision",

                "main_focus":
                "recovery",

                "recovery_focus":
                "mobility",

                "cooldown_focus":
                "relaxation"
            },

            "threshold_build": {

                "warmup_focus":
                "aerobic_activation",

                "preset_focus":
                "threshold_control",

                "main_focus":
                "threshold",

                "recovery_focus":
                "easy_aerobic",

                "cooldown_focus":
                "recovery"
            },

            "race_pace_precision": {

                "warmup_focus":
                "race_activation",

                "preset_focus":
                "technical_precision",

                "main_focus":
                "race_pace",

                "recovery_focus":
                "active_recovery",

                "cooldown_focus":
                "parasympathetic"
            }
        }

    # ------------------------------------------------
    # GET TEMPLATE
    # ------------------------------------------------

    def get_template(

        self,

        session_identity
    ):

        return self.identity_templates.get(

            session_identity,

            self.identity_templates[
                "race_pace_precision"
            ]
        )

    # ------------------------------------------------
    # BUILD BLOCK STRUCTURE
    # ------------------------------------------------

    def build_structure(

        self,

        session_identity
    ):

        template = self.get_template(
            session_identity
        )

        return {

            "warmup_focus":
            template["warmup_focus"],

            "preset_focus":
            template["preset_focus"],

            "main_focus":
            template["main_focus"],

            "recovery_focus":
            template["recovery_focus"],

            "cooldown_focus":
            template["cooldown_focus"]
        }