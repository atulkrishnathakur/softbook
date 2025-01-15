## Now we are going to develope a project. Project name is `softbook`
1. create softbook directory in your system
2. open terminal in ubuntu and go to `softbook` directory
 
 ```
 atul@atul-Lenovo-G570:~$ cd softbook
 ```

## github repository
 1. create a repository in github. repository name is `softbook`
  
## git configuration
- Reference: https://education.github.com/git-cheat-sheet-education.pdf
1. initializ the git
 
```
atul@atul-Lenovo-G570:~/softbook$ git init
```
2. set the user name in git
```
atul@atul-Lenovo-G570:~/softbook$ git config user.name "abcd"
```
 
3. check the user name in git
 
```
atul@atul-Lenovo-G570:~/softbook$ git config user.name
```
 
4. set the user email in git
 
```
atul@atul-Lenovo-G570:~/softbook$ git config user.email "****@***.com"
```
5. check the user email in git
 
```
atul@atul-Lenovo-G570:~/softbook$ git config user.email
```

6. set the remote url in git
```
atul@atul-Lenovo-G570:~/softbook$ git remote add origin https://github.com/atulkrishnathakur/softbook.git
```
7. check the remote urls
```
atul@atul-Lenovo-G570:~/softbook$ git remote -v
```
8. check status in git
```
atul@atul-Lenovo-G570:~/softbook$ git status
```
9. create a file `.gitignore` in softbook directory and write code in this file. This file is used to ignore some files and directories.
```
__pycache__
alembic/__pycache__
alembic/version/__pycache__
database/__pycache__
database/model/__pycache__
env
```
## how to create new branch in git?
- create a new branch like `v1-pydantic-validation`
```
(env) atul@atul-Lenovo-G570:~/softbook$ git branch v1-pydantic-validation
```
- check branch list. `*` indicate the current branch
```
(env) atul@atul-Lenovo-G570:~/softbook$ git branch
```
- switch master to new branch 
``` 
(env) atul@atul-Lenovo-G570:~/softbook$ git checkout v1-pydantic-validation
```
- push new branch on github. If branch is not in github repository then branch will be push with source code. If branch is already available  in github then only source code will be push. 
```
(env) atul@atul-Lenovo-G570:~/softbook$ git push origin v1-pydantic-validation
```
## How to merge a branch in other branch
1. Here merge `v1-pydantic-validation` branch in `master` brach.
2. first swich to `master` branch
3. run below command
```
(env) atul@atul-Lenovo-G570:~/softbook$ git merge v1-pydantic-validation
```

## How to create the virtual environment in python?
- Reference: https://fastapi.tiangolo.com/virtual-environments/

1. If in ubuntu python3.10 installed but you want to use python3.12 version then install python3.12 in ubuntu
2. create the virtual environment with python3.12 version
```
atul@atul-Lenovo-G570:~/softbook$ python3.12 -m venv env
```

3. activate the virtual environment
```
atul@atul-Lenovo-G570:~/softbook$ source env/bin/activate
```

4. After activating virtual environment check python virsion

```
(env) atul@atul-Lenovo-G570:~/softbook$ python --version

# or

(env) atul@atul-Lenovo-G570:~/softbook$ python3 --version

# or

(env) atul@atul-Lenovo-G570:~/softbook$ python3.12 --version

```
5. After activating virtual environment check the PIP

```
(env) atul@atul-Lenovo-G570:~/softbook$ pip --version

# or

(env) atul@atul-Lenovo-G570:~/softbook$ pip3 --version
```

## How to generate requirements.txt in python?
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip3 freeze > requirements.txt
```

## How to install `fastapi`?
- Reference: https://fastapi.tiangolo.com/virtual-environments/
- Reference: https://fastapi.tiangolo.com/#installation

```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install "fastapi[standard]"
```

## How to install `sqlalchemy`?
- Reference: https://docs.sqlalchemy.org/en/20/intro.html#installation-guide
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install SQLAlchemy
```

## How to install postgresql dialects
- Reference: https://docs.sqlalchemy.org/en/20/dialects/postgresql.html
- Reference: https://pypi.org/project/psycopg2-binary/
- Reference: https://www.geeksforgeeks.org/comparing-psycopg2-binary-vs-psycopg2-in-python/
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install psycopg2-binary
```

## How to install alembic to create migrations in fastapi?
- Reference: https://alembic.sqlalchemy.org/en/latest/front.html#installation
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install alembic
```
Below command will create an alembic directory with necessary configuration files.
```
(env) atul@atul-Lenovo-G570:~/softbook$ alembic init alembic
```

