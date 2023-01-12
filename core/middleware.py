import datetime
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request
from database import redis
from core.utils import show_process_time
from aioredis import Redis
from core.filelog import Logger
from core.filelog import Logger
import time

logger = Logger("HTTPMiddlewareLOG").getLogger


async def ip_intercept(ip: str):
    cache = await redis.sys_cache()
    state = await cache.get(ip)
    if state is None:
        await cache.set(ip, 1, datetime.timedelta(seconds=55))
    else:
        if state > 30:
            return False
        else:
            await cache.set(ip, state + 1)


class BaseMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        start_time = time.time()
        ip = scope.get("client")
        logger.info(f"Access from client {ip}")

        async def send_wapper(message: Message) -> None:
            process_time = time.time() - start_time
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)

        await self.app(scope, receive, send_wapper)
