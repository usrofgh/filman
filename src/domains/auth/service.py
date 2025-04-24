from src.core.security import generate_token, verify_password
from src.domains.auth.exceptions import InactiveUser, IncorrectCredentials
from src.domains.auth.schemas import AccessToken, LoginSchema
from src.domains.users.repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def login(self, login_schema: LoginSchema) -> AccessToken:
        db_user = await self._user_repository.get_by_email(login_schema.email)
        if not db_user or not verify_password(login_schema.password, db_user.hashed_password):
            raise IncorrectCredentials

        if not db_user.is_active:
            raise InactiveUser

        token = generate_token(db_user.id)
        return token
