from typing import Annotated

from fastapi import Depends

from src.core.db import SessionDep
from src.domains.comment_reactions.repository import CommentReactionRepository
from src.domains.comment_reactions.service import CommentReactionService


def get_gender_service(db: SessionDep) -> CommentReactionService:
    repository = CommentReactionRepository(db)
    service = CommentReactionService(repository)
    return service

CommentReactionServiceDep = Annotated[CommentReactionService, Depends(get_gender_service)]
