from app.services.validation.session_validator import SessionValidator
from app.services.decision_engine.models import DecisionResult

class DummySession:

    def __init__(
        self,
        total_volume,
        zones=None,
        blocks=None,
    ):

        self.total_volume = total_volume

        self.zones = zones or {}

        self.blocks = blocks or {
            "warmup": [1],
            "main_set": [1],
            "cooldown": [1],
        }

validator = SessionValidator()


def test_volume_ok():

    session = DummySession(4500)

    report = validator.validate(session)


def test_volume_too_low():

    session = DummySession(500)

    report = validator.validate(session)

    assert report.valid
    assert any(i.code == "LOW_VOLUME" for i in report.issues)


def test_volume_too_high():

    session = DummySession(12000)

    report = validator.validate(session)

    assert report.valid
    assert any(i.code == "HIGH_VOLUME" for i in report.issues)


def test_objective_match():

    session = DummySession(
        4500,
        zones={
            "Z4": 3200,
            "Z2": 1000,
        },
    )

    decision = DecisionResult(
        objectives=["threshold_control"],
        constraints={},
        reasoning=[],
        confidence=1.0,
        specialist="middle_distance",
        load_state="normal",
    )

    report = validator.validate(
        session,
        objective="threshold_control",
    )

    assert report.valid
    assert not any(i.code == "OBJECTIVE_MISMATCH" for i in report.issues)


def test_objective_mismatch():

    session = DummySession(
        4500,
        zones={
            "Z7": 3000,
        },
    )

    decision = DecisionResult(
        objectives=["threshold_control"],
        constraints={},
        reasoning=[],
        confidence=1.0,
        specialist="middle_distance",
        load_state="normal",
    )

    report = validator.validate(
        session=session,
        objective="threshold_control",
    )

    assert report.valid
    assert any(i.code == "OBJECTIVE_MISMATCH" for i in report.issues)