from src.core.base_exceptions import BException
from fastapi import status

class ProductionAlreadyInFavorite(BException):
    STATUS_CODE = status.HTTP_409_CONFLICT
    DETAIL = "Production already in a favorite list of this user"
