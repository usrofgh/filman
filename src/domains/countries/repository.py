from src.core.base_repository import BaseRepository
from src.domains.countries.models import CountryModel


class CountryRepository(BaseRepository[CountryModel]):
    MODEL = CountryModel
