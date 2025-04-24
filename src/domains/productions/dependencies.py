from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.productions.repository import ProductionRepository
from src.domains.productions.service import ProductionService


def get_production_service(db: SessionDep) -> ProductionService:
    repository = ProductionRepository(db)
    service = ProductionService(repository)
    return service

ProductionServiceDep = Annotated[ProductionService, Depends(get_production_service)]
