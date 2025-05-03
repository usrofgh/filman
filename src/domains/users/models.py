from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import BaseModel
from src.domains.associations.user_favorite import user_favorite_production_associations


class UserModel(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    avatar_url: Mapped[str] = mapped_column(nullable=True)
    comments: Mapped[list["CommentModel"]] = relationship(back_populates="user", lazy="selectin", cascade="all, delete-orphan")
    comment_reactions: Mapped[list["CommentReactionModel"]] = relationship(back_populates="user", lazy="selectin", cascade="all, delete-orphan")
    favorite_productions: Mapped[list["ProductionModel"]] = relationship(
        back_populates="favorited_by", secondary=user_favorite_production_associations, lazy="selectin"
    )

    def __str__(self):
        return self.email
