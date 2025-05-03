from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

import src.domains  # noqa: F401
from src.core.config import settings

engine = create_async_engine(
    url=settings.psql_dsn.get_secret_value()
)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise

SessionDep = Annotated[AsyncSession, Depends(get_session)]
