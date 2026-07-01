from sqlalchemy import or_

from app.models.exercise import Exercise

from app.services.semantic_training_preservation import (
    get_preserved_training_focus
)

from app.services.diversity_engine import (
    filter_already_used_exercises
)


def calculate_target_volume(
    swimmer_profile,
    fatigue_level
):

    base_volume = 2500

    if swimmer_profile[
        "volume_factor"
    ] > 1.2:

        base_volume = 3500

    elif swimmer_profile[
        "volume_factor"
    ] < 0.8:

        base_volume = 1800

    if fatigue_level == "extreme":

        base_volume *= 0.6

    elif fatigue_level == "high":

        base_volume *= 0.75

    return int(base_volume)


def estimate_session_volume(
    session
):

    total = 0

    for block_type in session:

        for ex in session[
            block_type
        ]:

            if hasattr(
                ex,
                "volume"
            ):

                total += (
                    ex.volume or 0
                )

    return total


def find_diverse_replacement(

    db,

    replacement_type,

    recent_sessions,

    stroke="crawl"
):

    exercises = (

        db.query(
            Exercise
        )

        .filter(

            Exercise.stroke == stroke,

            or_(

                Exercise.objective ==
                replacement_type,

                Exercise.category ==
                replacement_type
            )
        )

        .all()
    )

    if len(exercises) == 0:

        return None

    filtered = (
        filter_already_used_exercises(
            exercises,
            recent_sessions
        )
    )

    return filtered[0]


def rebuild_session_after_optimization(

    session,

    db,

    swimmer_profile,

    fatigue_level,

    recent_sessions,

    original_zone
):

    rebuild_actions = []

    target_volume = (
        calculate_target_volume(

            swimmer_profile,

            fatigue_level
        )
    )

    preserved_focus = (
        get_preserved_training_focus(
            original_zone
        )
    )

    # =========================
    # SPEED REBUILD
    # =========================

    if len(
        session.get(
            "speed",
            []
        )
    ) == 0:

        replacement = (
            find_diverse_replacement(

                db=db,

                replacement_type=
                preserved_focus,

                recent_sessions=
                recent_sessions,

                stroke="crawl"
            )
        )

        if replacement:

            session[
                "speed"
            ] = [
                replacement
            ]

            rebuild_actions.append(

                f"Preserved focus rebuild: {preserved_focus}"
            )

    # =========================
    # MAIN SET REBUILD
    # =========================

    if len(
        session.get(
            "main_set",
            []
        )
    ) == 0:

        replacement = (
            find_diverse_replacement(

                db=db,

                replacement_type=
                preserved_focus,

                recent_sessions=
                recent_sessions,

                stroke="crawl"
            )
        )

        if replacement:

            session[
                "main_set"
            ] = [
                replacement
            ]

            rebuild_actions.append(
                "Main set intelligently rebuilt"
            )

    # =========================
    # TARGET VOLUME
    # =========================

    current_volume = (
        estimate_session_volume(
            session
        )
    )

    while current_volume < target_volume:

        extra = (
            find_diverse_replacement(

                db=db,

                replacement_type=
                "aerobic",

                recent_sessions=
                recent_sessions,

                stroke="crawl"
            )
        )

        if not extra:

            break

        session[
            "main_set"
        ].append(
            extra
        )

        current_volume = (
            estimate_session_volume(
                session
            )
        )

        rebuild_actions.append(
            "Recovery volume added"
        )

        if current_volume > 8000:

            break

    return {

        "rebuilt_session":
        session,

        "rebuild_actions":
        rebuild_actions,

        "target_volume":
        target_volume,

        "final_volume":
        current_volume,

        "preserved_focus":
        preserved_focus
    }