from src.core.base_repository import BaseRepository
from src.domains.rating_companies.models import RatingCompanyModel


class RatingCompanyRepository(BaseRepository[RatingCompanyModel]):
    MODEL = RatingCompanyModel
