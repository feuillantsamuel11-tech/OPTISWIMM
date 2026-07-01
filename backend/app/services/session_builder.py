from sqlalchemy.orm import Session

from app.models.exercise import Exercise

from app.services.exercise_selector import (
    select_exercises
)


def build_session(
    db: Session,
    stroke: str,
    main_zone: str,
    week_number: int
):

    # WARMUP
    warmup_query = db.query(Exercise).filter(
       Exercise.category == "warmup"
    ).all()

    # PRESET
    preset_query = db.query(Exercise).filter(
        Exercise.category == "preset",
        Exercise.stroke == stroke
    ).all()

    # MAIN SET
    main_set_query = db.query(Exercise).filter(
        Exercise.category == "main_set",
        Exercise.zone_code == main_zone,
        Exercise.stroke == stroke
    ).all()

    # SPEED
    speed_query = db.query(Exercise).filter(
        Exercise.category == "speed",
        Exercise.stroke == stroke
    ).all()

    # COOLDOWN
    cooldown_query = db.query(Exercise).filter(
        Exercise.category == "cooldown"
    ).all()

    # SÉLECTION INTELLIGENTE

    warmup = select_exercises(
        warmup_query,
        week_number=week_number,
        max_count=1
    )

    preset = select_exercises(
        preset_query,
        week_number=week_number,
        max_count=1
    )

    main_set = select_exercises(
        main_set_query,
        week_number=week_number,
        max_count=1
    )

    speed = select_exercises(
        speed_query,
        week_number=week_number,
        max_count=1
    )

    cooldown = select_exercises(
        cooldown_query,
        week_number=week_number,
        max_count=1
    )

    return {

        "warmup": warmup,

        "preset": preset,

        "main_set": main_set,

        "speed": speed,

        "cooldown": cooldown
    }