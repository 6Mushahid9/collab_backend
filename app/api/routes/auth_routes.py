from fastapi import APIRouter, Depends
from app.utils.auth_middleware import firebase_auth

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/me")
async def get_current_user(decoded_token = Depends(firebase_auth)):
    return {
        "uid": decoded_token["uid"],
        "email": decoded_token.get("email"),
        "name": decoded_token.get("name"),
    }
