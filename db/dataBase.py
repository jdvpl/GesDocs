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

usuariosPn:Dict[str,UsuarioPN]
usuariosPn={
    "pepita@gmail.com": UsuarioPN(email="pepita@gmail.com",name="Pepita Perez",password="pepita01"),
    "juanito@gmail.com": UsuarioPN(email="juanito@gmail.com",name="Juan Trujillo",password="juanito2020")
}

documentosPn: Dict[int, DocsPn]
documentosPn={
    1: DocsPn(**{"id_docPN":1,"name_doc":"SOAT","frenov":2021-1-22,"fvenc":2021-1-23,"falarm":2021-122,"email":"pepita@gmail.com"}),
    2: DocsPn(**{"id_docPN":2,"name_doc":"Licencia de conducir","frenov":2022-11-30,"fvenc":2022-11-30,"falarm":2022-11-15,"email":"pepita@gmail.com"}),
    3: DocsPn(**{"id_docPN":3,"name_doc":"poliza de medicina prepagada","frenov":2020-12-20,"fvenc":2020-12-20,"falarm":2020-12-12,"email":"juanito@gmail.com"}),
    4: DocsPn(**{"id_docPN":4,"name_doc":"SOAT","frenov":2021-3-12,"fvenc":2021-3-12,"falarm":2021-3-12,"email":"juanito@gmail.com"}),
    5: DocsPn(**{"id_docPN":5,"name_doc":"ASODOCS","frenov":2020-4-30,"fvenc":2020-5-7,"falarm":2020-4-25,"email":"juanito@gmail.com"})  
}

def lista_usuarios():
    lista_usuarios=[]
    for usuario in usuariosPn:
        lista_usuarios.append(usuariosPn[usuario])
    return lista_usuarios

def obtener_usuario(usuario:str):
    if usuario in usuariosPn.keys():
        return usuariosPn[usuario]
    else:
        return None
    
def registrar_usuario(usuarioPn: UsuarioPN):
    if usuarioPn.email in usuariosPn:
        return False
    else:
        usuariosPn[usuarioPn.email]=usuarioPn
        return True

def obtener_usuario_email(email: str):
    if email in usuariosPn:
        return usuariosPn[email]
    else:
        return None


def obtener_Docs_email(email: str):
    lista_docs = []
    for documento in documentosPn.values():
        if documento.email == email:
            lista_docs.append(documento)
    return lista_docs


def crear_doc(documentoPn:DocsPn):
    if documentoPn.id_docPN in documentosPn:
        return False
    else:
        documentosPn[documentoPn.id_docPN]=documentoPn
        return True



