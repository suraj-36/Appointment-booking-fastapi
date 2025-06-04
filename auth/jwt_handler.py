"""necessary modules for the jwt"""
import time
from jwt import JWT
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token:str):
    "structure for token response"
    return {
        "access token":token
    }

def singJWT(userID: str):
    """singnJWT method"""
    payload = {
        "userID":userID,
        "expiry":time.time() + 600
    }
    token = JWT.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)