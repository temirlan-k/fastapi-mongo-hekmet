from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pydantic_settings import BaseSettings
import models as models

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"
        from_attributes = True

async def initiate_database():
    settings = Settings()
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )
