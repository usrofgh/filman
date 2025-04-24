from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID

from src.core.base_model import BaseModel

production_genre_associations = Table(
    "production_genre_associations",
    BaseModel.metadata,
    Column("production_id", UUID(as_uuid=True), ForeignKey("productions.id"), primary_key=True),
    Column("genre_id", UUID(as_uuid=True), ForeignKey("genres.id"), primary_key=True),
)
