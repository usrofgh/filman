from pydantic import EmailStr
from pydantic import UUID4

from src.core.base_exceptions import AlreadyExists, DoesNotExist
from src.core.base_service import BaseService
from src.core.security import get_password_hash
from src.domains.favorites.exceptions import ProductionAlreadyInFavorite
from src.domains.productions.service import ProductionService
from src.domains.users.models import UserModel
from src.domains.users.repository import UserRepository
from src.domains.users.schemas import UserCreateDBSchema, UserCreateSchema, UserFilterSchema, UserUpdateSchema


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

    async def add_to_favorite(
        self,
        db_user: UserModel,
        production_service: ProductionService,
        production_id: UUID4
    ) -> None:
        production_ids = [production.id for production in db_user.favorite_productions]
        if production_id in production_ids:
            raise ProductionAlreadyInFavorite

        db_production = await production_service.get_by_id(production_id)
        db_user.favorite_productions.append(db_production)
