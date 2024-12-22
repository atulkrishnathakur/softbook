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

## How to set python-dotenv in python?
- Reference: https://pypi.org/project/python-dotenv/
- Reference: https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/
```
(env) atul@atul-Lenovo-G570:~/softbook$ pip install python-dotenv
```
1. create the .env file in project root directory
