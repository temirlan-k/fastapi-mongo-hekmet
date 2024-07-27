from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserCreate, UserLogin
from service.user import create_user, get_user_by_email
from auth.jwt_handler import sign_jwt
from service.user import pwd_context

router = APIRouter()

@router.post("/register")
async def register_user(user_create: UserCreate):
    existing_user = await get_user_by_email(user_create.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await create_user(user_create)
    return user

@router.post("/login")
async def login_user(login_user:UserLogin):
    user = await get_user_by_email(login_user.email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if pwd_context.verify(login_user.password, user.password):
        return sign_jwt(str(user.id), user.role)
    else:
        raise HTTPException(status_code=403, detail="Invalid credentials")
    

    
