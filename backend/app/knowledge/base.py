from datetime import UTC, datetime

from typing import List

from pydantic import BaseModel, Field


class BaseKnowledgeObject(BaseModel):
    """
    Base class for every knowledge object in OPTISWIMM.
    """

    id: str = Field(..., description="Unique identifier")
    name: str = Field(..., description="Display name")

    type: str = Field(..., description="Knowledge type")
    category: str = Field(..., description="Knowledge category")

    description: str = ""

    tags: List[str] = Field(default_factory=list)

    version: str = "1.0.0"

    status: str = "draft"

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )