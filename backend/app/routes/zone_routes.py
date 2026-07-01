from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.zone import Zone
from app.schemas.zone_schema import ZoneCreate

router = APIRouter()


@router.post("/zones")
def create_zone(zone: ZoneCreate):

    db: Session = SessionLocal()

    new_zone = Zone(
        code=zone.code,
        name=zone.name,
        intensity=zone.intensity,
        objective=zone.objective
    )

    db.add(new_zone)
    db.commit()
    db.refresh(new_zone)

    db.close()

    return new_zone


@router.get("/zones")
def get_zones():

    db: Session = SessionLocal()

    zones = db.query(Zone).all()

    db.close()

    return zones