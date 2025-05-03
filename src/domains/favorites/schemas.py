from pydantic import UUID4, BaseModel


class FavoriteCreateSchema(BaseModel):
    production_id: UUID4


class FavoriteFilterSchema(BaseModel):
    user_id: UUID4
    production_id: UUID4
