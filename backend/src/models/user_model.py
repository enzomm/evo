from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    uuid: Mapped[UUID] = mapped_column(init=False, unique=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    is_superuser: Mapped[bool] = mapped_column(init=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), default=func.now()
    )

    class Config:
        orm_mode = True
