from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.genres.repository import GenreRepository
from src.domains.genres.service import GenreService


def get_gender_service(db: SessionDep) -> GenreService:
    repository = GenreRepository(db)
    service = GenreService(repository)
    return service

GenreServiceDep = Annotated[GenreService, Depends(get_gender_service)]
