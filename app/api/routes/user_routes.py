from fastapi import APIRouter, HTTPException
from app.db.models.user_model import UserCreate
from app.services import user_service

router = APIRouter()

@router.post("/users")
def create_user_route(user: UserCreate):
    return user_service.create_user(user.dict())

@router.get("/users/{user_id}")
def fetch_user_route(user_id: str):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
