from dao.item_dao import ItemDAO
from models.item import Item
from controllers.item_controller import ItemController

item = Item(nome="Teste", descricao="Teste", preco=1.99, imagem="Teste")
ItemDAO.get_instance().inserir_item(item)
print(ItemController().pegar_item(1))