from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql
import os
from config import settings
from core.utils import Logger

syslog = Logger("SystemStatusLog").getLogger


def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        if not os.path.exists(os.path.join(*settings.SINGLE_FILE_STORAGE_PATH)):
            os.makedirs(os.path.join(*settings.SINGLE_FILE_STORAGE_PATH))
        if not os.path.exists(os.path.join(*settings.META_FILE_STORAGE_PATH)):
            os.makedirs(os.path.join(*settings.META_FILE_STORAGE_PATH))

        await register_mysql(app)
        syslog.info("FASTAPI startup")
        pass

    return app_start


def stopping(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        syslog.info("FASTAPI shutdown")

    return stop_app
