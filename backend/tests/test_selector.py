from app.services.selector.selector import ExerciseSelector


class DummyBlock:

    zone = "Z4"
    objective = "threshold_control"


def test_selector():

    selector = ExerciseSelector()

    candidates = selector.select(DummyBlock())

    assert len(candidates) > 0

def test_selector_filters():

    selector = ExerciseSelector()

    class Block:
        zone = "Z4"
        objective = "threshold_control"

    result = selector.select(Block())

    assert len(result) == 1

    assert result[0].exercise_id == 1   