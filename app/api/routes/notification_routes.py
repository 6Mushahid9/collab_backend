from fastapi import APIRouter, HTTPException
from app.models.notification_model import Notification
from app.services.notification_service import (
    create_notification,
    get_notifications_for_user,
    mark_notification_as_read,
    delete_notification,
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", summary="Create a notification")
def create_notif(notif: Notification):
    return create_notification(notif.dict())

@router.get("/{user_id}", summary="Get all notifications for a user")
def list_user_notifications(user_id: str):
    return get_notifications_for_user(user_id)

@router.patch("/{notif_id}/read", summary="Mark a notification as read")
def read_notification(notif_id: str):
    return mark_notification_as_read(notif_id)

@router.delete("/{notif_id}", summary="Delete a notification")
def remove_notification(notif_id: str):
    return delete_notification(notif_id)
