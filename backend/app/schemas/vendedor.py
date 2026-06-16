# backend/app/schemas/vendedor.py
from pydantic import BaseModel, Field
from datetime import datetime

# O que o Admin envia ao cadastrar
class VendedorCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100, description="Nome completo do parceiro")
    pin: str = Field(..., min_length=4, max_length=20, description="PIN único de acesso (ex: JOAO12)")

# O que a API devolve (Response)
class VendedorResponse(BaseModel):
    id: int
    nome: str
    pin: str
    ativo: bool
    criado_em: datetime

    # Configuração para o Pydantic ler os modelos do SQLAlchemy
    class Config:
        from_attributes = True