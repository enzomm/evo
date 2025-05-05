from typing import Annotated, Dict

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.database import db_session
from src.providers.security import AuthProvider
from src.schemas.auth_schema import RefreshTokenResponse, TokenResponse
from src.schemas.user_schema import UserResponse
from src.services.auth_service import AuthService

router = APIRouter()
auth = AuthProvider()

Session = Annotated[AsyncSession, Depends(db_session)]
CurrentUser = Annotated[UserResponse, Depends(auth.get_current_user)]


@router.post(
    "/token",
    summary="Return valid access token",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(db_session),
) -> TokenResponse | Dict[str, str | None]:
    _service = AuthService(session)
    return await _service.login(form_data)


@router.post(
    "/refresh_token",
    summary="Return new access token",
    status_code=status.HTTP_200_OK,
    response_model=RefreshTokenResponse,
)
async def refresh_token(
    token: str,
    session: AsyncSession = Depends(db_session),
) -> RefreshTokenResponse | Dict[str, str | None]:
    _service = AuthService(session)
    return await _service.refresh_login(token)


@router.get(
    "/me",
    summary="Return authenticated user",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
)
async def me(current_user: CurrentUser) -> UserResponse:
    return current_user
