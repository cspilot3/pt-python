import logging
from fastapi import APIRouter
from app.api.routes import (
    inventory,
)

logger = logging.getLogger(__name__)

api_router = APIRouter()

api_router.include_router(inventory.router, tags=["Inventory"])