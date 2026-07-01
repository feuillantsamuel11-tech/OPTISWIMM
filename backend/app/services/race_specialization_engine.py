class RaceSpecializationEngine:

    def get_week_objectives(

    self,

    specialist,

    daily_focus,

    race_distance
):

        if race_distance == 50:

            mapping = {
                "speed": ["speed"],
                "race_pace": ["race_pace", "speed"],
                "mixed": ["speed", "race_pace"],
                "recovery": ["recovery"],
                "aerobic": ["aerobic_power"]
            }             

            

            return mapping.get(
                daily_focus,
                ["speed"]
            )

        elif race_distance == 100:

            mapping = {
                "speed": ["speed"],
                "race_pace": ["race_pace"],
                "mixed": ["speed", "race_pace"],
                "recovery": ["recovery"],
                "aerobic": ["aerobic_power"]
            }

            return mapping.get(
                daily_focus,
                ["race_pace"]
            )

        elif race_distance == 200:

            mapping = {
                "threshold": ["threshold_control"],
                "speed": ["speed"],
                "race_pace": ["race_pace"],
                "mixed": ["race_pace", "threshold_control"],
                "recovery": ["recovery"],
                "aerobic": ["aerobic_power"]
            }

            return mapping.get(
                daily_focus,
                ["race_pace"]
            )

        elif race_distance == 400:

            mapping = {
                "threshold": ["threshold_control"],
                "speed": ["threshold_control", "speed"],
                "race_pace": ["race_pace", "threshold_control"],
                "aerobic": ["aerobic_power", "threshold_control"],
                "mixed": ["race_pace", "threshold_control"],
                "recovery": ["recovery"],
                
            }

            return mapping.get(
                daily_focus,
                ["threshold_control"]
            )

        elif race_distance in [800, 1500]:

            mapping = {
                "threshold": ["threshold_control"],
                "aerobic": ["aerobic_power"],
                "race_pace": ["aerobic_power", "threshold_control"],
                "mixed": ["aerobic_power", "threshold_control"],
                "recovery": ["recovery"],
            
            }

            return mapping.get(
                daily_focus,
                ["aerobic_power"]
            )

        return [
            "threshold_control"
        ]