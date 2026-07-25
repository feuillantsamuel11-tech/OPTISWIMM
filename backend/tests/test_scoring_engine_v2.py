from app.services.exercise_repository.scoring_engine import ScoringEngine
from app.services.exercise_repository.models import Exercise


def test_perfect_match():

    engine = ScoringEngine()

    ex = Exercise(
        id="1",
        name="8x100",
        zone="Z4",
        objectives=["threshold_control"],
    )

    score = engine.score(
        ex,
        objective="threshold_control",
        zone="Z4",
    )

    assert score == 100


def test_wrong_zone():

    engine = ScoringEngine()

    ex = Exercise(
        id="1",
        name="8x100",
        zone="Z2",
        objectives=["threshold_control"],
    )

    score = engine.score(
        ex,
        objective="threshold_control",
        zone="Z4",
    )

    assert score == 50


def test_no_match():

    engine = ScoringEngine()

    ex = Exercise(
        id="1",
        name="Sprint",
        zone="Z7",
        objectives=["speed"],
    )

    score = engine.score(
        ex,
        objective="threshold_control",
        zone="Z4",
    )

    assert score == 0