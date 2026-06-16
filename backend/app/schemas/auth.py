# backend/app/schemas/auth.py
from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    pin: str = Field(..., description="PIN de acesso do vendedor")

class LoginResponse(BaseModel):
    vendedor_id: int
    nome: str
    expediente_id: int
    mensagem: str