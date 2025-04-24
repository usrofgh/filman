from datetime import datetime

from pydantic import BaseModel, Field
from pydantic import UUID4


class CountryCreateSchema(BaseModel):
    country_code: str = Field(max_length=2, min_length=2)
    name: str = Field(max_length=100)


class CountryReadSchema(BaseModel):
    id: UUID4
    name: str
    country_code: str
    created_at: datetime
    updated_at: datetime | None = None


class CountryFilterSchema(BaseModel):
    name: str = Field(max_length=100, default=None)
    country_code: str = Field(max_length=100, default=None)


class CountryUpdateSchema(BaseModel):
    name: str = Field(max_length=100, default=None)
    country_code: str = Field(max_length=2, min_length=2, default=None)
