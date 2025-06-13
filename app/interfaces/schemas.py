from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str
    country: Optional[str] = None
    is_virtual: Optional[bool] = None

class Community(BaseModel):
    name: str
    description: str
    country: str
    is_virtual: bool

class QueryResponse(BaseModel):
    communities: List[Community]
