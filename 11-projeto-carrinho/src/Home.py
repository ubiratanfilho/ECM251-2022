import streamlit as st
from modules.item import Item
from PIL import Image

# Inicializando session states
if "usuario" not in st.session_state:
    st.session_state.usuario = None

# Exibe o título da página inicial
col1, col2 = st.columns(2)
with col1:
    st.title("UbiraTec")
    st.markdown("### A única loja do seu ❤️💻")
with col2:
    st.image("imagens/Utec.png", width=200)
    
st.markdown("## Produtos") 

col1, col2, col3 = st.columns(3)
# Produtos no banco de dados
p1 = Item(354.99, "UbiraTec Washer", "Lavadora de tênis e sapatos", "imagens/washer.png")
p2 = Item(9999.99, "Samsung Neo G9", "Monitor Gamer Samsung Curvado", "imagens/neog9.jfif")
p3 = Item(449.99, "Nike PG4 Gatorade", "Tênis de Basquete do Paul George","imagens/pg4.png")

# Exibe os produtos
def exibe_produto(produto):
    img = Image.open(produto.get_imagem())
    st.image(img, width=200)
    st.markdown(f"### {produto.get_nome()}")
    st.markdown(f"{produto.get_descricao()}")
    st.markdown(f"#### R${produto.get_preco()}")
    st.button("Comprar 🛒", key=produto.get_nome())

exibe_produto(p1)
exibe_produto(p2)
exibe_produto(p3)