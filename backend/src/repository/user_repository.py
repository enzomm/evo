from typing import List, Optional

from pydantic import UUID4, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user_model import User
from src.schemas.user_schema import UserAuth, UserResponse, UserSchema


class UserRepository:
    """User Repository Class"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: UserSchema) -> UserResponse:
        """Create new user"""
        user = User(**data.model_dump(exclude_none=True))
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_all(self) -> List[Optional[UserResponse]]:
        """Get all users"""
        users = await self.session.scalars(select(User))
        return [user for user in users]

    async def get_by_id(self, _id: UUID4) -> UserResponse:
        """Get user by ID"""
        user = await self.session.scalar(select(User).where(User.uuid == _id))
        return user

    async def get_by_email(self, email: EmailStr) -> UserAuth:
        """Get user by email"""
        user = await self.session.scalar(select(User).where(User.email == email))
        return user
