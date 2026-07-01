from app.services.fatigue_memory_engine import (
    calculate_accumulated_fatigue
)

recent_sessions = [

    {
        "training_load": 15000,
        "high_cns_blocks": 2
    },

    {
        "training_load": 13000,
        "high_cns_blocks": 1
    },

    {
        "training_load": 9000,
        "high_cns_blocks": 0
    }
]

result = calculate_accumulated_fatigue(
    recent_sessions
)

print(result)