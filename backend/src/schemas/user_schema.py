from typing import Self

from pydantic import UUID4, BaseModel, ConfigDict, EmailStr, model_validator


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    @model_validator(mode="after")
    def password_validator(self) -> Self:
        # If the password is an empty string or None, set it to None
        if self.password == "" or self.password is None:
            raise ValueError("Password must not be empty")
        # If length of password is less than 8, raise a validation error
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return self


class UserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    uuid: UUID4
    name: str
    email: EmailStr


class UserAuth(UserResponse):
    password: str
