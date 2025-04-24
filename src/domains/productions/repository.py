from src.core.base_repository import BaseRepository
from src.domains.productions.models import ProductionModel


class ProductionRepository(BaseRepository[ProductionModel]):
    MODEL = ProductionModel
