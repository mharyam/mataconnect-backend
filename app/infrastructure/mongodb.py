from typing import List
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "mataconnect")

# Initialize MongoDB client and database
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client[MONGODB_DATABASE]
