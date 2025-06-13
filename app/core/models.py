from pydantic import BaseModel
from typing import List, Optional


class Community(BaseModel):
    id: str
    name: str
    description: str
    embedding: List[float]
    country: Optional[str]
    is_virtual: Optional[bool]
