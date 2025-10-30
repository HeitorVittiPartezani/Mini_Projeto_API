from fastapi import FastAPI
from DadosJogos import db_Jogos
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