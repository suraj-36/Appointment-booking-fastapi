"""Imports necessary libraries and manages mongodb related functionality."""
from pymongo import MongoClient

class MongoDB:
    "Represents the mongodb"
    _instance = None

    @staticmethod
    def get_instance():
        """Ensures a single instance of MongoDB connection."""
        if MongoDB._instance is None:
            MongoDB._instance = MongoClient('mongodb://127.0.0.1:27017')
        return MongoDB._instance
    
    def get_database():
        """Returns the mongodb instance."""
        return MongoDB.get_instance().my_database


