import json
import os

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.exercise import Exercise


def import_exercises_from_folder(folder_path):

    db: Session = SessionLocal()

    files = os.listdir(folder_path)

    for file_name in files:

        if not file_name.endswith(".json"):
            continue

        full_path = os.path.join(
            folder_path,
            file_name
        )

        with open(full_path, "r", encoding="utf-8") as f:

            exercises = json.load(f)

        for ex in exercises:

            existing = db.query(Exercise).filter(
                Exercise.title == ex["title"]
            ).first()

            if existing:
                continue

            new_exercise = Exercise(

                title=ex["title"],

                category=ex["category"],

                stroke=ex["stroke"],

                zone_code=ex["zone_code"],

                distance=ex["distance"],

                equipment=ex["equipment"],

                objective=ex["objective"],

                difficulty=ex["difficulty"],

                cns_fatigue=ex["cns_fatigue"],

                description=ex["description"],

                block_type=ex["block_type"],

                season_phase=ex["season_phase"],

                swimmer_level=ex["swimmer_level"],

                min_age=ex["min_age"],

                max_age=ex["max_age"],

                volume=ex["volume"],

                rest_seconds=ex["rest_seconds"],

                intensity_score=ex["intensity_score"]
            )

            db.add(new_exercise)

    db.commit()

    db.close()

    print("All exercises imported successfully")