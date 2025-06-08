"""Impotes necessary libraries and manages the databes related functions"""
from fastapi import Depends
from database.mongodb import MongoDB
from user_model.user_request import UserRequestModel
from auth.jwt_bearer import JwtBearer

class UserRepository:
    """
    Represents the user repository
    """
    def __init__(self, db=Depends(MongoDB.get_database)):
        self.collection = db["users"]
    
    async def user_login(self, user_data: UserRequestModel):
        """Insert user into MongoDB"""
        
        result = self.collection.insert_one(user_data)
        return result.inserted_id