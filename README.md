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
atul@atul-Lenovo-G570:~/softbook$ git config user.name "Atul Krishna Thakur"
```
 
3. check the user name in git
 
```
atul@atul-Lenovo-G570:~/softbook$ git config user.name
```
 
4. set the user email in git
 
```
atul@atul-Lenovo-G570:~/softbook$ git config user.email "gitvcs@gmail.com"
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
