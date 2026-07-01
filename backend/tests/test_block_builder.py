import pytest

from app.services.session_engine.block_builder import BlockBuilder


class FakeExercise:

    def __init__(
        self,
        title,
        intensity=5,
        volume=100,
        race_specificity="all",
        cns=2,
        fatigue=2,
        difficulty="national"
    ):
        self.title = title
        self.intensity_score = intensity
        self.volume = volume
        self.race_specificity = race_specificity
        self.cns_load = cns
        self.fatigue_cost = fatigue
        self.difficulty_level = difficulty


@pytest.fixture
def builder():
    return BlockBuilder()


def test_normalize_title(builder):
    assert builder.normalize_title(" Test ") == "test"


def test_filter_intensity(builder):

    exercises = [
        FakeExercise("A", intensity=3),
        FakeExercise("B", intensity=8),
        FakeExercise("C", intensity=10),
    ]

    result = builder.filter_intensity(
        exercises,
        max_intensity=8
    )

    assert len(result) == 2


def test_filter_volume(builder):

    exercises = [
        FakeExercise("A", volume=200),
        FakeExercise("B", volume=600),
        FakeExercise("C", volume=1000),
    ]

    result = builder.filter_volume(
        exercises,
        max_volume=700
    )

    assert len(result) == 2


def test_remove_duplicates(builder):

    exercises = [
        FakeExercise("Sprint"),
        FakeExercise("SPRINT"),
        FakeExercise("Recovery"),
    ]

    result = builder.remove_title_duplicates(
        exercises
    )

    assert len(result) == 2


def test_calculate_score(builder):

    ex = FakeExercise(
        "Elite",
        intensity=8,
        cns=2,
        fatigue=3,
        difficulty="elite"
    )

    score = builder.calculate_score(ex)

    assert score > 0