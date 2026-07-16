from pydantic import BaseModel


class GenerateSessionRequest(BaseModel):

    race_distance: int

    recent_loads: list[int]


class GenerateSessionResponse(BaseModel):

    session: dict

    explanation: dict

    confidence: float