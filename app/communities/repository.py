from pymongo import MongoClient
from app.communities.models import Community
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "mataconnect")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "communities")

mongo_client = MongoClient(MONGODB_URI)
collection = mongo_client[MONGODB_DATABASE][MONGODB_COLLECTION]


def save_community(community: Community) -> Community:
    collection.insert_one(community.dict())
    return community


def search_communities(query: str) -> List[Community]:
    results = collection.find({"name": {"$regex": query, "$options": "i"}})
    return [Community(**doc) for doc in results]
