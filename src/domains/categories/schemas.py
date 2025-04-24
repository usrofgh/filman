from datetime import datetime

from pydantic import BaseModel, Field
from pydantic import UUID4

from src.domains.genres.schemas import GenreReadSchema


class CategoryCreateSchema(BaseModel):
    name: str = Field(max_length=100)


class CategoryUpdateSchema(BaseModel):
    name: str = Field(max_length=100)


class CategoryReadSchema(BaseModel):
    id: UUID4
    name: str
    created_at: datetime
    genres: list[GenreReadSchema] = Field(default_factory=list)
    updated_at: datetime | None = None


class CategoryFilterSchema(BaseModel):
    name: str = Field(default=None, max_length=100)
    description: str = Field(default=None, max_length=500)
    content_type: str = None
