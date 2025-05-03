from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel
from src.domains.associations.production_genre import production_genre_associations


class GenreModel(BaseModel):
    __tablename__ = "genres"
    name: Mapped[str] = mapped_column(unique=True, index=True)

    productions: Mapped[list["ProductionModel"]] = relationship(
        back_populates="genres",
        secondary=production_genre_associations,
        lazy="selectin"
    )

    def __str__(self):
        return self.name
