def calculate_exercise_score(
    exercise,
    week_number
):

    score = 0

    # Compatibilité phase saison
    if week_number == 4:

        if exercise.cns_load == 1:
            score += 3

        if exercise.intensity_score <= 5:
            score += 2

    else:

        score += exercise.intensity_score

    # Bonus technique
    if exercise.objective == "technique":
        score += 2

    # Bonus VO2 surcharge
    if (
        week_number == 3
        and exercise.objective == "vo2"
    ):
        score += 3

    # Pénalité fatigue SNC
    if (
        week_number == 4
        and exercise.cns_load >= 3
    ):
        score -= 5

    return score