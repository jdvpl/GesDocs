from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DATE

from db.db_conection import Base, engine

class DocumentsInDB(Base):
    __tablename__ = "documents"

    id_doc      = Column(Integer, primary_key= True, autoincrement = True)
    name_doc    = Column(String)
    description = Column (String)
    duedate     = Column(DATE)
    alarmdate   = Column (DATE, index = True)
    email       = Column(String, ForeignKey("users.email"))
    state       = Column(Boolean)

Base.metadata.create_all(bind=engine)


