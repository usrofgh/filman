from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import Date
from src.core.base_model import BaseModel
from src.domains.associations.production_country import production_country_associations
from src.domains.associations.production_genre import production_genre_associations


class ProductionModel(BaseModel):
    __tablename__ = "productions"

    name: Mapped[str] = mapped_column(unique=True, index=True)
    poster_url: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    duration_min: Mapped[int]
    release_date: Mapped[datetime.date] = mapped_column(Date)
    release_year: Mapped[int]

    category_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("categories.id"))
    category: Mapped["CategoryModel"] = relationship(back_populates="productions", lazy="selectin")

    trailer: Mapped["TrailerModel"] = relationship(back_populates="production", uselist=False, lazy="selectin")
    genres: Mapped[list["GenreModel"]] = relationship(secondary=production_genre_associations, back_populates="productions", lazy="selectin")

    production_person_associations: Mapped[list["ProductionPersonAssociation"]] = relationship(back_populates="production", lazy="selectin")

    rating_associations: Mapped[list["ProductionRatingAssociation"]] = relationship(back_populates="production", lazy="selectin")

    countries: Mapped[list["CountryModel"]] = relationship(secondary=production_country_associations, back_populates="productions", lazy="selectin")
    comments: Mapped[list["CommentModel"]] = relationship(back_populates="production", lazy="selectin")

    def __str__(self):
        return self.name
