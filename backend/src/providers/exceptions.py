from enum import Enum

from fastapi import HTTPException, status


class ErrorMessage(str, Enum):
    """Error messages map"""

    USER_NOT_FOUND = "User not found"
    NOT_AUTHENTICAD = "Incorrect email or password"
    INVALID_CREDENTIALS = "Could not validate credentials"


class BaseException(HTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Generic error"
    HEADERS = {}

    def __init__(self, **kwargs):
        super().__init__(
            status_code=self.STATUS_CODE,
            detail=self.DETAIL,
            headers=self.HEADERS,
            **kwargs
        )


class AuthenticationException(BaseException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = ErrorMessage.NOT_AUTHENTICAD


class CredentialsException(BaseException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = ErrorMessage.INVALID_CREDENTIALS
    HEADERS = {"WWW-Authenticate": "Bearer"}
