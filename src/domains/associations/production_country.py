from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.core.base_model import BaseModel

production_country_associations = Table(
    "production_country_associations",
    BaseModel.metadata,
    Column("production_id", UUID(as_uuid=True), ForeignKey("productions.id"), primary_key=True),
    Column("country_id", UUID(as_uuid=True), ForeignKey("countries.id"), primary_key=True),
)
