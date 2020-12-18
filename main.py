from fastapi import Depends, FastAPI

from routers.user_router import router as router_users
from routers.documents_router import router as router_documents

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://127.0.0.1:8000", "http://localhost:8000",
    "http://127.0.0.1:8081","http://localhost:8081", "http://127.0.0.1:8080","http://localhost:8080",
    "https://ges-docs.herokuapp.com/"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

api.include_router(router_users)
api.include_router(router_documents)