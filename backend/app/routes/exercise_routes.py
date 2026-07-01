from fastapi import APIRouter
from fastapi import Query

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.exercise import Exercise

from app.schemas.exercise_schema import ExerciseCreate

router = APIRouter()


@router.post("/exercises")
def create_exercise(exercise: ExerciseCreate):

    db: Session = SessionLocal()

    new_exercise = Exercise(

        title=exercise.title,

        category=exercise.category,

        stroke=exercise.stroke,

        zone_code=exercise.zone_code,

        distance=exercise.distance,

        equipment=exercise.equipment,

        objective=exercise.objective,

        difficulty=exercise.difficulty,

        cns_load=exercise.cns_load,

        description=exercise.description,

        block_type=exercise.block_type,

        season_phase=exercise.season_phase,

        swimmer_level=exercise.swimmer_level,

        min_age=exercise.min_age,

        max_age=exercise.max_age,

        volume=exercise.volume,

        rest_seconds=exercise.rest_seconds,

        intensity_score=exercise.intensity_score
    )

    db.add(new_exercise)

    db.commit()

    db.refresh(new_exercise)

    db.close()

    return new_exercise


@router.get("/exercises")
def get_exercises(
    zone: str = Query(default=None),
    stroke: str = Query(default=None),
    category: str = Query(default=None)
):

    db: Session = SessionLocal()

    query = db.query(Exercise)

    if zone:
        query = query.filter(Exercise.zone_code == zone)

    if stroke:
        query = query.filter(Exercise.stroke == stroke)

    if category:
        query = query.filter(Exercise.category == category)

    exercises = query.all()

    db.close()

    return exercises