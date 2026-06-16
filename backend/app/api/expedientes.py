# backend/app/api/expedientes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.expediente import ExpedienteCreate, ExpedienteResponse
from app.services.expediente_service import ExpedienteService

router = APIRouter(prefix="/admin/expedientes", tags=["Admin - Expedientes"])

@router.post("/abrir", response_model=ExpedienteResponse, status_code=status.HTTP_201_CREATED)
def abrir_expediente(dados: ExpedienteCreate, db: Session = Depends(get_db)):
    """
    Rota para o Administrador abrir o dia de trabalho de um vendedor (Lançar os litros pegos).
    """
    return ExpedienteService.abrir_expediente(db, dados)