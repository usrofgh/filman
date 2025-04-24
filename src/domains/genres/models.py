from datetime import datetime
from uuid import uuid4

from sqlalchemy import func

from src.core.base_model import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime

from src.domains.associations.production_genre import production_genre_associations


class GenreModel(BaseModel):
    __tablename__ = "genres"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    productions: Mapped[list["ProductionModel"]] = relationship(
        back_populates="genres",
        secondary=production_genre_associations,
    )

    # category_genre_associations: Mapped[list["CategoryGenreAssociation"]] = relationship(back_populates="genre")
    # categories = association_proxy("category_genre_associations", "category")

    def __str__(self):
        return self.name
