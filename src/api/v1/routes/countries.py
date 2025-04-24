from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_active_user, get_current_admin_user
from src.domains.countries.dependencies import CountryServiceDep
from src.domains.countries.schemas import CountryCreateSchema, CountryFilterSchema, CountryReadSchema, CountryUpdateSchema

country_router: APIRouter = router_factory(
    prefix="/countries",
    tags=["Countries"],
    id_name="country_id",
    read_schema=CountryReadSchema,
    create_schema_=CountryCreateSchema,
    filter_schema_=CountryFilterSchema,
    update_schema_=CountryUpdateSchema,
    service_dep=CountryServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)