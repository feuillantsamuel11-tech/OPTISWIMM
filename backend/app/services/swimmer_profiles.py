def get_swimmer_profile(
    profile_name
):

    profiles = {

        # =========================
        # SPRINTER
        # =========================

        "sprinter": {

            "speed_tolerance": 6000,

            "lactate_tolerance": 8000,

            "vo2_tolerance": 5000,

            "cns_tolerance": 5,

            "recovery_factor": 0.8,

            "volume_factor": 0.7
        },

        # =========================
        # MIDDLE DISTANCE
        # =========================

        "middle_distance": {

            "speed_tolerance": 3500,

            "lactate_tolerance": 5000,

            "vo2_tolerance": 12000,

            "cns_tolerance": 3,

            "recovery_factor": 1.0,

            "volume_factor": 1.0
        },

        # =========================
        # DISTANCE
        # =========================

        "distance": {

            "speed_tolerance": 2000,

            "lactate_tolerance": 3000,

            "vo2_tolerance": 18000,

            "cns_tolerance": 2,

            "recovery_factor": 1.2,

            "volume_factor": 1.5
        },

        # =========================
        # YOUTH
        # =========================

        "youth": {

            "speed_tolerance": 1500,

            "lactate_tolerance": 2000,

            "vo2_tolerance": 6000,

            "cns_tolerance": 1,

            "recovery_factor": 1.5,

            "volume_factor": 0.6
        },

        # =========================
        # ELITE
        # =========================

        "elite": {

            "speed_tolerance": 7000,

            "lactate_tolerance": 10000,

            "vo2_tolerance": 20000,

            "cns_tolerance": 6,

            "recovery_factor": 0.7,

            "volume_factor": 1.4
        },

        # =========================
        # MASTER
        # =========================

        "master": {

            "speed_tolerance": 1500,

            "lactate_tolerance": 2500,

            "vo2_tolerance": 7000,

            "cns_tolerance": 1,

            "recovery_factor": 1.8,

            "volume_factor": 0.8
        }
    }

    return profiles.get(
        profile_name,
        profiles["middle_distance"]
    )