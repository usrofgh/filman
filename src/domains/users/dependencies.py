from typing import Annotated

from fastapi.params import Depends

from src.core.db import SessionDep
from src.domains.users.repository import UserRepository
from src.domains.users.service import UserService


def get_user_repository(session: SessionDep) -> UserRepository:
    return UserRepository(session)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repository)]


def get_user_service(user_repo: UserRepositoryDep) -> UserService:
    service = UserService(user_repo)
    return service


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
