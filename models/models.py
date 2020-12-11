from pydantic import BaseModel
from db.dataBase import UsuarioPN,DocsPn
from typing import List

class UserIn(BaseModel):
    email: str
    password: str


class ContactoConEmail(UsuarioPN):
    DocumentosPn: List[DocsPn]
