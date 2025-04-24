from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_active_user, get_current_admin_user
from src.domains.trailers.dependencies import TrailerServiceDep
from src.domains.trailers.schemas import TrailerCreateSchema, TrailerFilterSchema, TrailerReadSchema, TrailerUpdateSchema

trailer_router: APIRouter = router_factory(
    prefix="/trailers",
    tags=["Trailers"],
    id_name="trailer_id",
    read_schema=TrailerReadSchema,
    create_schema_=TrailerCreateSchema,
    filter_schema_=TrailerFilterSchema,
    update_schema_=TrailerUpdateSchema,
    service_dep=TrailerServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)