from starlette import status

from src.core.base_exceptions import BException


class InactiveUser(BException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Inactive user"
    HEADERS = {"WWW-Authenticate": "Bearer"}


class Forbidden(BException):
    STATUS_CODE = status.HTTP_403_FORBIDDEN
    DETAIL = "You do not have administrator privileges required to perform this action"
    HEADERS = {"WWW-Authenticate": "Bearer"}


class CredentialsValidation(BException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Could not validate credentials"
    HEADERS = {"WWW-Authenticate": "Bearer"}


class IncorrectCredentials(BException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Incorrect email or password"
    HEADERS = {"WWW-Authenticate": "Bearer"}


class PasswordMismatch(BException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Password and Repeat password must be the same"
