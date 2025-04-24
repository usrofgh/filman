from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.productions.dependencies import ProductionServiceDep
from src.domains.trailers.repository import TrailerRepository
from src.domains.trailers.service import TrailerService


def get_trailer_service(db: SessionDep, production_service: ProductionServiceDep) -> TrailerService:
    repository = TrailerRepository(db)
    service = TrailerService(repository, production_service)
    return service


TrailerServiceDep = Annotated[TrailerService, Depends(get_trailer_service)]
