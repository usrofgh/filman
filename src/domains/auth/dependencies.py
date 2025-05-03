from datetime import datetime
from typing import Annotated

import jwt
from fastapi import Depends
from jwt import InvalidTokenError

from src.core.config import settings
from src.core.security import oauth2_scheme
from src.domains.auth.exceptions import CredentialsValidation, Forbidden, InactiveUser
from src.domains.auth.service import AuthService
from src.domains.users.dependencies import UserRepositoryDep
from src.domains.users.models import UserModel


async def get_current_user(
    user_repo: UserRepositoryDep,
    token: Annotated[str, Depends(oauth2_scheme)]
) -> UserModel:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY.get_secret_value(), algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
    except InvalidTokenError:
        raise CredentialsValidation

    db_user = await user_repo.get_by_id(user_id)
    if db_user is None:
        raise CredentialsValidation

    return db_user


async def get_current_active_user(
    current_user: Annotated[UserModel, Depends(get_current_user)]
) -> UserModel:
    if not current_user.is_active:
        raise InactiveUser
    return current_user


async def get_current_admin_user(
    current_user: Annotated[UserModel, Depends(get_current_active_user)]
) -> UserModel:
    if not current_user.is_admin:
        raise Forbidden
    return current_user


async def get_auth_service(user_repository: UserRepositoryDep) -> AuthService:
    service = AuthService(user_repository)
    return service


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
