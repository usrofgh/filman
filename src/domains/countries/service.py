from src.core.base_exceptions import AlreadyExists
from src.core.base_repository import ModelG
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
        return {}

    async def create_one(self, create_schema: CountryCreateSchema) -> ModelG:
        db_country = await self._repository.get_by(country_code=create_schema.country_code)
        if db_country:
            raise AlreadyExists(self._subject)

        db_country = await self._repository.get_by(name=create_schema.name)
        if db_country:
            raise AlreadyExists(self._subject)

        return await self._repository.create(create_schema.model_dump())
