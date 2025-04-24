from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.base_model import BaseModel


class ProductionRatingAssociation(BaseModel):
    __tablename__ = "production_rating_associations"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    production_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("productions.id"))
    rating_company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("rating_companies.id"))
    rating: Mapped[float]
    count_votes: Mapped[int]

    production: Mapped["ProductionModel"] = relationship(back_populates="rating_associations", lazy="selectin")
    rating_company: Mapped["RatingCompanyModel"] = relationship(back_populates="rating_associations", lazy="selectin")

    __table_args__ = (
        UniqueConstraint("production_id", "rating_company_id",name="unique_production_rating_companies"),
    )
