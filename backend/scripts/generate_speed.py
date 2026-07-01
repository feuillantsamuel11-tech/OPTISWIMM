from pathlib import Path

output = []

objectives = [

    "speed",
    "speed_awareness",
    "speed_frequency",
    "max_velocity",
    "overspeed",
    "reaction_speed"

]

race_distances = [

    50,
    100,
    200

]

formats = [

    ("12x15",180),
    ("16x15",240),
    ("20x15",300),
    ("24x15",360),

    ("12x25",300),
    ("16x25",400),
    ("20x25",500),
    ("24x25",600),

    ("8x50",400),
    ("10x50",500),
    ("12x50",600),
    ("16x50",800)

]

focuses = [

    "reaction",
    "acceleration",
    "frequency",
    "velocity",
    "overspeed",
    "stroke_rate",
    "neural",
    "explosive"

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
'speed',
'{objective}',
'Z7',
'crawl',
'none',
{volume},
45,
10,
4,
4,
'{focus}',
'{race_distance}',
'alactic',
'elite',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/speed.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"
)

print(
    len(output),
    "speed exercises generated"
)