"""Importing the necessary files for the jwt_bearer file"""
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt_handler import decode_jwt

class JwtBearer(HTTPBearer):
    """
    Represents the Jwtbearer class

    Attributes:
        None
    """


    def __inti__(self, auto_error:bool = True):
        """Initializes a JwtBearer instance
        Args:
            auto_error (bool): True
        """

        super(JwtBearer, self).__init__(auto_error=auto_error)
    
    async def __call__(self, request:Request):
        credentials : HTTPAuthorizationCredentials = await super(JwtBearer,self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail= "Invalid or Expired Token form")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail= "Invalid or Expired Token form")
        
    def verify_jwt(self, jwt_token: str):
        """Verify the jwt_status
        Args:
            jwt_token (str):jwt_token
        Returns:
            is_token_valid (str):is_token_valid status
        """

        is_token_valid = bool = False
        payload = decode_jwt(jwt_token)    
        if payload:
            is_token_valid  = True
        return is_token_valid
