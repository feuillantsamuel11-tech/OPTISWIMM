def score_exercise(
    exercise,
    objective,
    race,
    level
):

    score = 0

    # OBJECTIVE

    if exercise["objective"] == objective:
        score += 100

    # RACE

    if exercise["race_specificity"] == race:
        score += 50

    elif exercise["race_specificity"] == "all":
        score += 20

    # LEVEL

    if exercise["difficulty_level"] == level:
        score += 25

    # BONUS

    score += exercise.get(
        "intensity_score",
        0
    )

    return score