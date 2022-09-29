# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.item import Item

class ItemController:
    def __init__(self):
        if "carrinho" not in st.session_state:
            st.session_state.carrinho = []
        if "estoque" not in st.session_state:
            # Produtos no banco de dados
            p1 = Item(354.99, "UbiraTec Washer", "Lavadora de tênis e sapatos", "./imagens/washer.png")
            p2 = Item(9999.99, "Samsung Neo G9", "Monitor Gamer Samsung Curvado", "./imagens/neog9.jfif")
            p3 = Item(449.99, "Nike PG4 Gatorade", "Tênis de Basquete do Paul George","./imagens/pg4.png")
            st.session_state.estoque = [p1, p2, p3]
