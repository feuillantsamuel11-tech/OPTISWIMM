from app.services.adaptive_training_orchestrator import (
    AdaptiveTrainingOrchestrator,
)


def test_decision_engine_is_called():

    orchestrator = AdaptiveTrainingOrchestrator()

    athlete = {
        "race_distance": 400,
        "recent_loads": [5000] * 28,
    }

    session = orchestrator.build_adaptive_session(
        athlete_profile=athlete
    )

    assert session is not None