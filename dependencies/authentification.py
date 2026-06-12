from typing import Annotated
from fastapi import Depends, HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError

from dependencies.services import get_user_service
from models import User
from constants import SECRET_KEY, ALGORITHM
from services import UserService
from security import oauth2_scheme


def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        service: Annotated[UserService, Depends(get_user_service)]
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = service.get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user
