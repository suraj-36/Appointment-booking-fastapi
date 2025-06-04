""" module providing the base model and model validation"""
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    """ Represents the user login request
    Attributes:
        Email (str): User-Email
        Password (str): User password
    """

    Email: EmailStr
    password: str
    class Config:
        """nested class for demo json"""
        json_schema_extra = {
            "user_login_request": {
                "Email": "example@gmailcom",
                "password": "example@123"
            }
        }