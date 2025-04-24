from src.core.base_exceptions import AlreadyExists
from src.core.base_service import BaseService
from src.domains.productions.models import ProductionModel
from src.domains.productions.service import ProductionService
from src.domains.trailers.models import TrailerModel
from src.domains.trailers.repository import TrailerRepository
from src.domains.trailers.schemas import TrailerCreateSchema, TrailerFilterSchema, TrailerUpdateSchema


class TrailerService(
    BaseService[
        TrailerModel,
        TrailerRepository,
        TrailerCreateSchema,
        TrailerFilterSchema,
        TrailerUpdateSchema
    ]
):
    def __init__(self, repository: TrailerRepository, production_service: ProductionService):
        super().__init__(repository)
        self._production_service = production_service

    def _unique_create_filter(self, create_schema: TrailerCreateSchema) -> dict:
        return {"name": create_schema.production_id}

    async def create_one(self, create_schema: TrailerCreateSchema) -> TrailerModel:
        filters = self._unique_create_filter(create_schema)
        db_model = await self._repository.get_by(**filters)
        if db_model:
            raise AlreadyExists(self._subject)

        db_production: ProductionModel = await self._production_service.get_by_id(create_schema.production_id)
        if await db_production.trailer:
            raise AlreadyExists(self._subject)

        return await self._repository.create(create_schema.model_dump())
