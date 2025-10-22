# app/core/firebase.py
import firebase_admin
from firebase_admin import credentials, firestore
import os

_firebase_app = None
_firestore_client = None

def init_firebase():
    """
    Initialize Firebase Admin SDK and Firestore client
    """
    global _firebase_app, _firestore_client
    if _firebase_app is not None:
        return _firebase_app, _firestore_client

    # Read service account path from environment variable
    sa_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "./serviceAccount.json")

    if not os.path.exists(sa_path):
        raise FileNotFoundError(f"Service account JSON not found at {sa_path}")

    cred = credentials.Certificate(sa_path)
    _firebase_app = firebase_admin.initialize_app(cred)
    _firestore_client = firestore.client()
    return _firebase_app, _firestore_client

def get_firestore():
    if _firestore_client is None:
        init_firebase()
    return _firestore_client
