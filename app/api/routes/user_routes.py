from app.models.user_model import User
from fastapi import Form, File, UploadFile, Depends
from app.services.user_service import create_or_update_user, get_user_by_uid, delete_user, save_uploaded_image
from app.utils.auth_middleware import firebase_auth
from app.utils.base_router import BaseRouter

router = BaseRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(firebase_auth)]
)

@router.post("/", summary="Create or update user (with optional image)")
async def create_user(
    uid=Depends(firebase_auth),
    displayName: str = Form(...),
    bio: str = Form(None),
    showContact: bool = Form(False),
    file: UploadFile = File(None)
):
    uid = uid["uid"]
    image_url = save_uploaded_image(file) if file else None

    user_data = {
        "uid": uid,
        "displayName": displayName,
        "bio": bio,
        "photoURL": image_url,
        "showContact": showContact
    }

    result = create_or_update_user(user_data)
    return result


@router.get("/{uid}", summary="Get user by UID")
def read_user(uid: str):
    user = get_user_by_uid(uid)
    if not user:
        raise Exception("User not found")
    return user


@router.delete("/{uid}", summary="Delete user by UID")
def remove_user(uid: str):
    return delete_user(uid)
