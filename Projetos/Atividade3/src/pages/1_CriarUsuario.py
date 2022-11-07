# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.usuario import Usuario

st.title("Criação de Novo Usuário")
if st.session_state.usuario != None:
    st.markdown("### Preencha os campos abaixo para criar um novo usuário")

    usuario = st.text_input("Usuário")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    enter = st.button("Adicionar")
    if enter:
        usuario = Usuario(usuario, email, senha)
        st.session_state.usuario_controller.inserir_usuario(usuario)
        st.success("Usuário criado com sucesso!")
else:
    st.error("Você precisa estar logado para acessar essa página!")