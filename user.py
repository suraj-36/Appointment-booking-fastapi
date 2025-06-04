""" module providing the base model and model validation"""
from pydantic import BaseModel

class UserModel(BaseModel):
    """ User model creation class"""
    name: str
    address: str
    phone: str
    class Config:
        """nested class for demo json"""
        json_schema_extra = {
            "usermodel": {
                "name": "suraj",
                "address": "Harippad",
                "phone": "6235613654"
            }
        }