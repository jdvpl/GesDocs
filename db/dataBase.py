from datetime import date
from pydantic import BaseModel
from typing import  Dict

class UsuarioPN(BaseModel):
    email: str
    name: str
    password: str

class DocsPn(BaseModel):
    id_docPN: int =0
    name_doc:str
    frenov:date
    fvenc: date
    falarm: date
    email: str

usuariosPn:Dict[str,UsuarioPN]
usuariosPn={
    "pepita@gmail.com": UsuarioPN(email="pepita@gmail.com",name="Pepita Perez",password="pepita01"),
    "juanito@gmail.com": UsuarioPN(email="juanito@gmail.com",name="Juan Trujillo",password="juanito2020"),
    "jdvpl@gmail.com": UsuarioPN(email="jdvpl@gmail.com",name="Juan Daniel",password="jdvpl2020")

}

documentosPn: Dict[int, DocsPn]
documentosPn={
    1: DocsPn(**{"id_docPN":1,"name_doc":"SOAT","frenov":date(2021,1,22),"fvenc":date(2021,1,23),"falarm":date(2021,1,22),"email":"juanito@gmail.com"}),
    2: DocsPn(**{"id_docPN":2,"name_doc":"Licencia de conducir","frenov":date(2022,11,30),"fvenc":date(2022,11,30),"falarm":date(2022,11,15),"email":"pepita@gmail.com"}),
    3: DocsPn(**{"id_docPN":3,"name_doc":"poliza de medicina prepagada","frenov":date(2020,12,20),"fvenc":date(2020,12,20),"falarm":date(2020,12,12),"email":"juanito@gmail.com"}),
    4: DocsPn(**{"id_docPN":4,"name_doc":"SOAT","frenov":date(2021,3,12),"fvenc":date(2021,3,12),"falarm":date(2021,3,12),"email":"juanito@gmail.com"}),
    5: DocsPn(**{"id_docPN":5,"name_doc":"ASODOCS","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"juanito@gmail.com"}),
    6: DocsPn(**{"id_docPN":6,"name_doc":"sayoranara","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"juanito@gmail.com"}),  
    7: DocsPn(**{"id_docPN":7,"name_doc":"ASODOCS","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"juanito@gmail.com"}),  
    8: DocsPn(**{"id_docPN":8,"name_doc":"carne","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"jdvpl@gmail.com"}),  
    9: DocsPn(**{"id_docPN":9,"name_doc":"papa","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"jdvpl@gmail.com"}),  
    10: DocsPn(**{"id_docPN":10,"name_doc":"pollo","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"juanito@gmail.com"}),  
    11: DocsPn(**{"id_docPN":11,"name_doc":"sastre","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"jdvpl@gmail.com"}),  
    12: DocsPn(**{"id_docPN":12,"name_doc":"ASODOCS","frenov":date(2020,4,30),"fvenc":date(2020,5,7),"falarm":date(2020,4,25),"email":"jdvpl@gmail.com"})  
  
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

generator = {"id":12}
def crear_docs(documentoPn:DocsPn):
    generator["id"] = generator["id"] + 1
    documentoPn.id_docPN=generator["id"]
    documentosPn[documentoPn.id_docPN]=documentoPn
    return True