## How to configure alembic.ini file?
1. Open the alembic.ini file set sqlalchemy database url

```
sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/softbookdb

```

## How to configure env.py of alembic?
1. Open the `alembic/env.py` 
2. import database connection Base
3. import database models
4. set target_metadata 

```
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from database.dbconnection import Base # by atul
from database.model import * # by atul

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

target_metadata = Base.metadata # by atul

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

## How to set python-dotenv in python?
- Reference: https://pypi.org/project/python-dotenv/
- Reference: https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install python-dotenv
```
1. create the .env file in project root directory
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456789
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=softbookdb
```


## How to create a model in sqlalchemy?
1. create `database/model/__init__.py` file import model
```
from .cs_grp_m import Csgrpm
```

2. create `database/model/cs_grp_m.py` 
```
from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey,Identity)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base

class Csgrpm(Base):
    __tablename__ = 'cs_grp_m'
    __table_args__ = (PrimaryKeyConstraint('id', name='cs_grp_m_pkey'),)

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,Identity(start=1, cycle=False),primary_key=True,nullable=False)
    cs_grp_code: Mapped[String] = mapped_column('cs_grp_code',String(255),nullable=True)
    cs_grp_name: Mapped[String] = mapped_column('cs_grp_name',String(255),nullable=True)
    status: Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)
```


## How to generate migration for sqlalchemy model?
1. run below command to generate a migration file
```
(env) atul@atul-Lenovo-G570:~/softbook$ alembic revision --autogenerate -m "Initial Migration"
```
2. You can see generated migration file in `alembic/versions` directory.


## How to install pydantic?
Reference: https://docs.pydantic.dev/latest/install/ 

1. install pydantic email validator
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install 'pydantic[email]'
```

2. install pydantic timezone validator
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install 'pydantic[timezone]'
```

## About response_model
- reference: https://fastapi.tiangolo.com/tutorial/response-model/ 
- reference: https://docs.pydantic.dev/latest/concepts/validators/
1. response_model used to show in swagger in 200 status code in successfull response. It is not server response. But here, you will see a response for example. If you remove it the you will not see 200 status code for example of response.

## What is Field() in pydantic?
- https://docs.pydantic.dev/latest/concepts/fields/
- https://fastapi.tiangolo.com/tutorial/body-fields/


## How to create custom exception in FastAPI?
- create the `exception/custom_exception.py` file
```
from fastapi import HTTPException, Response, Request
from fastapi.responses import JSONResponse, ORJSONResponse

class CustomException(HTTPException):
    def __init__(self, status_code: int, status:bool | None=None, message:str | None=None, data:list | None=None):
        self.status_code = status_code
        self.status = status
        self.message = message
        self.data = data

async def unicorn_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status_code":exc.status_code,"status":exc.status,"message":exc.message,"data":exc.data},
    )

```

- add the custom exception with app in `main.py` file. So, create a `main.py` in root directory of project.

```
from fastapi import FastAPI
from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from router.router_base import api_router
from exception.custom_exception import CustomException,unicorn_exception_handler

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(
        DEBUG=True,
        title="softbook",
        summary="This is a fastapi project",
        description="This is fastapi project with sqlalchemy",
        version="1.0.0",
        openapi_url="/softbook.json",
        docs_url="/softbook-docs",
        redoc_url="/softbook-redoc",
        root_path="/api",
        root_path_in_servers=True,
        )
    include_router(app)
    return app

app = start_application()
app.add_exception_handler(CustomException,unicorn_exception_handler)
```

## How to create pydantic validation?
- create a `validation/cs_g_m.py` file
```
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from exception.custom_exception import CustomException
from typing import List
from typing_extensions import Annotated
from typing import Any
from fastapi import status
from config.message import csgrpmessage
from config.constants import constants

def cs_grp_name_checker(value: str) -> str:
    # https://docs.pydantic.dev/latest/concepts/validators/
    if value == "":
         raise CustomException(
            status_code=status.HTTP_400_BAD_REQUEST,
            status=constants.STATUS_BAD_REQUEST,
            message=csgrpmessage.CS_GRP_NAME,
            data=[]
        )
    return value

def cs_grp_status_checker(value: int) -> int:
    # https://docs.pydantic.dev/latest/concepts/validators/
    if value != 0 and value != 1:
         raise CustomException(
            status_code=status.HTTP_400_BAD_REQUEST,
            status=constants.STATUS_BAD_REQUEST,
            message=csgrpmessage.CS_GRP_STATUS,
            data=[]
        )
    return value

