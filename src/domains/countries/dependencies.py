from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.countries.repository import CountryRepository
from src.domains.countries.service import CountryService


def get_gender_service(db: SessionDep) -> CountryService:
    repository = CountryRepository(db)
    service = CountryService(repository)
    return service

CountryServiceDep = Annotated[CountryService, Depends(get_gender_service)]
