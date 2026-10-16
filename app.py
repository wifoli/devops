from fastapi import FastAPI
from datetime import datetime

APP = FastAPI()

#ESTRUTURA DA TAREFA
"""
{
    "id" -> int,
    "titulo" -> str,
    "descricao" -> "str",
    "concluida" -> bool,
    "criado_em" -> datetime
}
"""
TAREFAS = []

def criar_tarefa(titulo, descricao):
    return {
        "id": len(TAREFAS),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "criado_em": datetime.now()
    }

@APP.get("/tarefas")
async def tarefas():
    return TAREFAS

@APP.post("/tarefas")
async def post_tarefas(titulo: str, descricao: str):
    global TAREFAS

    tarefa_nova = criar_tarefa(titulo, descricao)
    TAREFAS.append(tarefa_nova)

    return {"message": "ok"}

@APP.get("/")
async def index():
    return {"mensagem": "Olá, mundo!"}

