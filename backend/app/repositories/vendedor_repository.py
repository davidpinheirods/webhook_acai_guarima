# backend/app/repositories/vendedor_repository.py
from sqlalchemy.orm import Session
from app.models.vendedor import Vendedor
from app.schemas.vendedor import VendedorCreate

class VendedorRepository:
    
    @staticmethod
    def buscar_por_pin(db: Session, pin: str) -> Vendedor | None:
        return db.query(Vendedor).filter(Vendedor.pin == pin).first()

    @staticmethod
    def criar(db: Session, vendedor_dados: VendedorCreate) -> Vendedor:
        # Transforma o Schema do Pydantic em um Modelo do SQLAlchemy
        novo_vendedor = Vendedor(
            nome=vendedor_dados.nome,
            pin=vendedor_dados.pin.upper() # Salvamos o PIN sempre em maiúsculo
        )
        db.add(novo_vendedor)
        db.commit()
        db.refresh(novo_vendedor)
        return novo_vendedor
    
    @staticmethod
    def listar_todos(db: Session):
        # Busca todos os vendedores, ordenados por ID
        return db.query(Vendedor).order_by(Vendedor.id.asc()).all()