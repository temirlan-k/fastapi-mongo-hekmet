import os
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pydantic_settings import BaseSettings
import models

class Settings(BaseSettings):
    DATABASE_URL:str = 'mongodb+srv://admin:yBizVWOI2v1couIy@cluster0.djbpz07.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"
        from_attributes = True

async def initiate_database():
    settings = Settings()
    database_url = 'mongodb+srv://admin:yBizVWOI2v1couIy@cluster0.djbpz07.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    print(database_url)
    try:
        # Use the URL from settings to create the client
        client = AsyncIOMotorClient(database_url, serverSelectionTimeoutMS=30000)
        
        # Ensure models.__all__ is populated with all document models
        if not hasattr(models, '__all__') or not models.__all__:
            raise RuntimeError("models.__all__ is not defined or empty. Ensure it contains all Beanie document models.")
        
        await init_beanie(
            database=client.hikmet_db, document_models=models.__all__
        )
    except Exception as e:
        print(f"Failed to initialize database: {e}")
        raise

# Ensure that models.__all__ contains all the document models to be used with Beanie
# For example:
# models.__all__ = [User, Post, Comment]  # Replace these with your actual models
