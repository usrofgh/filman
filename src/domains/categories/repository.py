from src.core.base_repository import BaseRepository
from src.domains.categories.models import CategoryModel


class CategoryRepository(BaseRepository[CategoryModel]):
    MODEL = CategoryModel
