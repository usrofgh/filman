from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.base_model import BaseModel
from src.domains.persons.models import PersonModel


class ProductionPersonAssociation(BaseModel):
    __tablename__ = "production_person_associations"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    production_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("productions.id"))
    person_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("persons.id"))
    role_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("roles.id"))

    production: Mapped["ProductionModel"] = relationship(back_populates="production_person_associations", lazy="selectin")
    person:  Mapped["PersonModel"] = relationship(back_populates="production_person_associations", lazy="selectin")
    role: Mapped["RoleModel"] = relationship(back_populates="production_person_associations", lazy="selectin")

    __table_args__ = (
        UniqueConstraint("production_id", "person_id", "role_id", name="unique_production_person_role"),
    )
