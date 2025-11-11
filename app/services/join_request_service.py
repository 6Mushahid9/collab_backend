from app.core.firebase import get_firestore
from app.models.join_request_model import JoinRequest
from datetime import datetime

db = get_firestore()

def create_or_update_join_request(req_data: dict):
    req_id = req_data["id"]
    req_ref = db.collection("join_requests").document(req_id)

    # timestamps
    req_data["updatedAt"] = datetime.utcnow()
    if not req_ref.get().exists:
        req_data["createdAt"] = datetime.utcnow()

    req_ref.set(req_data, merge=True)
    return {"message": "Join request created/updated", "id": req_id}


def get_join_request_by_id(req_id: str):
    doc = db.collection("join_requests").document(req_id).get()
    if not doc.exists:
        return None
    return doc.to_dict()


def delete_join_request(req_id: str):
    db.collection("join_requests").document(req_id).delete()
    return {"message": f"Join request {req_id} deleted"}


def get_requests_by_project(project_id: str):
    requests = (
        db.collection("join_requests")
        .where("projectId", "==", project_id)
        .stream()
    )
    return [r.to_dict() for r in requests]
