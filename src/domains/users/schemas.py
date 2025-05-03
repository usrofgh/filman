from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr, Field, field_validator

from src.domains.auth.exceptions import PasswordMismatch
from src.domains.comment_reactions.schemas import CommentReactionReadSchema
from src.domains.comments.schemas import CommentReadSchema
from src.domains.productions.schemas import ProductionDetailSchema


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
    avatar_url: str | None
    is_active: bool
    is_admin: bool
    comments: list[CommentReadSchema]
    comment_reactions: list[CommentReactionReadSchema]
    favorite_productions: list[ProductionDetailSchema]
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
