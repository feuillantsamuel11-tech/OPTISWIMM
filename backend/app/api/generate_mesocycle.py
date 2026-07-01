
from fastapi import APIRouter
from fastapi import HTTPException

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
# GENERATE MESOCYCLE
# =====================================================

@router.post(
    "/generate-mesocycle"
)

def generate_mesocycle(

    request: SessionRequest
):

    try:

        result = (

            orchestrator
            .generate_mesocycle(

                athlete=
                request.athlete.dict(),

                readiness=
                request.readiness.dict()
            )
        )

        return {

            "success": True,

            "data": result
        }

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)
        )

