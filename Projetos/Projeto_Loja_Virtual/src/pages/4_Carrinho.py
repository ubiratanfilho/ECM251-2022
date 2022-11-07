# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st

st.title("Carrinho de Compras")

if st.session_state.usuario == None:
    st.error("Você precisa estar logado para acessar essa página!")
else:
    produtos = st.session_state.item_controller.get_all('Carrinho')
    for produto in produtos:
        st.markdown(f"### {produto.get_nome()}")
        st.image(produto.get_imagem(), width=200)
        st.markdown(f"{produto.get_descricao()}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"#### R${produto.get_preco()}")
        with col2:
            button_car = st.button("Remover do carrinho", key=produto.get_id())
            if button_car:
                st.session_state.item_controller.deletar_item(produto, 'Carrinho')