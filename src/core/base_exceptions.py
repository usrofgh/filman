from abc import ABC

from fastapi import HTTPException, status


class BException(ABC, HTTPException):
    STATUS_CODE: status = None
    DETAIL: str = None
    HEADERS: dict = None

    def __init__(self, subject: str | None = None):
        if not self.STATUS_CODE:
            raise NotImplementedError("STATUS_CODE MUST BE SPECIFIED")
        if not self.DETAIL:
            raise NotImplementedError("DETAIL MUST BE SPECIFIED")

        if subject:
            msg = f"{subject} {self.DETAIL}"
        else:
            msg = self.DETAIL

        super().__init__(status_code=self.STATUS_CODE, detail=msg, headers=self.HEADERS)


class AlreadyExists(BException):
    STATUS_CODE = status.HTTP_409_CONFLICT
    DETAIL = "already exists"


class DoesNotExist(BException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "not found"
