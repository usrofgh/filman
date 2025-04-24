from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel


class RatingCompanyModel(BaseModel):
    __tablename__ = "rating_companies"

    name: Mapped[str] = mapped_column(index=True)
    rating_associations: Mapped[list["ProductionRatingAssociation"]] = relationship(back_populates="rating_company", lazy="selectin")

    def __str__(self):
        return self.name
