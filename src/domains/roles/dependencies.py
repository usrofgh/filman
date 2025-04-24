from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.roles.repository import RoleRepository
from src.domains.roles.service import RoleService


def get_role_service(db: SessionDep) -> RoleService:
    repository = RoleRepository(db)
    service = RoleService(repository)
    return service


RoleServiceDep = Annotated[RoleService, Depends(get_role_service)]
