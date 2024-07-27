from typing import List, Optional
from pydantic import BaseModel,EmailStr
from models.user import ROLE_ENUM

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: ROLE_ENUM
    languages: Optional[List[str]] = None
    additional_skills: Optional[List[str]] = None


    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True