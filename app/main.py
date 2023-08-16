from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.router import api_router
from app.core.config import settings


def get_application() -> FastAPI:
    """
    The main function that the function call

    Return: The model of fastApi
    """

    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
    )

    application.add_middleware(CORSMiddleware, allow_origins=["*"])

    application.include_router(api_router)

    return application


app = get_application()
