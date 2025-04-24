from datetime import date

from pydantic import UUID4, BaseModel


class TrailerCreateSchema(BaseModel):
    video_url: str
    duration_sec: int
    production_id: UUID4


class TrailerReadSchema(BaseModel):
    id: UUID4
    video_url: str
    duration_sec: int
    created_at: date
    updated_at: date

    production_id: UUID4


class TrailerFilterSchema(BaseModel):
    pass


class TrailerUpdateSchema(BaseModel):
    video_url: str | None = None
    duration_sec: int | None = None
