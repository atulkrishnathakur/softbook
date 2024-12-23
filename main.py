from fastapi import FastAPI
from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from router.router_base import api_router
from exception.custom_exception import CustomException,unicorn_exception_handler

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(DEBUG=True)
    include_router(app)
    return app

app = start_application()
app.add_exception_handler(CustomException,unicorn_exception_handler)