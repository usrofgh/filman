from datetime import datetime

from pydantic import BaseModel
from pydantic import UUID4


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
