# app/models/user_model.py
from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Optional, Dict
from datetime import datetime

class ContactLinks(BaseModel):
    email: Optional[EmailStr] = None
    github: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None

class User(BaseModel):
    uid: str
    displayName: str
    photoURL: Optional[HttpUrl] = None
    bio: Optional[str] = None
    contactLinks: Optional[ContactLinks] = None
    showContact: bool = False
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()
