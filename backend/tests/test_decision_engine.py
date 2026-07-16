from app.services.decision_engine.decision_engine import (
    DecisionEngine,
)


def test_decision_engine():

    engine = DecisionEngine()

    athlete = {

        "race_distance": 400,

        "recent_loads": [5000] * 28,

        "level": "national"

    }

    decision = engine.analyze(athlete)

    assert decision.specialist == "middle_distance"

    assert decision.load_state == "normal"

    assert len(decision.objectives) > 0

    assert decision.confidence == 0.80