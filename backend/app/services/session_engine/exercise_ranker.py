def rank_exercises(
    exercises
):

    scored = []

    for ex in exercises:

        score = 0

        score += ex.intensity_score

        score += (
            10 - ex.cns_load
        )

        score += (
            10 - ex.fatigue_cost
        )

        scored.append(
            (ex, score)
        )

    scored.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return [
        x[0]
        for x in scored
    ]