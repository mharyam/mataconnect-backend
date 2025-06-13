from typing import List
from app.core.models import Community
from app.core.services import filter_communities
from app.infrastructure.mongodb import fetch_communities
from app.infrastructure.vertex_ai import generate_embedding


def search_communities(
    query: str, country: str = None, is_virtual: bool = None
) -> List[Community]:
    """Search communities based on a query, country, and virtual status."""
    # Generate embedding for the query
    embedding = generate_embedding(query)

    # Fetch communities from MongoDB using vector search
    communities = fetch_communities(embedding)

    # Filter communities based on country and virtual status
    return filter_communities(communities, country, is_virtual)
