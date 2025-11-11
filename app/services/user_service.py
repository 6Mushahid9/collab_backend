# app/services/user_service.py
from app.core.firebase import get_firestore
from app.models.user_model import User
from datetime import datetime
import os
from fastapi import UploadFile
from datetime import datetime


db = get_firestore()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_uploaded_image(file: UploadFile):
    if not file or not file.filename:   # <— safety check
        raise ValueError("No file uploaded")

    filename = os.path.basename(file.filename)  # clean name
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return f"/{file_path}"  # or return file_path if you prefer absolute path


db = get_firestore()

def create_or_update_user(user_data: dict):
    uid = user_data["uid"]
    user_ref = db.collection("users").document(uid)

    # Add timestamps
    user_data["updatedAt"] = datetime.utcnow()
    if not user_ref.get().exists:
        user_data["createdAt"] = datetime.utcnow()

    user_ref.set(user_data, merge=True)
    return {"message": "User created/updated successfully", "uid": uid}


def get_user_by_uid(uid: str):
    user_ref = db.collection("users").document(uid).get()
    if not user_ref.exists:
        return None
    return user_ref.to_dict()


def delete_user(uid: str):
    db.collection("users").document(uid).delete()
    return {"message": f"User {uid} deleted"}
