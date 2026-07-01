from pydantic import BaseModel

from app.schemas.athlete import (
    AthleteSchema
)

from app.schemas.readiness import (
    ReadinessSchema
)


class SessionRequest(BaseModel):

    athlete: AthleteSchema

    readiness: ReadinessSchema