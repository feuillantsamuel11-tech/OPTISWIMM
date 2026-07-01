from app.services.energy_scoring import (
    calculate_energy_scores
)

from app.services.profile_thresholds import (
    get_profile_adjusted_thresholds
)

from app.services.adaptive_session_rebuilder import (
    rebuild_session_after_optimization
)


# =========================
# SESSION ORDER
# =========================

def optimize_session_order(
    session
):

    optimized = {}

    order = [

        "warmup",

        "preset",

        "speed",

        "main_set",

        "cooldown"
    ]

    for block in order:

        optimized[block] = session.get(
            block,
            []
        )

    return optimized


# =========================
# REMOVE HIGH INTENSITY
# =========================

def remove_speed_block(
    session
):

    session["speed"] = []

    return session


def remove_main_set(
    session
):

    session["main_set"] = []

    return session


# =========================
# MULTI PASS OPTIMIZATION
# =========================

def apply_multi_pass_optimization(

    session,

    thresholds,

    optimizations
):

    max_passes = 3

    current_pass = 0

    while current_pass < max_passes:

        scores = (
            calculate_energy_scores(
                session
            )
        )

        overload_detected = False

        # =========================
        # GLOBAL LOAD
        # =========================

        if (

            scores[
                "high_intensity_load"
            ]

            >

            thresholds[
                "high_intensity_load"
            ]
        ):

            session = (
                remove_speed_block(
                    session
                )
            )

            optimizations.append(

                f"Pass {current_pass + 1}: high intensity reduction"
            )

            overload_detected = True

        # =========================
        # LACTATE
        # =========================

        if (

            scores[
                "lactate_score"
            ]

            >

            thresholds[
                "lactate_score"
            ]
        ):

            session = (
                remove_speed_block(
                    session
                )
            )

            optimizations.append(

                f"Pass {current_pass + 1}: lactate reduction"
            )

            overload_detected = True

        # =========================
        # SPEED
        # =========================

        if (

            scores[
                "speed_score"
            ]

            >

            thresholds[
                "speed_score"
            ]
        ):

            session = (
                remove_speed_block(
                    session
                )
            )

            optimizations.append(

                f"Pass {current_pass + 1}: speed reduction"
            )

            overload_detected = True

        # =========================
        # VO2
        # =========================

        if (

            scores[
                "vo2_score"
            ]

            >

            thresholds[
                "vo2_score"
            ]
        ):

            session = (
                remove_main_set(
                    session
                )
            )

            optimizations.append(

                f"Pass {current_pass + 1}: VO2 reduction"
            )

            overload_detected = True

        # =========================
        # STOP CONDITION
        # =========================

        if not overload_detected:

            break

        current_pass += 1

    return session


# =========================
# ENERGY OPTIMIZATION
# =========================

def optimize_energy_systems(

    session,

    db,

    week_number,

    swimmer_profile,

    fatigue_level,

    recent_sessions,

    original_zone
):

    # =========================
    # INITIAL SCORES
    # =========================

    initial_scores = (
        calculate_energy_scores(
            session
        )
    )

    # =========================
    # THRESHOLDS
    # =========================

    thresholds = (
        get_profile_adjusted_thresholds(

            week_number=
            week_number,

            swimmer_profile=
            swimmer_profile,

            fatigue_level=
            fatigue_level
        )
    )

    optimizations = []

    # =========================
    # MULTI PASS OPTIMIZATION
    # =========================

    session = (
        apply_multi_pass_optimization(

            session=session,

            thresholds=thresholds,

            optimizations=optimizations
        )
    )

    # =========================
    # REBUILD SESSION
    # =========================

    rebuilt = (
        rebuild_session_after_optimization(

            session=session,

            db=db,

            swimmer_profile=
            swimmer_profile,

            fatigue_level=
            fatigue_level,

            recent_sessions=
            recent_sessions,

            original_zone=
            original_zone
        )
    )

    session = rebuilt[
        "rebuilt_session"
    ]

    optimizations.extend(

        rebuilt[
            "rebuild_actions"
        ]
    )

    # =========================
    # FINAL SCORES
    # =========================

    final_scores = (
        calculate_energy_scores(
            session
        )
    )

    return {

        "optimized_session":
        session,

        "initial_scores":
        initial_scores,

        "final_scores":
        final_scores,

        "thresholds":
        thresholds,

        "target_volume":
        rebuilt[
            "target_volume"
        ],

        "final_volume":
        rebuilt[
            "final_volume"
        ],

        "preserved_focus":
        rebuilt[
            "preserved_focus"
        ],

        "optimizations":
        optimizations
    }


# =========================
# GLOBAL SESSION OPTIMIZER
# =========================

def optimize_session(

    session,

    db,

    week_number,

    swimmer_profile,

    fatigue_level,

    recent_sessions,

    original_zone
):

    # =========================
    # ORDER SESSION
    # =========================

    ordered_session = (
        optimize_session_order(
            session
        )
    )

    # =========================
    # OPTIMIZATION
    # =========================

    optimized = (
        optimize_energy_systems(

            session=
            ordered_session,

            db=db,

            week_number=
            week_number,

            swimmer_profile=
            swimmer_profile,

            fatigue_level=
            fatigue_level,

            recent_sessions=
            recent_sessions,

            original_zone=
            original_zone
        )
    )

    return optimized