from src.api.v1.routes.auth import auth_router
from src.api.v1.routes.categories import category_router
from src.api.v1.routes.comment_reactions import comment_reaction_router
from src.api.v1.routes.comments import comment_router
from src.api.v1.routes.countries import country_router
from src.api.v1.routes.genres import genre_router
from src.api.v1.routes.productions import production_router
from src.api.v1.routes.rating_company import rating_company_router
from src.api.v1.routes.roles import role_router
from src.api.v1.routes.trailers import trailer_router
from src.api.v1.routes.users import user_router
from fastapi import APIRouter

v1_router = APIRouter(
    prefix="/v1"
)

v1_router.include_router(auth_router)
v1_router.include_router(user_router)
v1_router.include_router(category_router)
v1_router.include_router(genre_router)
v1_router.include_router(production_router)
v1_router.include_router(trailer_router)
v1_router.include_router(role_router)
v1_router.include_router(rating_company_router)
v1_router.include_router(country_router)
v1_router.include_router(comment_router)
v1_router.include_router(comment_reaction_router)
