from fastapi import FastAPI, HTTPException
from db.dataBase import lista_usuarios,obtener_usuario,UsuarioPN,DocsPn,registrar_usuario,crear_doc,obtener_Docs_email
from models.models import UserIn
from models.repositorios import obtener_doc_con_email

app = FastAPI()
@app.get('/usuarios/')   #prueba
async def obtenerUsuarios():
    return lista_usuarios()
    

@app.post("/registrar-usuario/")
async def registrar(usuario:UsuarioPN):
    registro_exitoso=registrar_usuario(usuario)
    if registro_exitoso:
        return {"msg":"Usuario Creado Correctamente"}
    else:
        raise HTTPException(status_code=400,detail="Este usuario ya existe en la base de datos")

@app.post("/login-usuario/")
async def login(usuario:UserIn):
    login_usuario_exito=obtener_usuario(usuario.email)

    if login_usuario_exito==None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if login_usuario_exito.password != usuario.password:
        return {"msg":"La constraseña esta erronea"}
    else:
        return {"Autenticado":True}


@app.get('/documentos-usuario/')  
async def obtener_documentos(email:str):
    usuario=obtener_doc_con_email(email)
    if usuario is None:
        raise HTTPException(status_code=400, detail='Usuario no encontrado')
    else:
        return usuario


@app.post("/crear-documento/")
async def crear_doc(documento:DocsPn):
    documento_exitoso=crear_doc(documento)
    if documento_exitoso:
        return {"msg":"Documento Creado Correctamente"}
    else:
        raise HTTPException(status_code=400,detail="Este documento ya existe en la base de datos")

