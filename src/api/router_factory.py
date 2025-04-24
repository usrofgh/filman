from typing import Annotated, Literal, TypeVar

import inflect
from fastapi import APIRouter, Depends
from fastapi.params import Path, Query
from pydantic import UUID4
from starlette import status

from src.core.base_service import BaseService
from src.core.generics import CreateSchemaG, FilterSchemaG, ReadSchemaG, UpdateSchemaG

ServiceDepG = TypeVar("ServiceDepG", bound=BaseService)

def create_deps(deps: list[callable]) -> list:
    return [Depends(dep) for dep in deps]

def router_factory(
    prefix: str,
    tags: list[str],
    id_name: str,
    service_dep: ServiceDepG,
    include_endpoints: list[Literal["create", "list", "get", "update", "patch", "delete"]],
    read_schema: type(ReadSchemaG) | None = None,
    create_schema_: type(CreateSchemaG) | None = None,
    filter_schema_: type(FilterSchemaG) | None = None,
    update_schema_: type(UpdateSchemaG) | None = None,
    dependencies: dict[str, list[Depends]] | None = None
) -> APIRouter:
    router = APIRouter(
        prefix=prefix,
        tags=tags
    )
    resource = prefix.strip("/").replace("_", " ").capitalize()
    resource_singular = inflect.engine().singular_noun(resource) or resource

    if "create" in include_endpoints:
        @router.post(
            path="",
            response_model=read_schema,
            status_code=status.HTTP_201_CREATED,
            dependencies=create_deps(dependencies.get("create", [])),
            summary=f"Create {resource_singular}"
        )
        async def create_item(
            service: service_dep,
            create_schema: create_schema_
        ):
            return await service.create_one(create_schema)

    if "list" in include_endpoints:
        @router.get(
            path="",
            response_model=list[read_schema],
            status_code=status.HTTP_200_OK,
            dependencies=create_deps(dependencies.get("list", [])),
            summary=f"Get {resource}"
        )
        async def get_items(
            service: service_dep,
            filter_schema: Annotated[filter_schema_, Query()]
        ):
            return await service.get_many(filter_schema)

    if "get" in include_endpoints:
        @router.get(
            path=f"/{{{id_name}}}",
            response_model=read_schema,
            status_code=status.HTTP_200_OK,
            dependencies=create_deps(dependencies.get("get", [])),
            summary=f"Get {resource_singular}"
        )
        async def get_item(
            service: service_dep,
            id_: UUID4 = Path(alias=id_name)
        ):
            return await service.get_by_id(id_)

    if "patch" in include_endpoints:
        @router.patch(
            path=f"/{{{id_name}}}",
            response_model=read_schema,
            status_code=status.HTTP_200_OK,
            dependencies=create_deps(dependencies.get("patch", [])),
            summary=f"Patch {resource_singular}"
        )
        async def patch_item(
            service: service_dep,
            update_schema: update_schema_,
            id_: UUID4 = Path(alias=id_name)

        ):
            return await service.update_one(id_, update_schema)

    if "delete" in include_endpoints:
        @router.delete(
            path=f"/{{{id_name}}}",
            status_code=status.HTTP_204_NO_CONTENT,
            dependencies=create_deps(dependencies.get("delete", [])),
            summary=f"Delete {resource_singular}"
        )
        async def delete_item(
            service: service_dep,
            id_: UUID4 = Path(alias=id_name)
        ):
            return await service.delete_one(id_)

    return router
