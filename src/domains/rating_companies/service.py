from src.core.base_service import BaseService
from src.domains.rating_companies.models import RatingCompanyModel
from src.domains.rating_companies.repository import RatingCompanyRepository
from src.domains.rating_companies.schemas import RatingCompanyCreateSchema, RatingCompanyFilterSchema, RatingCompanyUpdateSchema


class RatingCompanyService(
    BaseService[
        RatingCompanyModel,
        RatingCompanyRepository,
        RatingCompanyCreateSchema,
        RatingCompanyFilterSchema,
        RatingCompanyUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: RatingCompanyCreateSchema) -> dict:
        return {"name": create_schema.name}
