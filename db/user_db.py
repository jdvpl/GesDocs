from sqlalchemy import Column, String
from db.db_conection import Base, engine

class UserInDB(Base):
    __tablename__ = "users"

    email       = Column(String, primary_key= True, unique = True)
    name        = Column(String)
    password    = Column(String)

Base.metadata.create_all(bind=engine)