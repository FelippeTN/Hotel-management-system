# Hotel-management-system

API de gerenciamento de pousada construída com FastAPI.

## Requisitos

- Python 3.11+
- FastAPI
- SQLAlchemy
- Uvicorn
- PostgreSQL 14+ (local ou remoto)

Instale as dependências principais com:

```powershell
pip install "fastapi[standard]" sqlalchemy "psycopg[binary]"
```

Crie o banco de dados e configure a URL de conexão (exemplo padrão):

```powershell
$env:DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/pousada_db"
```

## Executando o projeto

```powershell
uvicorn main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`. A documentação interativa pode ser acessada em `/docs`.

## Endpoints principais

- `POST /api/v1/guests`: cadastro de hóspedes
- `POST /api/v1/rooms`: cadastro de quartos
- `POST /api/v1/bookings`: criação de reservas com validação de disponibilidade
- `POST /api/v1/bookings/{id}/confirm`: confirma uma reserva
- `POST /api/v1/bookings/{id}/cancel`: cancela uma reserva
- `POST /api/v1/bookings/{id}/check-in`: realiza o check-in
- `POST /api/v1/bookings/{id}/check-out`: finaliza a estadia

Use o endpoint `GET /health` para verificação rápida de disponibilidade do serviço.