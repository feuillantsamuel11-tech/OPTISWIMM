from fastapi import APIRouter
from fastapi import HTTPException
import traceback

from app.schemas.session_request import (
    SessionRequest
)

from app.services.adaptive_training_orchestrator import (
    AdaptiveTrainingOrchestrator
)

router = APIRouter()

orchestrator = (
    AdaptiveTrainingOrchestrator()
)

# =====================================================
# GENERATE SESSION
# =====================================================

@router.post(
    "/generate-session"
)
def generate_session(

    request: SessionRequest

):

    try:

        result = (

            orchestrator
            .build_adaptive_session(

                athlete_data=
                request.athlete.dict(),

                previous_sessions=[],

                readiness_inputs=
                request.readiness.dict()
            )
        )

        return {

            "success": True,

            "data": result
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )