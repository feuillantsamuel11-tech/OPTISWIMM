
from app.services.macrocycle_engine import (
    MacrocycleEngine
)

from app.services.competition_engine import (
    CompetitionEngine
)


class SeasonPlanner:

    def __init__(self):

        self.macrocycle_engine = (
            MacrocycleEngine()
        )

        self.competition_engine = (
            CompetitionEngine()
        )

    # =================================================
    # SORT COMPETITIONS
    # =================================================

    def sort_competitions(

        self,

        competitions
    ):

        return sorted(

            competitions,

            key=lambda c:
            c["week"]
        )

    # =================================================
    # BUILD SEASON BLOCKS
    # =================================================

    def build_season_blocks(

        self,

        competitions
    ):

        blocks = []

        previous_week = 1

        competitions = (
            self.sort_competitions(
                competitions
            )
        )

        for competition in competitions:

            competition_week = (
                competition["week"]
            )

            preparation_weeks = max(

                4,

                competition_week
                -
                previous_week
                -
                2
            )

            # =========================================
            # PREPARATION BLOCK
            # =========================================

            blocks.append({

                "type":
                "preparation",

                "start_week":
                previous_week,

                "end_week":
                competition_week - 2,

                "weeks":
                preparation_weeks
            })

            # =========================================
            # TAPER BLOCK
            # =========================================

            blocks.append({

                "type":
                "taper",

                "start_week":
                competition_week - 1,

                "end_week":
                competition_week - 1,

                "weeks":
                1
            })

            # =========================================
            # COMPETITION BLOCK
            # =========================================

            blocks.append({

                "type":
                "competition",

                "competition":
                competition,

                "start_week":
                competition_week,

                "end_week":
                competition_week,

                "weeks":
                1
            })

            previous_week = (
                competition_week + 1
            )

        # =============================================
        # FINAL TRANSITION
        # =============================================

        blocks.append({

            "type":
            "transition",

            "start_week":
            previous_week,

            "end_week":
            previous_week + 1,

            "weeks":
            2
        })

        return blocks

    # =================================================
    # PHASE READINESS
    # =================================================

    def adjust_phase_readiness(

        self,

        readiness,

        block_type
    ):

        adjusted = readiness.copy()

        # =============================================
        # PREPARATION
        # =============================================

        if block_type == "preparation":

            adjusted[
                "motivation"
            ] = min(

                10,

                adjusted.get(
                    "motivation",
                    5
                ) + 1
            )

        # =============================================
        # TAPER
        # =============================================

        elif block_type == "taper":

            adjusted[
                "fatigue_subjective"
            ] = max(

                1,

                adjusted.get(
                    "fatigue_subjective",
                    5
                ) - 3
            )

            adjusted[
                "muscle_soreness"
            ] = max(

                1,

                adjusted.get(
                    "muscle_soreness",
                    5
                ) - 2
            )

            adjusted[
                "hrv_score"
            ] = min(

                10,

                adjusted.get(
                    "hrv_score",
                    5
                ) + 2
            )

        # =============================================
        # TRANSITION
        # =============================================

        elif block_type == "transition":

            adjusted[
                "stress_level"
            ] = max(

                1,

                adjusted.get(
                    "stress_level",
                    5
                ) - 2
            )

        return adjusted

    # =================================================
    # BUILD COMPETITION PEAK
    # =================================================

    def build_competition_peak(

        self,

        competition,

        readiness
    ):

        competition_profile = (

            self.competition_engine
            .build_profile(

                competition_type=
                competition[
                    "type"
                ],

                days_before_competition=1,

                readiness=readiness
            )
        )

        return {

            "competition":
            competition,

            "profile":
            competition_profile
        }

    # =================================================
    # GENERATE SEASON
    # =================================================

    def generate_season(

        self,

        athlete,

        readiness,

        competitions
    ):

        season_blocks = (

            self.build_season_blocks(
                competitions
            )
        )

        season = []

        cumulative_volume = 0

        cumulative_cns = 0

        # =============================================
        # BUILD BLOCKS
        # =============================================

        for block_index, block in enumerate(
            season_blocks
        ):

            block_type = block[
                "type"
            ]

            adjusted_readiness = (

                self.adjust_phase_readiness(

                    readiness,

                    block_type
                )
            )

            # =========================================
            # PREPARATION
            # =========================================

            if block_type == "preparation":

                macrocycle = (

                    self.macrocycle_engine
                    .generate_macrocycle(

                        athlete,

                        adjusted_readiness
                    )
                )

                block[
                    "content"
                ] = macrocycle

                cumulative_volume += (
                    macrocycle[
                        "season_volume"
                    ]
                )

                cumulative_cns += (
                    macrocycle[
                        "season_cns"
                    ]
                )

            # =========================================
            # TAPER
            # =========================================

            elif block_type == "taper":

                taper_profile = (

                    self.competition_engine
                    .build_profile(

                        competition_type=
                        "national",

                        days_before_competition=5,

                        readiness=
                        adjusted_readiness
                    )
                )

                block[
                    "content"
                ] = taper_profile

            # =========================================
            # COMPETITION
            # =========================================

            elif block_type == "competition":

                competition_peak = (

                    self.build_competition_peak(

                        block[
                            "competition"
                        ],

                        adjusted_readiness
                    )
                )

                block[
                    "content"
                ] = competition_peak

            # =========================================
            # TRANSITION
            # =========================================

            elif block_type == "transition":

                block[
                    "content"
                ] = {

                    "focus":
                    "recovery",

                    "objectives": [

                        "parasympathetic",

                        "mobility"
                    ]
                }

            block[
                "block_number"
            ] = block_index + 1

            season.append(
                block
            )

        # =============================================
        # FINAL RESPONSE
        # =============================================

        return {

            "athlete_specialist":
            athlete.get(

                "specialist",

                "middle_distance"
            ),

            "season_blocks":
            len(season),

            "annual_volume":
            cumulative_volume,

            "annual_cns":
            cumulative_cns,

            "season":
            season
        }
