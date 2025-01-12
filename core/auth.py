from typing import Annotated
from fastapi import Depends, status
import jwt
from sqlalchemy.orm import Session
from database.session import get_db
from validation.auth import Token, TokenData, TokenCredentialIn,TokenOut, Logout

from fastapi import HTTPException, Response, Request


def authenticate_user(username,password,db):
    user = get_user(db,username)
    if not user:
        return False
    if not HashData.verify_password(password, user.hashed_password):
        return False    
    return user

async def get_current_user(token: Annotated[str, Depends(get_api_key)], db: Annotated[Session, Depends(get_db)]):
    logger.debug('get current user function')
    if token in blacklist:
        http_status_code = status.HTTP_401_UNAUTHORIZED 
    else:    
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("email")
        token_data = TokenData(email=email)
        user = get_user(db, email=token_data.email)
        return user

async def get_current_active_user(
    current_user: Annotated[UserSchemaOut, Depends(get_current_user)],
):
    return current_user