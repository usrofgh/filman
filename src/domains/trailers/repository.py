from src.core.base_repository import BaseRepository
from src.domains.trailers.models import TrailerModel


class TrailerRepository(BaseRepository[TrailerModel]):
    MODEL = TrailerModel
