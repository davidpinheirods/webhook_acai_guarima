# backend/app/services/auth_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.vendedor_repository import VendedorRepository
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.auth import LoginRequest, LoginResponse

class AuthService:
    
    @staticmethod
    def login_vendedor(db: Session, credenciais: LoginRequest) -> LoginResponse:
        # 1. Verifica se o Vendedor existe pelo PIN e está ativo
        vendedor = VendedorRepository.buscar_por_pin(db, credenciais.pin.upper())
        if not vendedor or not vendedor.ativo:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="PIN inválido ou vendedor inativo."
            )

        # 2. Verifica se ele tem um expediente ABERTO (autorização para vender hoje)
        expediente = ExpedienteRepository.buscar_aberto_por_vendedor(db, vendedor.id)
        if not expediente:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você não tem um dia de trabalho aberto hoje. Fale com o administrador."
            )

        # 3. Retorna os dados essenciais para o frontend do celular salvar na memória
        return LoginResponse(
            vendedor_id=vendedor.id,
            nome=vendedor.nome,
            expediente_id=expediente.id, # O frontend vai precisar desse ID para gerar o Pix!
            mensagem="Login efetuado com sucesso!"
        )