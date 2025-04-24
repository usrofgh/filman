from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True, index=True)

    productions: Mapped[list["ProductionModel"]] = relationship(back_populates="category", lazy="selectin")

    # category_genre_associations: Mapped[list["CategoryGenreAssociation"]] = relationship(back_populates="category", lazy="selectin")
    # genres = association_proxy("category_genre_associations", "genre")

    def __str__(self):
        return self.name
