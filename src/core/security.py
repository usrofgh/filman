from datetime import UTC, datetime

import jwt
from asyncpg.pgproto.pgproto import timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import UUID4

from src.core.config import settings
from src.domains.auth.schemas import AccessToken

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY.get_secret_value(), settings.ALGORITHM)
    return encoded_jwt


def generate_token(id_: UUID4) -> AccessToken:
    token = {"sub": str(id_)}
    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_token = create_access_token(token, expires_delta)
    token = AccessToken(token=jwt_token, token_type="bearer")
    return token
