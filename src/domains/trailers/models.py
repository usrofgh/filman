from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.core.base_model import BaseModel


class TrailerModel(BaseModel):
    __tablename__ = "trailers"

    video_url: Mapped[str] = mapped_column(unique=True)
    duration_sec: Mapped[int]

    production_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("productions.id"))
    production: Mapped["ProductionModel"] = relationship(back_populates="trailer", lazy="selectin")
