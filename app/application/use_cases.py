from app.infrastructure.vertex_ai import get_embedding
from app.infrastructure.mongodb import search_in_mongodb
from app.interfaces.schemas import QueryRequest, QueryResponse

def search_communities(query_request: QueryRequest) -> QueryResponse:
    # Generate embedding for the query
    embedding = get_embedding(query_request.query)

    # Perform vector search in MongoDB
    communities = search_in_mongodb(embedding, query_request.country, query_request.is_virtual)

    return QueryResponse(communities=communities)
