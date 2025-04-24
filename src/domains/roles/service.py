from src.core.base_service import BaseService
from src.domains.roles.models import RoleModel
from src.domains.roles.repository import RoleRepository
from src.domains.roles.schemas import RoleCreateSchema, RoleFilterSchema, RoleUpdateSchema


class RoleService(
    BaseService[
        RoleModel,
        RoleRepository,
        RoleCreateSchema,
        RoleFilterSchema,
        RoleUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: RoleCreateSchema) -> dict:
        return {"name": create_schema.name}
