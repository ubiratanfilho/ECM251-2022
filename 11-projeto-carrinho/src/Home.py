import streamlit as st

col1, col2 = st.columns(2)
with col1:
    st.title("UbiraTec")
    st.markdown("### A única loja do seu ❤️💻")
with col2:
    st.image("imagens/Utec.png", width=200)
    
st.markdown("## Produtos") 

col1, col2, col3 = st.columns(3)
 