class CsgmSave(BaseModel):
    cs_grp_name: Annotated[str, PlainValidator(cs_grp_name_checker), Field(default="Python3",example="Python", title="The description of the item", max_length=300)]
    cs_grp_code: str | None = None
    status: Annotated[int | None, Field(default=1), PlainValidator(cs_grp_status_checker)]

def dataResponseStatusChecker(value: int)-> int:
    # https://docs.pydantic.dev/latest/concepts/validators/
    if value != 0 and value != 1:
        raise CustomException(
            status_code=status.HTTP_400_BAD_REQUEST,
            status=constants.STATUS_BAD_REQUEST,
            message="only 0 and 1 will be get in response",
            data=[]
        )    
    return value

class CsgmDataResponse(BaseModel):
    id: int = Field(example=1)
    cs_grp_name: str = Field(example="python")
    cs_grp_code: str | None = Field(example="py0011")
    status: Annotated[int, Field(example=1), PlainValidator(dataResponseStatusChecker)]

class CsgmResponse(BaseModel):
    status_code:int = Field(example=1)
    status:bool = Field(example=True)
    data: list[CsgmDataResponse] | None = None

```
- CsgmSave class used to validate data of request in router.
- CsgmResponse class used to validate data of response in router
- create `router/api/cs_g_m_route.py` file for route
```
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
```

## logging in FastAPI using loguru
Reference: https://loguru.readthedocs.io/en/stable/overview.html
Reference: https://loguru.readthedocs.io/en/stable/api/logger.html

1. install the loguru package
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install loguru
```
2. create `config/logconfig.py` file. If you use `logger.remove()` then log data will be write only in log file but if you not use `logger.remove()` then log data will be print in terminal and data will be append in log file.

```
from loguru import logger

logger.remove() # disable to print log data in linux teminal or console
logger.add("logs/softbook_{time:DD_MM_YYYY}.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
loglogger = logger
```

3. import the `loglogger` in python file and write message in log file
```
from config.logconfig import loglogger
......................
......................
......................

loglogger.debug("RESPONSE:"+str(response_data.dict()))

```

## Some important installation for authentication in FastAPI
Reference: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt
Reference: https://pyjwt.readthedocs.io/en/latest/installation.html
1. install the python-multipart

```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install python-multipart
```

2. install pyjwt

```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install pyjwt
```

3. install pyjwt[crypto]

```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install pyjwt[crypto]
```

4. install passlib
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install passlib
```

5. install passlib[bcrypt]

```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install passlib[bcrypt]
```

6. Create a random secret key that will be used to sign the JWT tokens
```
(env) atul@atul-Lenovo-G570:~/softbook$ openssl rand -hex 32
```
- copy the secrete key and add a key in .env file with secrete key
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456789
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=softbookdb
SECRET_KEY=a9e53f2c3db459d04f147f11a056a705f87fbbba6204a42efb9a37b4aed9cf48
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
## about bcrypt error
- bcrypt 4.2.1 version gives error in passlib
```
AttributeError: module 'bcrypt' has no attribute '__about__'
```

- again install bcrypt 4.0.1 version for the solution
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install bcrypt==4.0.1
```

## Registration for authentication
- create the `router/api/emp_route.py` file for route
```
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from database.session import get_db
from sqlalchemy import (select,insert,update,delete,join,and_, or_ )
from validation.emp_m import EmpSchemaIn,EmpSchemaOut,Status422Response,Status400Response
from fastapi.responses import JSONResponse, ORJSONResponse
from database.model_functions.emp_m import save_new_empm
from exception.custom_exception import CustomException
from config.message import empm_message
from config.logconfig import loglogger

router = APIRouter()

@router.post(
    "/emp-m-save",
    response_model=EmpSchemaOut,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": Status422Response},
        status.HTTP_400_BAD_REQUEST: {"model": Status400Response}
    },
    name="empmsave"
    )
def empSave(empm: EmpSchemaIn, db:Session = Depends(get_db)):
    # I keep duplicate_email_checker function outside of try block because duplicate_email_checker function raise an exception. If duplicate_email_checker keep inside function then Exception class will except it because Exception is parrent class.
    # Main point is raise keyword use the outside of try block.
    EmpSchemaIn.duplicate_email_checker(db,empm.email)
    try:
        insertedData = save_new_empm(db=db, empm=empm)
        http_status_code = status.HTTP_200_OK
        datalist = list()
        
        datadict = {}
        datadict['id'] = insertedData.id
        datadict['emp_name'] = insertedData.emp_name
        datadict['email'] = insertedData.email
        datadict['status'] = insertedData.status
        datadict['mobile'] = insertedData.mobile
        datalist.append(datadict)
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":empm_message.SAVE_SUCCESS,
            "data":datalist
        }
        response_data = EmpSchemaOut(**response_dict) 
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
```

