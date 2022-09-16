import streamlit as st

st.title("Pagamento")

if st.session_state.usuario != None:
    valor_total = sum([item.get_preco() for item in st.session_state.carrinho])
    st.markdown(f"### Valor total: R${valor_total:.2f}")
    st.button("Finalizar compra")
else:
    st.markdown("### Você precisa estar logado para acessar essa página")