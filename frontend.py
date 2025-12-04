# app.py (Streamlit)
import streamlit as st
import requests
from datetime import datetime

URL = "http://127.0.0.1:8000/Gols" 

st.title("Gols pelo Globo.")
resposta = requests.get(URL)
background = """
<div class="stContainer >
<style>
    background-color: gray;
</style>
"""

if resposta.status_code == 200:
    dados = resposta.json()
    partidas = dados.get("response", [])
    st.header("Feed")
    for partida in partidas:
        titulo = partida["title"]
        titulo_f = titulo.split("-")
        time_casa = titulo_f[0]
        time_visitante = titulo_f[1]
        competicao = partida["competition"]
        competicao_f = competicao.split(":")
        liga = competicao_f[1]
        thumbnail = partida["thumbnail"]
        videos = partida.get("videos", [])
        data = partida["date"]
        data_formatada = datetime.fromisoformat(data.replace("Z", "+00:00")).strftime("%d/%m/%Y %H:%M")
        with st.container():
            st.markdown(background)
            st.write(f"**Competição:** {liga}")
            st.write(f"**Jogo:** {time_casa} x {time_visitante}")
            st.write(f"**Data:** {data_formatada}") 
            if videos:
                embed_html = videos[0].get("embed")
                if embed_html:
                    st.components.v1.html(embed_html, height=360)
        st.divider()            
else:
    st.error(f"Erro ao buscar dados da API. Código de status: {resposta.status_code}")



