from app.repositories.exercise_repository import ExerciseRepository


def test_find_all():
    repo = ExerciseRepository()

    exercises = repo.find()

    assert len(exercises) == 3


def test_find_by_zone():
    repo = ExerciseRepository()

    exercises = repo.find(zone="Z4")

    assert len(exercises) == 1
    assert exercises[0].name == "8x100 seuil"


def test_find_by_objective():
    repo = ExerciseRepository()

    exercises = repo.find(objective="speed")

    assert len(exercises) == 1
    assert exercises[0].name == "16x50 sprint"


def test_find_by_zone_and_objective():
    repo = ExerciseRepository()

    exercises = repo.find(
        zone="Z4",
        objective="threshold_control",
    )

    assert len(exercises) == 1


def test_unknown_zone_returns_empty():
    repo = ExerciseRepository()

    assert repo.find(zone="Z99") == []


def test_unknown_objective_returns_empty():
    repo = ExerciseRepository()

    assert repo.find(objective="unknown") == []