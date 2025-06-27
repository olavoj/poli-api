import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Gerador de Descricoes de Produtos")

with st.form("form_descricoes"):
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    publico = st.text_input("Publico-alvo")
    submitted = st.form_submit_button("Gerar descricao")

if submitted and nome and categoria and publico:
    prompt = (
        f"Crie uma descricao de marketing para o produto '{nome}' "
        f"da categoria '{categoria}' voltado para o publico '{publico}'. "
        "Responda em portugues."
    )
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    descricao = resposta.choices[0].message.content.strip()
    st.session_state["descricao"] = descricao
else:
    descricao = st.session_state.get("descricao")

if descricao:
    st.markdown(
        f"""
        <textarea id='resultado' style='width:100%; height:200px;'>{descricao}</textarea>
        <button onclick="navigator.clipboard.writeText(document.getElementById('resultado').value)">Copiar</button>
        """,
        unsafe_allow_html=True,
    )
