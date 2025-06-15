from pydantic import BaseModel
from typing import List, Optional, Dict


class CommunityRequest(BaseModel):
    name: Optional[str]
    description: Optional[str]
    country: Optional[str]
    is_virtual: Optional[bool]


class CommunityResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    country: Optional[str]
    is_virtual: Optional[bool]
    tags: List[str]
    social_links: Optional[dict]
    website: Optional[str]
    community_info: Dict[str, str]
