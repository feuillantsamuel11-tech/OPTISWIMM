
from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.season_request import (
    SeasonRequest
)

from app.services.adaptive_training_orchestrator import (
    AdaptiveTrainingOrchestrator
)

router = APIRouter()

orchestrator = (
    AdaptiveTrainingOrchestrator()
)


# =====================================================
# GENERATE SEASON
# =====================================================

@router.post(
    "/generate-season"
)

def generate_season(

    request: SeasonRequest
):

    try:

        competitions = []

        for comp in request.competitions:

            competitions.append({

                "name":
                comp.name,

                "type":
                comp.type,

                "week":
                comp.week
            })

        result = (

            orchestrator
            .generate_season(

                athlete=
                request.athlete.dict(),

                readiness=
                request.readiness.dict(),

                competitions=
                competitions
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

