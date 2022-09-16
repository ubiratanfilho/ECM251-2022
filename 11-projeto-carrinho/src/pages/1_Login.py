import streamlit as st
from modules.usuarios.usuario import Usuario

st.title("Login")

if st.session_state.usuario == None:
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    enter = st.button("Entrar")
    usuario_correto = None
    if enter:
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
else:
    st.write(f"Você está logado como **{st.session_state.usuario.get_user_name()}**")