from app.domain.training_context import TrainingContext


def test_training_context_defaults():

    ctx = TrainingContext()

    assert ctx.fatigue_score == 0.0
    assert ctx.objective is None
    assert ctx.race_distance is None


def test_training_context_values():

    ctx = TrainingContext(
        objective="vo2",
        race_distance=200,
        specialist="middle_distance",
        fatigue_score=12.5,
    )

    assert ctx.objective == "vo2"
    assert ctx.race_distance == 200
    assert ctx.specialist == "middle_distance"
    assert ctx.fatigue_score == 12.5