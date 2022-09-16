import streamlit as st

st.title("Pagamento")

if st.session_state.usuario != None:
    st.text(st.session_state.usuario.get_user_name())
else:
    st.markdown("### Você precisa estar logado para acessar essa página")