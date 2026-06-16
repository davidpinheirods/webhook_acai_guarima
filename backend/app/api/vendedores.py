# backend/app/api/vendedores.py
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.vendedor import VendedorCreate, VendedorResponse
from app.services.vendedor_service import VendedorService

router = APIRouter(prefix="/admin/vendedores", tags=["Admin - Vendedores"])

@router.post("/", response_model=VendedorResponse, status_code=status.HTTP_201_CREATED)
def criar_vendedor(vendedor_dados: VendedorCreate, db: Session = Depends(get_db)):
    """
    Rota para o Administrador cadastrar novos vendedores parceiros.
    """
    return VendedorService.cadastrar_vendedor(db, vendedor_dados)

@router.get("/", response_model=List[VendedorResponse])
def listar_vendedores(db: Session = Depends(get_db)):
    """
    Rota para o Administrador listar todos os vendedores cadastrados.
    """
    return VendedorService.listar_vendedores(db)