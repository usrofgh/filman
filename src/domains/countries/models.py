from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel


class CountryModel(BaseModel):
    __tablename__ = "countries"

    name: Mapped[str] = mapped_column(index=True, unique=True)
    country_code: Mapped[str] = mapped_column(index=True, unique=True)

    productions: Mapped[list["ProductionModel"]] = relationship(secondary="production_country_associations", back_populates="countries", lazy="selectin")
    persons: Mapped[list["PersonModel"]] = relationship(back_populates="birth_country", lazy="selectin")

    def __str__(self):
        return self.name
