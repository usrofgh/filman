from src.core.base_repository import BaseRepository
from src.domains.roles.models import RoleModel


class RoleRepository(BaseRepository[RoleModel]):
    MODEL = RoleModel
