from app.services.explainability.explanation_engine import ExplanationEngine
from app.services.decision_engine.models import DecisionResult


def test_build_explanation():

    engine = ExplanationEngine()

    decision = DecisionResult(
        objectives=["threshold_control"],
        constraints={},
        reasoning=[
            "Specialist: middle_distance",
            "Load: normal",
        ],
        confidence=0.91,
        specialist="middle_distance",
        load_state="normal",
    )

    explanation = engine.build(
        decision=decision,
        knowledge_path=None,
        session=None,
    )

    assert explanation.summary
    assert len(explanation.reasoning) > 0
    assert explanation.confidence > 0