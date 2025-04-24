from src.core.base_repository import BaseRepository
from src.domains.genres.models import GenreModel


class GenreRepository(BaseRepository[GenreModel]):
    MODEL = GenreModel
