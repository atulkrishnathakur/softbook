from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi import APIRouter
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status
from validation.auth import AuthCredentialIn,AuthOut, Logout
from fastapi.responses import JSONResponse, ORJSONResponse
from database.session import get_db
from config.logconfig import loglogger
from core.auth import authenticate
from core.token import create_access_token
from config.loadenv import envconst
from config.message import auth_message

router = APIRouter()

@router.post(
    "/login",
    name="login"
    )
async def login(credentials:AuthCredentialIn,response_model=AuthOut, db:Session = Depends(get_db)):
    AuthCredentialIn.check_email_exist(db,credentials.email)
    authemp = authenticate(credentials.email, credentials.password, db)
    try:
        access_token_expires = timedelta(minutes=int(envconst.ACCESS_TOKEN_EXPIRE_MINUTES))
        access_token = create_access_token(
        data={"email": authemp.email}, expires_delta=access_token_expires
    )
        http_status_code = status.HTTP_200_OK
        datalist = list()
        
        datadict = {}
        datadict['id'] = authemp.id
        datadict['emp_name'] = authemp.emp_name
        datadict['email'] = authemp.email
        datadict['status'] = authemp.status
        datadict['mobile'] = authemp.mobile
        datalist.append(datadict)
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":auth_message.AUTH_SUCCESSFULL,
            "data":datalist
        }
        response_data = AuthOut(**response_dict) 
        response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
        loglogger.debug("RESPONSE:"+str(response_data.dict()))
        return response

    except Exception as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":"Type:"+str(type(e))+", Message:"+str(e)
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        loglogger.debug("RESPONSE:"+str(data))
        return response