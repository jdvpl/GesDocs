from pydantic import BaseModel
from datetime import date

class DocumentsIn(BaseModel):
    id_doc  : int
    email   : str
   
class DocumentNewIn(BaseModel):
    name_doc    : str
    description : str
    duedate     : date
    alarmdate   : date

class DocumentsOut(BaseModel):
    id_doc      : int
    name_doc    : str
    description : str
    duedate     : date
    alarmdate   : date
    class Config:
        orm_mode = True

class DocumentsSummaryOut(BaseModel):
    id_doc      : int
    name_doc    : str
    alarmdate   : date
    class Config:
        orm_mode = True
