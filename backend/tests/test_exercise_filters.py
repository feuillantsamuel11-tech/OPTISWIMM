from app.services.exercise_repository.filters import ExerciseFilters
from app.services.exercise_repository.models import Exercise


def test_filter_zone():

    exercises = [
        Exercise(id="1", name="A", zone="Z4"),
        Exercise(id="2", name="B", zone="Z2"),
    ]

    result = ExerciseFilters.by_zone(exercises, "Z4")

    assert len(result) == 1


def test_filter_objective():

    exercises = [
        Exercise(id="1", name="A", objective="speed"),
    ]

    result = ExerciseFilters.by_objective(
        exercises,
        "speed",
    )

    assert len(result) == 1


def test_filter_stroke():

    exercises = [
        Exercise(id="1", name="A", stroke="crawl"),
    ]

    result = ExerciseFilters.by_stroke(
        exercises,
        "crawl",
    )

    assert len(result) == 1


def test_filter_equipment():

    exercises = [
        Exercise(
            id="1",
            name="A",
            equipment=["palmes", "pull"],
        ),
    ]

    result = ExerciseFilters.by_equipment(
        exercises,
        "pull",
    )

    assert len(result) == 1


def test_filter_level():

    exercises = [
        Exercise(
            id="1",
            name="A",
            level="elite",
        ),
    ]

    result = ExerciseFilters.by_level(
        exercises,
        "elite",
    )

    assert len(result) == 1


def test_filter_distance():

    exercises = [
        Exercise(
            id="1",
            name="A",
            distance=100,
        ),
    ]

    result = ExerciseFilters.by_distance(
        exercises,
        100,
    )

    assert len(result) == 1