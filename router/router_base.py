from fastapi import APIRouter, FastAPI
from router.api import test_route

api_router = APIRouter()
api_router.include_router(test_route.router, prefix="", tags=["Test"])
