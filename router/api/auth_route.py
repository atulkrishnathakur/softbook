from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi import APIRouter
from passlib.context import CryptContext


from fastapi import Depends, FastAPI, HTTPException, status
from validation.auth import Token, TokenData, TokenCredentialIn,TokenOut, Logout
from fastapi.responses import JSONResponse, ORJSONResponse
from database.session import get_db
from core.auth import authenticate_user, get_current_active_user

router = APIRouter()

@router.post("/login",response_model=TokenOut, response_class=JSONResponse,name="login")
async def login_for_access_token(credentials: TokenCredentialIn,db:Session = Depends(get_db)):
    user = authenticate_user(credentials.email, credentials.password,db)
    if not user:
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=constants.STATUS_UNAUTHORIZED,
            message=message.INCORRECT_CREDENTIALS,
            data=[]
        )
    elif(user.is_active == False):
        raise CustomException(status_code=status.HTTP_403_FORBIDDEN,status=constants.STATUS_FORBIDDEN,message=message.INACTIVE_USER,data=[])  

    access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    http_status_code: int = status.HTTP_200_OK
    user_data = {
        "status_code": http_status_code,
        "status":constants.STATUS_OK,
        "access_token":access_token,
        "token_type":settings.TOKEN_TYPE,
        "first_name": user.first_name,
        "email": user.email,
        "role": user.role,
        "country":user.country,
        "state":user.state,
        "city":user.city,
        "address":user.address,
        "zeep_code":user.zeep_code
    }
    response_data = TokenOut(**user_data)
    response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
    return response
