# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.usuario import Usuario

class UsuarioController:
    def __init__(self):
        if "usuario" not in st.session_state:
            st.session_state.usuario = None
        if "all_users" not in st.session_state:
            # Usuários no banco de dados
            u1 = Usuario("bira", "123", "bira@gmail.com")
            u2 = Usuario("jordan", "123", "jordan@gmail.com")
            u3 = Usuario("lebron", "123", "lebron@gmail.com")
            st.session_state.all_users = [u1, u2, u3]
            
    def check_login(self, usuario, senha):
        usuario_correto = None
        for u in st.session_state.all_users:
            if usuario == u.get_user_name() and u.check_password(senha):
                usuario_correto = u
                break
        if usuario_correto == None:
            st.error("Usuário ou senha incorretos ❌")
            st.session_state.usuario = None
        else:
            st.success("Login realizado com sucesso ✔️")
            st.session_state.usuario = usuario_correto