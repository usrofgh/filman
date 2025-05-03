from datetime import date, datetime

from pydantic import UUID4, BaseModel

from src.api.v1.pagination import PaginationBaseModel
from src.domains.categories.schemas import CategoryReadSchema
from src.domains.countries.schemas import CountryReadSchema
from src.domains.genres.schemas import GenreReadSchema
from src.domains.productions.models import PublishStatus


class ProductionCreateSchema(BaseModel):
    name: str
    poster_url: str
    description: str
    duration_min: int
    release_date: date
    category_id: UUID4
    genre_ids: list[UUID4]
    country_ids: list[UUID4]


class ProductionListSchema(BaseModel):
    id: UUID4
    name: str
    poster_url: str
    description: str
    duration_min: int
    release_date: date
    category: CategoryReadSchema
    genres: list[GenreReadSchema]
    countries: list[CountryReadSchema]
    publish_status: PublishStatus


class ProductionDetailSchema(BaseModel):
    id: UUID4
    name: str
    poster_url: str
    description: str
    duration_min: int
    release_date: date
    category: CategoryReadSchema
    genre_ids: list[GenreReadSchema] | None = None
    countries: list[CountryReadSchema] | None = None
    comment_ids: list[UUID4] | None = None
    persons: list[UUID4] | None = None
    created_at: datetime
    publish_status: PublishStatus


class ProductionFilterSchema(PaginationBaseModel):
    name: str | None = None
    duration_min: int | None = None
    release_date: date | None = None
    category_id: UUID4 | None = None
    genre_ids: list[UUID4] | None = None
    country_ids: list[UUID4] | None = None
    persons: list[UUID4] | None = None



class ProductionUpdateSchema(BaseModel):
    pass
