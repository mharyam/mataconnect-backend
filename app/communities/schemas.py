from pydantic import BaseModel
from typing import List, Optional


class CommunityRequest(BaseModel):
    name: str
    description: str
    country: Optional[str]
    is_virtual: Optional[bool]


class CommunityResponse(BaseModel):
    id: str
    name: str
    description: str
    country: Optional[str]
    is_virtual: Optional[bool]
    embedding: List[float]
