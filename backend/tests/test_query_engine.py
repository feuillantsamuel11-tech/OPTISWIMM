from app.services.exercise_repository.models import Exercise
from app.services.exercise_repository.query_engine import QueryEngine


def test_query_single_filter():

    engine = QueryEngine()

    exercises = [
        Exercise(id="1", name="A", zone="Z4"),
        Exercise(id="2", name="B", zone="Z2"),
    ]

    result = engine.search(
        exercises,
        zone="Z4",
    )

    assert len(result) == 1


def test_query_multiple_filters():

    engine = QueryEngine()

    exercises = [
        Exercise(
            id="1",
            name="A",
            zone="Z4",
            objective="speed",
            stroke="crawl",
        ),
        Exercise(
            id="2",
            name="B",
            zone="Z4",
            objective="endurance",
            stroke="crawl",
        ),
    ]

    result = engine.search(
        exercises,
        zone="Z4",
        objective="speed",
    )

    assert len(result) == 1


def test_query_no_result():

    engine = QueryEngine()

    exercises = [
        Exercise(
            id="1",
            name="A",
            zone="Z2",
        )
    ]

    result = engine.search(
        exercises,
        zone="Z7",
    )

    assert len(result) == 0