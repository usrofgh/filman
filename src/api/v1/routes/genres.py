from fastapi import APIRouter

from src.api.router_factory import router_factory
from src.domains.auth.dependencies import get_current_admin_user, get_current_active_user
from src.domains.genres.dependencies import GenreServiceDep
from src.domains.genres.schemas import GenreReadSchema, GenreCreateSchema, GenreFilterSchema, GenreUpdateSchema


genre_router: APIRouter = router_factory(
    prefix="/genres",
    tags=["Genres"],
    id_name="genre_id",
    read_schema=GenreReadSchema,
    create_schema_=GenreCreateSchema,
    filter_schema_=GenreFilterSchema,
    update_schema_=GenreUpdateSchema,
    service_dep=GenreServiceDep,
    include_endpoints=["create", "list", "get", "patch", "delete"],
    dependencies={
        "create": [get_current_admin_user],
        "list": [get_current_active_user],
        "get": [get_current_active_user],
        "patch": [get_current_admin_user],
        "delete": [get_current_admin_user],
    }
)
