from fastapi import APIRouter, HTTPException
from app.interfaces.schemas import QueryRequest, QueryResponse
from app.application.use_cases import search_communities

router = APIRouter()


@router.post("/search", response_model=QueryResponse)
def search(query_request: QueryRequest):
    try:
        result = search_communities(query_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
