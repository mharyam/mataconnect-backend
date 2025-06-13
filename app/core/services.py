from typing import List
from app.core.models import Community


def filter_communities(
    communities: List[Community], country: str = None, is_virtual: bool = None
) -> List[Community]:
    """Filter communities based on country and virtual status."""
    filtered = communities

    if country:
        filtered = [c for c in filtered if c.country == country]

    if is_virtual is not None:
        filtered = [c for c in filtered if c.is_virtual == is_virtual]

    return filtered
