# Ubiratan da Motta Filho
# R.A - 20.00928-3

import streamlit as st
from models.item import Item
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController
from controllers.item_controller import ItemController

usuario_controller = UsuarioController()
item_controller = ItemController()

### Página Inicial
# Exibe o título da página inicial
col1, col2 = st.columns(2)
with col1:
    st.title("UbiraTec")
    st.markdown("### A única loja do seu ❤️💻")
with col2:
    # caso o arquivo seja rodado dentro de src ou fora de src
    st.image("https://dsm01pap009files.storage.live.com/y4maINQ8Xgz7FG0AUxeLQh4CpPFdB2g4_GYFvYG9neIhjBpQCQ6a9ldy86RSL14BqQ_rlCLTMm2X5ubVYXiWFirbJqxofB_9avqa2yE8BZpovEPpPCcSysf3_IDL5wgacBwDHCi2JcbGGJDzmqQblo5xASBEY-d2xZrKy7NBBt1qHgPEh0TeU95X6M1ZUFYkGnR?width=1000&height=1000&cropmode=none", width=200)
