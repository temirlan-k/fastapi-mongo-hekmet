from typing import Optional
from models.user import User
from schemas.user import UserCreate, UserLogin
from passlib.context import CryptContext
from auth.jwt_handler import sign_jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(user_create: UserCreate) -> User:
    user = User(
        email=user_create.email,
        password=pwd_context.hash(user_create.password),
        firstname=user_create.firstname,
        lastname=user_create.lastname,
        role=user_create.role,
        languages=user_create.languages,
        additional_skills=user_create.additional_skills,
    )

    return sign_jwt(str(user.get("_id")), user.role)

async def get_user_by_email(email: str) -> Optional[User]:
    return await User.find_one(User.email == email)

