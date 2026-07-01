from app.services.dynamic_thresholds import (
    get_dynamic_thresholds
)


def get_profile_adjusted_thresholds(
    week_number,
    swimmer_profile,
    fatigue_level
):

    # =========================
    # BASE PERIODIZATION
    # =========================

    thresholds = (
        get_dynamic_thresholds(
            week_number
        )
    )

    # =========================
    # PROFILE MODIFIERS
    # =========================

    thresholds[
        "speed_score"
    ] *= swimmer_profile[
        "speed_tolerance"
    ] / 3000

    thresholds[
        "lactate_score"
    ] *= swimmer_profile[
        "lactate_tolerance"
    ] / 6000

    thresholds[
        "vo2_score"
    ] *= swimmer_profile[
        "vo2_tolerance"
    ] / 12000

    thresholds[
        "high_intensity_load"
    ] *= swimmer_profile[
        "volume_factor"
    ]

    # =========================
    # FATIGUE MODIFIERS
    # =========================

    if fatigue_level == "extreme":

        thresholds[
            "speed_score"
        ] *= 0.5

        thresholds[
            "lactate_score"
        ] *= 0.5

        thresholds[
            "vo2_score"
        ] *= 0.6

        thresholds[
            "high_intensity_load"
        ] *= 0.5

    elif fatigue_level == "high":

        thresholds[
            "speed_score"
        ] *= 0.7

        thresholds[
            "lactate_score"
        ] *= 0.7

        thresholds[
            "vo2_score"
        ] *= 0.8

        thresholds[
            "high_intensity_load"
        ] *= 0.75

    # =========================
    # ROUND VALUES
    # =========================

    for key in thresholds:

        thresholds[key] = int(
            thresholds[key]
        )

    return thresholds