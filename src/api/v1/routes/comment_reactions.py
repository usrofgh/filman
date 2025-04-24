from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_active_user, get_current_admin_user
from src.domains.comment_reactions.dependencies import CommentReactionServiceDep
from src.domains.comment_reactions.schemas import CommentReactionCreateSchema, CommentReactionFilterSchema, CommentReactionReadSchema, CommentReactionUpdateSchema

comment_reaction_router: APIRouter = router_factory(
    prefix="/comment_reactions",
    tags=["Comment Reactions"],
    id_name="category_id",
    read_schema=CommentReactionReadSchema,
    create_schema_=CommentReactionCreateSchema,
    filter_schema_=CommentReactionFilterSchema,
    update_schema_=CommentReactionUpdateSchema,
    service_dep=CommentReactionServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)