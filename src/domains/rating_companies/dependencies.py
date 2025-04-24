from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.rating_companies.repository import RatingCompanyRepository
from src.domains.rating_companies.service import RatingCompanyService


def get_rating_company_service(db: SessionDep) -> RatingCompanyService:
    repository = RatingCompanyRepository(db)
    service = RatingCompanyService(repository)
    return service


RatingCompanyServiceDep = Annotated[RatingCompanyService, Depends(get_rating_company_service)]
