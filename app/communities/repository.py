from app.communities.models import Community
from app.infrastructure.mongodb import db
from typing import List, Optional
from vertexai.preview.language_models import TextEmbeddingModel

COLLECTION_NAME = "communities"
collection = db[COLLECTION_NAME]
SEARCH_INDEX = "communitySearchIndex"


def save_community(community: Community) -> Community:
    collection.insert_one(community.dict())
    return community


def search_communities(query: str) -> List[Community]:
    results = collection.find({"name": {"$regex": query, "$options": "i"}})
    return [Community(**doc) for doc in results]


def search_communities_by_filters(
    text: Optional[str] = None,
    featured: Optional[bool] = None,
    country: Optional[str] = None,
    categories: Optional[List[str]] = None,
    limit: int = 100,
    num_candidates: int = 100,
) -> List[Community]:
    filter_dict = {}
    if country:
        filter_dict["country"] = country
    if featured is not None:
        filter_dict["featured"] = featured
    if categories:
        filter_dict["tags"] = {"$in": categories}

    # Define projection to select only required fields
    projection = {
        "_id": 1,
        "name": 1,
        "description": 1,
        "country": 1,
        "is_virtual": 1,
        "tags": 1,
        "social_links": 1,
        "website": 1,
        "community_info": 1,
    }

    if text:
        # Generate embedding vector for the text
        model = TextEmbeddingModel.from_pretrained("gemini-embedding-001")
        response = model.get_embeddings([text])
        embedding = response[0].values

        # Build vector search stage
        vector_search_stage = {
            "$vectorSearch": {
                "index": SEARCH_INDEX,
                "path": "embedding",
                "queryVector": embedding,
                "numCandidates": num_candidates,
                "limit": limit,
            }
        }

        # Only add filter if we have any filters
        if filter_dict:
            vector_search_stage["$vectorSearch"]["filter"] = filter_dict

        projection_stage = {"$project": projection}
        pipeline = [vector_search_stage, projection_stage]
        results = collection.aggregate(pipeline)
    else:
        # Fallback to normal filter if no text is provided
        results = collection.find(filter_dict, projection=projection).limit(limit)

    communities = []
    for doc in results:
        doc = dict(doc)
        communities.append(Community(**doc))

    return communities
