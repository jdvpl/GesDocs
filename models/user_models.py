from pydantic import BaseModel

class UserIn(BaseModel):
    email       : str
    password    : str

class UserRegIn(BaseModel):
    email       : str
    name        : str
    password    : str

class UserOut(BaseModel):
    email       : str
    name        : str
    class Config:
        orm_mode = True
