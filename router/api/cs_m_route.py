from fastapi import APIRouter,Depends,status,HTTPException,Path
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import (select,insert,update,delete,join,and_, or_ )
from fastapi.encoders import jsonable_encoder
from validation.cs_m import CsmSave,CsmResponse,CsmUpdate,id_checker
from fastapi.responses import JSONResponse, ORJSONResponse
from database.model_functions.cs_m import (save_new_cs,get_all_data,get_all_active_data,get_data_by_id,update_by_id,soft_delete)
from exception.custom_exception import CustomException
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from config.message import csmmessage

router = APIRouter()

@router.post("/csm-save", response_model=CsmResponse, name="csmsave")
def csmSave(csm: CsmSave, db:Session = Depends(get_db)):
    try:
        CsmSave.cs_grpm_id_check_db(db,csm.cs_grp_m_id)
        
        insertedData = save_new_cs(db=db, csm=csm)
        http_status_code = status.HTTP_200_OK
        datalist = list()
        
        datadict = {}
        datadict['id'] = insertedData.id
        datadict['cs_m_name'] = insertedData.cs_m_name
        datadict['cs_m_code'] = insertedData.cs_m_code
        datadict['cs_grp_m_id'] = insertedData.cs_grp_m_id
        datadict['status'] = insertedData.status
        datalist.append(datadict)
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":csmmessage.CS_SAVE_MESSAGE,
            "data":datalist
        }
        response_data = CsmResponse(**response_dict) 
        response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
        return response
    except ValidationError as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response