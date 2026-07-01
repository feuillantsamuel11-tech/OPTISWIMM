def calculate_accumulated_fatigue(
    recent_sessions
):

    total_load = 0

    high_intensity_days = 0

    cns_load = 0

    for session in recent_sessions:

        load = session.get(
            "training_load",
            0
        )

        total_load += load

        # Journée haute intensité
        if load > 12000:

            high_intensity_days += 1

        # Charge SNC
        cns_load += session.get(
            "high_cns_blocks",
            0
        )

    fatigue_score = (

        total_load

        +

        (high_intensity_days * 2000)

        +

        (cns_load * 1500)
    )

    fatigue_level = "low"

    if fatigue_score > 40000:

        fatigue_level = "extreme"

    elif fatigue_score > 25000:

        fatigue_level = "high"

    elif fatigue_score > 12000:

        fatigue_level = "moderate"

    recommendations = []

    # Recommandations fatigue
    if fatigue_level == "extreme":

        recommendations.append(
            "Recovery session strongly recommended"
        )

        recommendations.append(
            "Avoid lactate and sprint work"
        )

    elif fatigue_level == "high":

        recommendations.append(
            "Reduce high intensity exposure"
        )

    elif fatigue_level == "moderate":

        recommendations.append(
            "Monitor CNS fatigue"
        )

    else:

        recommendations.append(
            "Fatigue level acceptable"
        )

    return {

        "fatigue_score":
        fatigue_score,

        "fatigue_level":
        fatigue_level,

        "high_intensity_days":
        high_intensity_days,

        "cns_load":
        cns_load,

        "recommendations":
        recommendations
    }