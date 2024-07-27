from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.user import router as UserRouter    
from contextlib import asynccontextmanager
import motor.motor_asyncio

token_listener = JWTBearer()


@asynccontextmanager
async def lifespan(app:FastAPI):
    await initiate_database()
    yield

app = FastAPI(lifespan=lifespan) 


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

app.include_router(UserRouter,tags=["Users"],prefix="/user",)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
