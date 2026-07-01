from pydantic import BaseModel


class ZoneCreate(BaseModel):
    code: str
    name: str
    intensity: str
    objective: str


class ZoneResponse(BaseModel):
    id: int
    code: str
    name: str
    intensity: str
    objective: str

    class Config:
        from_attributes = True