# 🎮 GamePedia API - Mini Projeto

Este projeto é uma solução completa de API e cliente para gerenciamento de um catálogo de jogos, desenvolvido como parte do mini-projeto sobre consumo de APIs da Fatec Rio Claro.

O projeto é dividido em duas partes principais:

1. **Server/**: Um servidor de API robusto construído com FastAPI que serve os dados dos jogos.

2. **Client/**: Uma interface de usuário (UI) interativa construída com Streamlit para consumir, visualizar e adicionar dados à API.

## 🏛️ Estrutura do Projeto

O repositório está organizado da seguinte maneira:

```
Mini_Projeto_API/
├── README.md           # Este arquivo que você está lendo
│
├── Server/
│   ├── run.py          # Script para iniciar o servidor (uvicorn)
│   ├── main.py         # Arquivo principal da API (endpoints FastAPI)
│   └── DadosJogos.py   # Simulação de banco de dados (lista Python em memória)
│
└── Client/
    ├── app.py          # Arquivo principal do cliente (interface Streamlit)
    └── api_consumer.py # Módulo para fazer requisições à API (requests)
```

## ✨ Funcionalidades

### 🚀 Backend (Servidor FastAPI)

O servidor, localizado na pasta `Server/`, fornece uma API RESTful para operações CRUD (Criar, Ler) em um catálogo de jogos.

- **Servir Catálogo Completo**: Disponibiliza um endpoint para listar todos os jogos.
- **Buscar Jogo Específico**: Permite a busca de um jogo pelo seu nome exato.
- **Adicionar Novo Jogo**: Permite que novos jogos sejam adicionados ao catálogo via POST.
- **Validação de Dados**: Utiliza Pydantic (Jogo) para garantir que os dados enviados para a API estejam no formato correto.

### 🖥️ Frontend (Cliente Streamlit)

O cliente, na pasta `Client/`, oferece uma interface web amigável para interagir com a API, sem a necessidade de ferramentas como Postman ou cURL.

- **Verificação de Status**: Verifica se a API (Server) está online antes de carregar a aplicação.
- **Listar Todos os Jogos**: Uma página que exibe o catálogo completo em expanders, mostrando detalhes de cada jogo.
- **Buscar Jogo Específico**: Uma página com um dropdown (alimentado pela própria API) que permite selecionar um jogo e ver seus detalhes.
- **Adicionar Novo Jogo**: Um formulário completo para enviar um novo jogo para a API, com validação de campos no lado do cliente.

## 🛠️ Tecnologias Utilizadas

### Backend (Servidor):

- **Python**: Linguagem principal.
- **FastAPI**: Framework web moderno para construção de APIs.
- **Uvicorn**: Servidor ASGI de alta performance para rodar o FastAPI.
- **Pydantic**: Para validação e modelagem de dados.

### Frontend (Cliente):

- **Streamlit**: Framework para criação rápida de aplicações web de dados.
- **Requests**: Biblioteca para realizar requisições HTTP e consumir a API.

## ▶️ Como Executar

Para rodar o projeto, você precisará de dois terminais: um para o servidor e outro para o cliente.

### 1. Servidor (FastAPI)

Primeiro, inicie o backend:

```
# 1. Navegue até a pasta do servidor
cd Server/

# 2. (Opcional, mas recomendado) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências (FastAPI e Uvicorn)
pip install fastapi uvicorn

# 4. Inicie o servidor
python run.py
```

O servidor estará rodando em http://127.0.0.1:8000.  
Você pode acessar a documentação interativa em http://127.0.0.1:8000/docs.

### 2. Cliente (Streamlit)

Agora, em um segundo terminal, inicie o frontend:

```
# 1. Navegue até a pasta do cliente
cd Client/

# 2. (Opcional, mas recomendado) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências (Streamlit e Requests)
pip install streamlit requests

# 4. Inicie a aplicação Streamlit
streamlit run app.py
```

A interface do cliente será aberta automaticamente no seu navegador.

## 🗺️ Endpoints da API (FastAPI)

A API (http://127.0.0.1:8000) expõe os seguintes endpoints:

| Método | Rota             | Descrição                        | Payload (Corpo) | Resposta de Sucesso (200)                  |
|--------|------------------|----------------------------------|-----------------|--------------------------------------------|
| GET    | /                | Rota raiz de boas-vindas.        | N/A             | {"mensagem": "Bem-vindo(a)..."}            |
| GET    | /jogos           | Retorna a lista completa de jogos. | N/A             | [{"id": 1, "nome": "Minecraft", ...}]      |
| GET    | /jogos/{nome_Jogo} | Busca um jogo pelo nome.         | N/A             | {"id": 1, "nome": "Minecraft", ...}        |
| POST   | /jogos           | Adiciona um novo jogo ao catálogo. | Jogo (JSON)     | {"mensagem": "Status: ...", "jogo": ...}   |

### Exemplo de Payload para POST /jogos

O JSON enviado deve seguir o modelo Jogo:

```json
{
  "nome": "Elden Ring",
  "criador_empresa": "FromSoftware",
  "descricao": "Um RPG de ação em mundo aberto...",
  "avaliacao_usuarios": 9.9,
  "media_jogadores_dez_2024": 4500000
}
```

O campo `id` é opcional e será gerenciado automaticamente pela API.
