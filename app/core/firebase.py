import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
import logging
from fastapi import HTTPException, status

logger = logging.getLogger("uvicorn")

firebase_app = None
firestore_client = None


def init_firebase():
    """Initialize Firebase only once for the app lifecycle."""
    global firebase_app, firestore_client

    if firebase_app is not None and firestore_client is not None:
        return firestore_client

    sa_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "./serviceAccount.json")
    if not os.path.exists(sa_path):
        logger.error(f"❌ Service account JSON not found at {sa_path}")
        raise FileNotFoundError(f"Service account JSON not found at {sa_path}")

    cred = credentials.Certificate(sa_path)
    firebase_app = firebase_admin.initialize_app(cred)
    firestore_client = firestore.client()

    logger.info("✅ Firebase initialized successfully")
    return firestore_client


def get_firestore():
    """Return initialized Firestore client (auto-init if needed)."""
    global firestore_client
    if firestore_client is None:
        logger.warning("⚠️ Firestore not initialized — initializing now...")
        return init_firebase()
    return firestore_client


def verify_firebase_token(id_token: str):
    """
    Verifies Firebase ID token and returns the decoded payload.
    Raises HTTP 401 if invalid.
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        logger.error(f"❌ Token verification failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired Firebase token"
        )
