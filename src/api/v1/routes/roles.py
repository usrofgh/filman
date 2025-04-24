from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_admin_user, get_current_active_user
from src.domains.roles.dependencies import RoleServiceDep
from src.domains.roles.schemas import RoleReadSchema, RoleCreateSchema, RoleFilterSchema, RoleUpdateSchema


role_router: APIRouter = router_factory(
    prefix="/roles",
    tags=["Roles"],
    id_name="role_id",
    read_schema=RoleReadSchema,
    create_schema_=RoleCreateSchema,
    filter_schema_=RoleFilterSchema,
    update_schema_=RoleUpdateSchema,
    service_dep=RoleServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)