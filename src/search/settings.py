from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 5555
    database_url: str
    es_host: str
    # es_user: str
    # es_password: str    использовал для авторизации в es
    es_index: str
    es_type: str


setting = Settings(
    _env_file="../.env",
    _env_file_encoding="utf-8"
)
