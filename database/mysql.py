
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os
from config import settings

DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('BASE_HOST', '192.168.0.3'),
                'user': os.getenv('BASE_USER', 'root'),
                'password': os.getenv('BASE_PASSWORD', 'Carvinte#616'),
                'port': int(os.getenv('BASE_PORT', 3306)),
                'database': os.getenv('BASE_DB', 'file_server_base'),
            }
        },
    },
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"},
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=settings.MYSQL_TABLE_AUTOGEN,
        add_exception_handlers=False,
    )
