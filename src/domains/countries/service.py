from src.core.base_service import BaseService
from src.domains.countries.models import CountryModel
from src.domains.countries.repository import CountryRepository
from src.domains.countries.schemas import CountryCreateSchema, CountryFilterSchema, CountryUpdateSchema


class CountryService(
    BaseService[
        CountryModel,
        CountryRepository,
        CountryCreateSchema,
        CountryFilterSchema,
        CountryUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: CountryCreateSchema) -> dict:
        return {"name": create_schema.name}
