from beanie import Document
import time

class Volunteer(Document):
    name: str
    email: str
    country: str
    skills: list[str]
    languages: list[str]
    is_verified: bool = False
    created_at: time.time()
    
    class Settings:
        name = "volunteers"


