# backend/app/api/dashboard.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.expediente import Expediente, StatusExpediente
from app.models.vendedor import Vendedor

router = APIRouter(prefix="/admin/dashboard", tags=["Admin - Dashboard"])

@router.get("/resumo")
def obter_resumo_dia(db: Session = Depends(get_db)):
    """
    Retorna as estatísticas do dia atual e a lista de expedientes abertos.
    """
    # 1. Soma total de litros na rua (Apenas de expedientes abertos)
    litros = db.query(func.sum(Expediente.litros_pegos))\
        .filter(Expediente.status == StatusExpediente.ABERTO).scalar() or 0.0
    
    # 2. Total de parceiros rodando agora
    ativos = db.query(Expediente)\
        .filter(Expediente.status == StatusExpediente.ABERTO).count()

    # 3. Valor de Pix Confirmados (Deixaremos 0 até integrarmos a API do banco)
    pix = 0.0

    # 4. Lista de Expedientes Abertos juntando (JOIN) com o nome do Vendedor
    expedientes_bd = db.query(Expediente, Vendedor.nome)\
        .join(Vendedor, Expediente.vendedor_id == Vendedor.id)\
        .filter(Expediente.status == StatusExpediente.ABERTO).all()
    
    lista_expedientes = []
    for exp, nome in expedientes_bd:
        lista_expedientes.append({
            "id": exp.id,
            "nome": nome,
            "pegos": float(exp.litros_pegos),
            "preco": float(exp.preco_litro),
            "status": exp.status.value
        })

    return {
        "litros_na_rua": float(litros),
        "pix_recebidos": pix,
        "parceiros_ativos": ativos,
        "expedientes": lista_expedientes
    }