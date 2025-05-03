from datetime import datetime

from pydantic import UUID4, BaseModel, Field

from src.api.v1.pagination import PaginationBaseModel


class GenreCreateSchema(BaseModel):
    name: str = Field(max_length=100, min_length=10)
    description: str = Field(max_length=1000)


class GenreReadSchema(BaseModel):
    id: UUID4
    name: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }

class GenreFilterSchema(PaginationBaseModel):
    name: str | None = Field(max_length=100, default=None)


class GenreUpdateSchema(BaseModel):
    name: str = Field(max_length=100, default=None)
    description: str = Field(max_length=1000)
