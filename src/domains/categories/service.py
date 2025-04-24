from src.core.base_service import BaseService
from src.domains.categories.models import CategoryModel
from src.domains.categories.repository import CategoryRepository
from src.domains.categories.schemas import CategoryCreateSchema, CategoryFilterSchema, CategoryUpdateSchema


class CategoryService(
    BaseService[
        CategoryModel,
        CategoryRepository,
        CategoryCreateSchema,
        CategoryFilterSchema,
        CategoryUpdateSchema
    ]
):

    def _unique_create_filter(self, create_schema: CategoryCreateSchema) -> dict:
        return {"name": create_schema.name}
