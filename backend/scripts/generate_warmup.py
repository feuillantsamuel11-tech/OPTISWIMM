from pathlib import Path

output = []

objectives = [

    "general_activation",
    "aerobic_activation",
    "technical_activation",
    "race_activation",
    "underwater_activation",
    "neural_activation"

]

race_distances = [

    50,
    100,
    200,
    400,
    800,
    1500

]

formats = [

    ("200 swim", 200),
    ("300 swim", 300),
    ("400 swim", 400),

    ("8x50", 400),
    ("10x50", 500),
    ("12x50", 600),

    ("4x100", 400),
    ("6x100", 600)

]

focuses = [

    "mobility",
    "stroke_prep",
    "breathing",
    "body_position",
    "streamline",
    "activation",
    "rhythm",
    "coordination"

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
'warmup',
'{objective}',
'Z1',
'crawl',
'none',
{volume},
15,
2,
1,
1,
'{focus}',
'{race_distance}',
'aerobic',
'all',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/warmup.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"

)

print(
    len(output),
    "warmup exercises generated"
)