from typing import Annotated

from fastapi.params import Depends

from src.core.db import SessionDep
from src.domains.categories.repository import CategoryRepository
from src.domains.categories.service import CategoryService


def get_category_service(db: SessionDep) -> CategoryService:
    repository = CategoryRepository(db)
    service = CategoryService(repository)
    return service

CategoryServiceDep = Annotated[CategoryService, Depends(get_category_service)]
