
class LoadValidator:

    def __init__(self):

        pass

    # =================================================
    # SESSION LIMITS
    # =================================================

    def get_session_limits(

        self,

        specialist
    ):

        mapping = {

            "sprint": {

                "max_volume": 6000,

                "max_cns": 20
            },

            "middle_distance": {

                "max_volume": 7500,

                "max_cns": 18
            },

            "distance": {

                "max_volume": 10000,

                "max_cns": 16
            },

            "im": {

                "max_volume": 8000,

                "max_cns": 18
            }
        }

        return mapping.get(

            specialist,

            mapping[
                "middle_distance"
            ]
        )

    # =================================================
    # WEEKLY LIMITS
    # =================================================

    def get_weekly_limits(

        self,

        specialist
    ):

        mapping = {

            "sprint": {

                "max_volume": 35000,

                "max_cns": 70
            },

            "middle_distance": {

                "max_volume": 55000,

                "max_cns": 65
            },

            "distance": {

                "max_volume": 80000,

                "max_cns": 55
            },

            "im": {

                "max_volume": 60000,

                "max_cns": 65
            }
        }

        return mapping.get(

            specialist,

            mapping[
                "middle_distance"
            ]
        )

    # =================================================
    # MESOCYCLE LIMITS
    # =================================================

    def get_mesocycle_limits(

        self,

        specialist
    ):

        mapping = {

            "sprint": {

                "max_volume": 140000,

                "max_cns": 240
            },

            "middle_distance": {

                "max_volume": 220000,

                "max_cns": 220
            },

            "distance": {

                "max_volume": 320000,

                "max_cns": 180
            },

            "im": {

                "max_volume": 240000,

                "max_cns": 220
            }
        }

        return mapping.get(

            specialist,

            mapping[
                "middle_distance"
            ]
        )

    # =================================================
    # VALIDATE SESSION
    # =================================================

    def validate_session(

        self,

        specialist,

        metrics
    ):

        limits = self.get_session_limits(
            specialist
        )

        warnings = []

        if (

            metrics.get(
                "total_volume",
                0
            )

            >

            limits[
                "max_volume"
            ]
        ):

            warnings.append(
                "Session volume exceeds limit"
            )

        if (

            metrics.get(
                "total_cns",
                0
            )

            >

            limits[
                "max_cns"
            ]
        ):

            warnings.append(
                "Session CNS exceeds limit"
            )

        return {

            "valid":
            len(warnings) == 0,

            "warnings":
            warnings
        }

    # =================================================
    # VALIDATE WEEK
    # =================================================

    def validate_week(

        self,

        specialist,

        weekly_metrics
    ):

        limits = self.get_weekly_limits(
            specialist
        )

        warnings = []

        if (

            weekly_metrics.get(
                "weekly_volume",
                0
            )

            >

            limits[
                "max_volume"
            ]
        ):

            warnings.append(
                "Weekly volume exceeds limit"
            )

        if (

            weekly_metrics.get(
                "weekly_cns",
                0
            )

            >

            limits[
                "max_cns"
            ]
        ):

            warnings.append(
                "Weekly CNS exceeds limit"
            )

        return {

            "valid":
            len(warnings) == 0,

            "warnings":
            warnings
        }

    # =================================================
    # VALIDATE MESOCYCLE
    # =================================================

    def validate_mesocycle(

        self,

        specialist,

        total_volume,

        total_cns
    ):

        limits = self.get_mesocycle_limits(
            specialist
        )

        warnings = []

        if total_volume > limits[
            "max_volume"
        ]:

            warnings.append(
                "Mesocycle volume exceeds limit"
            )

        if total_cns > limits[
            "max_cns"
        ]:

            warnings.append(
                "Mesocycle CNS exceeds limit"
            )

        return {

            "valid":
            len(warnings) == 0,

            "warnings":
            warnings
        }

    # =================================================
    # GLOBAL VALIDATION
    # =================================================

    def build_validation_report(

        self,

        specialist,

        session_metrics,

        weekly_metrics,

        mesocycle_volume,

        mesocycle_cns
    ):

        session_validation = (

            self.validate_session(

                specialist,

                session_metrics
            )
        )

        week_validation = (

            self.validate_week(

                specialist,

                weekly_metrics
            )
        )

        mesocycle_validation = (

            self.validate_mesocycle(

                specialist,

                mesocycle_volume,

                mesocycle_cns
            )
        )

        return {

            "session_validation":
            session_validation,

            "week_validation":
            week_validation,

            "mesocycle_validation":
            mesocycle_validation
        }

