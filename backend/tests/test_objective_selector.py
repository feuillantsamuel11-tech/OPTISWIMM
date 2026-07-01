import pytest

from app.services.session_engine.objective_selector import ObjectiveSelector


@pytest.fixture
def selector():
    return ObjectiveSelector()


def test_primary_sprint(selector):
    assert selector.get_primary_objectives("sprint") == [
        "speed",
        "race_pace"
    ]


def test_primary_distance(selector):
    assert selector.get_primary_objectives("distance") == [
        "aerobic_power",
        "threshold_control"
    ]


def test_primary_unknown(selector):
    assert selector.get_primary_objectives("unknown") == [
        "race_pace"
    ]


def test_speed_objectives_sprint(selector):
    assert selector.get_speed_objectives("sprint") == [
        "start_power",
        "speed",
        "explosive_power"
    ]


def test_activation_im(selector):
    assert selector.get_activation_objectives("im") == [
        "technical_activation"
    ]


def test_recovery(selector):
    assert selector.get_recovery_objectives() == [
        "recovery",
        "adaptive_recovery"
    ]