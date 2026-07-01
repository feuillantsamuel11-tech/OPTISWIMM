class AthleteProfileEngine:

    def __init__(self):

        pass

    def build_profile(

        self,

        age=18,

        level="elite",

        specialist="middle_distance",

        race_distance=400,

        injury_history=None,

        fatigue_resistance="moderate"
    ):

        if injury_history is None:
            injury_history = []

        profile = {

            "age": age,

            "level": level,

            "specialist": specialist,

            "race_distance": race_distance,

            "injury_history":
            injury_history,

            "fatigue_resistance":
            fatigue_resistance
        }

        profile.update(

            self.get_specialist_traits(
                specialist
            )
        )

        profile.update(

            self.get_age_traits(age)
        )

        profile.update(

            self.get_level_traits(level)
        )

        profile.update(

            self.get_injury_traits(
                injury_history
            )
        )

        return profile

    def get_specialist_traits(

        self,

        specialist
    ):

        if specialist == "sprint":

            return {

                "preferred_objectives": [

                    "speed",
                    "max_velocity",
                    "race_pace"
                ],

                "volume_tolerance": "low",

                "cns_tolerance": "high",

                "lactate_tolerance": "high"
            }

        if specialist == "distance":

            return {

                "preferred_objectives": [

                    "aerobic_power",
                    "threshold",
                    "tempo_frequency"
                ],

                "volume_tolerance": "high",

                "cns_tolerance": "moderate",

                "lactate_tolerance": "moderate"
            }

        if specialist == "IM":

            return {

                "preferred_objectives": [

                    "coordination",
                    "technical_precision",
                    "race_pace"
                ],

                "volume_tolerance": "moderate",

                "cns_tolerance": "moderate",

                "lactate_tolerance": "high"
            }

        return {

            "preferred_objectives": [

                "aerobic_power"
            ],

            "volume_tolerance": "moderate",

            "cns_tolerance": "moderate",

            "lactate_tolerance": "moderate"
        }

    def get_age_traits(

        self,

        age
    ):

        if age <= 12:

            return {

                "max_intensity_limit": 5,

                "recovery_priority": True,

                "technical_priority": True
            }

        if age <= 16:

            return {

                "max_intensity_limit": 7,

                "recovery_priority": False,

                "technical_priority": True
            }

        return {

            "max_intensity_limit": 10,

            "recovery_priority": False,

            "technical_priority": False
        }

    def get_level_traits(

        self,

        level
    ):

        if level == "beginner":

            return {

                "complexity_limit": 3,

                "volume_factor": 0.6
            }

        if level == "advanced":

            return {

                "complexity_limit": 7,

                "volume_factor": 0.9
            }

        if level == "elite":

            return {

                "complexity_limit": 10,

                "volume_factor": 1.2
            }

        return {

            "complexity_limit": 5,

            "volume_factor": 1.0
        }

    def get_injury_traits(

        self,

        injury_history
    ):

        traits = {}

        if "shoulder" in injury_history:

            traits.update({

                "shoulder_pain": True,

                "avoid_equipment": [
                    "pull"
                ]
            })

        if "knee" in injury_history:

            traits.update({

                "knee_pain": True,

                "avoid_strokes": [
                    "brasse"
                ]
            })

        if "lower_back" in injury_history:

            traits.update({

                "lower_back_pain": True
            })

        return traits