from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.exceptions import RequestValidationError
from core.middleware import BaseMiddleware
from endpoints import upload, download, hello
from core.events import startup, stopping
from core import exception
from tortoise.exceptions import OperationalError, DoesNotExist, IntegrityError, ValidationError
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from config import settings

application = FastAPI(
    debug=settings.APP_DEBUG,
    title=settings.PROJECT_NAME
)

# listen events
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))

# middleware
application.add_middleware(BaseMiddleware)

application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# errors
application.add_exception_handler(HTTPException, exception.http_error_handler)
application.add_exception_handler(RequestValidationError, exception.http422_error_handler)
application.add_exception_handler(exception.UnicornException, exception.unicorn_exception_handler)
application.add_exception_handler(DoesNotExist, exception.mysql_does_not_exist)
application.add_exception_handler(IntegrityError, exception.mysql_integrity_error)
application.add_exception_handler(ValidationError, exception.mysql_validation_error)
application.add_exception_handler(OperationalError, exception.mysql_operational_error)

# routers
application.include_router(upload.upload_route)
application.include_router(download.download_route)
application.include_router(hello.root_router)


app = application
