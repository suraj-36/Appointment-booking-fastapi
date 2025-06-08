"""
It imports necessary libraries and manages api route functions.
"""
from fastapi import APIRouter, Depends
from user_model.user_request import UserRequestModel
from repository.user import UserRepository
from auth.jwt_handler import sing_jwt

route = APIRouter()

@route.post("/api/user/login")
async def user_login(user:UserRequestModel, repo: UserRepository = Depends()):
    """Manages the user login functionality"""
    user_id = await repo.user_login(user.model_dump())
    return sing_jwt(user.Email)
