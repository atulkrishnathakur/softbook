from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse, ORJSONResponse, HTMLResponse
from fastapi import Depends, status, HTTPException, Request, Header
from router.router_base import api_router
from exception.custom_exception import CustomException
from config.message import auth_message

# https://fastapi.tiangolo.com/tutorial/middleware/

class AuthCheckerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, some_attribute: str):
        super().__init__(app)
        self.some_attribute = some_attribute
    # url_path_for("route name here")
    async def dispatch(self, request: Request, call_next):
        excluded_paths = [
            "/softbook-docs",
            "/api/softbook.json",
            "/api"+api_router.url_path_for("login"),
            "/api"+api_router.url_path_for("test")
            ]
        if request.url.path not in excluded_paths and not request.headers.get("ACCESS-TOKEN"):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code":status.HTTP_401_UNAUTHORIZED,
                    "status":"/api/"+api_router.url_path_for("login"),
                    "message":auth_message.LOGIN_REQUIRED,
                    "data":[]
                    },
            )
        response = await call_next(request)
        return response