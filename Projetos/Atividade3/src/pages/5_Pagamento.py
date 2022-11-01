# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st

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

st.title("Pagamento")

if st.session_state.usuario != None:
    st.markdown(f"### Usuário: {st.session_state.usuario.get_user_name()}")
    st.markdown(f"## Carrinho:")
    # exibe os produtos
    for item in st.session_state.carrinho:
        exibe_produto(item)
    
    # calcula o valor total do carrinho
    valor_total = sum([item.get_preco() for item in st.session_state.carrinho])
    st.markdown(f"### Valor total: R${valor_total:.2f}")
    
    forma_pagamento = st.radio("Forma de pagamento", ["Cartão de crédito", "Boleto", "Pix"])
    finalizar = st.button("Finalizar compra")
    if finalizar:
        st.session_state.carrinho = []
        st.success("Compra finalizada com sucesso!")
else:
    st.error("Você precisa estar logado para acessar essa página!")