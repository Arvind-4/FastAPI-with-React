from pymongo import MongoClient
from pymongo.collection import Collection

from app.config import get_settings

settings = get_settings()

def get_db():
    client = MongoClient(settings.mongo_uri)
    return client

def get_collection():
    client = get_db()
    collection: Collection = client["Auth"]["users"]
    return collection