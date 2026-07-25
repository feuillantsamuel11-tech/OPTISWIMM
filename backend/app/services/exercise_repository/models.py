from dataclasses import dataclass, field
from app.domain.exercise.models import Exercise

__all__ = ["Exercise"]

@dataclass
class Exercise:

    # -------------------------
    # Identification
    # -------------------------

    id: str
    name: str
    description: str = ""

    # -------------------------
    # Technique
    # -------------------------

    stroke: str = ""
    level: str = ""
    age_group: str = ""

    # -------------------------
    # Physiologie
    # -------------------------

    zone: str = ""
    energy_system: str = ""
    objective: str = ""

    # -------------------------
    # Volumes
    # -------------------------

    distance: int = 0
    repetitions: int = 1
    rest: int = 0

    # -------------------------
    # Biomécanique
    # -------------------------

    body_position: str = ""
    kick: bool = False
    pull: bool = False
    breathing: bool = False
    turns: bool = False
    start: bool = False

    # -------------------------
    # Matériel
    # -------------------------

    equipment: list[str] = field(default_factory=list)

    # -------------------------
    # Compatibilités
    # -------------------------

    compatible_profiles: list[str] = field(default_factory=list)

    contraindications: list[str] = field(default_factory=list)

    # -------------------------
    # Tags
    # -------------------------

    tags: list[str] = field(default_factory=list)

    # -------------------------
    # Intelligence
    # -------------------------

    historical_score: float = 0.0

    objectives: list[str] = field(default_factory=list)