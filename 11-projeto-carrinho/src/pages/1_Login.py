import streamlit as st
from modules.usuarios.usuario import Usuario

st.title("Login")

# Usuários no banco de dados
u1 = Usuario("bira", "123", "bira@gmail.com")
u2 = Usuario("jordan", "123", "jordan@gmail.com")
u3 = Usuario("lebron", "123", "lebron@gmail.com")
l_usuarios = [u1, u2, u3]

# Entrada de dados
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")
enter = st.button("Entrar")
usuario_correto = None
if enter:
    for u in l_usuarios:
        if usuario == u.get_user_name() and u.check_password(senha):
            usuario_correto = u
            break
    if usuario_correto == None:
        st.text("Usuário ou senha incorretos ❌")
    else:
        st.text("Login realizado com sucesso ✔️")
        st.session_state.usuario = usuario_correto
    
