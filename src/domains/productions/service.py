from src.core.base_service import BaseService
from src.domains.productions.models import ProductionModel
from src.domains.productions.repository import ProductionRepository
from src.domains.productions.schemas import ProductionCreateSchema, ProductionFilterSchema, ProductionUpdateSchema


class ProductionService(
    BaseService[
        ProductionModel,
        ProductionRepository,
        ProductionCreateSchema,
        ProductionFilterSchema,
        ProductionUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: ProductionCreateSchema) -> dict:
        return {"name": create_schema.name}
