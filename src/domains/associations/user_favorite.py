from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID

from src.core.base_model import BaseModel

user_favorite_production_associations = Table(
    "user_favorite_production_associations",
    BaseModel.metadata,
    Column("production_id", UUID(as_uuid=True), ForeignKey("productions.id"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
)
