# backend/app/schemas/expediente.py
from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional
from app.models.expediente import StatusExpediente

# O que o Admin envia pela manhã
class ExpedienteCreate(BaseModel):
    vendedor_id: int = Field(..., description="ID do Vendedor parceiro")
    litros_pegos: float = Field(..., gt=0, description="Quantidade de litros levada (deve ser maior que zero)")
    preco_litro: float = Field(..., gt=0, description="Preço de venda do litro no dia")
    comissao_fixa: float = Field(0.0, ge=0, description="Comissão do vendedor por litro ou valor fixo acordado")

# O que a API devolve (Response)
class ExpedienteResponse(BaseModel):
    id: int
    vendedor_id: int
    data_operacao: date
    litros_pegos: float
    litros_devolvidos: float
    preco_litro: float
    comissao_fixa: float
    status: StatusExpediente
    fechado_em: Optional[datetime] = None

    class Config:
        from_attributes = True