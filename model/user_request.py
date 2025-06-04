""" module providing the base model and model validation"""
from pydantic import BaseModel, EmailStr

class UserRequestModel(BaseModel):
    """ Represents the user model
    Attributes:
        name (str): user name
        address (str): Address
        phone (str): Phone number
        Email (str): User-Email
        Password (str): User password
    """
    name: str
    address: str
    phone: str
    Email: EmailStr
    password: str
    class Config:
        """nested class for demo json"""
        json_schema_extra = {
            "user_request_model": {
                "name": "suraj",
                "address": "Harippad",
                "phone": "6235613654",
                "Email": "example@gmailcom",
                "password": "example@123"
            }
        }
