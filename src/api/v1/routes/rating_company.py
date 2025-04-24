from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_active_user, get_current_admin_user
from src.domains.rating_companies.dependencies import RatingCompanyServiceDep
from src.domains.rating_companies.schemas import RatingCompanyCreateSchema, RatingCompanyFilterSchema, RatingCompanyReadSchema, RatingCompanyUpdateSchema

rating_company_router: APIRouter = router_factory(
    prefix="/rating_companies",
    tags=["Rating Company"],
    id_name="rating_company_id",
    read_schema=RatingCompanyReadSchema,
    create_schema_=RatingCompanyCreateSchema,
    filter_schema_=RatingCompanyFilterSchema,
    update_schema_=RatingCompanyUpdateSchema,
    service_dep=RatingCompanyServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)