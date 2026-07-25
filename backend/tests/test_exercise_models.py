from app.services.exercise_repository.models import Exercise


def test_create_exercise():

    ex = Exercise(
        id="EX001",
        name="8x50 Crawl",
    )

    assert ex.id == "EX001"
    assert ex.name == "8x50 Crawl"


def test_equipment_default():

    ex = Exercise(
        id="1",
        name="Test",
    )

    assert ex.equipment == []


def test_tags_default():

    ex = Exercise(
        id="1",
        name="Test",
    )

    assert ex.tags == []


def test_historical_score_default():

    ex = Exercise(
        id="1",
        name="Test",
    )

    assert ex.historical_score == 0.0