from src.core.base_service import BaseService
from src.domains.comment_reactions.models import CommentReactionModel
from src.domains.comment_reactions.repository import CommentReactionRepository
from src.domains.comment_reactions.schemas import CommentReactionCreateSchema, CommentReactionFilterSchema, CommentReactionUpdateSchema


class CommentReactionService(
    BaseService[
        CommentReactionModel,
        CommentReactionRepository,
        CommentReactionCreateSchema,
        CommentReactionFilterSchema,
        CommentReactionUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: CommentReactionCreateSchema) -> dict:
        return {}
