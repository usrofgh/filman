from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel


class RoleModel(BaseModel):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(index=True)
    production_person_associations: Mapped["ProductionPersonAssociation"] = relationship(back_populates="role", lazy="selectin")

    def __str__(self):
        return self.name
