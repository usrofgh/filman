from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel


class CommentReactionModel(BaseModel):
    __tablename__ = "comment_reactions"

    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    comment_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("comments.id"))
    reaction: Mapped[bool | None]


    user: Mapped["UserModel"] = relationship(back_populates="comment_reactions", lazy="selectin")
    comment: Mapped["CommentModel"] = relationship(back_populates="reactions", lazy="selectin")



    __table_args__ = (
        UniqueConstraint("user_id", "comment_id",name="unique_comment_reaction"),
    )
