from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import UUID4

from src.api.router_factory import router_factory, status
from src.domains.auth.dependencies import get_current_active_user
from src.domains.productions.dependencies import ProductionServiceDep
from src.domains.productions.schemas import ProductionDetailSchema
from src.domains.users.dependencies import UserServiceDep
from src.domains.users.models import UserModel

favorite_router: APIRouter = router_factory(
    prefix="/favorites",
    tags=["Favorites"]
)


@favorite_router.post(
    path="",
    status_code=status.HTTP_201_CREATED,
)
async def add_to_favorite(
    curr_user: Annotated[UserModel, Depends(get_current_active_user)],
    user_service: UserServiceDep,
    production_service: ProductionServiceDep,
    production_id: UUID4
):
    await user_service.add_to_favorite(curr_user, production_service, production_id)

@favorite_router.get(
    path="",
    response_model=list[ProductionDetailSchema],
    status_code=status.HTTP_200_OK
)
async def get_favorites(
    curr_user: Annotated[UserModel, Depends(get_current_active_user)],
):
    return curr_user.favorite_productions