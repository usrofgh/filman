from pydantic import BaseModel
from pydantic import UUID4


class PersonRoleSchema(BaseModel):
    person_id: UUID4
    role_id: UUID4
