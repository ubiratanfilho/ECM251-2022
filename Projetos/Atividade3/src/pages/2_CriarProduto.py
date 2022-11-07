# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.item import Item

st.title("Criar Produto")
if st.session_state.usuario != None:
    nome = st.text_input("Nome")
    descricao = st.text_input("Descrição")
    preco = st.number_input("Preço", min_value=0.0, step=0.1)
    imagem = st.text_input("URL Imagem")
    enter = st.button("Criar")

    if enter:
        item = Item(nome, descricao, preco, imagem)
        st.session_state.item_controller.inserir_item(item)
        st.success("Produto criado com sucesso!")
else:
    st.error("Você precisa estar logado para acessar essa página!")