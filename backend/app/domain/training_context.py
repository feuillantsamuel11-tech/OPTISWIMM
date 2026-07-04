from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class TrainingContext:
    """
    Contexte de décision utilisé par le Session Engine.

    Ce contexte sera progressivement enrichi sans modifier
    les autres composants.
    """

    # Objectif de la séance
    objective: Optional[str] = None

    # Distance cible
    race_distance: Optional[int] = None

    # Spécialité
    specialist: Optional[str] = None

    # Niveau
    level: Optional[str] = None

    # Phase de saison
    season_phase: Optional[str] = None

    # Volume restant
    remaining_volume: Optional[int] = None

    # Intensité maximale autorisée
    max_intensity: Optional[int] = None

    # Fatigue actuelle
    fatigue_score: float = 0.0

    # Bloc précédent
    previous_block: Optional[str] = None

    # Matériel disponible
    equipment: Optional[str] = None