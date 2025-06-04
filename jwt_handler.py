"""necessary modules for the jwt"""
import time
from jwt import JWT
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token:str):
    """Defining a structure to a token response
    Args:
        token (str): token

    Returns:
        token structure
    """
    return {
        "access token":token
    }

def sing_jwt(user_id: str):
    """singnJWT method
    Args:
        user_id (str):user id
    Returns:
        token (str):structured token response
    """
    payload = {
        "userID":user_id,
        "expiry":time.time() + 600
    }
    token = JWT.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)

def decode_jwt(token: str):
    """decode the jwt token
    Args:
        token (str):encoded token
    Returns:
        token (str):decoded token
    """
    try:
        decode_token = JWT.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decode_token if decode_token["expires"] >= time.time() else None
    except ValueError:
        return {"Decode token failed !!!"}