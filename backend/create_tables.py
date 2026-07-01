from app.database import Base
from app.database import engine

from app.models.exercise import Exercise

print("Creating tables...")

Base.metadata.create_all(
    bind=engine
)

print("Tables created.")