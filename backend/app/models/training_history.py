from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database import Base


class TrainingHistory(Base):

    __tablename__ = "training_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    week_number = Column(
        Integer
    )

    training_load = Column(
        Float
    )

    fatigue_level = Column(
        String
    )

    fatigue_score = Column(
        Float
    )

    high_cns_blocks = Column(
        Integer
    )

    high_intensity_load = Column(
        Float
    )

    session_type = Column(
        String
    )

    stroke = Column(
        String
    )