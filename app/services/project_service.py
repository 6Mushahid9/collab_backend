from app.core.firebase import get_firestore
from app.models.project_model import Project
from datetime import datetime

db = get_firestore()

def create_or_update_project(project_data: dict):
    project_id = project_data.get("id")
    if not project_id:
        # Generate Firestore-like ID if not provided
        project_ref = db.collection("projects").document()
        project_data["id"] = project_ref.id
    else:
        project_ref = db.collection("projects").document(project_id)

    # Add timestamps
    project_data["updatedAt"] = datetime.utcnow()
    if not project_ref.get().exists:
        project_data["createdAt"] = datetime.utcnow()

    project_ref.set(project_data, merge=True)
    return {"message": "Project created/updated successfully", "id": project_data["id"]}


def get_project_by_id(project_id: str):
    project_ref = db.collection("projects").document(project_id).get()
    if not project_ref.exists:
        return None
    return project_ref.to_dict()


def delete_project(project_id: str):
    db.collection("projects").document(project_id).delete()
    return {"message": f"Project {project_id} deleted"}


def get_projects_by_owner(owner_id: str):
    projects = db.collection("projects").where("ownerId", "==", owner_id).stream()
    return [p.to_dict() for p in projects]
