from app.services.planning.planner import Planner
from app.services.decision_engine.models import DecisionResult


def test_sprint_profile():

    planner = Planner()

    decision = DecisionResult(
        objectives=["speed"],
        constraints={},
        reasoning=[],
        confidence=1.0,
        specialist="sprinter",
        load_state="normal",
    )

    plan = planner.generate(
        4000,
        decision,
    )

    zones = [b.zone for b in plan.blocks]

    assert "Z7" in zones