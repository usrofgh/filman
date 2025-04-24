
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel
from src.domains.productions.models import ProductionModel


class CommentModel(BaseModel):
    __tablename__ = "comments"

    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    production_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("productions.id"))
    content: Mapped[str]

    user: Mapped["UserModel"] = relationship(back_populates="comments", lazy="selectin")
    production: Mapped["ProductionModel"] = relationship(back_populates="comments", lazy="selectin")
    reactions: Mapped[list["CommentReactionModel"]] = relationship(back_populates="comment", lazy="selectin")
