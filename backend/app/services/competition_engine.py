
class CompetitionEngine:

    def __init__(self):

        pass

    # =================================================
    # COMPETITION CLASSIFICATION
    # =================================================

    def classify_competition(

        self,

        competition_type
    ):

        mapping = {

            "local": {

                "importance": "low",

                "taper_days": 3
            },

            "regional": {

                "importance": "medium",

                "taper_days": 5
            },

            "national": {

                "importance": "high",

                "taper_days": 7
            },

            "international": {

                "importance": "peak",

                "taper_days": 14
            }
        }

        return mapping.get(

            competition_type,

            mapping[
                "regional"
            ]
        )

    # =================================================
    # TAPER MODIFIERS
    # =================================================

    def get_taper_modifiers(

        self,

        taper_days
    ):

        if taper_days >= 14:

            return {

                "volume_multiplier":
                0.45,

                "intensity_multiplier":
                0.95,

                "cns_multiplier":
                0.6,

                "recovery_multiplier":
                2.0
            }

        elif taper_days >= 7:

            return {

                "volume_multiplier":
                0.6,

                "intensity_multiplier":
                0.95,

                "cns_multiplier":
                0.7,

                "recovery_multiplier":
                1.7
            }

        return {

            "volume_multiplier":
            0.75,

            "intensity_multiplier":
            0.9,

            "cns_multiplier":
            0.8,

            "recovery_multiplier":
            1.4
        }

    # =================================================
    # PEAK READINESS
    # =================================================

    def build_peak_readiness(

        self,

        readiness
    ):

        adjusted = readiness.copy()

        adjusted[
            "fatigue_subjective"
        ] = 1

        adjusted[
            "muscle_soreness"
        ] = 1

        adjusted[
            "motivation"
        ] = 10

        adjusted[
            "hrv_score"
        ] = min(

            10,

            adjusted.get(
                "hrv_score",
                8
            ) + 2
        )

        adjusted[
            "sleep_quality"
        ] = min(

            10,

            adjusted.get(
                "sleep_quality",
                8
            ) + 1
        )

        return adjusted

    # =================================================
    # COMPETITION PHASE
    # =================================================

    def get_competition_phase(

        self,

        days_before_competition
    ):

        if days_before_competition <= 1:

            return "competition"

        if days_before_competition <= 3:

            return "final_taper"

        if days_before_competition <= 7:

            return "taper"

        if days_before_competition <= 14:

            return "pre_taper"

        return "normal_training"

    # =================================================
    # PHASE OBJECTIVES
    # =================================================

    def get_phase_objectives(

        self,

        phase
    ):

        mapping = {

            "normal_training": [

                "threshold",

                "race_pace"
            ],

            "pre_taper": [

                "race_pace",

                "neural_speed"
            ],

            "taper": [

                "race_activation",

                "parasympathetic"
            ],

            "final_taper": [

                "neural_activation",

                "parasympathetic"
            ],

            "competition": [

                "max_velocity",

                "race_pace"
            ]
        }

        return mapping.get(

            phase,

            [
                "race_pace"
            ]
        )

    # =================================================
    # FRESHNESS SCORE
    # =================================================

    def calculate_freshness(

        self,

        fatigue,

        soreness,

        hrv
    ):

        freshness = (

            hrv
            +
            (10 - fatigue)
            +
            (10 - soreness)
        )

        return round(

            freshness / 3,

            2
        )

    # =================================================
    # BUILD COMPETITION PROFILE
    # =================================================

    def build_profile(

        self,

        competition_type,

        days_before_competition,

        readiness
    ):

        competition_data = (

            self.classify_competition(
                competition_type
            )
        )

        phase = (

            self.get_competition_phase(
                days_before_competition
            )
        )

        taper_modifiers = (

            self.get_taper_modifiers(

                competition_data[
                    "taper_days"
                ]
            )
        )

        peak_readiness = (

            self.build_peak_readiness(
                readiness
            )
        )

        freshness = (

            self.calculate_freshness(

                peak_readiness[
                    "fatigue_subjective"
                ],

                peak_readiness[
                    "muscle_soreness"
                ],

                peak_readiness[
                    "hrv_score"
                ]
            )
        )

        return {

            "competition_type":
            competition_type,

            "importance":
            competition_data[
                "importance"
            ],

            "taper_days":
            competition_data[
                "taper_days"
            ],

            "phase":
            phase,

            "phase_objectives":
            self.get_phase_objectives(
                phase
            ),

            "taper_modifiers":
            taper_modifiers,

            "freshness_score":
            freshness,

            "peak_readiness":
            peak_readiness
        }

