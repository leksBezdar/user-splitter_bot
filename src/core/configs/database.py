from pydantic import model_validator

from src.core.configs.general import GeneralSettings


class PostgresSettings(GeneralSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    POSTGRES_DB_URL: str | None = None

    @model_validator(mode="before")  # noqa
    @classmethod
    def assemble_postgres_url(cls, values: dict[str, str]) -> dict[str, str]:
        if values.get("POSTGRES_DB_URL"):
            return values

        username = values.get("DB_USER")
        password = values.get("DB_PASS")
        db_name = values.get("DB_NAME")
        host = values.get("DB_HOST")
        port = values.get("DB_PORT")
        values["POSTGRES_DB_URL"] = (
            f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{db_name}"
        )

        return values
