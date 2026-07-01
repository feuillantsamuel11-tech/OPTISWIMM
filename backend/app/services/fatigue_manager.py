def adapt_session(session, analysis):

    warnings = analysis["warnings"]

    adapted_session = session.copy()

    adaptations = []

    if "High CNS fatigue accumulation" in warnings:

        adapted_session["speed"] = []

        adaptations.append(
            "Speed block removed due to CNS fatigue"
        )

    if analysis["total_volume"] > 6000:

        if len(adapted_session["main_set"]) > 1:

            adapted_session["main_set"] = adapted_session["main_set"][:1]

            adaptations.append(
                "Main set reduced due to excessive volume"
            )

    return {
        "adapted_session": adapted_session,
        "adaptations": adaptations
    }