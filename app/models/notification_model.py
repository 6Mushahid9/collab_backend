from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class Notification(BaseModel):
    userId: str
    type: str
    payload: Optional[Dict] = None
    read: bool = False
    createdAt: Optional[datetime] = None
