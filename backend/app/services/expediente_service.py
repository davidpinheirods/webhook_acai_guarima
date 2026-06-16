# backend/app/services/expediente_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.expediente_repository import ExpedienteRepository
from app.repositories.vendedor_repository import VendedorRepository
from app.schemas.expediente import ExpedienteCreate
from app.models.expediente import Expediente
from app.models.vendedor import Vendedor

class ExpedienteService:
    
    @staticmethod
    def abrir_expediente(db: Session, dados: ExpedienteCreate) -> Expediente:
        # 1. Verifica se o Vendedor existe (Precisamos adicionar uma função buscar_por_id no repositório do vendedor)
        vendedor = db.query(Vendedor).filter(Vendedor.id == dados.vendedor_id).first()
        if not vendedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vendedor não encontrado."
            )
        
        if not vendedor.ativo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este vendedor está inativo no sistema."
            )

        # 2. Verifica se já existe um expediente aberto para ele
        expediente_aberto = ExpedienteRepository.buscar_aberto_por_vendedor(db, dados.vendedor_id)
        if expediente_aberto:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este vendedor já possui um expediente ABERTO. Feche-o antes de abrir um novo."
            )
        
        # 3. Tudo certo, cria o novo expediente
        return ExpedienteRepository.criar(db, dados)