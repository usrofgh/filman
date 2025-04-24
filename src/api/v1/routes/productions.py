from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_admin_user, get_current_active_user
from src.domains.productions.dependencies import ProductionServiceDep
from src.domains.productions.schemas import ProductionReadSchema, ProductionCreateSchema, ProductionFilterSchema, \
    ProductionUpdateSchema

production_router: APIRouter = router_factory(
    prefix="/productions",
    tags=["Productions"],
    id_name="production_id",
    read_schema=ProductionReadSchema,
    create_schema_=ProductionCreateSchema,
    filter_schema_=ProductionFilterSchema,
    update_schema_=ProductionUpdateSchema,
    service_dep=ProductionServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)
