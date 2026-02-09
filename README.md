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
| **Vite**          | Extremamente rápido e simples de configurar            |
| **React**         | Componentização, estado previsível e amplo ecossistema |
| **TypeScript**    | Menos erros e melhor manutenção                        |
| **Tailwind CSS**  | Estilo rápido, consistente e sem CSS complexo          |
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
