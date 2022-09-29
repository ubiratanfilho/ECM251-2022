# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.item import Item
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

usuario_controller = UsuarioController()
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []
if "estoque" not in st.session_state:
    # Produtos no banco de dados
    p1 = Item(354.99, "UbiraTec Washer", "Lavadora de tênis e sapatos", "./imagens/washer.png")
    p2 = Item(9999.99, "Samsung Neo G9", "Monitor Gamer Samsung Curvado", "./imagens/neog9.jfif")
    p3 = Item(449.99, "Nike PG4 Gatorade", "Tênis de Basquete do Paul George","./imagens/pg4.png")
    st.session_state.estoque = [p1, p2, p3]

### Página Inicial
# Exibe o título da página inicial
col1, col2 = st.columns(2)
with col1:
    st.title("UbiraTec")
    st.markdown("### A única loja do seu ❤️💻")
with col2:
    st.image("./imagens/Utec.png", width=200)

if st.session_state.usuario != None:
    st.markdown("## Produtos") 

    # Exibe os produtos
    def exibe_produto(produto):
        from PIL import Image
        img = Image.open(produto.get_imagem())
        st.image(img, width=200)
        st.markdown(f"### {produto.get_nome()}")
        st.markdown(f"{produto.get_descricao()}")
        st.markdown(f"#### R${produto.get_preco()}")
        button = st.button("Comprar 🛒", key=produto.get_nome())
        if button:
            st.session_state.carrinho.append(produto)

    for produto in st.session_state.estoque:
        exibe_produto(produto)
else:
    st.error("Você precisa estar logado para ver os produtos, vá até a tela de login e coloque seu usuário e senha")