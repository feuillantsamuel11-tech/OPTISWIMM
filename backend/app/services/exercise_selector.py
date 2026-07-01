import random

from app.services.exercise_scoring import (
    calculate_exercise_score
)


def select_exercises(
    exercises,
    week_number,
    max_count=1
):

    if not exercises:
        return []

    scored = []

    for ex in exercises:

        score = calculate_exercise_score(
            ex,
            week_number
        )

        scored.append(
            (ex, score)
        )

    scored.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_exercises = [
        item[0]
        for item in scored[:5]
    ]

    if len(top_exercises) <= max_count:
        return top_exercises

    return random.sample(
        top_exercises,
        max_count
    )