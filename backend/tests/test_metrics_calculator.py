from app.services.session_engine.metrics_calculator import (
    MetricsCalculator
)


def test_metrics_calculator():

    calculator = MetricsCalculator()

    exercises = [

        {
            "volume": 400,
            "cns": 2,
            "intensity": 5,
        },

        {
            "volume": 600,
            "cns": 3,
            "intensity": 7,
        },
    ]

    metrics = calculator.calculate(
        exercises
    )

    assert metrics["total_volume"] == 1000

    assert metrics["total_cns"] == 5

    assert metrics["average_intensity"] == 6

    assert metrics["fatigue_state"] == "fresh"