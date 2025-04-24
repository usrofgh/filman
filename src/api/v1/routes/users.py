from fastapi import APIRouter
from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_active_user, get_current_admin_user
from src.domains.users.dependencies import UserServiceDep
from src.domains.users.schemas import UserReadSchema, UserFilterSchema, UserCreateSchema


user_router: APIRouter = router_factory(
    prefix="/users",
    tags=["Users"],
    id_name="user_id",
    read_schema=UserReadSchema,
    create_schema_=UserCreateSchema,
    filter_schema_=UserFilterSchema,
    service_dep=UserServiceDep,
    include_endpoints=["create", "list", "get", "delete"],
    dependencies={
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "delete": [get_current_admin_user],
    }
)