from pathlib import Path

output = []

objectives = [

    "core_stability",
    "core_control",
    "postural_control",
    "scapular_control",
    "injury_prevention",
    "mobility_activation"

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

    ("5min",5),
    ("8min",8),
    ("10min",10),

    ("12min",12),
    ("15min",15),
    ("20min",20)

]

focuses = [

    "plank",
    "rotation",
    "balance",
    "mobility",
    "stability",
    "activation",
    "shoulder_health",
    "posture"

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
'dryland',
'{objective}',
'Z1',
'dryland',
'bodyweight',
{volume},
0,
2,
1,
1,
'{focus}',
'{race_distance}',
'neuromuscular',
'all',
'{objective},{focus},{race_distance}'
);
"""

                output.append(sql)

Path(
    "sql/dryland.sql"
).write_text(
    "\n".join(output),
    encoding="utf-8"
)

print(
    len(output),
    "dryland exercises generated"
)