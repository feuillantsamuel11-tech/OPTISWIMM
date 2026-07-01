from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.database import Base


class Exercise(Base):

    __tablename__ = "exercise_library"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    category = Column(String)

    objective = Column(String)

    zone_code = Column(String)

    stroke = Column(String)

    equipment = Column(String)

    volume = Column(Integer)

    rest = Column(Integer)

    intensity_score = Column(Integer)

    cns_load = Column(Integer)

    fatigue_cost = Column(Integer)

    pedagogical_focus = Column(String)

    race_specificity = Column(String)

    energy_system = Column(String)

    difficulty_level = Column(String)

    tags = Column(String)