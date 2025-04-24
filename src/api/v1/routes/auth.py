from fastapi import APIRouter, status
from src.domains.auth.dependencies import AuthServiceDep
from src.domains.auth.schemas import AccessToken, LoginSchema

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post(
    path="/login",
    response_model=AccessToken,
    status_code=status.HTTP_200_OK
)
async def login(
    auth_service: AuthServiceDep,
    login_schema: LoginSchema
):
    return await auth_service.login(login_schema)
