from datetime import datetime
from uuid import uuid4

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DateTime

from src.core.base_model import BaseModel


class RoleModel(BaseModel):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(index=True)
    production_person_associations: Mapped["ProductionPersonAssociation"] = relationship(back_populates="role")

    def __str__(self):
        return self.name
