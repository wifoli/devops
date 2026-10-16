from fastapi import FastAPI, Response, status
from datetime import datetime

APP = FastAPI()

@APP.get("/")
async def index():
    return {"mensagem": "Olá, mundo!"}


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

def encontrar_tarefa(id: int) -> dict | None:
    global TAREFAS
    for tarefa in TAREFAS:
        if id == int(tarefa["id"]):
            return tarefa

@APP.get("/tarefas")
async def tarefas():
    return TAREFAS

@APP.post("/tarefas")
async def post_tarefas(titulo: str, descricao: str):
    tarefa_nova = criar_tarefa(titulo, descricao)
    TAREFAS.append(tarefa_nova)

    return {"message": "ok"}

@APP.get("/tarefas/{id}")
async def tarefa_especifica(id: int):
    tarefa = encontrar_tarefa(id)

    return tarefa if tarefa else {"message": "Tarefa não existente"} 

@APP.put("/tarefas/{id}")
async def concluir_tarefa(id: int):
    tarefa = encontrar_tarefa(id)

    if not tarefa:
        return {"message": "Tarefa não existente"}
    elif tarefa["concluida"] == True:
        return {"message": "Atarefa já está concluida"}
    
    tarefa["concluida"] = True
    tarefa["concluida_em"] = datetime.now()
    return tarefa

@APP.delete("/tarefas/{id}")
async def apagar_tarefa(id: int):
    tarefa = encontrar_tarefa(id)

    if not tarefa:
        return {"message": "Tarefa não existente"}

    TAREFAS.remove(tarefa)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

