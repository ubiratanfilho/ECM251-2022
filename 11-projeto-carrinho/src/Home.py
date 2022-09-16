import streamlit as st
from modules.item import Item
from modules.usuarios.usuario import Usuario


# Inicializando session states
if "usuario" not in st.session_state:
    st.session_state.usuario = None
if "all_users" not in st.session_state:
    # Usuários no banco de dados
    u1 = Usuario("bira", "123", "bira@gmail.com")
    u2 = Usuario("jordan", "123", "jordan@gmail.com")
    u3 = Usuario("lebron", "123", "lebron@gmail.com")
    st.session_state.all_users = [u1, u2, u3]
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []
if "estoque" not in st.session_state:
    # Produtos no banco de dados
    p1 = Item(354.99, "UbiraTec Washer", "Lavadora de tênis e sapatos", "https://github.com/ubiratanfilho/ECM251-2022/blob/a79044d6d2546a9fc8d24e7e4685683f82e9b0c1/11-projeto-carrinho/imagens/washer.png")
    p2 = Item(9999.99, "Samsung Neo G9", "Monitor Gamer Samsung Curvado", "https://github.com/ubiratanfilho/ECM251-2022/blob/a79044d6d2546a9fc8d24e7e4685683f82e9b0c1/11-projeto-carrinho/imagens/neog9.jfif")
    p3 = Item(449.99, "Nike PG4 Gatorade", "Tênis de Basquete do Paul George","https://github.com/ubiratanfilho/ECM251-2022/blob/a79044d6d2546a9fc8d24e7e4685683f82e9b0c1/11-projeto-carrinho/imagens/pg4.png")
    st.session_state.estoque = [p1, p2, p3]

# Exibe o título da página inicial
col1, col2 = st.columns(2)
with col1:
    st.title("UbiraTec")
    st.markdown("### A única loja do seu ❤️💻")
with col2:
    st.image("https://github.com/ubiratanfilho/ECM251-2022/blob/66a8c0c369d0c7690aab71fa6d82903fa0b6f4a8/11-projeto-carrinho/imagens/Utec.png", width=200)
    
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