from database.model.cs_grp_m import Csgrpm
from fastapi import Depends, status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import func
from config.constants import constants
from database.dbconnection import engine
from fastapi.responses import JSONResponse, ORJSONResponse

def save_new_cs_group(db, csgm):
    db_csgm = Csgrpm(
        cs_grp_code=csgm.cs_grp_code,
        cs_grp_name=csgm.cs_grp_name,
        status=csgm.status
        )
    db.add(db_csgm)
    db.commit()
    db.refresh(db_csgm)
    return db_csgm

def get_all_data(db):
    try:
        stmt = select(Csgrpm).where(Csgrpm.deleted_at == None).order_by(Csgrpm.id.desc())
        result = db.execute(stmt)
        data = result.all()
        return data
    except ValueError as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response


def get_all_active_data(db):
    try:
        stmt = select(Csgrpm).where(Csgrpm.deleted_at == None).where(Csgrpm.status == constants.DB_ACTIVE_STATUS).order_by(Csgrpm.id.asc())
        result = db.execute(stmt)
        data = result.all()
        return data
    except ValueError as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response

def get_data_by_id(db,id):
    try:
        stmt = select(Csgrpm).where(Csgrpm.deleted_at == None).where(Csgrpm.id == id)
        result = db.execute(stmt)
        data = result.first()
        return data
    except ValueError as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response

def update_by_id(db,csgm,id):
    try:
        stmt = update(Csgrpm).where(Csgrpm.deleted_at == None).where(Csgrpm.id == id).values(cs_grp_name=csgm.cs_grp_name,cs_grp_code=csgm.cs_grp_code)
        db.execute(stmt)
        db.commit()
        updatedData = get_data_by_id(db,id)
        return updatedData
    except ValueError as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response

def soft_delete(db,**kwargs):
    try:
        stmt = update(Csgrpm).where(Csgrpm.deleted_at == None)
        for key, value in kwargs.items():
            stmt = stmt.where(getattr(Csgrpm,key) == value)
        stmt = stmt.values(deleted_at=func.now())
        db.execute(stmt)
        db.commit()
        return True
    except ValueError as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response
