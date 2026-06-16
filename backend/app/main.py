# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base

from app.models.vendedor import Vendedor
from app.models.expediente import Expediente
from app.models.pix import TransacaoPix

from app.api.vendedores import router as vendedores_router
from app.api.expedientes import router as expedientes_router
from app.api.auth import router as auth_router # <-- Importamos a rota de login
from app.api.dashboard import router as dashboard_router
from app.api.vendedor_app import router as vendedor_app_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Açaí Guarima")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Na produção, colocaremos o domínio real aqui
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vendedores_router)
app.include_router(expedientes_router)
app.include_router(auth_router) # <-- Registramos a rota
app.include_router(dashboard_router)
app.include_router(vendedor_app_router)

@app.get("/")
def read_root():
    return {
        "status": "online", 
        "mensagem": "Motor do Açaí Guarima rodando 100% no Docker!"
    }