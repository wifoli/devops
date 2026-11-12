# Lista de Tarefas - DevOps

API REST de lista de tarefas feita com FastAPI para a extensão DevOps da PUCPR.
Permite criar, listar, ver, concluir e apagar tarefas. Os dados ficam num banco PostgreSQL.

## Tecnologias

- Python 3.14
- FastAPI
- SQLModel e PostgreSQL
- pytest e pylint
- Docker e Docker Hub
- GitHub Actions
- Render

## Como rodar na sua máquina

### Com Docker

```
docker network create tarefas
docker run -d --name banco --network tarefas -e POSTGRES_USER=devops -e POSTGRES_PASSWORD=password -e POSTGRES_DB=devops postgres:16-alpine
docker run -d --name api --network tarefas --restart on-failure -p 8000:8000 -e DATABASE_USERNAME=devops -e DATABASE_PASSWORD=password -e DATABASE_ADDRESS=banco -e DATABASE=devops wifoli/tarefas:2.0
```

Depois abra http://localhost:8000/docs

### Sem Docker (precisa de um PostgreSQL rodando na sua máquina)

```
pip install -r requirements.txt
export DATABASE_USERNAME=devops DATABASE_PASSWORD=password DATABASE_ADDRESS=localhost DATABASE=devops
fastapi run app/api.py
```

Depois abra http://localhost:8000/docs

### Testes

```
pytest
pylint app/
```
