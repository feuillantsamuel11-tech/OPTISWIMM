def calculate_progression_factor(
    week_number
):

    progression_map = {

        1: 1.0,

        2: 1.05,

        3: 1.10,

        4: 0.75
    }

    return progression_map.get(
        week_number,
        1.0
    )


def apply_progression(
    analysis,
    week_number
):

    factor = calculate_progression_factor(
        week_number
    )

    adjusted_load = (
        analysis["training_load"] * factor
    )

    adjusted_volume = (
        analysis["total_volume"] * factor
    )

    recommendations = []

    if factor > 1.05:

        recommendations.append(
            "High overload week"
        )

    if factor < 1.0:

        recommendations.append(
            "Recovery week"
        )

    return {

        "week_number": week_number,

        "progression_factor": factor,

        "adjusted_training_load": round(
            adjusted_load,
            2
        ),

        "adjusted_volume": round(
            adjusted_volume,
            2
        ),

        "recommendations": recommendations
    }