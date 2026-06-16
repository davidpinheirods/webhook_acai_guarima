webhook_acai_guarima/
│
├── backend/
│   ├── app/
│   │   ├── api/             # Rotas (ex: /pix/webhook, /vendedor/login)
│   │   ├── services/        # Lógica (ex: gerenciar_fechamento.py)
│   │   ├── repositories/    # Banco (ex: pix_repository.py)
│   │   ├── models/          # Tabelas (SQLAlchemy)
│   │   ├── schemas/         # Validação (Pydantic)
│   │   └── core/            # Configurações de Banco, JWT, variáveis de ambiente
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend-vendedor/
│   ├── js/
│   │   ├── api/             # Chamadas para o backend
│   │   ├── utils/           # Formatadores
│   │   └── pages/           # Lógica específica de cada tela (ex: app.js, login.js)
│   ├── css/
│   └── index.html
│
├── frontend-admin/          # Mesma lógica de módulos do vendedor
│
└── docker-compose.yml       # Orquestração do MySQL + Backend