from pydantic import BaseModel

from typing import Dict

from typing import List

from typing import Any


class SessionResponse(BaseModel):

    profile: Dict[str, Any]

    fatigue_state: Dict[str, Any]

    readiness_state: Dict[str, Any]

    prediction: Dict[str, Any]

    adaptive_session: Dict[str, Any]