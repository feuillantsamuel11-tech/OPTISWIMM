def validate_session(session):

    warnings = []

    total_volume = 0

    total_intensity = 0

    total_training_load = 0

    high_cns_blocks = 0

    all_blocks = []

    for block_name, exercises in session.items():

        for ex in exercises:

            all_blocks.append(ex)

            volume = ex.volume or 0

            intensity = ex.intensity_score or 0

            cns = ex.cns_fatigue or 1

            total_volume += volume

            total_intensity += intensity

            total_training_load += (
                volume * intensity * cns
            )

            if cns >= 3:
                high_cns_blocks += 1

    average_intensity = 0

    if len(all_blocks) > 0:
        average_intensity = (
            total_intensity / len(all_blocks)
        )

    if total_volume > 6000:
        warnings.append(
            "Very high session volume"
        )

    if high_cns_blocks >= 3:
        warnings.append(
            "High CNS fatigue accumulation"
        )

    if total_training_load > 50000:
        warnings.append(
            "Extremely high training load"
        )

    return {

        "total_volume": total_volume,

        "average_intensity": round(
            average_intensity,
            2
        ),

        "high_cns_blocks": high_cns_blocks,

        "training_load": total_training_load,

        "warnings": warnings
    }