import streamlit as st
from modelos.item import Item
from PIL import Image

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
img1 = Image.open(p1.get_imagem())
st.image(img1)
st.markdown(f"### {p1.get_nome()}")
st.markdown(f"{p1.get_descricao()}")
st.markdown(f"#### R${p1.get_preco()}")
st.button("Comprar Washer")

img2 = Image.open(p2.get_imagem())
st.image(img2, width=200)
st.markdown(f"### {p2.get_nome()}")
st.markdown(f"{p2.get_descricao()}")
st.markdown(f"#### R${p2.get_preco()}")
st.button("Comprar Neo G9")

img3 = Image.open(p3.get_imagem())
st.image(img3, width=200)
st.markdown(f"### {p3.get_nome()}")
st.markdown(f"{p3.get_descricao()}")
st.markdown(f"#### R${p3.get_preco()}")
st.button("Comprar PG4")