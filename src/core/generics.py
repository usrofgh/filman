from typing import TypeVar

from pydantic import BaseModel as PydanticBaseModel


ReadSchemaG = TypeVar("ReadSchemaG", bound=PydanticBaseModel)
CreateSchemaG = TypeVar("CreateSchemaG", bound=PydanticBaseModel)
FilterSchemaG = TypeVar("FilterSchemaG", bound=PydanticBaseModel)
UpdateSchemaG = TypeVar("UpdateSchemaG", bound=PydanticBaseModel)
