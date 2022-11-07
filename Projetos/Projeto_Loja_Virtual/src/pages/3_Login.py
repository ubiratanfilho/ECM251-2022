# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

st.title("Login")

if st.session_state.usuario == None:
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    enter = st.button("Entrar")
    if enter:
        if st.session_state.usuario_controller.check_login(usuario, senha):
            st.session_state.usuario = st.session_state.usuario_controller.pegar_usuario(usuario)
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos!")
else:
    st.write(f"Você está logado como **{st.session_state.usuario.get_user_name()}**")