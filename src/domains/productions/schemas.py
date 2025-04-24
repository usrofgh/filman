from datetime import date

from pydantic import UUID4, BaseModel

from src.domains.persons.schemas import PersonRoleSchema


class ProductionCreateSchema(BaseModel):
    name: str
    poster_url: str
    description: str
    duration_min: int
    release_date: date
    release_year: int
    category_id: UUID4
    genre_ids: list[UUID4]
    country_ids: list[UUID4]
    # persons: list[PersonRoleSchema]



class ProductionReadSchema(BaseModel):
    id: UUID4
    name: str
    poster_url: str
    description: str
    duration_min: int
    release_year: int
    release_date: date
    category_id: UUID4
    genre_ids: list[UUID4]
    country_ids: list[UUID4]
    comment_ids: list[UUID4]
    persons: list[PersonRoleSchema]

    created_at: date
    updated_at: date | None = None


class ProductionFilterSchema(BaseModel):
    name: str
    duration_min: int
    release_year: int
    release_date: date
    category_id: UUID4
    genre_ids: list[UUID4]
    country_ids: list[UUID4]
    persons: list[PersonRoleSchema]



class ProductionUpdateSchema(BaseModel):
    pass
