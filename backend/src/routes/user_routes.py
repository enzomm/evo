from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.database import db_session
from src.providers.security import AuthProvider
from src.schemas.user_schema import UserResponse, UserSchema
from src.services.user_service import UserService

router = APIRouter()
auth = AuthProvider()

Session = Annotated[AsyncSession, Depends(db_session)]
CurrentUser = Annotated[UserResponse, Depends(auth.get_current_user)]

@router.get("", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_users(session: Session, current_user: CurrentUser) -> List[Optional[UserResponse]]:
    _service = UserService(session)
    return await _service.get_all()

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
        data: UserSchema,
        session: Session,
        #current_user: CurrentUser
) -> UserResponse:
    _service = UserService(session)
    return await _service.create(data)

@router.get("/{_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(
        _id: UUID4,
        session: Session,
        current_user: CurrentUser
    ) -> UserResponse:
    _service = UserService(session)
    return await _service.get_by_id(_id)
