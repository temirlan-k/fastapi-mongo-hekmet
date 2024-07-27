from beanie import Document
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional, List

class ROLE_ENUM(str, Enum):
    PILGRIM = "PILGRIM"
    VOLUNTEER = "VOLUNTEER"

class User(Document):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: ROLE_ENUM
    languages: Optional[List[str]] = None
    additional_skills: Optional[List[str]] = None
    is_verified: bool = False

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
                "password": "securepassword",
                "role": "PILGRIM",
                "languages": ["English", "Spanish"],
                "additional_skills": ["First Aid", "Cooking"],
                "is_verified": False,
            }
        }
