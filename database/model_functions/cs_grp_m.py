from database.model.cs_grp_m import Csgrpm
from fastapi import Depends, status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from config.constants import constants

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
        stmt = select(Csgrpm)
        result = db.execute(stmt)
        data = result.all()
        return data
    except ValueError as e:
        pass

def get_all_active_data(db):
    try:
        stmt = select(Csgrpm).where(Csgrpm.status == constants.DB_ACTIVE_STATUS)
        result = db.execute(stmt)
        data = result.all()
        return data
    except ValueError as e:
        pass

def get_data_by_id(db,id):
    try:
        stmt = select(Csgrpm).where(Csgrpm.id == id)
        result = db.execute(stmt)
        data = result.first()
        return data
    except ValueError as e:
        pass

def update_by_id(db,csgm,id):
    try:
        stmt = update(Csgrpm).where(Csgrpm.id == id).values(cs_grp_name=csgm.cs_grp_name,cs_grp_code=csgm.cs_grp_code)
        db.execute(stmt)
        db.commit()
        updatedData = get_data_by_id(db,id)
        return updatedData
    except ValueError as e:
        pass