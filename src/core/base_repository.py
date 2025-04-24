from abc import ABC
from typing import Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update
from pydantic import UUID4
from typing_extensions import Generic

from src.core.base_model import BaseModel

ModelG = TypeVar("ModelG", bound=BaseModel)


class BaseRepository(ABC, Generic[ModelG]):
    MODEL: Type[ModelG] = None

    def __init__(self, db: AsyncSession):
        self._db = db
        if not self.MODEL:
            raise NotImplementedError("SPECIFY MODEL")

    async def create(self, obj_data: dict) -> ModelG:
        obj = self.MODEL(**obj_data)
        self._db.add(obj)
        await self._db.commit()
        await self._db.refresh(obj)
        return obj

    async def get_by_id(self, id_: UUID4) -> ModelG:
        stmt = select(self.MODEL).where(self.MODEL.id == id_)
        result = await self._db.execute(stmt)
        return result.scalars().one_or_none()

    async def get_by(self, **filter_) -> ModelG | None:
        stmt = select(self.MODEL).filter_by(**filter_)
        result = await self._db.execute(stmt)
        return result.scalars().one_or_none()

    async def get_all(self, **filters) -> list[ModelG]:
        stmt = select(self.MODEL).filter_by(**filters)
        result = await self._db.execute(stmt)
        return list(result.scalars().all())

    async def update(self, id_: UUID4, update_data: dict) -> ModelG:
        stmt = update(self.MODEL).where(self.MODEL.id == id_).values(**update_data).returning(self.MODEL)
        result = await self._db.execute(stmt)
        await self._db.commit()

        updated_record = result.scalars().first()
        return updated_record

    async def delete(self, id_: UUID4) -> None:
        stmt = delete(self.MODEL).where(self.MODEL.id == id_)
        await self._db.execute(stmt)
        await self._db.commit()
