from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.core.base_exceptions import BException
from src.core.config import settings
from src.core.db import session_maker
from src.domains.auth.dependencies import get_current_user
from src.domains.auth.schemas import LoginSchema
from src.domains.auth.service import AuthService
from src.domains.users.repository import UserRepository


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        async with session_maker() as session:
            user_repo = UserRepository(session)
            auth_service = AuthService(user_repo)
            try:
                token_obj = await auth_service.login(
                    LoginSchema(email=email, password=password)
                )
                db_user = await get_current_user(user_repo, token_obj.token)
            except Exception:
                return False

            if db_user.is_active and db_user.is_admin:
                request.session["token"] = token_obj.token
                return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        async with session_maker() as session:
            user_repo = UserRepository(session)
            try:
                db_user = await get_current_user(user_repo, token)
            except BException:
                return False

            if db_user.is_active and db_user.is_admin:
                return True
        return False


authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY.get_secret_value())
