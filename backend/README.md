# Tasks Backend 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)

### Português

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


## Endpoints

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


## Instalação e configuração

Importante:
- definir uma 'secret_key' no arquivo .env.example
- renomear arquivo para .env

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
```


### English

## Description
RESTful API for task management, including:
- Task creation, update, listing, and deletion
- JWT-based authentication
- Date handling using São Paulo timezone (GMT-3)

## Technologies
- Python 3.11+ → Programming language
- FastAPI → API framework
- Uvicorn → ASGI server
- SQLAlchemy → ORM
- Pydantic → Data validation and serialization
- Passlib (bcrypt) → Password hashing
- Python-JOSE → JWT token handling
- Pytz → Date and timezone management
- SQLite → Database

## Endpoints

Authentication
| Method | Route           | Description          |
| ------ | --------------- | -------------------- |
| POST   | /auth/login     | Login with JWT       |
| POST   | /auth/register  | User registration    |

Tasks
| Method | Route           | Description                            |
| ------ | --------------- | -------------------------------------- |
| GET    | /tasks          | List tasks                             |
| POST   | /tasks          | Create task (default status = Pending) |
| PUT    | /tasks/{id}     | Update task                            |
| DELETE | /tasks/{id}     | Delete task                            |


## Installation and Setup

Important:
- Set a secret_key value inside the .env.example file
- Rename the file to .env

```bash
- Create Virtual Environment
python -m venv venv

- Activate the virtual environment:

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

- Install Dependencies
pip install -r requirements.txt

- Run the Server
uvicorn app.main:app --reload

# Server will be available at: http://127.0.0.1:8000

# Swagger documentation (interactive API testing): http://localhost:8000/docs
```

