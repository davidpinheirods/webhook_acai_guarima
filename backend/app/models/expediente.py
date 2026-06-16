from sqlalchemy import Column, Integer, Numeric, Date, Enum, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

# Definindo as opções de status do expediente
class StatusExpediente(str, enum.Enum):
    ABERTO = "Aberto"
    FECHADO = "Fechado"

class Expediente(Base):
    __tablename__ = "expedientes"

    id = Column(Integer, primary_key=True, index=True)
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"), nullable=False)
    data_operacao = Column(Date, nullable=False, default=func.current_date())
    
    # Controle Físico e Financeiro (Numeric(10,2) garante precisão de centavos)
    litros_pegos = Column(Numeric(10, 2), nullable=False)
    litros_devolvidos = Column(Numeric(10, 2), default=0.00)
    preco_litro = Column(Numeric(10, 2), nullable=False)
    comissao_fixa = Column(Numeric(10, 2), default=0.00)
    
    status = Column(Enum(StatusExpediente), default=StatusExpediente.ABERTO)
    fechado_em = Column(DateTime(timezone=True), nullable=True)

    # Relacionamentos
    vendedor = relationship("Vendedor", back_populates="expedientes")
    transacoes = relationship("TransacaoPix", back_populates="expediente")