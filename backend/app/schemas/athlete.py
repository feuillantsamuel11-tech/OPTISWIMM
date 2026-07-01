from pydantic import BaseModel
from typing import List, Dict
from typing import Optional

class AthleteSchema(BaseModel):

    age: int = 18

    level: str = "elite"

    specialist: str = "middle_distance"

    race_distance: int = 400

    injury_history: List[str] = []

    fatigue_resistance: str = "moderate"

    distance_focus: Optional[str] = None

    daily_focus: Optional[str] = None

    objective_blocklist: List[str] = []

    mesocycle_structure: Dict = {}