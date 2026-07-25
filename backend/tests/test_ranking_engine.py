from app.services.exercise_repository.models import Exercise
from app.services.exercise_repository.ranking_engine import RankingEngine


def test_rank_best_first():

    engine = RankingEngine()

    a = Exercise(id="1", name="A")
    a.score = 80

    b = Exercise(id="2", name="B")
    b.score = 95

    c = Exercise(id="3", name="C")
    c.score = 60

    ranked = engine.rank([a, b, c])

    assert ranked[0].score == 95
    assert ranked[1].score == 80
    assert ranked[2].score == 60


def test_empty_list():

    engine = RankingEngine()

    ranked = engine.rank([])

    assert ranked == []