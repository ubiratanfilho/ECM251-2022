# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.item import Item
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController
from controllers.item_controller import ItemController

# Inicializando controllers e variáveis globais
if 'usuario_controller' not in st.session_state:
    st.session_state.usuario_controller = UsuarioController()
if 'item_controller' not in st.session_state:
    st.session_state.item_controller = ItemController()
    st.session_state.item_controller.limpar_tabela('Carrinho')
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

### Página Inicial
# Exibe o título da página inicial
col1, col2 = st.columns(2)
with col1:
    st.title("UbiraTec")
    st.markdown("### A única loja do seu ❤️💻")
with col2:
    # caso o arquivo seja rodado dentro de src ou fora de src
    st.image("https://dsm01pap009files.storage.live.com/y4maINQ8Xgz7FG0AUxeLQh4CpPFdB2g4_GYFvYG9neIhjBpQCQ6a9ldy86RSL14BqQ_rlCLTMm2X5ubVYXiWFirbJqxofB_9avqa2yE8BZpovEPpPCcSysf3_IDL5wgacBwDHCi2JcbGGJDzmqQblo5xASBEY-d2xZrKy7NBBt1qHgPEh0TeU95X6M1ZUFYkGnR?width=1000&height=1000&cropmode=none", width=200)

# Checa se usuário está logado
if st.session_state.usuario == None:
    st.error("Você precisa estar logado para acessar essa página!")
else:
    st.markdown("## Produtos")
    produtos = st.session_state.item_controller.get_all()
    for produto in produtos:
        st.markdown(f"### {produto.get_nome()}")
        st.image(produto.get_imagem(), width=200)
        st.markdown(f"{produto.get_descricao()}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"#### R${produto.get_preco()}")
        with col2:
            button_car = st.button("Adicionar ao carrinho", key=produto.get_id())
            if button_car:
                st.session_state.item_controller.inserir_item(produto, 'Carrinho')