from pydantic import UUID4, BaseModel


class PersonRoleSchema(BaseModel):
    person_id: UUID4
    role_id: UUID4
