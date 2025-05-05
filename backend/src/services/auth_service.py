from typing import Dict

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.providers.exceptions import AuthenticationException, CredentialsException
from src.providers.security import AuthProvider
from src.repository.user_repository import UserRepository
from src.schemas.auth_schema import RefreshTokenResponse, TokenResponse


class AuthService:
    "Auth Service Class"

    def __init__(self, session: AsyncSession):
        self.auth = AuthProvider()
        self.repository = UserRepository(session)

    async def login(
        self, data: OAuth2PasswordRequestForm
    ) -> TokenResponse | Dict[str, str | None]:
        user = await self.repository.get_by_email(data.username)

        if not user:
            raise AuthenticationException()
        if not await self.auth.verify_password(data.password, user.password):
            raise AuthenticationException()

        access_token = await self.auth.create_access_token(data={"sub": user.email})
        refresh_token = await self.auth.create_refresh_token(data={"sub": user.email})
        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
        return TokenResponse(**response)

    async def refresh_login(self, token: str) -> RefreshTokenResponse:
        email = await self.auth.decode_refresh_token(token)

        user = await self.repository.get_by_email(email)
        if not user:
            raise CredentialsException()

        access_token = await self.auth.create_access_token(data={"sub": user.email})
        response = {
            "access_token": access_token,
            "token_type": "bearer",
        }
        return RefreshTokenResponse(**response)
