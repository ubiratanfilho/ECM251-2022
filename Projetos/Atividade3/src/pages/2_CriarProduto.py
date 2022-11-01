import streamlit as st
from models.item import Item

st.title("Criar Produto")

nome = st.text_input("Nome")
descricao = st.text_input("Descrição")
preco = st.number_input("Preço", min_value=0.0, step=0.1)
imagem = st.text_input("URL Imagem")
enter = st.button("Criar")

if enter:
    item = Item(nome, descricao, preco, imagem)
    st.session_state.item_controller.inserir_item(item)
    st.success("Produto criado com sucesso!")