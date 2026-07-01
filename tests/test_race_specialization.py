from app.services.race_specialization_engine import RaceSpecializationEngine


engine = RaceSpecializationEngine()


def test_50_speed():
    assert engine.get_week_objectives(
        "sprint",
        "speed",
        50
    ) == [
        "speed"
    ]


def test_200_threshold():
    assert engine.get_week_objectives(
        "middle_distance",
        "threshold",
        200
    ) == [
        "threshold_control"
    ]


def test_400_aerobic():
    assert engine.get_week_objectives(
        "distance",
        "aerobic",
        400
    ) == [
        "aerobic_power",
        "threshold_control"
    ]


def test_1500_recovery():
    assert engine.get_week_objectives(
        "distance",
        "recovery",
        1500
    ) == [
        "recovery"
    ]