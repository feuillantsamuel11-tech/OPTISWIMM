from app.services.decision_engine.models import DecisionResult


def test_decision_result_defaults():
    result = DecisionResult(
        objectives=["DO-001"]
    )

    assert result.objectives == ["DO-001"]
    assert result.constraints == {}
    assert result.reasoning == []
    assert result.confidence == 0.0
    assert result.specialist == "unknown"
    assert result.load_state == "unknown"