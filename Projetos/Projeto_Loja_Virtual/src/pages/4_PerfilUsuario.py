import streamlit as st
from models.usuario import Usuario

st.title("Perfil do Usuário")

if st.session_state.usuario == None:
    st.error("Você precisa estar logado para acessar essa página!")
else:
    st.markdown('## Informações Pessoais')
    st.markdown(f'**Usuário:** {st.session_state.usuario.get_user_name()}')
    st.markdown(f'**e-mail:** {st.session_state.usuario.get_email()}')
    st.markdown(f'**Senha:** {st.session_state.usuario.get_password()}')
    
    st.markdown('## Alterar dados')
    email = st.text_input('Digite o novo e-mail')
    if st.button('Alterar e-mail'):
        st.session_state.usuario.set_email(email)
        st.session_state.usuario_controller.atualizar_usuario(st.session_state.usuario)
        st.success('E-mail alterado com sucesso!')
        
    senha = st.text_input('Digite a nova senha')
    if st.button('Alterar senha'):
        st.session_state.usuario.set_password(senha)
        st.session_state.usuario_controller.atualizar_usuario(st.session_state.usuario)
        st.success('Senha alterada com sucesso!')