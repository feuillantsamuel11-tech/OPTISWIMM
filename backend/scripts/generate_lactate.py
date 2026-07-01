from pathlib import Path

output = []

objectives = [

    "lactate",
    "lactate_tolerance",
    "lactate_production",
    "lactate_clearance"

]

race_distances = [

    50,
    100,
    200,
    400

]

formats = [

    ("8x50",400),
    ("10x50",500),
    ("12x50",600),

    ("6x75",450),
    ("8x75",600),
    ("10x75",750),

    ("6x100",600),
    ("8x100",800),
    ("10x100",1000)

]

focuses = [

    "lactate_accumulation",
    "lactate_repeatability",
    "lactate_clearance",
    "high_intensity_repeat",
    "speed_endurance",
    "fatigue_resistance",
    "finish_speed",
    "acid_tolerance"

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
45,
9,
3,
5,
'{focus}',
'{race_distance}',
'anaerobic_lactic',
'elite',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/lactate.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"
)

print(
    len(output),
    "lactate exercises generated"
)