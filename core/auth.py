from typing import Annotated
from fastapi import Depends, status
import jwt
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.login import get_emp_for_login
from exception.custom_exception import CustomException
from fastapi import HTTPException, Response, Request
from core.hashing import HashData
from config.message import auth_message

def authenticate(email,password,db):
    dbempm = get_emp_for_login(db,email)
    if not dbempm:
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=False,
            message=auth_message.INCORRECT_CREDENTIALS,
            data=[]
        )
        
    if not HashData.verify_password(password, dbempm.password):
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=False,
            message=auth_message.INCORRECT_CREDENTIALS,
            data=[]
        )   
    return dbempm

'''
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


'''