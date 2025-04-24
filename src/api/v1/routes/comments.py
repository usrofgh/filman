from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_admin_user, get_current_active_user
from src.domains.comments.dependencies import CommentServiceDep
from src.domains.comments.schemas import CommentReadSchema, CommentCreateSchema, CommentFilterSchema, \
    CommentUpdateSchema

comment_router: APIRouter = router_factory(
    prefix="/comments",
    tags=["Comments"],
    id_name="comment_id",
    read_schema=CommentReadSchema,
    create_schema_=CommentCreateSchema,
    filter_schema_=CommentFilterSchema,
    update_schema_=CommentUpdateSchema,
    service_dep=CommentServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)
