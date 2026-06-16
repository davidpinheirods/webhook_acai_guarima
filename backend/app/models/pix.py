from sqlalchemy import Column, Integer, String, Numeric, Enum, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

# Opções de status do Pix
class StatusPix(str, enum.Enum):
    PENDENTE = "Pendente"
    CONCLUIDO = "Concluido"
    EXPIRADO = "Expirado"

class TransacaoPix(Base):
    __tablename__ = "transacoes_pix"

    id = Column(Integer, primary_key=True, index=True)
    expediente_id = Column(Integer, ForeignKey("expedientes.id"), nullable=False)
    txid = Column(String(255), unique=True, nullable=False, index=True)
    brcode = Column(Text, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(StatusPix), default=StatusPix.PENDENTE)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    pago_em = Column(DateTime(timezone=True), nullable=True)

    # Relacionamento inverso
    expediente = relationship("Expediente", back_populates="transacoes")