from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            Path(__file__).parent.parent.parent.joinpath(".env.prod"),
            Path(__file__).parent.parent.parent.joinpath(".env")
        )
    )

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_EXTERNAL_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr

    API_HOST: str
    API_PORT: int
    API_EXTERNAL_PORT: int

    SECRET_KEY: SecretStr
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str

    @property
    def psql_dsn(self) -> SecretStr:
        dsn = f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}" # noqa
        return SecretStr(dsn)


settings = Settings()
print()