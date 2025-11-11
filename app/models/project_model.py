from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class Project(BaseModel):
    id: Optional[str] = None
    ownerId: str
    title: str
    slug: str
    description: Optional[str] = None
    tags: List[str] = []
    teamMembers: List[str] = []
    maxMembers: int = 5
    visibility: Literal["public", "private"] = "public"
    status: Literal["active", "paused", "completed", "archived"] = "active"
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
