# backend/app/repositories/expediente_repository.py
from sqlalchemy.orm import Session
from app.models.expediente import Expediente, StatusExpediente
from app.schemas.expediente import ExpedienteCreate

class ExpedienteRepository:
    
    @staticmethod
    def buscar_aberto_por_vendedor(db: Session, vendedor_id: int) -> Expediente | None:
        # Busca se o vendedor já tem um expediente aberto (para evitar duplicidade)
        return db.query(Expediente).filter(
            Expediente.vendedor_id == vendedor_id,
            Expediente.status == StatusExpediente.ABERTO
        ).first()

    @staticmethod
    def criar(db: Session, dados: ExpedienteCreate) -> Expediente:
        novo_expediente = Expediente(
            vendedor_id=dados.vendedor_id,
            litros_pegos=dados.litros_pegos,
            preco_litro=dados.preco_litro,
            comissao_fixa=dados.comissao_fixa
        )
        db.add(novo_expediente)
        db.commit()
        db.refresh(novo_expediente)
        return novo_expediente