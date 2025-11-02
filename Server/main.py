from fastapi import FastAPI, HTTPException
from DadosJogos import db_Jogos
from pydantic import BaseModel
from typing import Optional

class Jogo(BaseModel):
    id: Optional[int] = None
    nome: str
    criador_empresa: str
    descricao:str
    avaliacao_usuarios: float
    media_jogadores_dez_2024: int

app = FastAPI()
@app.get("/")
def raiz():
    dictraiz = {
  "mensagem": "Bem-vindo(a) à API de Jogos! 👋",
  "versao": "1.0",
  "descricao": "Use o endpoint /jogos para ver a lista de jogos."
}
    return dictraiz

@app.get("/jogos")
def Listar_Jogos():
    return db_Jogos

@app.get("/jogos/{nome_Jogo}")
def Listar_jogo(nome_Jogo):
    for jogo in db_Jogos:
        if nome_Jogo == jogo["nome"]:
            return jogo
    raise HTTPException(status_code=404, detail="Jogo não encontrado")

@app.post("/jogos")
def Adicionar_Jogo(jogo: Jogo):
    jogo = jogo.dict()
    jogo["id"] = len(db_Jogos) + 1
    db_Jogos.append(jogo)
    return {
        "mensagem": "Status: jogo adicionado com sucesso!",
        "jogo": jogo
    }
