from app.services.planning.planner import Planner


def test_total_volume():

    planner = Planner()

    plan = planner.generate(5000)

    assert plan.total_volume == 5000

    assert plan.planned_volume == 5000