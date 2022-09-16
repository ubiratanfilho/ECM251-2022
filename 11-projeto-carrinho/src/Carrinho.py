import streamlit as st
from Login import usuario

if usuario != None:
    st.title("Carrinho de", usuario)