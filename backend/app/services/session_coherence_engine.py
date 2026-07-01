def validate_session_coherence(
    session
):

    progression = []

    coherence_warnings = []

    # Ordre logique séance
    ordered_blocks = [

        "warmup",

        "preset",

        "speed",

        "main_set"
    ]

    # Construction progression intensité
    for block in ordered_blocks:

        exercises = session.get(
            block,
            []
        )

        if len(exercises) > 0:

            avg_intensity = sum(
                ex.intensity_score
                for ex in exercises
            ) / len(exercises)

            progression.append(
                avg_intensity
            )

    # Vérification cohérence
    for i in range(
        1,
        len(progression)
    ):

        previous = progression[
            i - 1
        ]

        current = progression[
            i
        ]

        # Chute brutale anormale
        if current < previous - 2:

            coherence_warnings.append(
                "Abrupt intensity drop detected"
            )

    # Vérification pic principal
    if len(progression) > 0:

        max_intensity = max(
            progression
        )

        # Pic trop tôt
        if (
            progression.index(
                max_intensity
            ) < len(progression) - 2
        ):

            coherence_warnings.append(
                "Main intensity peak occurs too early"
            )

    # Si aucune alerte
    if len(coherence_warnings) == 0:

        coherence_warnings.append(
            "Session structure is coherent"
        )

    return {

        "intensity_progression":
        progression,

        "coherence_warnings":
        coherence_warnings
    }