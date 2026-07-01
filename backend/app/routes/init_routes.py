from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.zone import Zone

router = APIRouter()


@router.post("/init-zones")
def init_zones():

    db: Session = SessionLocal()

    existing = db.query(Zone).first()

    if existing:
        db.close()
        return {"message": "Zones already initialized"}

    zones = [
        {
            "code": "Z1",
            "name": "Récupération",
            "intensity": "50-60%",
            "objective": "Recovery"
        },
        {
            "code": "Z2",
            "name": "Endurance fondamentale",
            "intensity": "60-70%",
            "objective": "Aerobic base"
        },
        {
            "code": "Z3",
            "name": "Endurance active",
            "intensity": "70-80%",
            "objective": "Aerobic endurance"
        },
        {
            "code": "Z4",
            "name": "Seuil",
            "intensity": "80-88%",
            "objective": "Threshold"
        },
        {
            "code": "Z5",
            "name": "PMA",
            "intensity": "88-94%",
            "objective": "VO2max"
        },
        {
            "code": "Z6",
            "name": "Lactique",
            "intensity": "95-100%",
            "objective": "Lactate tolerance"
        },
        {
            "code": "Z7",
            "name": "Sprint nerveux",
            "intensity": "Maximal",
            "objective": "Neuromuscular speed"
        }
    ]

    for z in zones:
        zone = Zone(
            code=z["code"],
            name=z["name"],
            intensity=z["intensity"],
            objective=z["objective"]
        )

        db.add(zone)

    db.commit()
    db.close()

    return {"message": "Zones initialized successfully"}