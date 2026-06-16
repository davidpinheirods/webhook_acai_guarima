# backend/app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Cria o "motor" que conecta no MySQL
engine = create_engine(settings.DATABASE_URL)

# Cria a fábrica de sessões (cada requisição terá sua própria sessão)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base que todos os nossos modelos (tabelas) vão herdar
Base = declarative_base()

# Dependência do FastAPI para injetar o banco nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()