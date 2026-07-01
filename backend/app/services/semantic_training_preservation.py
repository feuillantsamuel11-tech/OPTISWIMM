def get_preserved_training_focus(
    original_zone
):

    mapping = {

        "Z7": "speed_technical",

        "Z6": "aerobic_power",

        "Z5": "threshold_control",

        "Z4": "aerobic_threshold",

        "Z3": "aerobic",

        "Z2": "aerobic",

        "Z1": "recovery"
    }

    return mapping.get(
        original_zone,
        "aerobic"
    )