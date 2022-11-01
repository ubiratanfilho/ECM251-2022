# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st

st.title("Carrinho de Compras")

if st.session_state.usuario != None:
    def exibe_produto(produto):
        from PIL import Image
        img = Image.open(produto.get_imagem())
        st.image(img, width=200)
        st.markdown(f"### {produto.get_nome()}")
        st.markdown(f"{produto.get_descricao()}")
        st.markdown(f"#### R${produto.get_preco()}")
        button = st.button("Remover 🛒", key=produto.get_nome())
        if button:
            st.session_state.carrinho.remove(produto)

    # exibe os produtos
    for item in st.session_state.carrinho:
        exibe_produto(item)
else:
    st.error("Você precisa estar logado para acessar essa página!")