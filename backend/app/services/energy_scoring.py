def calculate_energy_scores(session):

    lactate_score = 0

    vo2_score = 0

    speed_score = 0

    threshold_score = 0

    aerobic_score = 0

    for block_name, exercises in session.items():

        for ex in exercises:

            volume = ex.volume or 0

            intensity = (
                ex.intensity_score or 0
            )

            load = volume * intensity

            # Z1-Z2
            if ex.zone_code in [
                "Z1",
                "Z2"
            ]:

                aerobic_score += load

            # Z4
            elif ex.zone_code == "Z4":

                threshold_score += load

            # Z5
            elif ex.zone_code == "Z5":

                vo2_score += load

            # Z6
            elif ex.zone_code == "Z6":

                lactate_score += load

            # Z7
            elif ex.zone_code == "Z7":

                speed_score += load

    # Charge haute intensité globale
    high_intensity_load = (

        lactate_score

        + vo2_score

        + speed_score
    )

    warnings = []

    # Lactique
    if lactate_score > 6000:

        warnings.append(
            "Very high lactate load"
        )

    # VO2
    if vo2_score > 12000:

        warnings.append(
            "Very high VO2 load"
        )

    # Sprint SNC
    if speed_score > 3000:

        warnings.append(
            "Very high speed SNC load"
        )

    # Charge globale haute intensité
    if high_intensity_load > 6000:

        warnings.append(
            "Excessive global high intensity load"
        )

    return {

        "aerobic_score":
        aerobic_score,

        "threshold_score":
        threshold_score,

        "vo2_score":
        vo2_score,

        "lactate_score":
        lactate_score,

        "speed_score":
        speed_score,

        "high_intensity_load":
        high_intensity_load,

        "energy_score_warnings":
        warnings
    }