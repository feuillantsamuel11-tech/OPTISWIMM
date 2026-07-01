def get_replacement_profile(
    overload_type
):

    profiles = {

        "lactate": {

            "replacement_type":
            "aerobic_technical",

            "message":
            "Lactate work replaced with aerobic technical recovery"
        },

        "speed": {

            "replacement_type":
            "speed_technical",

            "message":
            "Sprint work replaced with technical speed work"
        },

        "vo2": {

            "replacement_type":
            "threshold_control",

            "message":
            "VO2 work replaced with controlled threshold work"
        },

        "threshold": {

            "replacement_type":
            "aerobic",

            "message":
            "Threshold work replaced with aerobic work"
        }
    }

    return profiles.get(
        overload_type
    )