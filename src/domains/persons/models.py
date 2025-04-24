from datetime import datetime

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.base_model import BaseModel


class PersonModel(BaseModel):
    __tablename__ = "persons"

    name: Mapped[str] = mapped_column(index=True)
    birthdate: Mapped[datetime.date] = mapped_column(Date, nullable=True)
    bio: Mapped[str | None]
    photo_url: Mapped[str | None]

    birth_country_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("countries.id"))
    birth_country: Mapped["CountryModel"] = relationship()
    production_person_associations: Mapped[list["ProductionPersonAssociation"]] = relationship(back_populates="person")

    def __str__(self):
        return self.name
