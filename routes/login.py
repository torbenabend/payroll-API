from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from security import authenticate_user, create_access_token
from models import User
from models.security import Token
from dependencies.services import get_user_service
from dependencies.authentification import get_current_user

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/token")
def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        service = Depends(get_user_service)
) -> Token:
    user = authenticate_user(
        username=form_data.username,
        password=form_data.password,
        service=service
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user)
    return Token(access_token=access_token, token_type="bearer")


@router.get("/active_user")
def get_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    return current_user
