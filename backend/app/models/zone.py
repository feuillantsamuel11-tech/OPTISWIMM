from sqlalchemy import Column, Integer, String

from app.database import Base


class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, unique=True, nullable=False)

    name = Column(String, nullable=False)

    intensity = Column(String)

    objective = Column(String)