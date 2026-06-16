FROM python:3.11-slim

# Cria um usuário de sistema sem privilégios de root
RUN useradd -m -s /bin/bash acai_user

WORKDIR /app

# Instala as dependências primeiro (aproveita o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Transfere a propriedade dos arquivos para o usuário seguro
RUN chown -R acai_user:acai_user /app

# Altera para o usuário seguro ANTES de rodar a aplicação
USER acai_user

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]