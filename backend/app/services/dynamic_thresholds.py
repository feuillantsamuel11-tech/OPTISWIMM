def get_dynamic_thresholds(
    week_number
):

    # Semaine récupération
    if week_number % 4 == 0:

        return {

            "high_intensity_load": 3000,

            "lactate_score": 2500,

            "speed_score": 1500,

            "vo2_score": 6000
        }

    # Semaine surcharge
    elif week_number % 3 == 0:

        return {

            "high_intensity_load": 8000,

            "lactate_score": 7000,

            "speed_score": 4000,

            "vo2_score": 15000
        }

    # Semaine standard
    else:

        return {

            "high_intensity_load": 6000,

            "lactate_score": 6000,

            "speed_score": 3000,

            "vo2_score": 12000
        }