from fastapi import APIRouter, HTTPException
from app.communities.schemas import CommunityRequest, CommunityResponse
from app.communities.services import create_community, search_community_by_name

router = APIRouter()


@router.post("/communities", response_model=CommunityResponse)
def create(data: CommunityRequest):
    try:
        return create_community(data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/communities", response_model=List[CommunityResponse])
def search(query: str):
    try:
        return search_community_by_name(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
