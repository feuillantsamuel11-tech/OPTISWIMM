from pathlib import Path

output = []

objectives = [

    "recovery",
    "adaptive_recovery",
    "active_recovery",
    "mobility_recovery"

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

    ("200 easy",200),
    ("300 easy",300),
    ("400 easy",400),

    ("8x50 easy",400),
    ("10x50 easy",500),
    ("12x50 easy",600)

]

focuses = [

    "flush",
    "mobility",
    "relaxation",
    "breathing",
    "decompression",
    "recovery_flow",
    "low_hr",
    "technique_reset"

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
'cooldown',
'{objective}',
'Z1',
'crawl',
'none',
{volume},
10,
1,
0,
0,
'{focus}',
'{race_distance}',
'recovery',
'all',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/cooldown.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"

)

print(
    len(output),
    "cooldown exercises generated"
)