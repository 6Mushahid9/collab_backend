from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(UserCreate):
    id: Optional[str]
    created_at: Optional[datetime]
