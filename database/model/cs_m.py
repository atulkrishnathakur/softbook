from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey,Identity)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base

class Csm(Base):
    __tablename__ = 'cs_m'
    __table_args__ = (PrimaryKeyConstraint('id', name='cs_m_pkey'),)

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,Identity(start=1, cycle=False),primary_key=True,nullable=False)
    cs_m_code: Mapped[String] = mapped_column('cs_code',String(255),nullable=True)
    cs_m_name: Mapped[String] = mapped_column('cs_name',String(255),nullable=True)
    cs_grp_m_id: Mapped[String] = mapped_column('cs_grp_m_id',BigInteger,ForeignKey('cs_grp_m.id', onupdate="CASCADE",ondelete="SET NULL"),nullable=True)
    status: Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)
    deleted_at: Mapped[DateTime] = mapped_column('deleted_at',DateTime,nullable=True,default=None)