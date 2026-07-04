from app.services.session_engine.scoring_engine import ScoringEngine
from app.domain.training_context import TrainingContext

class DummyExercise:

    def __init__(
        self,
        intensity_score,
        cns_load,
        fatigue_cost,
        difficulty_level,
    ):
        self.intensity_score = intensity_score
        self.cns_load = cns_load
        self.fatigue_cost = fatigue_cost
        self.difficulty_level = difficulty_level


def test_calculate_score_standard():

    engine = ScoringEngine()

    exercise = DummyExercise(
        intensity_score=8,
        cns_load=3,
        fatigue_cost=2,
        difficulty_level="advanced",
    )

    assert engine.calculate_score(exercise) == 23


def test_calculate_score_elite():

    engine = ScoringEngine()

    exercise = DummyExercise(
        intensity_score=8,
        cns_load=3,
        fatigue_cost=2,
        difficulty_level="elite",
    )

    assert engine.calculate_score(exercise) == 28


def test_calculate_score_none_values():

    engine = ScoringEngine()

    exercise = DummyExercise(
        intensity_score=None,
        cns_load=None,
        fatigue_cost=None,
        difficulty_level=None,
    )

    assert engine.calculate_score(exercise) == 20

def test_context_max_intensity_penalty():

    engine = ScoringEngine()

    exercise = DummyExercise(
        intensity_score=9,
        cns_load=1,
        fatigue_cost=1,
        difficulty_level="advanced",
    )

    context = TrainingContext(
        max_intensity=5
    )

    score = engine.calculate_score(
        exercise,
        context
    )

    assert score == 7    