from fastapi import APIRouter
from app.communities.api import router as communities_router

api_router = APIRouter()

# Register all feature routers here
api_router.include_router(
    communities_router, prefix="/communities", tags=["communities"],
)
