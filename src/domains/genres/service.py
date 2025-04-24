from src.core.base_service import BaseService
from src.domains.genres.models import GenreModel
from src.domains.genres.repository import GenreRepository
from src.domains.genres.schemas import GenreCreateSchema, GenreFilterSchema, GenreUpdateSchema


class GenreService(
    BaseService[
        GenreModel,
        GenreRepository,
        GenreCreateSchema,
        GenreFilterSchema,
        GenreUpdateSchema
    ]
):
    def _unique_create_filter(self, create_schema: GenreCreateSchema) -> dict:
        return {"name": create_schema.name}
