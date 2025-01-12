from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

class TokenCredentialIn(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    status_code:int | None = None
    status:bool | None = None
    access_token: str
   
class Logout(BaseModel):
    message: str | None = None
    status: bool | None = None
    status_code: int | None = None 
    