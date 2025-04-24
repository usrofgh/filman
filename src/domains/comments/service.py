from src.core.base_service import BaseService
from src.domains.comments.models import CommentModel
from src.domains.comments.repository import CommentRepository
from src.domains.comments.schemas import CommentCreateSchema, CommentFilterSchema, CommentUpdateSchema


class CommentService(
    BaseService[
        CommentModel,
        CommentRepository,
        CommentCreateSchema,
        CommentFilterSchema,
        CommentUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: CommentCreateSchema) -> dict:
        return {}
