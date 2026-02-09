# Tasks Backend 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)

## Descrição
API RESTful para gerenciamento de tarefas, incluindo:
- Criação, edição, listagem e exclusão de tarefas
- Autenticação via JWT
- Datas no fuso horário São Paulo (GMT-3)

## Tecnologias
- Python 3.11+ --> Linguagem
- FastAPI --> API
- Uvicorn --> Servidor
- SQLAlchemy --> ORM
- Pydantic --> Validação e serialização
- Passlib(bcrypt) --> Hash
- Python-JOSE --> Token JWT
- Pytz --> Datas e horários
- SQLite --> Banco de dados

## Instalação

```bash
# criar ambiente virtual
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate    # Windows

# instalar dependências
pip install -r requirements.txt

# executar servidor
uvicorn app.main:app --reload

# Servidor disponível em: http://127.0.0.1:8000

# Swagger(descrição e teste dos endpoints): http://localhost:8000/docs


# Endpoints

Autenticação
| Método | Rota           | Descrição           |
| ------ | -------------- | ------------------- |
| POST   | /auth/login    | Login via JWT       |
| POST   | /auth/register | Registro de usuário |

Tarefas
| Método | Rota        | Descrição                        |
| ------ | ----------- | -------------------------------- |
| GET    | /tasks      | Listar tarefas                   |
| POST   | /tasks      | Criar tarefa (status = Pendente) |
| PUT    | /tasks/{id} | Atualizar tarefa                 |
| DELETE | /tasks/{id} | Excluir tarefa                   |
