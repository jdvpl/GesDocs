from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.user_db import UserInDB
from models.user_models import UserIn, UserRegIn, UserOut

from db.documents_db import DocumentsInDB
from models.documents_models import DocumentsIn, DocumentNewIn, DocumentsOut, DocumentsSummaryOut

router = APIRouter()

@router.post("/login-usuario/", response_model = UserOut)
async def login_user(user_in: UserIn, db: Session=Depends(get_db)):

    user_in_db = db.query(UserInDB).get(user_in.email)
    
    if user_in_db == None:
        raise HTTPException(status_code=404, detail= "El usuario NO EXISTE")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de AUTENTICACIÓN")

    return user_in_db

@router.post("/registrar-usuario/", response_model = UserOut)
async def register_user(user_in: UserRegIn, db: Session=Depends(get_db)):

    user_in_db = db.query(UserRegIn).get(user_in.email)

    if user_in_db != None:
        raise HTTPException(status_code=400, detail="El usuario YA EXISTE")

    new_user_in_db = UserInDB(**UserRegIn.dic())
    db.add(new_user_in_db)
    db.commit()
    db.refresh(user_in_db)

    return user_in_db