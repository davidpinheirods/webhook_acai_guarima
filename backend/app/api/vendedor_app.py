# backend/app/api/vendedor_app.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.expediente import Expediente
from app.models.pix import TransacaoPix, StatusPix

router = APIRouter(prefix="/vendedor/app", tags=["Vendedor - App Mobile"])

@router.get("/status/{expediente_id}")
def obter_status_vendedor(expediente_id: int, db: Session = Depends(get_db)):
    # Busca os dados do dia
    expediente = db.query(Expediente).filter(Expediente.id == expediente_id).first()
    if not expediente:
        return {"litros_pegos": 0.0, "total_pix": 0.0, "comissao_pix": 0.0}
        
    # Soma todos os Pix Concluídos de hoje
    total_pix = db.query(func.sum(TransacaoPix.valor))\
        .filter(TransacaoPix.expediente_id == expediente_id, TransacaoPix.status == StatusPix.CONCLUIDO)\
        .scalar() or 0.0
        
    # Lógica da Comissão do Pix: (Total Pix / Preço do Litro) * Comissão por Litro
    comissao_pix = 0.0
    if expediente.preco_litro > 0:
        litros_pix = float(total_pix) / float(expediente.preco_litro)
        comissao_pix = litros_pix * float(expediente.comissao_fixa)
        
    return {
        "litros_pegos": float(expediente.litros_pegos),
        "total_pix": float(total_pix),
        "comissao_pix": comissao_pix
    }