from app.core.firebase import get_firestore
from google.cloud import firestore

db = get_firestore()

def create_user(user_data: dict):
    """Create new user in Firestore"""
    users_ref = db.collection("users")
    user_doc = users_ref.document()  # auto-ID

    # Add timestamp for Firestore, but don’t return it yet
    user_data["created_at"] = firestore.SERVER_TIMESTAMP

    user_doc.set(user_data)
    print("✅ User created with ID:", user_doc.id)

    # Return only clean data for FastAPI response
    return {
        "id": user_doc.id,
        "name": user_data["name"],
        "email": user_data["email"],
        "message": "User created successfully 🚀"
    }

def get_user(user_id: str):
    """Fetch user by ID"""
    doc_ref = db.collection("users").document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None
