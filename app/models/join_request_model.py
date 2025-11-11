from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime

class JoinRequest(BaseModel):
    id: str
    projectId: str
    userId: str
    message: Optional[str] = None
    status: Literal["pending", "approved", "rejected", "cancelled"] = "pending"
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
