from pathlib import Path

output = []

distances = [

    (50, "Z6", "race_pace"),
    (100, "Z6", "race_pace"),
    (200, "Z5", "race_pace"),
    (400, "Z5", "race_pace"),
    (800, "Z4", "race_pace"),
    (1500, "Z4", "race_pace")

]

formats = [

    ("12x25", 300),
    ("16x25", 400),
    ("20x25", 500),
    ("24x25", 600),
    ("8x50", 400),
    ("10x50", 500),
    ("12x50", 600),
    ("16x50", 800)

]

focuses = [

    "precision",
    "density",
    "frequency",
    "broken",
    "descending",
    "ascending",
    "negative_split",
    "exact_pace"

]

for race_distance, zone, energy in distances:

    for fmt, volume in formats:

        for focus in focuses:

            title = (
                f"{fmt} race pace "
                f"{race_distance} "
                f"{focus}"
            )

            sql = f"""
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
'{title}',
'main_set',
'race_pace',
'{zone}',
'crawl',
'none',
{volume},
30,
8,
2,
4,
'{focus}',
'{race_distance}',
'{energy}',
'elite',
'race_pace,{race_distance},{focus}'
);
"""

            output.append(sql)

Path(
    "sql/race_pace.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"
)

print(
    len(output),
    "exercises generated"
)