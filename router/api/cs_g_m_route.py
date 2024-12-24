from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import (select,insert,update,delete,join,and_, or_ )
from fastapi.encoders import jsonable_encoder
from validation.cs_g_m import CsgmSave
from fastapi.responses import JSONResponse, ORJSONResponse
from database.model_functions.cs_grp_m import save_new_cs_group
from exception.custom_exception import CustomException

router = APIRouter()

@router.post("/cs-g-m-save",name="csgmsave")
def csgmSave(csgm: CsgmSave, db:Session = Depends(get_db)):
    try:
        insertedData = save_new_cs_group(db=db, csgm=csgm)
        http_status_code = status.HTTP_200_OK
        data = {
            "cs_grp_name": insertedData.cs_grp_name,
            "cs_grp_code": insertedData.cs_grp_code,
            "status": insertedData.status
        }
        response_data = {
            "status_code": http_status_code,
            "status":True,
            "data":data
        }
        response = JSONResponse(content=jsonable_encoder(response_data),status_code=http_status_code)
        return response
    except Exception as e:
        http_status_code = 500
        data = []
        response_data = {
            "status_code": http_status_code,
            "status":False,
            "data":data
        }
        response = JSONResponse(content=jsonable_encoder(response_data),status_code=http_status_code)
        return response