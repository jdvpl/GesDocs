from datetime import date
from pydantic import BaseModel
from typing import  Dict

class UsuarioPN(BaseModel):
    email: str
    name: str
    password: str

class DocsPn(BaseModel):
    id_docPN: int 
    name_doc:str
    frenov:date
    fvenc: date
    falarm: date
    email: str

UsuariosPn:Dict[str,UsuarioPN]
UsuariosPn={
    "pepita@gmail.com": UsuarioPN(email="pepita@gmail.com",name="Pepita Perez",password="pepita01"),
    "juanito@gmail.com": UsuarioPN(email="juanito@gmail.com",name="Juan Trujillo",password="juanito2020")
}

DocumentosPn: Dict[int, DocsPn]
DocumentosPn={
    1: DocsPn(**{"id_docPN":1,"name_doc":"SOAT","frenov":date(2021,1,22),"fvenc":date(2021,1,23),"falarm":date(2021,1,22),"email":"pepita@gmail.com"}),
    2: DocsPn(**{"id_docPN":2,"name_doc":"Licencia de conducir","frenov":date(2022,11,30),"fvenc":date(2022,11,30),"falarm":date(2022,11,15),"email":"pepita@gmail.com"}),
    3: DocsPn(**{"id_docPN":3,"name_doc":"poliza de medicina prepagada","frenov":'2020-12-20',"fvenc":'2020-12-20',"falarm":'2020-12-12',"email":"juanito@gmail.com"}),
    4: DocsPn(**{"id_docPN":4,"name_doc":"SOAT","frenov":'2021-03-12',"fvenc":'2021-03-12',"falarm":'2021-03-12',"email":"juanito@gmail.com"}),
    5: DocsPn(**{"id_docPN":5,"name_doc":"ASODOCS","frenov":'2020-04-30',"fvenc":'2020-05-07',"falarm":'2020-04-25',"email":"juanito@gmail.com"})  

}

def lista_usuarios():
    lista_usuarios=[]
    for usuario in UsuariosPn:
        lista_usuarios.append(UsuariosPn[usuario])
    return lista_usuarios

def obtener_usuario(usuario:str):
    if usuario in UsuariosPn.keys():
        return UsuariosPn[usuario]
    else:
        return None
    
def registrar_usuario(usuarioPn: UsuarioPN):
    if usuarioPn.email in UsuariosPn:
        return False
    else:
        UsuariosPn[usuarioPn.email]=usuarioPn
        return True

def obtener_usuario_email(email: int):
    if email in UsuariosPn:
        return UsuariosPn[email]
    else:
        return None


def obtener_Docs_email(email: str):
    lista_docs = []
    for documento in DocumentosPn.values():
        if documento.email == email:
            lista_docs.append(documento)
    return lista_docs



def crear_doc(documentoPn:DocsPn):
    if documentoPn.id_docPN in DocumentosPn:
        return False
    else:
        DocumentosPn[documentoPn.id_docPN]=documentoPn
        return True



