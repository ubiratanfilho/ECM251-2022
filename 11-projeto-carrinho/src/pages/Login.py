import streamlit as st
from modelos.usuarios.usuario import Usuario

st.title("Login")

# Usuários no banco de dados
u1 = Usuario("bira", "123", "bira@gmail.com")
u2 = Usuario("jordan", "123", "jordan@gmail.com")
u3 = Usuario("lebron", "123", "lebron@gmail.com")