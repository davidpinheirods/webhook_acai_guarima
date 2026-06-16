from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Vendedor(Base):
    __tablename__ = "vendedores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    pin = Column(String(20), unique=True, nullable=False, index=True)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamento: Um vendedor tem vários expedientes (dias trabalhados)
    expedientes = relationship("Expediente", back_populates="vendedor")