# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st

st.title("Pagamento")

if st.session_state.usuario == None:
    st.error("Você precisa estar logado para acessar essa página!")
else:
    st.markdown("## Carrinho")
    produtos = st.session_state.item_controller.get_all('Carrinho')
    if len(produtos) == 0:
        st.error("Você não tem nenhum produto no carrinho!")
    else:
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
        st.markdown("## Forma de Pagamento")
        forma_pagamento = st.radio("Selecione a forma de pagamento", ("Cartão de Crédito", "Cartão de Débito", "Boleto"))

        # valor total
        total = 0
        for produto in produtos:
            total += produto.get_preco()
        st.markdown(f"### Total: R${total:.2f}")
        compra = st.button("Finalizar Compra")
        if compra:
            st.session_state.item_controller.limpar_tabela('Carrinho')
            st.success("Compra realizada com sucesso!")