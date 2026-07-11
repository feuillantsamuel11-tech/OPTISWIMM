
from app.services.readiness_engine import (
    ReadinessEngine
)

from app.services.fatigue_engine import (
    FatigueEngine
)

from app.services.performance_prediction_engine import (
    PerformancePredictionEngine
)

from app.services.intelligent_session_builder_v10 import (
    IntelligentSessionBuilder
)


from app.services.session_serializer import (
    SessionSerializer
)

from app.services.microcycle_engine import (
    MicrocycleEngine
)

from app.services.mesocycle_engine import (
    MesocycleEngine
)

from app.services.macrocycle_engine import (
    MacrocycleEngine
)

from app.services.season_planner import (
    SeasonPlanner
)

from app.services.athlete_monitoring import (
    AthleteMonitoring
)

from app.services.load_validator import (
    LoadValidator
)

from app.services.duplication_manager import (
    DuplicationManager
)
from app.services.training_memory import (
    TrainingMemory
)
from app.services.periodization_engine import (
    PeriodizationEngine
)
from app.services.race_distance_engine import (
    RaceDistanceEngine
)
from app.services.session_engine.specialist_manager import (
    SpecialistManager
)
from app.services.context_builder import( 
    AthleteContextBuilder)

from app.services.load_analyzer import LoadAnalyzer


