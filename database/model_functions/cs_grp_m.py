from database.model.cs_grp_m import Csgrpm
from fastapi import Depends, status

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

def update_user(db, currentUser, profileImage):
    db_user = db.query(User).filter(User.id == currentUser.id).first()
    db_user.profile_img = profileImage
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_user(db):
    try:
        alluser = db.query(User).all()
        return alluser
    except ValueError as e:
        pass