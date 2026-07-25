from fastapi import APIRouter

from app.api.schemas import GenerateSessionRequest
from app.services.optiswimm_engine import OptiSwimmEngine

router = APIRouter(
    prefix="/api/v1",
    tags=["OPTISWIMM"],
)


@router.post("/generate-session")
def generate_session(request: GenerateSessionRequest):

    engine = OptiSwimmEngine()

    result = engine.generate(
        request.model_dump()
    )

    return {
        "session": result.session,
        "decision": result.decision,
        "knowledge_path": result.knowledge_path,
        "explanation": {
            "summary": result.explanation.summary,
            "reasoning": result.explanation.reasoning,
            "confidence": result.explanation.confidence,
        },
    }