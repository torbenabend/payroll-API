import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import jwt
from pwdlib import PasswordHash

from services import UserService
from models import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_dummy_hash() -> str:
    return password_hash.hash("dummypassword")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


def authenticate_user(
        username: str,
        password: str,
        service: UserService
) -> User | bool:
    user = service.get_user_by_username(username)
    if not user:
        dummy_hash = get_dummy_hash()
        verify_password(password, dummy_hash)
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(
        user: User,
        expires_delta: timedelta | None = None
) -> str:
    to_encode = {"sub": user.username}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode["exp"] = expire
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
