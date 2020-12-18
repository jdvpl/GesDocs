from typing import List

from fastapi                    import Depends, APIRouter ,HTTPException
from sqlalchemy.orm             import Session

from db.db_conection            import get_db

from db.user_db                 import UserInDB
from models.user_models         import UserIn, UserOut, UserRegIn

from db.documents_db            import DocumentsInDB
from models.documents_models    import DocumentsIn, DocumentNewIn, DocumentsOut, DocumentsSummaryOut

router = APIRouter()

@router.post("/crear-documento/", response_model = DocumentsSummaryOut)
async def create_docs(document: DocumentNewIn, db: Session=Depends(get_db)):
    
    new_document_in_db = DocumentsInDB(**DocumentNewIn.dic(), state = True)
    db.add(new_document_in_db)
    db.commit()
    db.refresh(DocumentsInDB)

    return DocumentsInDB

@router.get("/documentos-usuario/", response_model = DocumentsSummaryOut)
async def consult_docs(doc: DocumentsIn, db: Session=Depends(get_db)):
    
    documents_user_in_db =  db.query(documents).filter((email == doc.email)and( state == True)).all

    return documents_user_in_db

@router.get("/detalles-documento/", response_model = DocumentsOut)
async def  consult_one_doc(doc: DocumentsIn, db: Session=Depends(get_db)):

    document_in_db = db.query(documents).get(doc.id_doc)

    return document_in_db

@router.post("/eliminar-documento/",)
async def delete_doc(doc: DocumentsIn, db: Session=Depends(get_db)):

    document_in_db = db.query(documents).get(doc.id_doc)

    document_in_db.state = False
    db.commit()
    db.refresh(document_in_db)
    
    return {"Documento ELIMINADO"}







