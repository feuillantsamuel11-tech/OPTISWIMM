
from pydantic import BaseModel

from app.schemas.session_request import (
    AthleteProfile
)

from app.schemas.session_request import (
    ReadinessProfile
)


class Competition(
    BaseModel
):

    name: str

    type: str

    week: int


class SeasonRequest(
    BaseModel
):

    athlete: AthleteProfile

    readiness: ReadinessProfile

    competitions: list[Competition]

