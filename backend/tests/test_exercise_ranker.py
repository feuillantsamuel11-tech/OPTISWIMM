from app.services.session_engine.exercise_ranker import ExerciseRanker


class DummyExercise:

    def __init__(
        self,
        score,
        cns,
        fatigue
    ):

        self.intensity_score = score
        self.cns_load = cns
        self.fatigue_cost = fatigue
        self.difficulty_level = "advanced"


def test_rank():

    ranker = ExerciseRanker()

    exercises = [

        DummyExercise(2, 5, 5),

        DummyExercise(9, 1, 1),

        DummyExercise(5, 3, 3),
    ]

    ranked = ranker.rank(exercises)

    assert ranked[0].intensity_score == 9


def test_select():

    ranker = ExerciseRanker()

    exercises = [

        DummyExercise(2, 5, 5),

        DummyExercise(9, 1, 1),

        DummyExercise(5, 3, 3),
    ]

    selected = ranker.select(

        exercises,

        limit=2
    )

    assert len(selected) == 2