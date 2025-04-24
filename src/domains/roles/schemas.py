from datetime import datetime

from pydantic import UUID4, BaseModel


class RoleCreateSchema(BaseModel):
    name: str


class RoleReadSchema(BaseModel):
    id: UUID4
    name: str
    created_at: datetime
    updated_at: datetime | None = None


class RoleFilterSchema(BaseModel):
    name: str | None = None


class RoleUpdateSchema(BaseModel):
    name: str | None = None
