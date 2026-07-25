class ObjectiveRules:

    OBJECTIVE_ZONE = {
        "threshold_control": {"Z4"},
        "race_pace": {"Z5"},
        "aerobic_capacity": {"Z2", "Z3"},
        "speed": {"Z7"},
        "recovery": {"Z1"},
    }
class ValidationRules:
    MIN_TOTAL_VOLUME = 2000
    MAX_TOTAL_VOLUME = 9000
    REQUIRED_BLOCKS = (
        "warmup",
        "main_set",
        "cooldown",
    )
    MAX_MAINSET_RATIO = 0.70
    MAX_ZONE7_RATIO = 0.15   