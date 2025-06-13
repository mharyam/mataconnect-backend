from app.communities.models import Community
from app.communities.repository import save_community, search_communities
from typing import List


def create_community(data: dict) -> Community:
    community = Community(**data)
    return save_community(community)


def search_community_by_name(query: str) -> List[Community]:
    return search_communities(query)
