from fastapi import APIRouter, HTTPException, Depends
from app.models.project_model import Project
from app.utils.auth_middleware import firebase_auth
from app.services.project_service import (
    create_or_update_project,
    get_project_by_id,
    delete_project,
    get_projects_by_owner,
)

router = APIRouter(
    prefix="/projects", 
    tags=["Projects"],
    dependencies=[Depends(firebase_auth)]
    )

@router.post("/", summary="Create or update a project")
def create_project(project: Project):
    result = create_or_update_project(project.dict())
    return result


@router.get("/{project_id}", summary="Get project by ID")
def read_project(project_id: str):
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/owner/{owner_id}", summary="Get all projects of a user")
def list_user_projects(owner_id: str):
    return get_projects_by_owner(owner_id)


@router.delete("/{project_id}", summary="Delete project by ID")
def remove_project(project_id: str):
    return delete_project(project_id)
