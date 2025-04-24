from src.core.base_repository import BaseRepository
from src.domains.users.models import UserModel


class UserRepository(BaseRepository[UserModel]):
    MODEL = UserModel

    async def get_by_email(self, email: str) -> UserModel | None:
        return await self.get_by(email=email)
