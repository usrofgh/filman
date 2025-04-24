from datetime import datetime

from pydantic import UUID4, BaseModel


class RatingCompanyCreateSchema(BaseModel):
    name: str


class RatingCompanyReadSchema(BaseModel):
    id: UUID4
    name: str
    created_at: datetime
    updated_at: datetime | None = None


class RatingCompanyFilterSchema(BaseModel):
    name: str | None = None


class RatingCompanyUpdateSchema(BaseModel):
    name: str
