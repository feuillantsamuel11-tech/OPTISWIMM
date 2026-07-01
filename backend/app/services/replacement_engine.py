import copy

from app.models.exercise import Exercise


def clone_exercise(
    exercise,
    new_block_type
):

    cloned = copy.deepcopy(
        exercise
    )

    cloned.block_type = (
        new_block_type
    )

    cloned.category = (
        new_block_type
    )

    return cloned


def find_replacement_exercise(
    db,
    replacement_type,
    stroke
):

    # =========================
    # SPEED TECHNIQUE
    # =========================

    if replacement_type == "speed_technical":

        replacement = db.query(
            Exercise
        ).filter(

            Exercise.objective == "technique",

            Exercise.stroke == stroke

        ).first()

        if replacement:

            return clone_exercise(
                replacement,
                "speed"
            )

    # =========================
    # AEROBIC TECHNIQUE
    # =========================

    elif replacement_type == "aerobic_technical":

        replacement = db.query(
            Exercise
        ).filter(

            Exercise.zone_code == "Z2",

            Exercise.stroke == stroke

        ).first()

        if replacement:

            return clone_exercise(
                replacement,
                "main_set"
            )

    # =========================
    # THRESHOLD CONTROL
    # =========================

    elif replacement_type == "threshold_control":

        replacement = db.query(
            Exercise
        ).filter(

            Exercise.zone_code == "Z4",

            Exercise.stroke == stroke

        ).first()

        if replacement:

            return clone_exercise(
                replacement,
                "main_set"
            )

    # =========================
    # AEROBIC
    # =========================

    elif replacement_type == "aerobic":

        replacement = db.query(
            Exercise
        ).filter(

            Exercise.zone_code == "Z2",

            Exercise.stroke == stroke

        ).first()

        if replacement:

            return clone_exercise(
                replacement,
                "main_set"
            )

    return None