from app.communities.models import Community
from app.communities.repository import save_community, search_communities_by_filters
from typing import List, Optional


def create_community(data: dict) -> Community:
    community = Community(**data)
    return save_community(community)


def search_community_by_filters(
    text: Optional[str] = None,
    featured: Optional[bool] = None,
    country: Optional[str] = None,
    categories: Optional[List[str]] = None,
) -> List[Community]:
    return search_communities_by_filters(
        text=text, featured=featured, country=country, categories=categories
    )
