from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.generator_schema import (
    SessionGenerateRequest
)

from app.services.swimmer_profiles import (
    get_swimmer_profile
)

from app.services.microcycle_engine import (
    analyze_microcycle
)

from app.services.session_builder import (
    build_session
)

from app.services.constraints_engine import (
    validate_session
)

from app.services.fatigue_manager import (
    adapt_session
)

from app.services.progression_engine import (
    apply_progression
)

from app.services.energy_system_manager import (
    validate_energy_balance
)

from app.services.energy_scoring import (
    calculate_energy_scores
)

from app.services.session_coherence_engine import (
    validate_session_coherence
)

from app.services.session_optimizer import (
    optimize_session
)

from app.services.fatigue_memory_engine import (
    calculate_accumulated_fatigue
)

from app.services.history_manager import (
    save_training_session,
    get_recent_sessions,
    get_week_load,
    get_recent_cns_load,
    get_high_intensity_frequency
)

router = APIRouter()


@router.post("/generate-session")
def generate_session(
    data: SessionGenerateRequest
):

    db: Session = SessionLocal()

    try:

        # =========================
        # 1 — SWIMMER PROFILE
        # =========================

        swimmer_profile = (
            get_swimmer_profile(
                data.swimmer_profile
            )
        )

        # =========================
        # 2 — RECENT HISTORY
        # =========================

        recent_sessions = (
            get_recent_sessions(
                db=db,
                limit=7
            )
        )

        # Fallback si vide
        if len(recent_sessions) == 0:

            recent_sessions = [

                {
                    "training_load": 0,
                    "high_cns_blocks": 0,
                    "session_type": "Z1"
                }
            ]

        # =========================
        # 3 — FATIGUE MEMORY
        # =========================

        fatigue_memory = (
            calculate_accumulated_fatigue(
                recent_sessions
            )
        )

        # =========================
        # 4 — MICROCYCLE ANALYSIS
        # =========================

        microcycle_analysis = (
            analyze_microcycle(
                recent_sessions
            )
        )

        # =========================
        # 5 — BUILD SESSION
        # =========================

        initial_session = build_session(
            db=db,
            stroke=data.stroke,
            main_zone=data.zone,
            week_number=data.week_number
        )

        # =========================
        # 6 — SESSION OPTIMIZATION
        # =========================

        optimization = optimize_session(

    session=
    initial_session,

    db=db,

    week_number=
    data.week_number,

    swimmer_profile=
    swimmer_profile,

    fatigue_level=
    fatigue_memory[
        "fatigue_level"
    ],

    recent_sessions=
    recent_sessions,

    original_zone=
    data.zone
)

        optimized_session = (
            optimization[
                "optimized_session"
            ]
        )

        # =========================
        # 7 — PROFILE PROTECTION
        # =========================

        # Protection profils fragiles
        if (
            data.swimmer_profile
            in [
                "master",
                "youth"
            ]
        ):

            if (
                fatigue_memory[
                    "fatigue_level"
                ] in [
                    "high",
                    "extreme"
                ]
            ):

                optimized_session[
                    "speed"
                ] = []

                fatigue_memory[
                    "recommendations"
                ].append(
                    "Speed removed for protective profile"
                )

        # Protection fatigue extrême
        elif (
            fatigue_memory[
                "fatigue_level"
            ] == "extreme"
        ):

            optimized_session[
                "speed"
            ] = []

            fatigue_memory[
                "recommendations"
            ].append(
                "Speed removed due to extreme fatigue"
            )

        # Protection microcycle sprint
        if (
            "Avoid additional sprint sessions"

            in

            microcycle_analysis[
                "recommendations"
            ]
        ):

            optimized_session[
                "speed"
            ] = []

        # =========================
        # 8 — ANALYSES
        # =========================

        analysis = validate_session(
            optimized_session
        )

        energy_analysis = (
            validate_energy_balance(
                optimized_session
            )
        )

        energy_scores = (
            calculate_energy_scores(
                optimized_session
            )
        )

        coherence_analysis = (
            validate_session_coherence(
                optimized_session
            )
        )

        # =========================
        # 9 — LOCAL ADAPTATION
        # =========================

        adaptation = adapt_session(
            session=optimized_session,
            analysis=analysis
        )

        # =========================
        # 10 — PROGRESSION
        # =========================

        progression = apply_progression(
            analysis=analysis,
            week_number=data.week_number
        )

        # =========================
        # 11 — SAVE SESSION
        # =========================

        saved_session = (
            save_training_session(

                db=db,

                analysis=analysis,

                fatigue_memory=
                fatigue_memory,

                energy_scores=
                energy_scores,

                week_number=
                data.week_number,

                stroke=
                data.stroke,

                session_type=
                data.zone
            )
        )

        # =========================
        # 12 — HISTORY METRICS
        # =========================

        weekly_load = (
            get_week_load(
                db,
                data.week_number
            )
        )

        recent_cns = (
            get_recent_cns_load(
                db
            )
        )

        intensity_frequency = (
            get_high_intensity_frequency(
                db
            )
        )

        # =========================
        # 13 — FINAL RESPONSE
        # =========================

        return {

            "swimmer_profile":
            swimmer_profile,

            "week_context": {

                "week_number":
                data.week_number,

                "dynamic_thresholds":
                optimization[
                    "thresholds"
                ]
            },

            "fatigue_memory":
            fatigue_memory,

            "microcycle_analysis":
            microcycle_analysis,

            "history_metrics": {

                "weekly_load":
                weekly_load,

                "recent_cns":
                recent_cns,

                "intensity_frequency":
                intensity_frequency
            },

            "saved_session_id":
            saved_session.id,

            "initial_session":
            initial_session,

            "optimized_session":
            optimized_session,

            "analysis":
            analysis,

            "energy_analysis":
            energy_analysis,

            "energy_scores":
            energy_scores,

            "coherence_analysis":
            coherence_analysis,

            "optimization":
            optimization,

            "adaptation":
            adaptation,

            "progression":
            progression
        }

    finally:

        db.close()