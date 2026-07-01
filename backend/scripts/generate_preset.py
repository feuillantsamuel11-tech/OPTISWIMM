from pathlib import Path

output = []

objectives = [

    "tempo_frequency",
    "breakout_skill",
    "hypoxic_control",
    "speed_technical",
    "coordination",
    "stroke_diversity"

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

    ("8x25",200),
    ("12x25",300),
    ("16x25",400),

    ("8x50",400),
    ("10x50",500),
    ("12x50",600)

]

focuses = [

    "tempo",
    "frequency",
    "timing",
    "coordination",
    "rhythm",
    "stroke_control",
    "technical_precision",
    "efficiency"

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
'preset',
'{objective}',
'Z2',
'crawl',
'none',
{volume},
15,
3,
1,
1,
'{focus}',
'{race_distance}',
'technical',
'all',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/preset.sql"
).write_text(

    "\n".join(output),

    encoding="utf-8"

)

print(
    len(output),
    "preset exercises generated"
)