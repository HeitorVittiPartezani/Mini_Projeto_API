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