- create `validation/emp_m.py` file for pydantic schema
```
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from typing import List
from exception.custom_exception import CustomException
from fastapi import status,Depends
from config.message import empm_message
from config.constants import constants
from typing_extensions import Annotated
from database.model_functions import emp_m

class BaseEmpSchema(BaseModel):
    emp_name: str = Field(example="Atul")
    email: EmailStr = Field(example="atul@comsysapp.com")
    mobile: str | None = Field(example="000000")
    status: int | None = Field(default=1)

class EmpSchemaIn(BaseEmpSchema):
    password: str = Field(example="aa")
    confirm_password:str = Field(example="aa")
    
    def duplicate_email_checker(db,email):
        empmObj = emp_m.get_data_by_email(db,email)
        if(empmObj is not None):
            raise CustomException(
                status_code=status.HTTP_400_BAD_REQUEST,
                status=constants.STATUS_BAD_REQUEST,
                message=empm_message.EMAIL_DUPLICATE,
                data=[]
            )

    @model_validator(mode='after')
    def check_passwords_match(self):
        pw1 = self.password
        pw2 = self.confirm_password
        if(pw1 is None):
            raise CustomException(
                status_code=status.HTTP_400_BAD_REQUEST,
                status=constants.STATUS_BAD_REQUEST,
                message=empm_message.EMP_M_PASS_REQUIRED,
                data=[]
            )
        elif(pw2 is None):
            raise CustomException(
                status_code=status.HTTP_400_BAD_REQUEST,
                status=constants.STATUS_BAD_REQUEST,
                message=empm_message.EMP_M_C_PASS_REQUIRED,
                data=[]
            )
        elif pw1 != pw2:
            raise CustomException(
                status_code=status.HTTP_400_BAD_REQUEST,
                status=constants.STATUS_BAD_REQUEST,
                message=empm_message.PASS_NOT_MATCH,
                data=[]
            )
        return self

def dataResponseStatusChecker(value: int)-> int:
    # https://docs.pydantic.dev/latest/concepts/validators/
    if value != 0 and value != 1:
        raise CustomException(
            status_code=status.HTTP_400_BAD_REQUEST,
            status=constants.STATUS_BAD_REQUEST,
            message="only 0 and 1 will be get in response",
            data=[]
        )    
    return value

class EmpDataResponse(BaseModel):
    id: int = Field(example=1)
    emp_name: str = Field(example="abcd")
    email: EmailStr = Field(example="atul@comsysapp.com") 
    mobile: str | None = Field(example="000000")
    status: Annotated[int, Field(example=1), PlainValidator(dataResponseStatusChecker)]

class EmpSchemaOut(BaseModel):
    status_code:int = Field(example=1)
    status:bool = Field(example=True)
    message:str | None = None
    data: list[EmpDataResponse] | None = None

class EmpInDB(BaseEmpSchema):
    hashed_password: str

class Status422Response(BaseModel):
    status_code:int = Field(default=422)
    status:bool = Field(default=False)
    message:str | None = "Not Processable data"
    data:list | None = []

class Status400Response(BaseModel):
    status_code:int = Field(default=400)
    status:bool = Field(default=False)
    message:str | None = "Bad request"
    data:list | None = []

```

- create the `core\hashing.py` file to generate hashed password

```
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashData():
    @staticmethod
    def create_password_hash(password):
        return pwd_context.hash(password)

    @staticmethod 
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
        
```

- create a `database/model_functions/emp_m.py`
```
from database.model.emp_m import Empm
from fastapi import Depends, status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import func
from core.hashing import HashData
from config.constants import constants
from database.dbconnection import engine
from config.logconfig import loglogger

def save_new_empm(db, empm):
    db_empm = Empm(
        emp_name=empm.emp_name,
        email=empm.email,
        mobile=empm.mobile,
        status=empm.status,
        password=HashData.create_password_hash(empm.password)
        )
    db.add(db_empm)
    db.commit()
    db.refresh(db_empm)
    return db_empm

def get_data_by_email(db,email):
    try:
        stmt = select(Empm).where(Empm.email == email)
        result = db.execute(stmt)
        data = result.first()
        return data
    except Exception as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        loglogger.debug("RESPONSE:"+str(data))
        return response

```

## Get jwt token after authentication


## About timedelta
Reference: https://www.geeksforgeeks.org/python-datetime-timedelta-function/
