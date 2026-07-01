from pathlib import Path

output = []

objectives = [

    "turn_efficiency",
    "turn_speed",
    "turn_power",
    "turn_frequency"

]

race_distances = [

    50,
    100,
    200,
    400

]

formats = [

    ("12x15",180),
    ("16x15",240),
    ("20x15",300),

    ("12x25",300),
    ("16x25",400),
    ("20x25",500),

    ("8x50",400),
    ("10x50",500),
    ("12x50",600)

]

focuses = [

    "wall_push",
    "rotation_speed",
    "turn_timing",
    "breakout_transition",
    "kick_frequency",
    "distance_off_wall",
    "turn_power",
    "flip_speed"

]

for objective in objectives:

    for race_distance in race_distances:

        for fmt, volume in formats:

            for focus in focuses:

                title = (

                    f"{fmt} "
                    f"{focus} "
                    f"{objective}"

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
'{objective}',
'Z6',
'crawl',
'none',
{volume},
25,
8,
3,
4,
'{focus}',
'{race_distance}',
'neuromuscular',
'elite',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/turns.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"
)

print(
    len(output),
    "turn exercises generated"
)