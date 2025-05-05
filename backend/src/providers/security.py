from datetime import datetime, timedelta
from typing import Annotated
from zoneinfo import ZoneInfo

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, ExpiredSignatureError, decode, encode
from pwdlib import PasswordHash
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.database import db_session
from src.configs.settings import settings
from src.providers.exceptions import CredentialsException
from src.repository.user_repository import UserRepository
from src.schemas.user_schema import UserResponse

PWD = PasswordHash.recommended()
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="v1/auth/token")


class AuthProvider:
    """Class to provider user authenticate methods"""

    def __init__(self) -> None:
        self.JWT_ACCESS_SECRET_KEY = settings.JWT_ACCESS_SECRET_KEY
        self.ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.JWT_REFRESH_SECRET_KEY = settings.JWT_REFRESH_SECRET_KEY
        self.REFRESH_TOKEN_EXPIRE_HOURS = settings.REFRESH_TOKEN_EXPIRE_HOURS
        self.ALGORITHM = settings.ALGORITHM
        if not self.JWT_ACCESS_SECRET_KEY:
            raise EnvironmentError("TOKEN_SECRET_STRING environment variable not found")
        if not self.ACCESS_TOKEN_EXPIRE_MINUTES:
            raise EnvironmentError(
                "ACCESS_TOKEN_EXPIRE_MINUTES environment variable not found"
            )
        if not self.JWT_REFRESH_SECRET_KEY:
            raise EnvironmentError(
                "TOKEN_REFRESH_STRING environment variable not found"
            )
        if not self.REFRESH_TOKEN_EXPIRE_HOURS:
            raise EnvironmentError(
                "REFRESH_TOKEN_EXPIRE_HOURS environment variable not found"
            )
        if not self.ALGORITHM:
            raise EnvironmentError("ALGORITHM environment variable not found")

    async def password_hash(self, password: str) -> str:
        """Generate a hash from string"""
        return PWD.hash(password)

    async def verify_password(self, password: str, hashed_password: str) -> bool:
        """Check if passwords are equal"""
        return PWD.verify(password, hashed_password)

    async def create_access_token(self, data: dict) -> str:
        """Create access token"""
        to_encode = data.copy()
        expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
            minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        encoded_jwt = encode(
            to_encode, self.JWT_ACCESS_SECRET_KEY, algorithm=self.ALGORITHM
        )
        return encoded_jwt

    async def create_refresh_token(self, data: dict, expires_hours: int = 0) -> str:
        """Create refresh token"""
        to_encode = data.copy()
        if expires_hours:
            expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(hours=expires_hours)
        else:
            expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
                hours=self.REFRESH_TOKEN_EXPIRE_HOURS
            )

        to_encode = to_encode | {"exp": expire}
        encoded_jwt = encode(to_encode, self.JWT_REFRESH_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt

    async def decode_access_token(self, token: str) -> str:
        """Decode JWT Access Token"""
        try:
            payload = decode(
                token, self.JWT_ACCESS_SECRET_KEY, algorithms=[self.ALGORITHM]
            )
            email: EmailStr = payload.get("sub")
            if not email:
                raise CredentialsException()

            return email
        except DecodeError:
            raise CredentialsException()
        except ExpiredSignatureError:
            raise CredentialsException()

    async def decode_refresh_token(self, token: str) -> str:
        """Decode JWT Refresh Token"""
        try:
            payload = decode(
                token, self.JWT_REFRESH_SECRET_KEY, algorithms=[self.ALGORITHM]
            )
            email: EmailStr = payload.get("sub")
            if not email:
                raise CredentialsException()

            return email
        except DecodeError:
            raise CredentialsException()
        except ExpiredSignatureError:
            raise CredentialsException()

    async def get_current_user(
        self,
        token: Annotated[str, Depends(OAUTH2_SCHEME)],
        session: AsyncSession = Depends(db_session),
    ) -> UserResponse:
        """Return user authenticated"""

        email = await self.decode_access_token(token)

        user = await UserRepository(session).get_by_email(email)
        if not user:
            raise CredentialsException()

        return user
