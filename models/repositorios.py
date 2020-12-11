from models.models import UserIn,ContactoConEmail
from db.dataBase import obtener_usuario_email,obtener_Docs_email

def obtener_doc_con_email(email: str):
    usuario = obtener_usuario_email(email)
    if usuario is None:
        return None
    documentos = obtener_Docs_email(email)

    documentos_con_email = ContactoConEmail(
        **usuario.dict(), documentosPn=documentos)
    return documentos_con_email