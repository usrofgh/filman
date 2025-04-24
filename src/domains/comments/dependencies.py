from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.comments.repository import CommentRepository
from src.domains.comments.service import CommentService


def get_gender_service(db: SessionDep) -> CommentService:
    repository = CommentRepository(db)
    service = CommentService(repository)
    return service

CommentServiceDep = Annotated[CommentService, Depends(get_gender_service)]
