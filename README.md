## Now we are going to develope a project. Project name is `softbook`
1. create softbook directory in your system
2. open terminal in ubuntu and go to `softbook` directory
 
 ```
 atul@atul-Lenovo-G570:~$ cd softbook
 ```

## github repository
 1. create a repository in github. repository name is `softbook`
  
## git configuration
Reference: https://education.github.com/git-cheat-sheet-education.pdf
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

```

## How to create the virtual environment in python?
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
