# from dao.item_dao import ItemDAO
# from models.item import Item
# from controllers.item_controller import ItemController
from controllers.item_controller import ItemController
from controllers.usuario_controller import UsuarioController

UsuarioController().limpar_tabela()
ItemController().limpar_tabela()
