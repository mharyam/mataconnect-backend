from pymongo import MongoClient
from app.core.models import Community
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "mataconnect")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "communities")

mongo_client = MongoClient(MONGODB_URI)
collection = mongo_client[MONGODB_DATABASE][MONGODB_COLLECTION]


def fetch_communities(embedding: List[float]) -> List[Community]:
    """Fetch communities from MongoDB using vector search."""
    query = {
        "$vectorSearch": {
            "queryVector": embedding,
            "path": "embedding",
            "k": 10,  # Number of nearest neighbors to fetch
        }
    }
    results = collection.find(query)
    return [Community(**doc) for doc in results]
