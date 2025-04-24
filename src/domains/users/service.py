from pydantic import EmailStr

from src.core.base_exceptions import AlreadyExists, DoesNotExist
from src.core.base_service import BaseService
from src.core.security import get_password_hash
from src.domains.users.models import UserModel
from src.domains.users.repository import UserRepository
from src.domains.users.schemas import UserFilterSchema, UserCreateDBSchema, UserCreateSchema, UserUpdateSchema


class UserService(
    BaseService[
        UserModel,
        UserRepository,
        UserCreateSchema,
        UserFilterSchema,
        UserUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: UserCreateSchema) -> dict:
        return {"email": create_schema.email}

    async def create_one(self, create_schema: UserCreateSchema) -> UserModel:
        record = await self._repository.get_by_email(create_schema.email)
        if record:
            raise AlreadyExists(self._subject)

        hashed_password = get_password_hash(create_schema.password)
        db_schema = UserCreateDBSchema(email=create_schema.email, hashed_password=hashed_password)
        db_user = await self._repository.create(db_schema.model_dump())
        return db_user

    async def get_user_by_email(self, email: EmailStr) -> UserModel:
        record = await self._repository.get_by_email(email)
        if not record:
            raise DoesNotExist(self._subject)
        return record
