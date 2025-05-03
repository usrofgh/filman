from fastapi import APIRouter

from src.api.v1.routes.auth import auth_router
from src.api.v1.routes.categories import category_router
from src.api.v1.routes.comment_reactions import comment_reaction_router
from src.api.v1.routes.comments import comment_router
from src.api.v1.routes.countries import country_router
from src.api.v1.routes.favorites import favorite_router
from src.api.v1.routes.genres import genre_router
from src.api.v1.routes.productions import production_router
from src.api.v1.routes.rating_company import rating_company_router
from src.api.v1.routes.roles import role_router
from src.api.v1.routes.trailers import trailer_router
from src.api.v1.routes.users import user_router

v1_router = APIRouter(
    prefix="/v1"
)

include_router_list = [
    auth_router,
    user_router,
    category_router,
    genre_router,
    production_router,
    trailer_router,
    role_router,
    rating_company_router,
    country_router,
    comment_router,
    comment_reaction_router,
    favorite_router
]

[v1_router.include_router(router) for router in include_router_list]
