from pydantic import BaseModel, EmailStr


class AccessToken(BaseModel):
    token: str
    token_type: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
