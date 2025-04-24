from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator
from pydantic import Field
from pydantic import UUID4

from src.domains.auth.exceptions import PasswordMismatch


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str = Field(exclude=True, min_length=8, max_length=150)
    repeat_password: str = Field(exclude=True, min_length=8, max_length=150)

    @field_validator("repeat_password")
    def passwords_match(cls, v, info):
        if v != info.data["password"]:
            raise PasswordMismatch
        return v


class UserCreateDBSchema(BaseModel):
    email: EmailStr
    hashed_password: str


class UserReadSchema(BaseModel):
    id: UUID4
    email: EmailStr
    is_active: bool
    is_admin: bool
    comments: list
    comment_reactions: list
    created_at: datetime
    updated_at: datetime | None


class UserFilterSchema(BaseModel):
    email: EmailStr | None = None
    is_active: bool | None = None
    is_admin: bool | None = None
    # created_after: datetime | None = Field(exclude=True)
    # created_before: datetime | None = Field(exclude=True)

class UserUpdateSchema(BaseModel):
    pass
