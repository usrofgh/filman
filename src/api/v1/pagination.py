from pydantic import BaseModel
from typing_extensions import Generic
from fastapi import Request

from src.core.generics import ReadSchemaG


class MetaSchema(BaseModel):
    total: int
    next: str | None = None
    previous: str | None = None


class PaginatedResponseSchema(BaseModel, Generic[ReadSchemaG]):
    items: list[ReadSchemaG]
    meta: MetaSchema

class PaginationBaseModel(BaseModel):
    offset: int | None = 0
    limit: int | None = 20

    def make_meta(self, req: Request, total: int) -> MetaSchema:
        # TODO: Implement correctly
        base = req.url.remove_query_params(["offset", "limit"])
        def u(o: int | None = None):
            return str(base.include_query_params(offset=o, limit=self.limit)) if o is not None else None
        if not total:
            nxt = None
        else:
            nxt = self.offset + self.limit if self.offset + self.limit < total else None

        prv = self.offset - self.limit if self.offset - self.limit >= 0 else None

        return MetaSchema(
            total=total,
            next=u(nxt),
            previous=u(prv),
        )
