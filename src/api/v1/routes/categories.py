from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_active_user, get_current_admin_user
from src.domains.categories.dependencies import CategoryServiceDep
from src.domains.categories.schemas import CategoryCreateSchema, CategoryFilterSchema, CategoryReadSchema, CategoryUpdateSchema

category_router: APIRouter = router_factory(
    prefix="/categories",
    tags=["Categories"],
    id_name="category_id",
    read_schema=CategoryReadSchema,
    create_schema_=CategoryCreateSchema,
    filter_schema_=CategoryFilterSchema,
    update_schema_=CategoryUpdateSchema,
    service_dep=CategoryServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)