
from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON
)

from app.database import Base


class Exercise(Base):

    __tablename__ = "exercises"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # =================================================
    # CORE
    # =================================================

    title = Column(String)

    category = Column(String)

    objective = Column(String)

    zone_code = Column(String)

    stroke = Column(String)

    equipment = Column(String)

    # =================================================
    # LOAD
    # =================================================

    volume = Column(Integer)

    rest = Column(Integer)

    intensity_score = Column(Integer)

    cns_load = Column(Integer)

    fatigue_cost = Column(Integer)

    # =================================================
    # PERFORMANCE
    # =================================================

    pedagogical_focus = Column(String)

    race_specificity = Column(String)

    energy_system = Column(String)

    difficulty_level = Column(String)

    # =================================================
    # ELITE PERFORMANCE
    # =================================================

    pace_target = Column(String)

    speed_percentage = Column(Integer)

    stroke_rate = Column(String)

    distance_per_stroke = Column(String)

    breathing_pattern = Column(String)

    start_type = Column(String)

    underwater_focus = Column(String)

    technical_focus = Column(String)

    biomechanical_focus = Column(String)

    recovery_mode = Column(String)

    lactate_target = Column(String)

    work_rest_ratio = Column(String)

    # =================================================
    # TAGS
    # =================================================

    tags = Column(JSON)

