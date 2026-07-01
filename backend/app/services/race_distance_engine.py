class RaceDistanceEngine:

    def get_distance_profile(

        self,

        distance
    ):

        profiles = {

            50: {

                "focus": "speed",

                "volume": 0.8,

                "intensity": 1.2
            },

            100: {

                "focus": "race_pace",

                "volume": 0.9,

                "intensity": 1.1
            },

            200: {

                "focus": "race_pace",

                "volume": 1.0,

                "intensity": 1.0
            },

            400: {

                "focus": "threshold",

                "volume": 1.1,

                "intensity": 1.0
            },

            800: {

                "focus": "aerobic",

                "volume": 1.2,

                "intensity": 0.95
            },

            1500: {

                "focus": "aerobic",

                "volume": 1.3,

                "intensity": 0.9
            }
        }

        return profiles.get(

            distance,

            profiles[400]
        )