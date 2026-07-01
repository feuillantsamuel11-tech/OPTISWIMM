
import json
import os
import pandas as pd
from sqlalchemy import create_engine

# =========================================================
# DATABASE CONNECTION
# =========================================================

engine = create_engine(
    "postgresql://postgres:admin@localhost/optiswimm_db"
)

# =========================================================
# JSON ROOT DIRECTORY
# =========================================================

JSON_FOLDER = "series_json"

# =========================================================
# EXCLUDED FOLDERS
# =========================================================

EXCLUDED_FOLDERS = [
    "AI_constraints"
]

# =========================================================
# LOAD ALL EXERCISES
# =========================================================

all_exercises = []

for root, dirs, files in os.walk(JSON_FOLDER):

    dirs[:] = [
        d for d in dirs
        if d not in EXCLUDED_FOLDERS
    ]

    for file in files:

        if file.endswith(".json"):

            filepath = os.path.join(root, file)

            print(f"Lecture : {filepath}")

            try:

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)

                    if isinstance(data, list):

                        for item in data:

                            if isinstance(item, dict):
                                all_exercises.append(item)

                    elif isinstance(data, dict):

                        all_exercises.append(data)

            except Exception as e:

                print()
                print("ERREUR :", filepath)
                print(e)
                print()

# =========================================================
# DATAFRAME
# =========================================================

df = pd.DataFrame(all_exercises)

print()
print("=" * 60)
print("Nombre d'exercices trouvés :", len(df))
print("=" * 60)

if len(df) == 0:

    print("Aucun exercice trouvé.")
    quit()

# =========================================================
# KEEP ONLY EXERCISE COLUMNS
# =========================================================

exercise_columns = [

    "title",
    "category",
    "objective",
    "zone_code",
    "stroke",
    "equipment",
    "volume",
    "rest",
    "intensity_score",
    "cns_load",
    "fatigue_cost",
    "pedagogical_focus",
    "race_specificity",
    "energy_system",
    "difficulty_level",
    "tags"
]

existing_columns = [

    col
    for col in exercise_columns
    if col in df.columns
]

df = df[existing_columns]

# =========================================================
# TAGS
# =========================================================

if "tags" in df.columns:

    df["tags"] = df["tags"].apply(

        lambda x:
        ",".join(x)

        if isinstance(x, list)

        else str(x)
    )

# =========================================================
# CONVERT DICTS/LISTS
# =========================================================

for col in df.columns:

    df[col] = df[col].apply(

        lambda x:

        json.dumps(
            x,
            ensure_ascii=False
        )

        if isinstance(
            x,
            (dict, list)
        )

        else x
    )

# =========================================================
# DISPLAY COLUMNS
# =========================================================

print()
print("Colonnes retenues :")

for col in df.columns:

    print("-", col)

# =========================================================
# REMOVE DUPLICATES
# =========================================================

if "title" in df.columns:

    df = df.drop_duplicates(
        subset=["title"]
    )

# =========================================================
# EXPORT TO POSTGRESQL
# =========================================================

print()
print("Import vers PostgreSQL...")
print()

try:

    df.to_sql(
        "exercise_library",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print()
    print("=" * 60)
    print(
        f"{len(df)} exercices importés avec succès."
    )
    print("=" * 60)

except Exception as e:

    print()
    print("ERREUR SQL :")
    print(e)
    print()

