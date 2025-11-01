import streamlit as st
import api_consumer
from typing import Dict, Any

st.set_page_config(page_title="GamePedia API", layout="wide", initial_sidebar_state="expanded")

# Funções de Renderização das Páginas

def render_page_list_all():
    # Renderizar a página 'Listar Todos os Jogos'
    st.header("Catálogo Completo de Jogos")
    
    # Tentar buscar os jogos
    games = api_consumer.get_all_games()
    
    if not games:
        st.info("Nenhum jogo encontrado no catálogo ou erro ao acessar a API.")
        return

    st.write(f"Total de jogos encontrados: **{len(games)}**")
    
    # Exibir os jogos em "expanders" para um visual limpo
    for game in games:
        with st.expander(f"**{game['nome']}** (Avaliação: {game['avaliacao_usuarios']})"):
            st.write(f"**Criador/Empresa:** {game['criador_empresa']}")
            st.write(f"**Descrição:** {game['descricao']}")
            st.metric(label="Média de Jogadores (Dez/2024)", value=f"{game['media_jogadores_dez_2024']:,}".replace(",", "."))

def render_page_search_one():
    # Renderiza a página 'Buscar Jogo Específico'
    st.header("Busque um Jogo pelo Nome")
    
    all_games = api_consumer.get_all_games()
    if not all_games:
        st.info("Carregando lista de jogos...")
        return
        
    game_names = [game['nome'] for game in all_games]
    selected_name = st.selectbox("Selecione um jogo:", options=game_names, index=None, placeholder="Digite ou selecione um jogo...")

    if selected_name:
        game_details = api_consumer.get_game_by_name(selected_name)
        if game_details:
            st.subheader(game_details['nome'])
            
            col1, col2 = st.columns(2)
            col1.info(f"**Empresa:** {game_details['criador_empresa']}")
            col2.warning(f"**Avaliação:** {game_details['avaliacao_usuarios']} / 10.0")
            
            st.markdown(f"**Descrição:**\n> {game_details['descricao']}")
            st.success(f"**Média de Jogadores (Dez/2024):** {game_details['media_jogadores_dez_2024']:,}".replace(",", "."))

def render_page_add_new():
    # Renderizar a página 'Adicionar Novo Jogo'
    st.header("Adicione um Novo Jogo ao Catálogo")
    st.markdown("Preencha o formulário abaixo para adicionar um novo jogo via API.")

    with st.form(key="add_game_form"):
        nome = st.text_input("Nome do Jogo *", placeholder="Ex: Elden Ring")
        criador_empresa = st.text_input("Criador / Empresa *", placeholder="Ex: FromSoftware")
        descricao = st.text_area("Descrição *", placeholder="Um RPG de ação em mundo aberto...")
        
        # Colunas para avaliaçã e média de jogadores
        col1, col2 = st.columns(2)
        avaliacao_usuarios = col1.number_input("Avaliação (0.0 a 10.0) *", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
        media_jogadores_dez_2024 = col2.number_input("Média de Jogadores (Dez/2024) *", min_value=0, step=1000, format="%d")
        
        st.caption("* Campos obrigatórios")
        
        # Botão de submit do formulário
        submit_button = st.form_submit_button(label="Adicionar Jogo")

    if submit_button:
        # Validação simples no lado do cliente
        if not nome or not criador_empresa or not descricao:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            # Criar o dicionário de dados (payload)
            game_data: Dict[str, Any] = {
                "nome": nome,
                "criador_empresa": criador_empresa,
                "descricao": descricao,
                "avaliacao_usuarios": avaliacao_usuarios,
                "media_jogadores_dez_2024": media_jogadores_dez_2024
            }
            
            st.info("Enviando dados para a API...")
            response = api_consumer.add_game(game_data)
            
            if response:
                st.success("Jogo adicionado com sucesso!")
                st.json(response) # Mostra a resposta da API (com o novo ID)
            else:
                st.error("Falha ao adicionar o jogo. Verifique os logs do servidor FastAPI.")

st.sidebar.title("🎮 GamePedia")
st.sidebar.markdown("Interface de cliente para a API de Jogos.")

# Verificar o status do servidor FastAPI
if not api_consumer.check_server_status():
    st.sidebar.error("Servidor (API) está offline!")
    st.error("Não foi possível conectar ao servidor da API em `http://127.0.0.1:8000`.")
    st.info("Verifique se o seu colega iniciou o servidor na pasta `Server/` usando `python run.py`.")
else:
    st.sidebar.success("Servidor (API) está Online!")
    
    # Menu de Navegação na Sidebar
    page = st.sidebar.radio(
        "Navegação",
        ["Listar Todos os Jogos", "Buscar Jogo Específico", "Adicionar Novo Jogo"]
    )

    # Renderizar a página selecionada
    if page == "Listar Todos os Jogos":
        render_page_list_all()
    elif page == "Buscar Jogo Específico":
        render_page_search_one()
    elif page == "Adicionar Novo Jogo":
        render_page_add_new()

st.sidebar.markdown("---")
st.sidebar.caption("Mini Projeto API - Python")