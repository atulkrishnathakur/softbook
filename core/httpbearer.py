from fastapi import Security
from passlib.context import CryptContext
from config.logconfig import loglogger
from config.loadenv import envconst
from fastapi import Depends, status
from config.message import auth_message
from exception.custom_exception import CustomException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

http_bearer = HTTPBearer() 

async def get_api_token(credentials: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)]):
    api_key = credentials.credentials
    if not api_key:
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=False,
            message=auth_message.INCORRECT_CREDENTIALS,
            data=[]
        )
    return api_key