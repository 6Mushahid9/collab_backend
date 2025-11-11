from fastapi import APIRouter, HTTPException
from app.models.join_request_model import JoinRequest
from app.services.join_request_service import (
    create_or_update_join_request,
    get_join_request_by_id,
    delete_join_request,
    get_requests_by_project
)

router = APIRouter(prefix="/join_requests", tags=["Join Requests"])

@router.post("/", summary="Create or update join request")
def create_join_request(req: JoinRequest):
    return create_or_update_join_request(req.dict())

@router.get("/{req_id}", summary="Get join request by ID")
def read_join_request(req_id: str):
    req = get_join_request_by_id(req_id)
    if not req:
        raise HTTPException(status_code=404, detail="Join request not found")
    return req

@router.get("/project/{project_id}", summary="Get all join requests for a project")
def read_requests_for_project(project_id: str):
    return get_requests_by_project(project_id)

@router.delete("/{req_id}", summary="Delete join request by ID")
def remove_join_request(req_id: str):
    return delete_join_request(req_id)
