### Português

## 📝 Desafio AFL — Gerenciador de Tarefas

Este repositório contém a implementação de um sistema de gerenciamento de tarefas, desenvolvido como parte de um desafio técnico.
O projeto é dividido em backend (API) e frontend (interface web), seguindo boas práticas de separação de responsabilidades e arquitetura moderna.

## 🎯 Objetivo do Projeto

Criar uma aplicação fullstack que permita:

- Criar tarefas

- Listar tarefas

- Editar tarefas

- Excluir tarefas

- Autenticar usuários (signup/login)

- Associar tarefas a usuários autenticados


## Backend

| Tecnologia     | Por que foi escolhida                                                        |
| -------------- | ---------------------------------------------------------------------------- |
| **Python**     | Requisito do desafio                                                         |
| -------------- | ---------------------------------------------------------------------------- |
| **FastAPI**    | Alta performance, tipagem forte, validação automática e documentação Swagger |
| -------------- | ---------------------------------------------------------------------------- |
| **SQLAlchemy** | Abstração do banco de dados com controle e clareza compatível com SQLite     |
| -------------- | ---------------------------------------------------------------------------- |
| **SQLite**     | Requisito do desafio                                                         |
| -------------- | ---------------------------------------------------------------------------- |
| **Pydantic**   | Garantia de contratos entre API e frontend (Padrão do FastAPI)               |
| -------------- | ---------------------------------------------------------------------------- |
| **JWT**        | Padrão moderno e stateless                                                   |
| -------------- | ---------------------------------------------------------------------------- |
| **Uvicorn**    | Compatível e otimizado para FastAPI                                          |


## Frontend

| Tecnologia        | Por que foi escolhida                                  |
| ----------------- | ------------------------------------------------------ |
| **Node.js**       | Necessário para ferramentas modernas de frontend       |
| ----------------- | ------------------------------------------------------ |
| **Vite**          | Extremamente rápido e simples de configurar            |
| ----------------- | ------------------------------------------------------ |
| **React**         | Componentização, estado previsível e amplo ecossistema |
| ----------------- | ------------------------------------------------------ |
| **TypeScript**    | Menos erros e melhor manutenção                        |
| ----------------- | ------------------------------------------------------ |
| **Tailwind CSS**  | Estilo rápido, consistente e sem CSS complexo          |
| ----------------- | ------------------------------------------------------ |
| **Axios / Fetch** | Tratamento JSON e integração natural com APIs REST     |


## 📌 Regras de Negócio
👤 Usuário

- Um usuário pode se cadastrar com email e senha
- O login retorna um token JWT
- O token é necessário para acessar rotas protegidas

📝 Tarefas

- Toda tarefa pertence a um usuário
- A data de criação é gerada automaticamente no backend
- Apenas o dono da tarefa pode editá-la ou excluí-la
- Toda tarefa é criada com status PENDENTE
- O status não pode ser alterado na criação

- Status possíveis:

- pending -> Pendente
- in_progress -> Em progresso
- done -> Finalizada

🔐 Observação sobre Autenticação

- O frontend armazena o token JWT e o envia automaticamente nas requisições protegidas
- Caso o token seja inválido ou expirado, o usuário é redirecionado para o login


## 🚀 Como Rodar o Projeto (Backend + Frontend)

- Para rodar o projeto completo, tanto o Backend quanto o Frontend devem estar rodando
- Após rodar ambos o Backend e o Frontend, você pode testar as funcionalidades pelo frontend da aplicação
- Instruções para rodar as partes do projeto estão nos arquivos README dentro de suas respectivas pastas


## ✅ Considerações Finais

Este projeto foi desenvolvido com foco em:
- Clareza de regras de negócio
- Código legível e organizado
- Separação entre frontend e backend
- Uso de tecnologias modernas e amplamente adotadas no mercado

Ele pode ser facilmente expandido:
- Paginação
- Filtros de tarefas
- Refresh token
- Deploy em produção


### English

## 📝 AFL Challenge — Task Management System

This repository contains the implementation of a task management system developed as part of a technical challenge. The project is divided into backend (API) and frontend (web interface), following best practices for separation of concerns and modern architecture.

## 🎯 Project Objective

Build a fullstack application that allows users to:

- Create tasks

- List tasks

- Update tasks

- Delete tasks

- Authenticate users (signup/login)

- Associate tasks with authenticated users


## Backend

| Technology     | Why it was chosen                                                               |
| -------------- | ------------------------------------------------------------------------------- |
| **Python**     | Challenge requirement                                                           |
| -------------- | ------------------------------------------------------------------------------- |
| **FastAPI**    | High performance, strong typing, automatic validation and Swagger documentation |
| -------------- | ------------------------------------------------------------------------------- |
| **SQLAlchemy** | Clear and controlled database abstraction compatible with SQLite                |
| -------------- | ------------------------------------------------------------------------------- |
| **SQLite**     | Challenge requirement                                                           |
| -------------- | ------------------------------------------------------------------------------- |
| **Pydantic**   | Ensures API contracts between backend and frontend (FastAPI standard)           |
| -------------- | ------------------------------------------------------------------------------- |
| **JWT**        | Modern and stateless authentication approach                                    |
| -------------- | ------------------------------------------------------------------------------- |
| **Uvicorn**    | Lightweight and optimized ASGI server for FastAPI                               |


## Frontend

| Technology        | Why it was chosen                                                   |
| ----------------- | ------------------------------------------------------------------- |
| **Node.js**       | Required for modern frontend tooling                                |
| ----------------- | ------------------------------------------------------------------- |
| **Vite**          | Extremely fast and simple build tool                                |
| ----------------- | ------------------------------------------------------------------- |
| **React**         | Component-based architecture, predictable state and large ecosystem |
| ----------------- | ------------------------------------------------------------------- |
| **TypeScript**    | Better maintainability and fewer runtime errors                     |
| ----------------- | ------------------------------------------------------------------- |
| **Tailwind CSS**  | Fast, consistent styling without complex CSS                        |
| ----------------- | ------------------------------------------------------------------- |
| **Axios / Fetch** | Simplified JSON handling and seamless REST API integration          |


## 📌 Business Rules
👤 User

- A user can sign up with email and password
- Login returns a JWT token
- The token is required to access protected routes

📝 Tasks

- Each task belongs to a single authenticated user
- The creation date is automatically generated by the backend
- Only the task owner can update or delete it
- Every task is created with the status PENDING
- The status cannot be changed during creation

Allowed status values:

- pending → Pending
- in_progress → In Progress
- done → Completed

🔐 Authentication Notes

- The frontend stores the JWT token and automatically attaches it to protected requests
- If the token is invalid or expired, the user is redirected to the login page

## 🚀 How to Run the Project (Backend + Frontend)

- To run the full application, both the backend and the frontend must be running.
- After starting both services, you can test all features through the frontend interface.
- Detailed setup instructions are available in the README files inside the backend and frontend folders.


## ✅ Final Considerations

This project was developed with focus on:
- Clear business rules
- Clean and readable code
- Proper separation between frontend and backend
- Use of modern and widely adopted technologies

It can be easily extended with features such as:
- Pagination
- Task filtering
- Refresh tokens
- Production deployment

