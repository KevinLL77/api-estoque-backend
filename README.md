# API de Gestão de Stock - KL STORE 📦

## Descrição
Este projeto é uma API RESTful completa desenvolvida em Python para gerir o stock e os produtos da KL STORE. A aplicação permite a realização de operações CRUD (Criar, Ler, Atualizar e Apagar), garantindo a validação de dados em tempo real e uma arquitetura estruturada para facilitar a escalabilidade e a manutenção.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Framework:** FastAPI (escolhido pela excelente performance e validação automática de dados)
* **Base de Dados Relacional:** SQLite (com SQLAlchemy como ORM)
* **Servidor Local:** Uvicorn

## Estrutura do Projeto (Arquitetura)
O código foi dividido de forma a separar as responsabilidades:
* `database.py`: Configuração e ligação à base de dados.
* `models.py`: Modelação das tabelas relacionais.
* `schemas.py`: Regras e validação de dados de entrada/saída (Pydantic).
* `main.py`: Endpoints da API e lógica principal.

## Como testar o projeto
1. Instale as dependências necessárias no terminal:
   ```bash
   pip install "fastapi[all]" sqlalchemy