# backend/app/api/auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Vendedor - Autenticação"])

@router.post("/login", response_model=LoginResponse)
def login(credenciais: LoginRequest, db: Session = Depends(get_db)):
    """
    Rota para o Vendedor fazer login no aplicativo de rua usando apenas o PIN.
    """
    return AuthService.login_vendedor(db, credenciais)