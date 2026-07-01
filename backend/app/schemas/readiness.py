from pydantic import BaseModel


class ReadinessSchema(BaseModel):

    sleep_hours: int = 8

    sleep_quality: int = 8

    hrv_score: int = 8

    muscle_soreness: int = 2

    stress_level: int = 2

    motivation: int = 8

    fatigue_subjective: int = 2