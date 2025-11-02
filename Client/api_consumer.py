import requests
import streamlit as st
from typing import List, Dict, Any, Optional

BASE_URL = "http://127.0.0.1:8000"

def check_server_status() -> bool:
    """Verifica se o servidor está online."""
    try:
        response = requests.get(f"{BASE_URL}/")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# @st.cache_data(ttl=60)  # opcional: cache de 60 segundos
def get_all_games() -> Optional[List[Dict[str, Any]]]:
    """Busca todos os jogos da API."""
    try:
        response = requests.get(f"{BASE_URL}/jogos")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar lista de jogos: {e}")
        return None

def get_game_by_name(nome: str) -> Optional[Dict[str, Any]]:
    """Busca jogo pelo nome."""
    try:
        # rota correta do servidor FastAPI → /jogos/{nome}
        response = requests.get(f"{BASE_URL}/jogos/{nome}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None and e.response.status_code == 404:
            st.warning("Jogo não encontrado.")
        else:
            st.error(f"Erro ao buscar jogo: {e}")
        return None

def add_game(jogo_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Adiciona novo jogo ao catálogo."""
    try:
        # garantir tipos corretos
        jogo_data["avaliacao_usuarios"] = float(jogo_data["avaliacao_usuarios"])
        jogo_data["media_jogadores_dez_2024"] = int(jogo_data["media_jogadores_dez_2024"])

        response = requests.post(f"{BASE_URL}/jogos", json=jogo_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao adicionar jogo: {e}")
        if e.response is not None:
            try:
                detalhe = e.response.json().get("detail", "N/A")
                st.error(f"Detalhe da API: {detalhe}")
            except:
                pass
        return None
