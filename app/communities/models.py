from pydantic import BaseModel
from typing import List, Optional, Dict


class Community(BaseModel):
    _id: str
    name: str
    description: Optional[str] = None
    website: Optional[str] = None
    tags: List[str] = []
    country: Optional[str] = None
    city: Optional[str] = None
    language: Optional[List[str]] = []
    contact_email: Optional[str] = None
    is_virtual: Optional[bool] = False
    social_links: Dict[str, str] = {}
    community_info: Dict[str, str] = {}
    pricing_model: Optional[str] = None
    topics_supported: List[str] = []
    audience_type: List[str] = []
    event_types: List[str] = []
    year_founded: Optional[int] = None
    verified: Optional[bool] = False
    data_source: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    last_verified_at: Optional[str] = None