class AdaptiveTrainingOrchestrator:

    def __init__(self):
        
        # =============================================
        # LEGACY ENGINES
        # =============================================

        self.readiness_engine = (
            ReadinessEngine()
        )

        self.periodization_engine = (
            PeriodizationEngine()
        )

        self.fatigue_engine = (
            FatigueEngine()
        )

        self.prediction_engine = (
            PerformancePredictionEngine()
        )

        self.session_builder = (
            IntelligentSessionBuilder()
        )
        self.training_memory = (
            TrainingMemory()
        )

        self.serializer = (
            SessionSerializer()
        )
        self.race_distance_engine = (
            RaceDistanceEngine()
        )
        self.context_builder = AthleteContextBuilder()

        self.load_analyzer = LoadAnalyzer()

        # =============================================
        # LONGITUDINAL ENGINES
        # =============================================

        self.microcycle_engine = (
            MicrocycleEngine()
        )

        self.mesocycle_engine = (
            MesocycleEngine()
        )

        self.macrocycle_engine = (
            MacrocycleEngine()
        )

        self.season_planner = (
            SeasonPlanner()
        )

        # =============================================
        # STABILIZATION ENGINES
        # =============================================

        self.monitoring = (
            AthleteMonitoring()
        )

        self.validator = (
            LoadValidator()
        )

        self.duplication = (
            DuplicationManager()
        )

       # =================================================
       # BUILD ADAPTIVE SESSION
       # =================================================

    def build_adaptive_session(

        self,

        athlete_profile=None,

        athlete_data=None,

        readiness_inputs=None,

        previous_sessions=None,

        current_block=None,

        target_competition=None,

        **kwargs
    ):

        # =============================================
        # LEGACY COMPATIBILITY
        # =============================================

        if athlete_profile is None:

            athlete_profile = athlete_data

        athlete_state = dict(
            athlete_profile or {}
        )

        specialist = athlete_state.get(
            "specialist",
            "middle_distance"
        )

        race_distance = athlete_state.get(
            "race_distance",
            400
        )

        distance_profile = (
            self.race_distance_engine.get_distance_profile(
                race_distance
            )
        )

        profile = SpecialistManager().build_profile(
            athlete_state
        )

        specialist = profile["specialist"]

        athlete_state["specialist"] = specialist

        print(
            "ATHLETE STATE:",
            athlete_state
        )

        print(
            "RACE DISTANCE:",
            race_distance
        )

        print(
            "DISTANCE PROFILE:",
            distance_profile
        )

        if not athlete_state.get("distance_focus"):

            athlete_state["distance_focus"] = (
                distance_profile["focus"]
            )

        # =============================================
        # READINESS INPUTS
        # =============================================

        readiness_inputs = readiness_inputs or {}

        athlete_state.update(
            readiness_inputs
        )

        # =============================================
        # OPTIONAL CONTEXT
        # =============================================

        athlete_state["previous_sessions"] = (
            previous_sessions or []
        )

        athlete_state["current_block"] = (
            current_block
        )

        athlete_state["target_competition"] = (
            target_competition
        )

        # =============================================
        # EXTRA KWARGS
        # =============================================

        athlete_state.update(kwargs)

        # =============================================
        # FATIGUE ESTIMATION
        # =============================================

        fatigue_state = (

            self.fatigue_engine
            .estimate_fatigue_state(
                athlete_state
            )
        )

        athlete_state[
            "fatigue_state"
        ] = fatigue_state.get(
            "fatigue_state",
            "low"
        )

        athlete_state[
            "estimated_cns"
        ] = fatigue_state.get(
            "estimated_cns",
            0
        )

        athlete_state[
            "estimated_soreness"
        ] = fatigue_state.get(
            "estimated_soreness",
            0
        )

        # =============================================
        # READINESS
        # =============================================

        readiness_state = (

            self.readiness_engine
            .calculate_readiness(
                athlete_state
            )
        )

        athlete_state[
            "readiness_score"
        ] = readiness_state.get(
            "readiness_score",
            50
        )

        athlete_state[
            "readiness_state"
        ] = readiness_state.get(
            "readiness_state",
            "moderate"
        )

        # =============================================
        # DUPLICATION PROFILE
        # =============================================

        duplication_profile = (

            self.duplication.build_profile(
                previous_sessions or []
            )
        )

        # =============================================
        # PREVIEW SESSION
        # =============================================

        preview_session = (

            self.session_builder
            .build_session(

                athlete=athlete_state,

                readiness=athlete_state
            )
        )

        session_identity = (
            preview_session.get(
                "session_identity",
                "balanced"
            )
        )

        # =============================================
        # PERFORMANCE PREDICTION
        # =============================================

        prediction = (

            self.prediction_engine
            .predict_performance(

                readiness_score=athlete_state.get(
                    "readiness_score",
                    50
                ),

                readiness_state=athlete_state.get(
                    "readiness_state",
                    "moderate"
                ),

                fatigue_state=athlete_state.get(
                    "fatigue_state",
                    "low"
                ),

                session_identity=session_identity
            )
        )

        athlete_state.update(
            prediction
        )

        # =============================================
        # FINAL SESSION
        # =============================================
        recent_objectives = (

            self.training_memory
            .get_recent_primary_objectives(

                athlete_state.get(
                    "id",
                    1
        )
    )
)
        session_count = (

            self.training_memory
            .get_session_count(

                athlete_state.get(
                   "id",
                   1
        )
    )
)
        meso_structure = (

            self.mesocycle_engine
            .get_current_structure(

                session_count
            )
        )

        print(
            "MESOCYCLE:",
            meso_structure
        )
        athlete_state[
            "mesocycle_structure"
        ] = meso_structure
        
        microcycle_day = (

            session_count % 7

        ) + 1

        daily_focus = (

            self.periodization_engine
            .get_daily_focus(

                athlete_state.get(
                    "specialist",
                    "middle_distance"
                ),
            
                microcycle_day
            )
        )    
        
        print(
            "DAILY FOCUS:",
            daily_focus
        )
        athlete_state[
            "daily_focus"
        ] = daily_focus

        print(
            "MICROCYCLE DAY:",
            microcycle_day
        )

        print(
            "RECENT OBJECTIVES:",
            recent_objectives
)
                       
        recent_cns = (

            self.training_memory
            .get_recent_cns(

                athlete_state.get(
                    "id",
                    1
                )
            )
        )

        print(
            "RECENT CNS:",
            recent_cns
        )
        recent_loads = (

            self.training_memory
            .get_recent_training_loads(

                athlete_state.get(
                    "id",
                    1
                )
            )
        )

        print(
            "RECENT LOADS:",
            recent_loads
        )
        print(
            "LOAD COUNT:",
            len(
                recent_loads
            )
        )

        acute_load = sum(
            recent_loads[:7]
        )

        if len(recent_loads) < 28:

            chronic_load = 0

            acwr = 1.0

            load_state = "building"

        else:

            chronic_load = (

                sum(
                    recent_loads[:28]
                ) / 4
            )

            acwr = (

                acute_load /
                chronic_load
            )

            load_state = "normal"

            if acwr > 1.5:

                load_state = "overload"

            elif acwr < 0.8:

                load_state = "underload"

        print(
            "ACUTE LOAD:",
            acute_load
        )

        print(
            "CHRONIC LOAD:",
            chronic_load
        )

        print(
            "ACWR:",
            round(
                acwr,
                2
            )
        )

        print(
            "LOAD STATE:",
            load_state
        )
    
        
        print(
            "ACUTE LOAD:",
            acute_load
        )

        print(
            "CHRONIC LOAD:",
            round(
                chronic_load,
                2
            )
        )

        print(
            "ACWR:",
            round(
                acwr,
                2
            )
        )
        
        

        print(
            "LOAD STATE:",
            load_state
        )

        cumulative_cns = sum(
            recent_cns
        )

        print(
            "CUMULATIVE CNS:",
            cumulative_cns
        )

        cns_fatigue = "low"

        if cumulative_cns >= 30:

            cns_fatigue = "high"

        elif cumulative_cns >= 15:

            cns_fatigue = "moderate"

        print(
            "CNS FATIGUE:",
            cns_fatigue
        )


        objective_blocklist = []

        if recent_objectives.count(
            "race_pace"
        ) >= 2:

            objective_blocklist.append(
            "race_pace"
            )
        
        print(
            "BLOCKLIST:",
            objective_blocklist
        )

        athlete_state[
            "objective_blocklist"
        ] = objective_blocklist
        athlete_state[
            "cns_fatigue"
        ] = cns_fatigue
        
        athlete_state[
            "load_state"
        ] = load_state

        athlete_state[
            "acwr"
        ] = acwr

        adaptive_session = (

            self.session_builder
            .build_session(

                athlete=athlete_state,

                readiness=athlete_state
            )
        )
        # Determine session identity and objectives
        session_identity = adaptive_session.get("session_identity", "")

        primary_objective = None
        secondary_objective = None

        if session_identity == "threshold_control":

            primary_objective = (
                "threshold_control"
            )

            secondary_objective = None

        elif "threshold_control" in session_identity:

            secondary_objective = (
                "threshold_control"
            )

        print(
            "SAVE SESSION:",
            session_identity,
            primary_objective,
            secondary_objective,
        )
   
        metrics = (
            adaptive_session.get(
                "metrics",
                {}
            )
        )

        training_load = (
            metrics.get(
                "total_volume",
                0
            )
        )

        average_intensity = (
            metrics.get(
                "average_intensity",
                1
            )
        )

        duration_minutes = max(
            30,
            int(
                training_load / 50
            )
        )

        rpe = max(
            1,
            round(
                average_intensity
            )
        )

        session_score = (
            duration_minutes * rpe
        )

        print(
            "TRAINING LOAD:",
            training_load
        )

        print(
            "DURATION:",
            duration_minutes
        )

        print(
            "RPE:",
            rpe
        )

        print(
            "SESSION SCORE:",
            session_score
        )

        self.training_memory.save_generated_session(

            athlete_id=
            athlete_state.get(
                "id",
                1
            ),

            session_identity=
            session_identity,

            primary_objective=
            primary_objective,

            secondary_objective=
            secondary_objective,

            total_cns=
            adaptive_session
            .get(
                "metrics",
                {}
            )
            .get(
                "total_cns",
                0
            ),

            training_load=
            training_load,

            duration_minutes=
            duration_minutes,

            rpe=
            rpe,

            session_score=
            session_score
        )
        print("SESSION SAVED")
            
        # =============================================
        # VALIDATION
        # =============================================

        validation = (

            self.validator.validate_session(

                athlete_state.get(
                    "specialist",
                    "middle_distance"
                ),

                adaptive_session.get(
                    "metrics",
                    {}
                )
            )
        )

        # =============================================
        # MONITORING
        # =============================================

        monitoring = (

            self.monitoring.build_profile(

                readiness=athlete_state,

                weekly_cns_history=[],

                latest_session=
                adaptive_session.get(
                    "metrics",
                    {}
                )
            )
        )

        # =============================================
        # SERIALIZATION
        # =============================================

        serialized_session = (

            self.serializer
            .serialize_session(
                adaptive_session
            )
        )

        # =============================================
        # FINAL RESPONSE
        # =============================================

        return {

            "profile":
            athlete_profile,

            "fatigue_state":
            fatigue_state,

            "readiness_state":
            readiness_state,

            "prediction":
            prediction,

            "monitoring":
            monitoring,

            "validation":
            validation,

            "duplication":
            duplication_profile,

            "adaptive_session":
            serialized_session
        }

    # =================================================
    # GENERATE MICROCYCLE
    # =================================================

    def generate_microcycle(

        self,

        athlete,

        readiness
    ):

        microcycle = (

            self.microcycle_engine
            .generate_microcycle(

                athlete,

                readiness
            )
        )

        validation = (

            self.validator.validate_week(

                athlete.get(
                    "specialist",
                    "middle_distance"
                ),

                microcycle.get(
                    "weekly_metrics",
                    {}
                )
            )
        )

        return {

            "microcycle":
            microcycle,

            "validation":
            validation
        }

    # =================================================
    # GENERATE MESOCYCLE
    # =================================================

    def generate_mesocycle(

        self,

        athlete,

        readiness
    ):

        mesocycle = (

            self.mesocycle_engine
            .generate_mesocycle(

                athlete,

                readiness
            )
        )

        validation = (

            self.validator.validate_mesocycle(

                athlete.get(
                    "specialist",
                    "middle_distance"
                ),

                mesocycle.get(
                    "total_volume",
                    0
                ),

                mesocycle.get(
                    "total_cns",
                    0
                )
            )
        )

        return {

            "mesocycle":
            mesocycle,

            "validation":
            validation
        }

    # =================================================
    # GENERATE MACROCYCLE
    # =================================================

    def generate_macrocycle(

        self,

        athlete,

        readiness
    ):

        macrocycle = (

            self.macrocycle_engine
            .generate_macrocycle(

                athlete,

                readiness
            )
        )

        return {

            "macrocycle":
            macrocycle
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

        season = (

            self.season_planner
            .generate_season(

                athlete,

                readiness,

                competitions
            )
        )

        return {

            "season":
            season
        }

