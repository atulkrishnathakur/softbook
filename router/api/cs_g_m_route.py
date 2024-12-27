from fastapi import APIRouter,Depends,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import (select,insert,update,delete,join,and_, or_ )
from fastapi.encoders import jsonable_encoder
from validation.cs_g_m import CsgmSave,CsgmResponse
from fastapi.responses import JSONResponse, ORJSONResponse
from database.model_functions.cs_grp_m import save_new_cs_group
from exception.custom_exception import CustomException
from pydantic import ValidationError

router = APIRouter()

@router.post("/cs-g-m-save", response_model=CsgmResponse, name="csgmsave")
def csgmSave(csgm: CsgmSave, db:Session = Depends(get_db)):
    try:
        insertedData = save_new_cs_group(db=db, csgm=csgm)
        http_status_code = status.HTTP_200_OK
        datalist = list()
        
        datadict = {}
        datadict['id'] = insertedData.id
        datadict['cs_grp_name'] = insertedData.cs_grp_name
        datadict['cs_grp_code'] = insertedData.cs_grp_code
        datadict['status'] = insertedData.status
        datalist.append(datadict)
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "data":datalist
        }
        # by help of jsonable_encode we are sending response in json with pydantic validation
        #response = JSONResponse(content=jsonable_encoder(response_dict),status_code=http_status_code)
        #response = JSONResponse(content=response_dict,status_code=http_status_code)
        response_data = CsgmResponse(**response_dict) 
        response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
        return response
    except ValidationError as e:
        raise CustomException(
            status_code=422,
            status=False,
            message=e.errors(),
            data=[]
        )