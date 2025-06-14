from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.communities.schemas import CommunityRequest, CommunityResponse
from app.communities.services import create_community, search_community_by_filters

router = APIRouter()


@router.post("/create", response_model=CommunityResponse)
def create(data: CommunityRequest):
    try:
        return create_community(data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search", response_model=List[CommunityResponse])
def search(
    text: Optional[str] = Query(None),
    featured: Optional[bool] = Query(None),
    country: Optional[str] = Query(None),
    categories: Optional[List[str]] = Query(None),
):
    try:
        return search_community_by_filters(
            text=text, featured=featured, country=country, categories=categories
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
