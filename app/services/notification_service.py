from app.core.firebase import get_firestore
from app.models.notification_model import Notification
from datetime import datetime

db = get_firestore()

def create_notification(notif_data: dict):
    notif_ref = db.collection("notifications").document()  # auto ID
    notif_data["id"] = notif_ref.id
    notif_data["createdAt"] = datetime.utcnow()
    notif_ref.set(notif_data)
    return {"message": "Notification created", "id": notif_ref.id}


def get_notifications_for_user(user_id: str):
    notifications = (
        db.collection("notifications")
        .where("userId", "==", user_id)
        .order_by("createdAt", direction="DESCENDING")
        .stream()
    )
    return [n.to_dict() for n in notifications]


def mark_notification_as_read(notif_id: str):
    notif_ref = db.collection("notifications").document(notif_id)
    notif = notif_ref.get()
    if not notif.exists:
        return {"error": "Notification not found"}
    notif_ref.update({"read": True})
    return {"message": "Notification marked as read"}


def delete_notification(notif_id: str):
    db.collection("notifications").document(notif_id).delete()
    return {"message": f"Notification {notif_id} deleted"}
