"""necessary modules for the jwt"""
import time
import jwt

SECRET_KEY = "609280dc4459e51fb3be75889f76029a"
ALGORITHM = "HS256"

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
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token_response(token)

def decode_jwt(token: str):
    """decode the jwt token
    Args:
        token (str):encoded token
    Returns:
        token (str):decoded token
    """
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decode_token if decode_token["expires"] >= time.time() else None
    except ValueError:
        return {"Decode token failed !!!"}
