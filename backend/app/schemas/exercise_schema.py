from pydantic import BaseModel


class ExerciseCreate(BaseModel):

    title: str

    category: str

    stroke: str

    zone_code: str

    distance: int

    equipment: str

    objective: str

    difficulty: int

    cns_fatigue: int

    description: str

    block_type: str

    season_phase: int

    swimmer_level: int

    min_age: int

    max_age: int

    volume: int

    rest_seconds: int

    intensity_score: int


class ExerciseResponse(BaseModel):

    id: int

    title: str

    category: str

    stroke: str

    zone_code: str

    distance: int

    equipment: str

    objective: str

    difficulty: int

    cns_fatigue: int

    description: str

    block_type: str

    season_phase: int

    swimmer_level: int

    min_age: int

    max_age: int

    volume: int

    rest_seconds: int

    intensity_score: int

    class Config:
        from_attributes = True