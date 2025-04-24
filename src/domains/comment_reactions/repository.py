from src.core.base_repository import BaseRepository
from src.domains.comment_reactions.models import CommentReactionModel


class CommentReactionRepository(BaseRepository[CommentReactionModel]):
    MODEL = CommentReactionModel
