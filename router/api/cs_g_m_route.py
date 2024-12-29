from fastapi import APIRouter,Depends,status,HTTPException,Path,Depends
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import (select,insert,update,delete,join,and_, or_ )
from fastapi.encoders import jsonable_encoder
from validation.cs_g_m import CsgmSave,CsgmResponse,CsgmUpdate,id_checker
from fastapi.responses import JSONResponse, ORJSONResponse
from database.model_functions.cs_grp_m import (save_new_cs_group,get_all_data,get_all_active_data,get_data_by_id,update_by_id)
from exception.custom_exception import CustomException
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)

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

@router.get("/cs-g-m-list", response_model=CsgmResponse, name="csgmlist")
def getCsgmList(db:Session = Depends(get_db)):
    try:
        allDbData = get_all_data(db=db)
        http_status_code = status.HTTP_200_OK
        datalist = list()
        
        for dbdata in allDbData:
            datadict = {}
            datadict['id'] = dbdata.Csgrpm.id
            datadict['cs_grp_name'] = dbdata.Csgrpm.cs_grp_name
            datadict['cs_grp_code'] = dbdata.Csgrpm.cs_grp_code
            datadict['status'] = dbdata.Csgrpm.status
            datalist.append(datadict)
            response_dict = {
                "status_code": http_status_code,
                "status":True,
                "data":datalist
            }
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

@router.get("/cs-g-m-active-list", response_model=CsgmResponse, name="csgmactivelist")
def getCsgmList(db:Session = Depends(get_db)):
    try:
        allDbData = get_all_active_data(db=db)
        http_status_code = status.HTTP_200_OK
        datalist = list()
        
        for dbdata in allDbData:
            datadict = {}
            datadict['id'] = dbdata.Csgrpm.id
            datadict['cs_grp_name'] = dbdata.Csgrpm.cs_grp_name
            datadict['cs_grp_code'] = dbdata.Csgrpm.cs_grp_code
            datadict['status'] = dbdata.Csgrpm.status
            datalist.append(datadict)
            response_dict = {
                "status_code": http_status_code,
                "status":True,
                "data":datalist
            }
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

@router.post("/cs-g-m-update/{id}", response_model=CsgmResponse, name="csgmupdate")
def csgmUpdate(
    csgm: CsgmUpdate,
    id:int = Depends(id_checker),
    db:Session = Depends(get_db)
    ):
    try:
        updatedData = update_by_id(db=db,csgm=csgm,id=id)
        http_status_code = status.HTTP_200_OK
        datalist = list()

        datadict = {}
        datadict['id'] = updatedData.Csgrpm.id
        datadict['cs_grp_name'] = updatedData.Csgrpm.cs_grp_name
        datadict['cs_grp_code'] = updatedData.Csgrpm.cs_grp_code
        datadict['status'] = updatedData.Csgrpm.status
        datalist.append(datadict)
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "data":datalist
        }

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