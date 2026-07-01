import os
import json
import sys

# Add backend root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.exercise import Exercise

LIBRARY_PATH = "exercise_library"


def import_json_file(db, file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        print(f"Skipped {file_path} (not a list)")
        return

    imported_count = 0

    for item in data:

        # Ignore empty objects
        if not item:
            print(f"Skipped empty object in {file_path}")
            continue

        # Ignore AI constraints accidentally loaded
        if "constraint_name" in item:
            print(f"Skipped AI constraint in {file_path}")
            continue

        # Mandatory field protection
        if not item.get("title"):
            print(f"Skipped invalid exercise (missing title) in {file_path}")
            continue

        try:

            exercise = Exercise(
                title=item.get("title"),
                category=item.get("category"),
                objective=item.get("objective"),
                zone_code=item.get("zone_code"),
                stroke=item.get("stroke", "crawl"),
                equipment=item.get("equipment"),
                volume=item.get("volume", 0),
                rest=item.get("rest", 0),
                intensity_score=item.get("intensity_score", 1),
                cns_load=item.get("cns_load", 0),
                fatigue_cost=item.get("fatigue_cost", 1),
                pedagogical_focus=item.get("pedagogical_focus"),
                race_specificity=item.get("race_specificity"),
                energy_system=item.get("energy_system"),
                difficulty_level=item.get("difficulty_level"),
                tags=item.get("tags", [])
            )

            db.add(exercise)
            imported_count += 1

        except Exception as e:
            print(f"Error importing item from {file_path}")
            print(e)

    try:
        db.commit()
        print(f"Imported {imported_count} exercises from {file_path}")

    except Exception as e:
        db.rollback()
        print(f"Database commit failed for {file_path}")
        print(e)


def import_library():

    db = SessionLocal()

    try:

        for root, dirs, files in os.walk(LIBRARY_PATH):

            # Skip AI constraints folder
            if "AI_constraints" in root:
                print(f"Skipping constraints folder: {root}")
                continue

            for file in files:

                if not file.endswith(".json"):
                    continue

                file_path = os.path.join(root, file)

                print(f"\nImporting {file_path}")

                import_json_file(
                    db=db,
                    file_path=file_path
                )

    finally:
        db.close()


if __name__ == "__main__":
    import_library()