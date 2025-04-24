from src.core.base_repository import BaseRepository
from src.domains.comments.models import CommentModel


class CommentRepository(BaseRepository[CommentModel]):
    MODEL = CommentModel
