from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import UUID4

from src.core.base_exceptions import AlreadyExists, DoesNotExist
from src.core.base_repository import BaseRepository, ModelG
from src.core.generics import CreateSchemaG, FilterSchemaG, UpdateSchemaG

RepositoryG = TypeVar("RepositoryG", bound=BaseRepository)


class BaseService(
    ABC,
    Generic[
        ModelG,
        RepositoryG,
        CreateSchemaG,
        FilterSchemaG,
        UpdateSchemaG
    ]
):
    def __init__(self, repository: RepositoryG):
        self._repository = repository
        self._subject = self._repository.MODEL.__name__.split("Model")[0]

    @abstractmethod
    def _unique_create_filter(self, create_schema: CreateSchemaG) -> dict:
        pass

    async def create_one(self, create_schema: CreateSchemaG) -> ModelG:
        filters = self._unique_create_filter(create_schema)
        db_model = await self._repository.get_by(**filters)
        if db_model:
            raise AlreadyExists(self._subject)
        return await self._repository.create(create_schema.model_dump())

    async def get_by_id(self, id_: UUID4) -> ModelG:
        db_record = await self._repository.get_by_id(id_)
        if not db_record:
            raise DoesNotExist(self._subject)
        return db_record

    async def get_many(self, filter_schema: FilterSchemaG) -> tuple[list[ModelG], int]:
        filters = {**filter_schema.model_dump(exclude_none=True)}
        offset = filters.pop("offset", 0)
        limit = filters.pop("limit", 20)
        total = await self._repository.count(**filters)
        items = await self._repository.get_all(**filters, offset=offset, limit=limit)
        return items, total

    async def update_one(self, id_: UUID4, update_schema: UpdateSchemaG) -> ModelG:
        await self.get_by_id(id_)
        return await self._repository.update(id_, update_schema.model_dump(exclude_none=True))

    async def delete_one(self, id_: UUID4) -> None:
        await self.get_by_id(id_)
        await self._repository.delete(id_)
