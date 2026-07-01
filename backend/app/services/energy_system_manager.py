ZONE_SYSTEMS = {

    "Z1": "aerobic",

    "Z2": "aerobic",

    "Z3": "aerobic_power",

    "Z4": "threshold",

    "Z5": "vo2",

    "Z6": "lactate",

    "Z7": "speed"
}


def get_energy_system(zone_code):

    return ZONE_SYSTEMS.get(
        zone_code,
        "unknown"
    )


def validate_energy_balance(session):

    systems = []

    for block_name, exercises in session.items():

        for ex in exercises:

            system = get_energy_system(
                ex.zone_code
            )

            systems.append(system)

    warnings = []

    # Trop de systèmes lourds
    heavy_systems = [
        "vo2",
        "lactate",
        "speed"
    ]

    heavy_count = 0

    for s in systems:

        if s in heavy_systems:
            heavy_count += 1

    if heavy_count >= 3:

        warnings.append(
            "Too many high intensity energy systems"
        )

    # Lactique + speed
    if (
        "lactate" in systems
        and "speed" in systems
    ):

        warnings.append(
            "Lactate and speed combination is highly demanding"
        )

    return {

        "energy_systems": systems,

        "energy_warnings": warnings
    }