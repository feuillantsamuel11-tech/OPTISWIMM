from app.services.training_distribution_engine import (
    TrainingDistributionEngine
)

from app.services.session_identity_engine import (
    SessionIdentityEngine
)

from app.services.intelligent_session_builder import (
    IntelligentSessionBuilder
)


class MicrocyclePlanner:

    def __init__(self):

        self.distribution_engine = (
            TrainingDistributionEngine()
        )

        self.identity_engine = (
            SessionIdentityEngine()
        )

        self.session_builder = (
            IntelligentSessionBuilder()
        )

    # =================================================
    # BUILD MICROCYCLE
    # =================================================

    def build_microcycle(

        self,

        athlete_state,

        days=6,

        distribution_model="polarized"
    ):

        microcycle = []

        previous_sessions = []

        for day in range(days):

            # -----------------------------------------
            # SELECT SESSION IDENTITY
            # -----------------------------------------

            session_identity = (

                self.select_session_identity(

                    athlete_state,

                    previous_sessions,

                    distribution_model
                )
            )

            athlete_state[
                "forced_session_identity"
            ] = session_identity

            # -----------------------------------------
            # GENERATE SESSION
            # -----------------------------------------

            session = (

                self.session_builder
                .generate(
                    athlete_state
                )
            )

            microcycle.append(session)

            previous_sessions.append(
                session
            )

        # ---------------------------------------------
        # ANALYZE DISTRIBUTION
        # ---------------------------------------------

        distribution_analysis = (

            self.distribution_engine
            .analyze_microcycle(
                microcycle
            )
        )

        warnings = (

            self.distribution_engine
            .distribution_warning(

                microcycle,

                distribution_model
            )
        )

        return {

            "microcycle":
            microcycle,

            "distribution":
            distribution_analysis,

            "warnings":
            warnings
        }

    # =================================================
    # SELECT SESSION IDENTITY
    # =================================================

    def select_session_identity(

        self,

        athlete_state,

        previous_sessions,

        distribution_model
    ):

        # =============================================
        # RECOVERY AFTER HIGH CNS
        # =============================================

        if len(previous_sessions) > 0:

            last_session = previous_sessions[-1]

            identity = last_session.get(
                "session_identity",
                ""
            )

            if identity in [

                "sprint_neural",

                "lactate_overload"
            ]:

                return "aerobic_recovery"

        # =============================================
        # TWO HIGH CNS SESSIONS
        # =============================================

        if len(previous_sessions) >= 2:

            last_two = previous_sessions[-2:]

            high_cns_count = 0

            for s in last_two:

                metrics = s.get(
                    "metrics",
                    {}
                )

                if (
                    metrics.get(
                        "total_cns",
                        0
                    ) >= 8
                ):

                    high_cns_count += 1

            if high_cns_count >= 2:

                return "aerobic_recovery"

        # =============================================
        # DISTRIBUTION ANALYSIS
        # =============================================

        analysis = (

            self.distribution_engine
            .analyze_microcycle(
                previous_sessions
            )
        )

        model = (

            self.distribution_engine
            .get_model(
                distribution_model
            )
        )

        # =============================================
        # PRIORITY LOW INTENSITY
        # =============================================

        if (

            analysis["low_intensity"]

            <

            model["low_intensity"]
        ):

            return "aerobic_recovery"

        # =============================================
        # SPECIALIST LOGIC
        # =============================================

        specialist = athlete_state.get(
            "specialist",
            "middle_distance"
        )

        if specialist == "sprint":

            return "sprint_neural"

        elif specialist == "distance":

            return "threshold_build"

        return "race_pace_precision"