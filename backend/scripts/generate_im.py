from pathlib import Path

OUTPUT_FILE = "sql/im.sql"

OBJECTIVES = {
    "race_pace": {
        "category": "main_set",
        "zone": "Z6",
        "energy": "race_pace"
    },
    "speed": {
        "category": "speed",
        "zone": "Z7",
        "energy": "speed"
    },
    "threshold_control": {
        "category": "main_set",
        "zone": "Z4",
        "energy": "threshold"
    },
    "aerobic_power": {
        "category": "main_set",
        "zone": "Z2",
        "energy": "aerobic"
    },
    "coordination": {
        "category": "preset",
        "zone": "Z1",
        "energy": "technical"
    },
    "stroke_diversity": {
        "category": "preset",
        "zone": "Z1",
        "energy": "technical"
    },
    "technical_precision": {
        "category": "preset",
        "zone": "Z1",
        "energy": "technical"
    },
    "lactate_tolerance": {
        "category": "main_set",
        "zone": "Z6",
        "energy": "lactate"
    },
    "competition": {
        "category": "main_set",
        "zone": "Z6",
        "energy": "competition"
    }
}

FORMATS_200 = [
    ("8x50", 400),
    ("12x50", 600),
    ("16x50", 800),
    ("8x100", 800),
    ("10x100", 1000),
    ("12x100", 1200),
    ("4x200", 800),
    ("6x200", 1200)
]

FORMATS_400 = [
    ("8x100", 800),
    ("10x100", 1000),
    ("12x100", 1200),
    ("6x200", 1200),
    ("8x200", 1600),
    ("4x300", 1200),
    ("6x300", 1800)
]

TITLE_MAP = {
    "race_pace": [
        "IM race pace",
        "IM exact pace",
        "IM pace control",
        "IM race rehearsal",
        "Broken IM race pace"
    ],

    "speed": [
        "IM sprint transitions",
        "IM acceleration",
        "IM transition speed",
        "IM sprint ladder",
        "IM speed order"
    ],

    "threshold_control": [
        "IM threshold hold",
        "IM threshold progression",
        "IM threshold control",
        "IM aerobic threshold"
    ],

    "aerobic_power": [
        "IM aerobic build",
        "IM aerobic ladder",
        "IM aerobic progression",
        "IM aerobic sustain"
    ],

    "coordination": [
        "IM transitions",
        "IM stroke changes",
        "IM coordination",
        "IM transition rhythm"
    ],

    "stroke_diversity": [
        "IM stroke diversity",
        "IM mixed strokes",
        "IM stroke sequencing",
        "IM stroke variation"
    ],

    "technical_precision": [
        "IM technical precision",
        "IM stroke mechanics",
        "IM efficiency",
        "IM technical control"
    ],

    "lactate_tolerance": [
        "IM lactate tolerance",
        "IM lactate build",
        "IM lactate progression",
        "IM lactate sustain"
    ],

    "competition": [
        "Broken 400 IM simulation",
        "IM race rehearsal",
        "IM competition model",
        "IM championship preparation"
    ]
}

EQUIPMENT = [
    "none",
    "pull",
    "paddles",
    "fins",
    "kickboard",
    "tempo_trainer",
    "snorkel"
]

RACE_DISTANCES = [
    "200",
    "400"
]

RESTS = [10, 15, 20, 25, 30]

INTENSITY = {
    "race_pace": 9,
    "speed": 10,
    "threshold_control": 7,
    "aerobic_power": 5,
    "coordination": 2,
    "stroke_diversity": 2,
    "technical_precision": 2,
    "lactate_tolerance": 9,
    "competition": 10
}

sql_lines = []
count = 0

for objective, meta in OBJECTIVES.items():

    titles = TITLE_MAP[objective]

    for race_distance in RACE_DISTANCES:

        formats = (
            FORMATS_200
            if race_distance == "200"
            else FORMATS_400
        )

        for fmt, volume in formats:

            for title in titles:

                for equipment in EQUIPMENT:

                    for rest in RESTS:

                        full_title = (
                            f"{fmt} "
                            f"{title} "
                            f"{race_distance}"
                        )

                        tag_string = (
                            f"IM,"
                            f"{objective},"
                            f"{race_distance}"
                        )

                        sql_lines.append(
f"""
INSERT INTO exercise_library
(
title,
category,
objective,
zone_code,
stroke,
equipment,
volume,
rest,
intensity_score,
cns_load,
fatigue_cost,
pedagogical_focus,
race_specificity,
energy_system,
difficulty_level,
tags
)
VALUES
(
'{full_title}',
'{meta["category"]}',
'{objective}',
'{meta["zone"]}',
'IM',
'{equipment}',
{volume},
{rest},
{INTENSITY[objective]},
2,
4,
'im',
'{race_distance}',
'{meta["energy"]}',
'elite',
'{tag_string}'
);
"""
                        )

                        count += 1

Path("sql").mkdir(exist_ok=True)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(sql_lines)
    )

print("=" * 50)
print("IM SQL GENERATED")
print("Exercises:", count)
print("Output:", OUTPUT_FILE)
print("=" * 50)