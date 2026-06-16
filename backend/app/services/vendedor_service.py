# backend/app/services/vendedor_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.vendedor_repository import VendedorRepository
from app.schemas.vendedor import VendedorCreate
from app.models.vendedor import Vendedor

class VendedorService:
    
    @staticmethod
    def cadastrar_vendedor(db: Session, vendedor_dados: VendedorCreate) -> Vendedor:
        # Regra de Negócio: Verificar se o PIN já está em uso
        pin_existente = VendedorRepository.buscar_por_pin(db, vendedor_dados.pin.upper())
        if pin_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este PIN já está sendo utilizado por outro vendedor."
            )
        
        # Se estiver tudo certo, manda para o repositório salvar
        return VendedorRepository.criar(db, vendedor_dados)
    
    @staticmethod
    def listar_vendedores(db: Session):
        return VendedorRepository.listar_todos(db)