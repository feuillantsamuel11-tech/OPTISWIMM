from pathlib import Path

output = []

objectives = [

    "threshold_control",
    "threshold_density",
    "threshold_progressive"

]

race_distances = [

    100,
    200,
    400,
    800,
    1500

]

formats = [

    ("8x100",800),
    ("10x100",1000),
    ("12x100",1200),

    ("6x200",1200),
    ("8x200",1600),

    ("4x300",1200),
    ("5x300",1500),

    ("4x400",1600),
    ("5x400",2000)

]

focuses = [

    "pace_control",
    "density",
    "negative_split",
    "aerobic_threshold",
    "lactate_balance",
    "tempo_hold",
    "sustainable_speed",
    "progressive_build"

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
'Z4',
'crawl',
'none',
{volume},
20,
7,
2,
4,
'{focus}',
'{race_distance}',
'aerobic_threshold',
'advanced',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/threshold.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"
)

print(
    len(output),
    "threshold exercises generated"
)