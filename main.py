from fastapi import FastAPI, HTTPException
import db.dataBase

app = FastAPI()

@app.get('/usuarios')   #prueba
async def obtenerUsuarios():
    return db.dataBase.lista_usuarios()
    

@app.post("/registrar-usuario")
async def registrar(usuario:db.dataBase.UsuarioPN):
    registro_exitoso=db.dataBase.registrar_usuario(usuario)
    if registro_exitoso:
        return {"msg":"Usuario Creado Correctamente"}
    else:
        raise HTTPException(status_code=400,detail="Este usuario ya existe en la base de datos")

@app.post("/login-usuario")
async def login(usuario:db.dataBase.UsuarioPN):
    

@app.get('/documentos/{email}')   #prueba
async def obtenerDocumentos(email):
    return db.dataBase.obtener_Docs_email(email)

@app.post("/crear-documento")
async def crear_doc(documento:db.dataBase.DocsPn):
    documento_exitoso=db.dataBase.crear_doc(documento)
    if documento_exitoso:
        return {"msg":"Documento Creado Correctamente"}
    else:
        raise HTTPException(status_code=400,detail="Este documento ya existe en la base de datos")