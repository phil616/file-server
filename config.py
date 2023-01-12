from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    APP_DEBUG: bool = False

    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "FileServerAPI"

    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]

    SINGLE_FILE_STORAGE_PATH: List = [".", "storage", "single"]
    META_FILE_STORAGE_PATH: List = [".", "storage", "meta"]

    MYSQL_TABLE_AUTOGEN = True


settings = Config()
